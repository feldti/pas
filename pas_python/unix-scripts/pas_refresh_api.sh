#!/bin/bash
#
# This script should be executed with each new model version loaded into a stone
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name>
initializes the API structure within the database

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

if [ ! -f ./credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it'
  exit 1
fi

#
# load all the needed information
#
source ./credentials.sh

#
# Umgebung setzen
#
cd
source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$1/defStone.env $1
echo "2"
if [ -s $GS_HOME/server/stones/$1/product/seaside/etc/gemstone.secret ]; then
    . $GS_HOME/server/stones/$1/product/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GS_HOME/server/stones/$1/defStone.env esystem'
    exit 1
fi

cat << EOF | topaz -l
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
$PAS_APP_RESTCALL_CLASS buildAPIDefinitionsStructure.
%
commit
EOF
