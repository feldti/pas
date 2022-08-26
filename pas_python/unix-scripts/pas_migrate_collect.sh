#!/bin/bash
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name> <path>
Migriert die Instanzen auf die aktuelle Version

EXAMPLES
  $(basename $0) webcati70 /home/...../__temp_migration_classes.bm

HELP
}

#
# Sind genuegend Parameter mitgegeben ...
#
if [ $# -ne 2 ]; then
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

echo 'Creating the GsBitmap File'

cat << EOF | topaz -l -T 4000000 -u dev_migrate_collector_${1}
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
| domainClassesToConsider migrator|
domainClassesToConsider := $PAS_APP_PROJECT_CLASS classCreated select: [ :eachClass | eachClass isSubclassOf: $PAS_APP_TOPDOMAIN_CLASS ].
domainClassesToConsider add: $PAS_APP_PROJECT_CLASS.
migrator := MSKMigrater collector: '${2}' classes: domainClassesToConsider fastMode: true.
migrator createGsBitmapFile.
%
EOF
