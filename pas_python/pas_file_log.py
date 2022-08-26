#!/usr/bin/env python3
import pika
import sys
import argparse
import logging
import logging.handlers
import paslib.api
import paslib.swagger
from datetime import datetime
import json

PGMNAME = "RabbitMQ Log File Logger"
PGMVERSION = "1.0"
APPLOGNAME = "app-logger"
CLLOCDATETIME = 26
CLLOCDATETIMEFMT = "{0:>"+str(CLLOCDATETIME) + "}"
CLLEVEL = 4
CLLEVELFMT = "{0:>"+str(CLLEVEL) + "}"
CLREMDATETIME = 27
CLREMDATETIMEFMT = "{0:>"+str(CLREMDATETIME) + "}"
CLAPPNAME = 18
CLAPPNAMEFMT = "{0:>"+str(CLAPPNAME) + "}"
CLSRCNAME = 18
CLSRCNAMEFMT = "{0:>"+str(CLSRCNAME) + "}"
CLSRCDATETIME = 30
CLSRCDATETIMEFMT = "{0:>"+str(CLSRCDATETIME) + "}"
CLAPPLOC = 15
CLAPPLOCFMT = "{0:>"+str(CLAPPLOC) + "}"
CLAPPCNT = 12
CLAPPCNTFMT = "{0:>"+str(CLAPPCNT) + "}"
CLLOCCNT = 10
CLLOCCNTFMT = "{0:>"+str(CLLOCCNT) + "}"

CLMSGTXT = 5
CLCLMSGTXTFMT = "{0:>"+str(CLMSGTXT) + "}"

localCounter = 0

def levelprint(pTSTAPIPayloadLog : paslib.api.TSTAPIPayloadLog ):
    global logger, localCounter, CLLOCDATETIMEFMT, CLLEVELFMT, CLREMDATETIMEFMT, CLAPPNAMEFMT, CLAPPLOCFMT, CLAPPCNTFMT, CLLOCCNTFMT
    msgNow = datetime.now()
    msgNowString = msgNow.strftime("%Y-%m-%dT%H:%M:%S.%f")
    level ="*?*"
    if pTSTAPIPayloadLog.logLevel == 2000:
        level = "*I*"
    elif pTSTAPIPayloadLog.logLevel == 6000:
        level = "*E*"
    elif pTSTAPIPayloadLog.logLevel == 4000:
        level = "*W*"
    elif pTSTAPIPayloadLog.logLevel == 1000:
        level = "*D*"

    msg =  CLLOCCNTFMT.format(localCounter) \
            + CLREMDATETIMEFMT.format(str(msgNowString)) \
            + ("{0:>"+str(4) + "}").format(level) \
            + ("{0:>"+str(5) + "}").format(pTSTAPIPayloadLog.logLevel) \
            + CLREMDATETIMEFMT.format(pTSTAPIPayloadLog.whenAppTS.strftime("%Y-%m-%dT%H:%M:%S.%f")) \
            + CLAPPNAMEFMT.format(pTSTAPIPayloadLog.appName) \
            + CLAPPCNTFMT.format(pTSTAPIPayloadLog.appLogCounter) \
            + ("{0:>"+str(40) + "}").format(pTSTAPIPayloadLog.srvAppName) \
            + CLAPPCNTFMT.format(pTSTAPIPayloadLog.srvAppLogCounter) \
            + ("{0:>"+str(15) + "}").format("?" if pTSTAPIPayloadLog.sessionID is None else pTSTAPIPayloadLog.sessionID) \
            + ("{0:>" + str(3) + "}").format("NL" if (pTSTAPIPayloadLog.logData is None or pTSTAPIPayloadLog.logData == "") else "LD") \
            + ("{0:>" + str(3) + "}").format("NS" if (pTSTAPIPayloadLog.stackTrace is None or pTSTAPIPayloadLog.stackTrace == "") else "ST") \
            + CLCLMSGTXTFMT.format(0 if pTSTAPIPayloadLog.messageNumber is None else pTSTAPIPayloadLog.messageNumber ) \
            + " : " \
            + pTSTAPIPayloadLog.messageText

    logger.log(logging.INFO, msg)
    if (pTSTAPIPayloadLog.stackTrace is not None and len(pTSTAPIPayloadLog.stackTrace) > 0):
        logger.log(logging.INFO, pTSTAPIPayloadLog.stackTrace)
    localCounter += 1
    return

def infoandprint(pString):
    global localCounter, APPLOGNAME
    levelprint(pString, logging.INFO, "", APPLOGNAME, "localhost", localCounter, APPLOGNAME, "")
    return

def callback(ch, method, properties, body):
    global localCounter, apiClient
    aTSTAPIMessageCarrier = apiClient.deserialize(json.loads(body), 'TSTAPIMessageCarrier')
    aTSTAPIPayloadLog = apiClient.deserialize(json.loads(aTSTAPIMessageCarrier.payload), aTSTAPIMessageCarrier.payloadType)
    levelprint(aTSTAPIPayloadLog)




parser = argparse.ArgumentParser(description='Process the arguments')
parser.add_argument('-s', type=str, dest='mqHostName', required=True, help='Hostname of computer')
parser.add_argument('-u', type=str, dest='account', required=True, help='login')
parser.add_argument('-p', type=str, dest='password', required=True, help='password')
parser.add_argument('-o', type=str, dest='port', required=True, help='Port of the connection')
parser.add_argument('-l', type=str, dest='logfile', required=False, help='set the path of the log file name')
parser.add_argument('-c', type=bool, dest='console', required=False, help='To turn on/off the console log')
parser.add_argument('-q', type=str, dest='mqPrefixName', required=True, help='defines the prefix in MQ names')
args = parser.parse_args()

#
# We need to use the client for json support based on swagger definitions
#
apiClient = paslib.swagger.ApiClient(apiKey = "dummy")
#
# Aufbereitung des Dateiloggers
#
logger = logging.getLogger("app_logging")
logger.setLevel(logging.DEBUG)
#
# Raw Format of the messager - I do all the stuff by myself
#
formatter = logging.Formatter(fmt="%(message)s")

if args.logfile is not None:
    handler = logging.handlers.TimedRotatingFileHandler(args.logfile, when='midnight',
                                                        backupCount=14)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

#
#
#
if args.console is not None and (args.console is True):
    console = logging.StreamHandler()
    console.setLevel(logging.NOTSET)
    console.setFormatter(formatter)
    logger.addHandler(console)

# Los gehts
logger.log(logging.INFO, PGMNAME + " " + PGMVERSION)

# Kontaktaufnahme mit RabbitMQ
credentials = pika.PlainCredentials(args.account, args.password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(args.mqHostName, args.port, "/", credentials ))
channel = connection.channel()


# Wir definieren einen Exchange - wenn er bereits vorhanden ist, egal
exchangeName = args.mqPrefixName + paslib.api.TSTENUMMQTARGETDEFINITION_LOG
channel.exchange_declare(exchange=exchangeName, exchange_type="fanout")
# Eine private Queue definieren
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
# Und diese an den Exchange binden
channel.queue_bind(exchange=exchangeName, queue=queue_name)

# Warten auf Telegramme
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

connection.close()
