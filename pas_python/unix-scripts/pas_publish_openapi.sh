#!/bin/bash
#
#
# This script publishes the OpenAPI specification at the file location
#    /var/www/html/api/<interface>/<version>/openapi.json
#
usage() {
  cat <<HELP

USAGE: $(basename $0) 
writes the file of the OpenAPI specification of the interface
to the following file location:
      /var/www/html/openapi/<interface>/openapi.json

HELP
}

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


# We build a path - so we would even work in a CRON environment
cd $HOME
if [ ! -d "GsDevKit_home" ]; then
   echo "Error: GsDevKit_home directory not found"
   exit 1
fi
cd GsDevKit_home
export GS_HOME=`pwd`
export PATH=$GS_HOME/bin:$PATH

if [ ! -d "/var/www/html/openapi" ]; then
  sudo mkdir "/var/www/html/openapi"
  sudo chown -R $USER.$GRPNAME "/var/www/html/openapi"
  sudo chmod a+wrx "/var/www/html/openapi"
fi

#
# Umgebung setzen
#
cd
source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$1/defStone.env $1
if [ -s $GS_HOME/server/stones/$1/product/seaside/etc/gemstone.secret ]; then
    . $GS_HOME/server/stones/$1/product/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GS_HOME/server/stones/$STONEDBNAME/defStone.env $STONEDBNAME'
    exit 1
fi

cat << EOF | topaz -l
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
| aMSKGeneralOpenAPICreator |
aMSKGeneralOpenAPICreator := MSKGeneralOpenAPICreator new.
aMSKGeneralOpenAPICreator
  aMSKRestCallV2: $PAS_APP_RESTCALL_CLASS ;
  baseDirectory: '/var/www/html' ;
  startDocumentCreation ;
  createRootDocumentAtDirectories: (Array with: 'apis' with: $PAS_APP_RESTCALL_CLASS firstPartOfPath with: $PAS_APP_RESTCALL_CLASS versionPartOfPath)
%
commit
doit
%
EOF
