#!/bin/bash
#
#
# This script starts the session activity handler
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0)
starts the session activity handler

EXAMPLES

  $(basename $0)

HELP
}

if [ ! -f ./credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it'
  exit 1
fi

#
# load all the needed information
#
source ./credentials.sh

source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$PAS_STONE_NAME/defStone.env "$PAS_STONE_NAME"
 
if [ -s $GEMSTONE/seaside/etc/gemstone.secret ]; then
    . $GEMSTONE/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GEMSTONE/seaside/etc/gemstone.secret'
    exit 1
fi

while [ -f $PAS_STONE_NAME ]
do

nowTS=`date +%Y-%m-%d-%H-%M`
cat << EOF | nohup $GEMSTONE/bin/topaz -l -T 50000 -u session_activity 2>&1 >> $GEMSTONE_LOGDIR/session_activity_task_${nowTS}.log

set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME

display oops
iferror where

login

run

"record gems pid in the pid file"

$PAS_APP_SERVICE_CLASS taskStartSessionActivityMaintainance: '$PAS_APP_RMQ_ACCOUNT' password: '$PAS_APP_RMQ_PASSWD' hostname: '$PAS_APP_RMQ_ADR'.

%

EOF
#
# Wenn die Datei nicht mehr vorhanden ist -> sofort Abbruch
# ansonsten 60 sekunden warten, damit nicht zu schnell respawned wird
#
if [ ! -f $PAS_STONE_NAME ]; then
   exit 0
else
   sleep 60s
fi
done
