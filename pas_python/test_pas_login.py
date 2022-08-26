#!/usr/bin/env python3

import json
import pika
import argparse
import paslib.api
import paslib.swagger
from datetime import datetime

def createMessageStructure( pText: str, pLogLeve: str, ) -> paslib.api.TSTAPIParMessage:
    aTSTAPIPayloadLog = paslib.api.TSTAPIPayloadLog()
    aTSTAPIPayloadLog.whenAppTS = datetime.now()
    aTSTAPIPayloadLog.messageText = pText
    aTSTAPIPayloadLog.messageNumber = -1
    aTSTAPIPayloadLog.logLevelText = pLogLeve
    aTSTAPIPayloadLog.payloadClass = 'TSTAPIPayloadLog'

    aTSTAPIParAppMessage = paslib.api.TSTAPIParMessage()
    aTSTAPIParAppMessage.payload = client.serialize(aTSTAPIPayloadLog)
    aTSTAPIParAppMessage.payloadType = aTSTAPIPayloadLog.payloadClass
    aTSTAPIParAppMessage.vHost = "/"
    aTSTAPIParAppMessage.contentType = "application/json"
    aTSTAPIParAppMessage.exchange = "pas.log"

    return aTSTAPIParAppMessage

PGMNAME = "RabbitMQ Log File Logger Test"
PGMVERSION = "1.0"


parser = argparse.ArgumentParser(description='Process the arguments')
parser.add_argument('-s', type=str, dest='dbHostName', required=True, help='Hostname of computer')
parser.add_argument('-u', type=str, dest='account', required=True, help='login')
parser.add_argument('-p', type=str, dest='password', required=True, help='password')
args = parser.parse_args()


#
# Verbindung
#
client = paslib.swagger.ApiClient('', args.dbHostName)
client.debugOption = False
api = paslib.api.RESTApi(client)


aTSTAPIParNewSession = paslib.api.TSTAPIParNewSession()
aTSTAPIParNewSession.login = args.account
aTSTAPIParNewSession.password = args.password

aTSTAPIResSingleSession = api.NewSession( aTSTAPIParNewSession)
# print(json.dumps(client.serialize(aTSTAPIResSingleSession)))
if aTSTAPIResSingleSession.success:
    print("Login with success")
    api.RequestSessionID = aTSTAPIResSingleSession.session.gop
    for x in range(0, 1000):
        aTSTAPIParMessage = createMessageStructure( "Hello", paslib.api.TSTENUMAPPLOGLEVEL_LOGLEVELINFO)
        api.SendAppMessage(aTSTAPIParMessage)

    api.CloseSession()
else:
    print("Error Login " + json.dumps(client.serialize(aTSTAPIResSingleSession)))



