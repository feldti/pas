#!/bin/bash
#
#
# This application loads the RabbitMQ  package
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name>
Loads the RabbitMQ package stuff

EXAMPLES
  $(basename $0)  <stonename>

HELP
}

#
# Sind genuegend Parameter mitgegeben ...
#
if [ $# -ne 1 ]; then
  usage; exit 1
fi

if [ ! -f ./credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it. Localtion: ' $INSTALL_HOME
  exit 1
fi

#
# load all the needed information
#
source ./credentials.sh

export INSTALL_HOME=`pwd`
if [ ! -d ~/GemConnectForRabbitMQ ]; then
  mkdir ~/GemConnectForRabbitMQ
  cd ~
  git clone https://github.com/feldti/GemConnectForRabbitMQ.git
fi
if [ -d ~/GemConnectForRabbitMQ ]; then
  cd ~/GemConnectForRabbitMQ
  git pull
fi
cd $INSTALL_HOME

if [ -d ~/GemConnectForRabbitMQ ]; then
  echo "Installation of GemConnect for RabbitMQ"
  cd ~/GemConnectForRabbitMQ
  ./load_rabbitmq.sh  $1
  cd $INSTALL_HOME
else
  echo "ERROR: No GemConnect for Postgres found !"
  exit 1
fi

#
# Umgebung setzen
#
cd
source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$1/defStone.env $1
if [ -s $GEMSTONE/seaside/etc/gemstone.secret ]; then
    . $GEMSTONE/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GEMSTONE/seaside/etc/gemstone.secret'
    exit 1
fi
#
# Load the extensions to the package from GemTalk
#
cat << EOF | $GEMSTONE/bin/topaz -l -T 1000000
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKGemConnectRabbitMQExtension' ;
        load.
%
commit
EOF

cd $INSTALL_HOME


