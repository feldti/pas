#!/bin/bash
#
# Script to stop the complete application. You will need to adapt this script
# to your project needs
#
usage() {
  cat <<HELP

USAGE: $(basename $0)
Stops the complete application

HELP
}

if [ ! -f ./credentials.sh ]; then
  echo 'Missing credentials.sh - copy demo_credentials.sh and make the needed changes to it'
  exit 1
fi

#
# load all the needed information
#
source ./credentials.sh

source $GS_HOME/bin/defGsDevKit.env
source $GS_HOME/server/stones/$PAS_STONE_NAME/defStone.env "$PAS_STONE_NAME"
 
if [ -s $GEMSTONE/seaside/etc/gemstone.secret ]; then
    . $GEMSTONE/seaside/etc/gemstone.secret
else
    echo 'Missing password file $GEMSTONE/seaside/etc/gemstone.secret'
    exit 1
fi

rm $PAS_STONE_NAME

#
# We stop the network access for development
#
stopNetldi  $PAS_STONE_NAME

#
# Now we stop all processes - qaccessable via names
pkill -f pas_start_http_task.sh


#
# And at the end we stop database
#
stopStone $PAS_STONE_NAME
