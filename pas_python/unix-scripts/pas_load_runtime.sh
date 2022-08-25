#!/bin/bash
#
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0)  <stonename> 
Loads all packages of the runtime

EAXMPLES
  $(basename $0)

HELP
}

#
# Are enough parameter available ?
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

source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$1/defStone.env $1
if [ -s $GEMSTONE/seaside/etc/gemstone.secret ]; then
    . $GEMSTONE/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GEMSTONE/seaside/etc/gemstone.secret'
    exit 1
fi
cat << EOF | $GEMSTONE/bin/topaz -l -T 1000000 -u pum_runtime_loading
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
 Metacello new
    baseline: 'ZincHTTPComponents';
    repository: 'github://GsDevKit/zinc:gs_master/repository';
    onLock: [:ex | ex honor ];
    load: 'REST'.
  Metacello new
    baseline: 'ZincHTTPComponents';
    repository: 'github://GsDevKit/zinc:gs_master/repository';
    onLock: [:ex | ex honor ];
    load: 'Zinc-WebSocket-Core'.
  Metacello new
    baseline: 'ZincHTTPComponents';
    repository: 'github://GsDevKit/zinc:gs_master/repository';
    onLock: [:ex | ex honor ];
    load: 'Zinc-SSO-OAuth2-Core'.
  Metacello new
    baseline: 'ZincHTTPComponents';
    repository: 'github://GsDevKit/zinc:gs_master/repository';
    onLock: [:ex | ex honor ];
    load: 'Zinc-SSO-OpenID-Core'.
  Metacello new
    baseline: 'Zodiac';
    repository: 'github://GsDevKit/zodiac:gs_master/repository';
    onLock: [:ex | ex honor ];
    load: 'Zodiac-Core'.
  Metacello new
    baseline: 'Zodiac';
    repository: 'github://GsDevKit/zodiac:gs_master/repository';
    onLock: [:ex | ex honor ];
    load: 'Zodiac-GemStone-Core'.
  Metacello new
    baseline: 'Cryptography';
    repository: 'github://GsDevKit/Cryptography:master/repository';
    onLock: [:ex | ex honor ];
    load: 'default'.
  Metacello new
    baseline: 'PharoCompatibility';
    repository: 'github://GsDevKit/PharoCompatibility:master/repository';
    onConflictUseIncoming;
    load: 'default' .
%
doit
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKExtensions' ;
        load.
%
doit
  Metacello new
    baseline: 'JsonWebToken';
    repository: 'github://feldti/Json-WebToken:main/repository';
    onLock: [:ex | ex honor ];
    load: 'default'.
  Metacello new
    baseline: 'GsNeoCSV';
    repository: 'github://feldti/GsNeoCSV:main/repository';
    onLock: [:ex | ex honor ];
    load.
%
doit
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'Multibase-Core' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKUlid' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKMigrationSupport' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKZeroMQBase' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKZeroMQGemstone' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKZeroMQWrapper' ;
        load.        
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKRESTSupport' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKSwaggerSupport' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSKJSONSchemaSupport' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'MSK-ModelBaseRuntime' ;
        load.
Gofer new
        url: '$PAS_RUNTIME_PACKAGES' ;
        package: 'Neo-JSON-Core' ;
        load.
%
doit        
ZnConstants 
  defaultMaximumEntitySize: (16 * 1024 * 1024) ; 
  maximumEntitySize: (16 * 1024 * 1024).
%
commit
EOF
