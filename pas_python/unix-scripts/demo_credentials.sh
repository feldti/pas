#!/usr/bin/env bash
#

#
#
#
export PAS_STONE_NAME="test365_10"

#
# Options for starting the monitor task of Gemstone
#
export PAS_STONE_STATMON_START="true"
export PAS_STONE_STATMON_INTERVALL=30

#
# Settings for HTTP - scheduling via Apache, here are the local ports
#
export PAS_STONE_NORMAL_PORT=19000
export PAS_STONE_LONG_PORT=19100
export PAS_STONE_MEMORY_PORT=19200
export PAS_STONE_LIMITED_PORT=19300
export PAS_STONE_EXTDB_PORT=19400

export PAS_STONE_NORMAL_MEMORY=100000
export PAS_STONE_LONG_MEMORY=200000
export PAS_STONE_MEMORYMEMORY=500000
export PAS_STONE_LIMITEDMEMORY=200000
export PAS_STONE_EXTDBMEMORY=50000

#
# Public address of the API - consider the apache configuration file
#
export PAS_STONE_API_ADR="http://localhost"

#
# Should the NETLDI be started
#
export PAS_STONE_NETLDI="false"

#
#
# Points to a directory, where ALL the Monticello packages for the runtime can be found 
#
export PAS_RUNTIME_PACKAGES="http://<remote host>/pas_runtime/v80/sources"

#
# Application Specific stuff
#
export PAS_APP_MODEL_TOPAZ_FILE='test'
export PAS_APP_SERVICE_CLASS='TSTServiceClass'
export PAS_APP_PROJECT_CLASS='TSTProject'
export PAS_APP_TOPAPI_CLASS='TSTAPIGeneralObject'
export PAS_APP_TOPDOMAIN_CLASS='TSTGeneralDomain'
# e.g. TSTEnumErrorDefinition (from PUM) + LocaleErrorDefinition
export PAS_APP_ERROR_CLASS='TSTEnumErrorDefinitionLocaleErrorDefinition'
export PAS_APP_RESTCALL_CLASS='TSTRestClass'
export PAS_APP_DATA_CLASS='TestData'
export PAS_APP_PACKAGES="e.g. http://<remote host>/pum_apps/test/v00/sources/"
export PAS_APP_MDL_PACKAGE="Test"
export PAS_APP_EXT_PACKAGE="TestExtension"
export PAS_APP_SERVERTYPE="test-srvapp"
#
# migration file for the migration task
#
export PAS_STONE_MIGRATION_INSTANCES_FILE="$HOME/__temp_migration_classes.bm"


#
# Connection information for the RabbitMQ System
#
export PAS_APP_RMQ_ADR="<host>"
export PAS_APP_RMQ_PORT=5672
export PAS_APP_RMQ_ACCOUNT="<account>"
export PAS_APP_RMQ_PASSWD="<password>"
export PAS_APP_RMQ_VHOST="/"
export PAS_APP_TLS="false"
export PAS_APP_RMQ_PRVKEY="/home/mf/ssl/privkey.pem"
export PAS_APP_RMQ_CERT_PATH="/home/mf/ssl/fullchain.pem"
export PAS_APP_RMQ_CACERT_PATH="/home/mf/ssl/all_cacerts.pem"
export PAS_APP_RMQ_PREFIXNME="pas."


#
# Connection information for the PostgreSQL
#
export PAS_APP_PSQL_ADR="<host>"
export PAS_APP_PSQL_PORT=5432
export PAS_APP_PSQL_ACCOUNT="<pgsql account>"
export PAS_APP_PSQL_PASSWD="<pgsql password>"
export PAS_APP_PSQL_DBNAME="<pgsql dbname>"

#
# Special flags regarding used Ubuntu software. Check in bash scripot on
# non empty strings ...
#
export ULTS1804=`lsb_release -d | grep "Ubuntu 18.04 LTS"`
export ULTS2004=`lsb_release -d | grep "Ubuntu 20.04 LTS"`
export ULTS2204=`lsb_release -d | grep "Ubuntu 22.04 LTS"`

