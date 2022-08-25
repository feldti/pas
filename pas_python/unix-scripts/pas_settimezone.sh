#!/bin/bash
#
#
# Sets the database timezone to the OS timezone used
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name>
sets the database timezone to the OS timezone

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
set user SystemUser pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
run
| osTZ |
System beginTransaction.
osTZ := TimeZone fromOS.
osTZ installAsCurrentTimeZone.
TimeZone default: osTZ.
TimeZoneInfo default: osTZ.
System commitTransaction.
%

logout
errorCount
EOF
