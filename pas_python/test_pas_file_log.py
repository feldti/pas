#!/usr/bin/env python3

import json
import pika
import argparse
import paslib.api
import paslib.swagger
from datetime import datetime

PGMNAME = "RabbitMQ Log File Logger Test"
PGMVERSION = "1.0"


parser = argparse.ArgumentParser(description='Process the arguments')
parser.add_argument('-s', type=str, dest='mqHostName', required=True, help='Hostname of computer')
parser.add_argument('-u', type=str, dest='account', required=True, help='login')
parser.add_argument('-p', type=str, dest='password', required=True, help='password')
parser.add_argument('-o', type=str, dest='port', required=True, help='Port of the connection')
args = parser.parse_args()

# Kontaktaufnahme mit RabbitMQ
credentials = pika.PlainCredentials(args.account, args.password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(args.mqHostName, args.port, "/", credentials ))
channel = connection.channel()

# Wir definieren einen Exchange - wenn er bereits vorhanden ist, egal
channel.exchange_declare(exchange=paslib.api.TSTENUMMQTARGETDEFINITION_LOG, exchange_type="fanout")

message = paslib.api.TSTAPIMessageCarrier()

# Den Client benötigen wir nur für JSON Arbeiten
apiClient = paslib.swagger.ApiClient(apiKey = "dummy")





for i in range(1):
    logEntry = paslib.api.TSTAPIPayloadLog()
    logEntry.logLevel = 1
    logEntry.logLevelText = paslib.api.TSTENUMAPPLOGLEVEL_LOGLEVELINFO
    logEntry.payloadClass = "TSTAPIPayloadLog"
    logEntry.messageText = "Hallo - this is a test message with dummy log information: " + str(i)
    logEntry.whenAppTS =  datetime.now()
    logEntry.appLogCounter = i
    logEntry.appName = 'test_log'


    message = paslib.api.TSTAPIMessageCarrier()
    message.name = "evLog"
    message.payloadType = "TSTAPIPayloadLog"
    message.payload = json.dumps(apiClient.serialize(logEntry))

    messageBody = json.dumps(apiClient.serialize(message))
    channel.basic_publish(exchange=paslib.api.TSTENUMMQTARGETDEFINITION_LOG, routing_key='', body=messageBody)


connection.close()
