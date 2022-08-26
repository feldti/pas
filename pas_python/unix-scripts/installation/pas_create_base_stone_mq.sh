#!/bin/bash
#
# This script creates a named stone including all prerequisites needed
# for development an application for the pum application stack should
#
usage() {
  cat <<HELP

USAGE: $(basename $0)  <stonename> <gemstone-version>
Creates a new base development stone based on a specific Gemstone version and framework version
EXAMPLES
  $(basename $0) stonename 3.6.3 

HELP
}

GRPNAME=`id -n -g`
CURRENT=`pwd`
#
# Are enough parameter available ?
#
if [ $# -ne 2 ]; then
  usage; exit 1
fi

#
# We create the stone with tode installed
#
createStone $1 $2
if [ ! -d "$GS_HOME/server/stones/$1" ]; then
  exit 1
fi
#
# If we have configuration files, then we copy it and stop the system
#
if [ -f "../../configuration/gem.conf" ]; then
  sudo cp ../../configuration/gem.conf "$GS_HOME/server/stones/$1/gem.conf"
  stopStone $1
fi
if [ -f "../../configuration/system.conf" ]; then
    sudo cp ../../configuration/system.conf "$GS_HOME/server/stones/$1/extents/system.conf"
    stopStone $1
fi

#
# Now restarting the stone with the new configuration values
#
startStone $1
#
# Still in unix-scripts directory
#
cd ..
export CURRENT=`pwd`
echo "Loading Third-Party libraries"
./pas_update_gemstone.sh $1
echo "Loading the PDF framework"
./pas_load_report4pdf.sh $1

echo "Loading GemConnect PostgreSQL"
./pas_load_postgresql.sh $1
cd $CURRENT
echo "Loading GemConnect RabbitMQ"
pwd
./pas_load_rabbitmq.sh $1
cd $CURRENT
echo "Loading PAS runtime"
./pas_load_runtime.sh $1
cd $CURRENT

stopStone $1


