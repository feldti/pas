##!/bin/bash
#
# This script loads all application source code needed for the webcati server
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <stone-name> <software-branch>  <versions-name>
Loads all core packages WITH the model definition

EXAMPLES
  $(basename $0) testdb develop|production v74

HELP
}

GRPNAME=`id -n -g`

export INSTALL_HOME=`pwd`

if [ ! -f ../credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it. Localtion: ' $INSTALL_HOME
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

startStone $1
waitstone $1 0
cd $INSTALL_HOME
./pas_preinitialize_gemstone.sh $1

cat << EOF | $GEMSTONE/bin/topaz -l -T 4000000
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
Gofer new
        url: '$PAS_APP_PACKAGES' ;
        package: '$PAS_APP_MDL_PACKAGE' ;
        load.
%
doit
Gofer new
        url: '$PAS_APP_PACKAGES' ;
        package: '$PAS_APP_EXT_PACKAGE' ;
        load.
%
commit
doit
MSKRESTLocaleErrorDefinition initialize.
$PAS_APP_ERROR_CLASS initialize.
%
commit
EOF
echo $INSTALL_HOME
cd $INSTALL_HOME
./pas_postinitialize_gemstone.sh $1
./pas_initialize_stone_app.sh $1
../pas_settimezone.sh $1
cd ..
./pas_refresh_api.sh $1
./pas_publish_openapi.sh $1




