#!/bin/bash
#
#
# This script loads the GLASS component, updates ist and loads the GsApplicationTools
# all stuff is loaded from the internet
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <db-name>
Updates the product software

EAXMPLES
  $(basename $0) stonename

HELP
}

if [ $# -ne 1 ]; then
  usage; exit 1
fi
source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$1/defStone.env $1
if [ -s $GEMSTONE/seaside/etc/gemstone.secret ]; then
    . $GEMSTONE/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GEMSTONE/seaside/etc/gemstone.secret'
    exit 1
fi
cat << EOF | $GEMSTONE/bin/topaz -l -T 1000000 -u product_update
set user DataCurator pass $GEMSTONE_CURATOR_PASS gems $GEMSTONE_NAME
iferror where
login
doit
Gofer new
  package: 'GsUpgrader-Core';
  url: 'http://ss3.gemtalksystems.com/ss/gsUpgrader';
  load.
(Smalltalk at: #GsUpgrader) upgradeGrease.
%
doit
"Install GLASS from github"
GsDeployer deploy: [
 Metacello new
  baseline: 'GLASS1';
  repository: 'github://glassdb/glass:master/repository';
  get.
 Metacello new
  baseline: 'GLASS1';
  repository: 'github://glassdb/glass:master/repository';
  onLock: [:ex | ex honor ];
  load: 'default' ].
%
doit
GsDeployer deploy: [
  "Load GsApplicationTools packages"
  Metacello new
    baseline: 'GsApplicationTools';
    repository: 'github://GsDevKit/gsApplicationTools:master/repository';
    load: 'default'
].
%
commit
EOF
