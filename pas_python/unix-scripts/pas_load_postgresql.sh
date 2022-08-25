#!/bin/bash
#
#
# This application loads the PostgreSQL package
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name>
Loads the PostgreSQL package

EXAMPLES
  $(basename $0)  <stonename>

HELP
}

#
# All paremater defined ?
#
if [ $# -ne 1 ]; then
  usage; exit 1
fi
export INSTALL_HOME=`pwd`

if [ ! -f ./credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it. Localtion: ' $INSTALL_HOME
  exit 1
fi

#
# load all the needed information
#
source ./credentials.sh

if [ ! -d ~/GemConnect-for-Postgres ]; then
  mkdir ~/GemConnect-for-Postgres
  cd ~
  git clone https://github.com/feldti/GemConnect-for-Postgres.git
fi
if [ -d ~/GemConnect-for-Postgres ]; then
  cd ~/GemConnect-for-Postgres
  git pull
fi
cd $INSTALL_HOME

if [ -d ~/GemConnect-for-Postgres ]; then
  echo "Installation of GemConnect for PostgreSQL"
  cd ~/GemConnect-for-Postgres
  ./load_postgresql.sh  $1
  cd $INSTALL_HOME
else
  echo "ERROR: No GemConnect for Postgres found !"
  exit 1
fi

#
# Set the environment for Gemstone running
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
        package: 'MSKGemConnectPostgresExtension' ;
        load.
%
commit
EOF

cd $INSTALL_HOME

