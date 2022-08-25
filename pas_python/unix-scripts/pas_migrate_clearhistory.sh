#!/bin/bash
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name>
Entfernt von allen Projektklassen die Klassenhistorie. Dies sollte erst nach
einer erfolgreichen Migration erfolgen

EXAMPLES
  $(basename $0) webcati71

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
if [ -s $GS_HOME/server/stones/$1/product/seaside/etc/gemstone.secret ]; then
    . $GS_HOME/server/stones/$1/product/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GS_HOME/server/stones/$1/defStone.env'
    exit 1
fi

cat << EOF | topaz -l -T 4000000 -u dev_migrate_collector_${1}
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
| domainClassesToConsider migrator|
domainClassesToConsider := $PAS_APP_PROJECT_CLASS classCreated select: [ :eachClass | eachClass isSubclassOf: $PAS_APP_TOPDOMAIN_CLASS ].
domainClassesToConsider do:[ :eachClass |
  eachClass removeClassHistory
].
$PAS_APP_TOPAPI_CLASS allSubclasses do:[ :eachClass |
    eachClass removeClassHistory
].
PUMGeneralProjectClass allSubclasses do:[ :eachClass |
    eachClass removeClassHistory
].
System commit
%
EOF
