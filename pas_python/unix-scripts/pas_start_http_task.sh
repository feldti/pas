#!/bin/bash
#
#
# This script starts a http response task
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name> <memory> <http-port> <name>
starts a http response task

1 <stone-name>   - Name der Datenbank
2 <memory>       - Temp memory of this GEM
3 <http-port>    - HTTP-Port
4 <name>         - Name of this script



EXAMPLES

  $(basename $0) webcati6 75000 19000 long 12000

HELP
}

#
# Sind genuegend Parameter mitgegeben ...
#
if [ $# -ne 4 ]; then
  usage; exit 1
fi

if [ ! -f ./credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it'
  exit 1
fi

#
# load all the needed information
#
source ./credentials.sh

source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$1/defStone.env "$1"
 
if [ -s $GEMSTONE/seaside/etc/gemstone.secret ]; then
    . $GEMSTONE/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GEMSTONE/seaside/etc/gemstone.secret'
    exit 1
fi

while [ -f $1 ]
do

nowTS=`date +%Y-%m-%d-%H-%M`
cat << EOF | nohup $GEMSTONE/bin/topaz -l -T $2 -u ${4}_${3} 2>&1 >> $GEMSTONE_LOGDIR/${4}_server_${nowTS}.log

set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME

display oops
iferror where

login

run

"record gems pid in the pid file"

| file |

(GsFile isServerDirectory: '$GEMSTONE_DATADIR') ifFalse: [ ^nil ].

file := GsFile openWriteOnServer: '$GEMSTONE_DATADIR/${4}.pid'.
file nextPutAll: (System gemVersionReport at: 'processId') printString.
file cr.
file close.

(ObjectLogEntry
  info: '${4}_server: startup'
  object: 'pid: ', (System gemVersionReport at: 'processId') printString) addToLog.
System commitTransaction
    ifFalse: [
      System abortTransaction.
      nil error: 'Could not commit ObjectLog entry' ].
%
run

| count server rabbitMQConnector |

GsProcess usingNativeCode not
  ifTrue: [
    "Enable remote Breakpoing handling"
    Breakpoint trappable: true.
    GemToGemAnnouncement installStaticHandler.
    System commitTransaction ifFalse: [ nil error: 'Could not commit for GemToGemSignaling' ].
  ].

System transactionMode: #manualBegin.


"This thread is needed to handle the SigAbort exception, when the primary
thread is blocked. Assuming default 60 second STN_GEM_ABORT_TIMEOUT, wake
up at 30 second intervals."

[
  [ true ] whileTrue: [ 
	(Delay forSeconds: 30) wait ].

] forkAt: Processor lowestPriority.

IndexManager sessionAutoCommit: true.

GsFile gciLogServer: '$1 Server started on port ', $3 printString.

('$PAS_APP_TLS' = 'true')
  ifTrue:[
    rabbitMQConnector := MSKRabbitMQConnector new initialize.
    rabbitMQConnector
      hostname: '$PAS_APP_RMQ_ADR' ;
      port: $PAS_APP_RMQ_PORT ;
      userID: '$PAS_APP_RMQ_ACCOUNT' ;
      password: '$PAS_APP_RMQ_PASSWD' ;
      applicationID: '$PAS_APP_SERVERTYPE' ;
      caCertPath: '$PAS_APP_RMQ_CACERT_PATH' ;
      certPath: '$PAS_APP_RMQ_CERT_PATH' ;
      privateKey: '$PAS_APP_RMQ_PRVKE' ;
      login;
      openChannel.
  ]
  ifFalse:[
    rabbitMQConnector := MSKRabbitMQConnector new initialize.
    rabbitMQConnector
      hostname: '$PAS_APP_RMQ_ADR' ;
      port: $PAS_APP_RMQ_PORT ;
      userID: '$PAS_APP_RMQ_ACCOUNT' ;
      password: '$PAS_APP_RMQ_PASSWD' ;
      applicationID: '$PAS_APP_SERVERTYPE' ;
      login;
      openChannel.
	].

GsFile gciLogServer: '$1 RabbitMQ Setup'.
$PAS_APP_SERVICE_CLASS mqStartupInitialize: rabbitMQConnector.


server := MSKRestCallServerMQ newDefaultServer.
server
	startServer: true 
	httpDebug: false 
	localhost: true
	port: $3 printString asNumber
	serviceClass: $PAS_APP_SERVICE_CLASS
	mqConnector: rabbitMQConnector
%

run

GemToGemAnnouncement uninstallStaticHandler.
System beginTransaction.
(ObjectLogEntry
  fatal: '${4}_server: topaz exit'
  object:
    'pid: ', (System gemVersionReport at: 'processId') printString) addToLog.
System commitTransaction.

%

EOF
#
# Wenn die Datei nicht mehr vorhanden ist -> sofort Abbruch
# ansonsten 60 sekunden warten, damit nicht zu schnell respawned wird
#
if [ ! -f $1 ]; then
   exit 0
else
   sleep 60s
fi
done
