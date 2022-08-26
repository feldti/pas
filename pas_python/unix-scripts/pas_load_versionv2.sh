#!/bin/bash
#
#
usage() {
  cat <<HELP

USAGE: $(basename $0) <version> <pumversion> <stone>

Importiert eine neue Modellversion (als TOPAZ-Quelltext) von

http://dev.projekt.tv/extfiles/gess/<version>/sources/webcati-modelsource-<pumversion>.sh

in den Stone mit dem Namen <stone>. Die Datei wird nach dem Herunterladen
noch von DOS nach Unix konvertiert.

EAXMPLES
  $(basename $0) v00 0_001 test365 

HELP
}

if [ $# -ne 3 ]; then
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

rm out.txt
curl $PAS_APP_PACKAGES/$PAS_APP_MODEL_TOPAZ_FILE-modelsource-$2.sh > $PAS_APP_MODEL_TOPAZ_FILE_$2.sh
dos2unix $PAS_APP_MODEL_TOPAZ_FILE_$2.sh
sudo chmod a+x $PAS_APP_MODEL_TOPAZ_FILE_$2.sh
./$PAS_APP_MODEL_TOPAZ_FILE_$2.sh $3 4000000 &>$PAS_APP_MODEL_TOPAZ_FILE_$2_out.txt
less $PAS_APP_MODEL_TOPAZ_FILE_$2_out.txt
