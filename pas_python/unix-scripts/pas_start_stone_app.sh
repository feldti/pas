#!/bin/bash
#
# Script to start the stone with all processes needed for the application
#
usage() {
  cat <<HELP

USAGE: $(basename $0)
Starts the complete application according to the definition in the active credentials.sh file

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

#
#
# We are starting the database
startStone $PAS_STONE_NAME

#
# We wait for the working database
#
waitstone $PAS_STONE_NAME >/dev/null 2>&1

#
# We define a file as a help information, that the application is running
#
touch $PAS_STONE_NAME
startTS=`date +%Y-%m-%d-%H-%M`

#
# Now we start the sub processes of the application. You may adapt this to your needs
#
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_NORMAL_MEMORY $(($PAS_STONE_NORMAL_PORT + 00)) pas_normal.0  >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_NORMAL_MEMORY $(($PAS_STONE_NORMAL_PORT + 10)) pas_normal.1  >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_NORMAL_MEMORY $(($PAS_STONE_NORMAL_PORT + 20)) pas_normal.2  >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_NORMAL_MEMORY $(($PAS_STONE_NORMAL_PORT + 30)) pas_normal.3 >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_NORMAL_MEMORY $(($PAS_STONE_NORMAL_PORT + 40)) pas_normal.4  >/dev/null 2>&1 &

nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_LONG_MEMORY $(($PAS_STONE_LONG_PORT + 00)) pas_long.0  >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_LONG_MEMORY $(($PAS_STONE_LONG_PORT + 10)) pas_long.1  >/dev/null 2>&1 &

nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_MEMORYMEMORY $(($PAS_STONE_MEMORY_PORT + 00)) pas_memory.0  >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_MEMORYMEMORY $(($PAS_STONE_MEMORY_PORT + 10)) pas_memory.1  >/dev/null 2>&1 &

nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_LIMITEDMEMORY $(($PAS_STONE_LIMITED_PORT + 00)) pas_limited.0  >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_LIMITEDMEMORY $(($PAS_STONE_LIMITED_PORT + 10)) pas_limited.1  >/dev/null 2>&1 &

nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_EXTDBMEMORY $(($PAS_STONE_EXTDB_PORT + 00)) pas_extdb.0 >/dev/null 2>&1 &
nohup ./pas_start_http_task.sh $PAS_STONE_NAME $PAS_STONE_EXTDBMEMORY $(($PAS_STONE_EXTDB_PORT + 10)) pas_extdb.1  >/dev/null 2>&1 &
