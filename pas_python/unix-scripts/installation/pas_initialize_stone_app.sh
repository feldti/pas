#!/bin/bash
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name>
initializes the webcati server structure and creates a new user and root admin

EXAMPLES
  $(basename $0) webcati6
 
HELP
}

#
# Sind genuegend Parameter mitgegeben ...
#
if [ $# -ne 1 ]; then
  usage; exit 1
fi

if [ ! -f ../credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it'
  exit 1
fi

#
# load all the needed information
#
source ../credentials.sh


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

cat << EOF | $GEMSTONE/bin/topaz -l
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
$PAS_APP_SERVICE_CLASS basicInitialize.
System commit.
%
commit
EOF
