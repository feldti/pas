#!/usr/bin/env python
"""
    " Model-Version: '0.001'  "
    " Generator: 'Python3 (REST API Klassen, HTTP-RPC and Remote Database)' Version: '09.00.00-03.01.03' LastRun: '2022_08_22_08_59_37' "/**
*
* Summary:
*
*/

"""


PUM_PROJECT_VERSION = "0.001"
PUM_GENERATOR_VERSION = "09.00.00-03.01.03"


class TSTAPIMessageCarrier:
    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'payloadType': 'str',
            'payload': 'str'
        }
        self.name = None
        """:type : str"""
        self.payloadType = None
        """:type : str"""
        self.payload = None
        """:type : str"""


class TSTAPICustomerVisualInfo:
    def __init__(self):
        self.swaggerTypes = {
            'customerLoginName': 'str',
            'customerGop': 'int'
        }
        self.customerLoginName = None
        """:type : str"""
        self.customerGop = None
        """:type : int"""


class TSTAPIPayloadEvSessionChanged:
    def __init__(self):
        self.swaggerTypes = {
            'replyExchange': 'str',
            'replyRoutingKey': 'str',
            'payloadClass': 'str',
            'textInfo': 'str',
            'sessionGop': 'int',
            'serverAppType': 'str',
            'serverAppName': 'str'
        }
        self.replyExchange = None
        """:type : str"""
        self.replyRoutingKey = None
        """:type : str"""
        self.payloadClass = None
        """:type : str"""
        self.textInfo = None
        """:type : str"""
        self.sessionGop = None
        """:type : int"""
        self.serverAppType = None
        """:type : str"""
        self.serverAppName = None
        """:type : str"""


class TSTAPIPayloadLog:
    def __init__(self):
        self.swaggerTypes = {
            'replyExchange': 'str',
            'replyRoutingKey': 'str',
            'payloadClass': 'str',
            'rdbid': 'str',
            'cltcid': 'str',
            'whenAppTS': 'datetime',
            'whenLogSrvTS': 'datetime',
            'logLevel': 'int',
            'logLevelText': 'str',
            'stackTrace': 'str',
            'messageText': 'str',
            'messageNumber': 'int',
            'appLogCounter': 'int',
            'logAppCounter': 'int',
            'srvAppLogCounter': 'int',
            'srvAppTypeName': 'str',
            'srvAppName': 'str',
            'appName': 'str',
            'logData': 'str',
            'sessionID': 'str'
        }
        self.replyExchange = None
        """:type : str"""
        self.replyRoutingKey = None
        """:type : str"""
        self.payloadClass = None
        """:type : str"""
        self.rdbid = None
        """:type : str"""
        self.cltcid = None
        """:type : str"""
        self.whenAppTS = None
        """:type : datetime"""
        self.whenLogSrvTS = None
        """:type : datetime"""
        self.logLevel = None
        """:type : int"""
        self.logLevelText = None
        """:type : str"""
        self.stackTrace = None
        """:type : str"""
        self.messageText = None
        """:type : str"""
        self.messageNumber = None
        """:type : int"""
        self.appLogCounter = None
        """:type : int"""
        self.logAppCounter = None
        """:type : int"""
        self.srvAppLogCounter = None
        """:type : int"""
        self.srvAppTypeName = None
        """:type : str"""
        self.srvAppName = None
        """:type : str"""
        self.appName = None
        """:type : str"""
        self.logData = None
        """:type : str"""
        self.sessionID = None
        """:type : str"""


class TSTAPIPayloadEvSessionEntered:
    def __init__(self):
        self.swaggerTypes = {
            'replyExchange': 'str',
            'replyRoutingKey': 'str',
            'payloadClass': 'str',
            'textInfo': 'str',
            'sessionGop': 'int',
            'serverAppType': 'str',
            'serverAppName': 'str'
        }
        self.replyExchange = None
        """:type : str"""
        self.replyRoutingKey = None
        """:type : str"""
        self.payloadClass = None
        """:type : str"""
        self.textInfo = None
        """:type : str"""
        self.sessionGop = None
        """:type : int"""
        self.serverAppType = None
        """:type : str"""
        self.serverAppName = None
        """:type : str"""


class TSTAPIPayloadEvSessionClosed:
    def __init__(self):
        self.swaggerTypes = {
            'replyExchange': 'str',
            'replyRoutingKey': 'str',
            'payloadClass': 'str',
            'textInfo': 'str',
            'sessionGop': 'int',
            'serverAppType': 'str',
            'serverAppName': 'str'
        }
        self.replyExchange = None
        """:type : str"""
        self.replyRoutingKey = None
        """:type : str"""
        self.payloadClass = None
        """:type : str"""
        self.textInfo = None
        """:type : str"""
        self.sessionGop = None
        """:type : int"""
        self.serverAppType = None
        """:type : str"""
        self.serverAppName = None
        """:type : str"""


class TSTAPIPayloadSessionActivity:
    def __init__(self):
        self.swaggerTypes = {
            'replyExchange': 'str',
            'replyRoutingKey': 'str',
            'payloadClass': 'str',
            'lastActivityTS': 'datetime',
            'sessionGop': 'int'
        }
        self.replyExchange = None
        """:type : str"""
        self.replyRoutingKey = None
        """:type : str"""
        self.payloadClass = None
        """:type : str"""
        self.lastActivityTS = None
        """:type : datetime"""
        self.sessionGop = None
        """:type : int"""


class TSTAPILicenseInfo:
    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'info': 'str',
            'deathDate': 'date'
        }
        self.name = None
        """:type : str"""
        self.info = None
        """:type : str"""
        self.deathDate = None
        """:type : datetime"""


class TSTAPICustomerUserGroupListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIAppUserGroup]'
        }
        self.items = []
        """:type : list[TSTAPIAppUserGroup]"""


class TSTAPICustomerListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIAppCustomer]'
        }
        self.items = []
        """:type : list[TSTAPIAppCustomer]"""


class TSTAPIServerListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'server': 'list[TSTAPIServerDefinition]'
        }
        self.server = []
        """:type : list[TSTAPIServerDefinition]"""


class TSTAPIUserProjectMembershipListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIProjectUserMembership]'
        }
        self.items = []
        """:type : list[TSTAPIProjectUserMembership]"""


class TSTAPISessionListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIAppSession]'
        }
        self.items = []
        """:type : list[TSTAPIAppSession]"""


class TSTAPIUserListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIAppUser]'
        }
        self.items = []
        """:type : list[TSTAPIAppUser]"""


class TSTAPIProjectMembershipListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIProjectUserMembership]'
        }
        self.items = []
        """:type : list[TSTAPIProjectUserMembership]"""


class TSTAPIUserUserGroupMembershipListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIAppUserGroup]'
        }
        self.items = []
        """:type : list[TSTAPIAppUserGroup]"""


class TSTAPIUserGroupMembershipListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIAppUserGroup]'
        }
        self.items = []
        """:type : list[TSTAPIAppUserGroup]"""


class TSTAPICustomerProjectListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIAppProject]'
        }
        self.items = []
        """:type : list[TSTAPIAppProject]"""


class TSTAPIUpdateSessionActivityPL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPIPayloadSessionActivity]'
        }
        self.items = []
        """:type : list[TSTAPIPayloadSessionActivity]"""


class TSTAPILogNoticeListStorePL:
    def __init__(self):
        self.swaggerTypes = {
            'items': 'list[TSTAPILogNotice]'
        }
        self.items = []
        """:type : list[TSTAPILogNotice]"""


class TSTAPIGSStatisticInfo:
    def __init__(self):
        self.swaggerTypes = {
            'createdTS': 'datetime',
            'name': 'str',
            'value': 'str',
            'statisticGroup': 'str'
        }
        self.createdTS = None
        """:type : datetime"""
        self.name = None
        """:type : str"""
        self.value = None
        """:type : str"""
        self.statisticGroup = None
        """:type : str"""


class TSTAPIParLogListGC:
    def __init__(self):
        self.swaggerTypes = {
            'maxDays': 'int'
        }
        self.maxDays = None
        """:type : int"""


class TSTAPIParTerminateSession:
    def __init__(self):
        self.swaggerTypes = {
            'sessionGop': 'list[int]'
        }
        self.sessionGop = []
        """:type : int"""


class TSTAPIParRequestPendingSession:
    def __init__(self):
        self.swaggerTypes = {
            'serverAppType': 'str',
            'serverAppName': 'str',
            'internalCall': 'bool',
            'clientStartType': 'str'
        }
        self.serverAppType = None
        """:type : str"""
        self.serverAppName = None
        """:type : str"""
        self.internalCall = None
        """:type : bool"""
        self.clientStartType = None
        """:type : str"""


class TSTAPIParEnterSession:
    def __init__(self):
        self.swaggerTypes = {
            'sessionGop': 'int'
        }
        self.sessionGop = None
        """:type : int"""


class TSTAPIParSessionListGC:
    def __init__(self):
        self.swaggerTypes = {
            'maxDays': 'int'
        }
        self.maxDays = None
        """:type : int"""


class TSTAPIPagedRequest:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""


class TSTAPIPRProjectMembershipListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'projectGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.projectGop = None
        """:type : int"""


class TSTAPIPRCustomerListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""


class TSTAPIPRUserUserGroupMembershipListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'userGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.userGop = None
        """:type : int"""


class TSTAPIPRLicenseListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""


class TSTAPIPRUserGroupMembershipListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'userGroupGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.userGroupGop = None
        """:type : int"""


class TSTAPIPRServerListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'customerGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.customerGop = None
        """:type : int"""


class TSTAPIPRCustomerUserGroupListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'customerGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.customerGop = None
        """:type : int"""


class TSTAPIPRSessionListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""


class TSTAPIPRLogListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""


class TSTAPIPRVisInfoCustomerListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""


class TSTAPIPRLogNoticeListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'domainGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.domainGop = None
        """:type : int"""


class TSTAPIPRGSStatisticListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'statisticGroup': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.statisticGroup = None
        """:type : str"""


class TSTAPIPRUserProjectMembershipListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'userGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.userGop = None
        """:type : int"""


class TSTAPIPRUserListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'customerGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.customerGop = None
        """:type : int"""


class TSTAPIPRCustomerProjectListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str',
            'customerGop': 'int'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""
        self.customerGop = None
        """:type : int"""


class TSTAPIPRSoftwarePackageListStore:
    def __init__(self):
        self.swaggerTypes = {
            'limit': 'int',
            'start': 'int',
            'page': 'int',
            'gsquery': 'str',
            'sort': 'str',
            'filter': 'str'
        }
        self.limit = None
        """:type : int"""
        self.start = None
        """:type : int"""
        self.page = None
        """:type : int"""
        self.gsquery = None
        """:type : str"""
        self.sort = None
        """:type : str"""
        self.filter = None
        """:type : str"""


class TSTAPIParCheckPassword:
    def __init__(self):
        self.swaggerTypes = {
            'userGop': 'int',
            'userLogin': 'str',
            'password': 'str'
        }
        self.userGop = None
        """:type : int"""
        self.userLogin = None
        """:type : str"""
        self.password = None
        """:type : str"""


class TSTAPIParChangePassword:
    def __init__(self):
        self.swaggerTypes = {
            'userGop': 'int',
            'userLogin': 'str',
            'oldPassword': 'str',
            'newPassword': 'str'
        }
        self.userGop = None
        """:type : int"""
        self.userLogin = None
        """:type : str"""
        self.oldPassword = None
        """:type : str"""
        self.newPassword = None
        """:type : str"""


class TSTAPIChangeServerPasswordParameter:
    def __init__(self):
        self.swaggerTypes = {
            'newPassword': 'str',
            'serverGop': 'int'
        }
        self.newPassword = None
        """:type : str"""
        self.serverGop = None
        """:type : int"""


class TSTAPIParMessage:
    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'payloadType': 'str',
            'vHost': 'str',
            'deliveryMode': 'int',
            'contentType': 'str',
            'routingKey': 'str',
            'exchange': 'str',
            'correlationID': 'str',
            'payload': 'str'
        }
        self.name = None
        """:type : str"""
        self.payloadType = None
        """:type : str"""
        self.vHost = None
        """:type : str"""
        self.deliveryMode = None
        """:type : int"""
        self.contentType = None
        """:type : str"""
        self.routingKey = None
        """:type : str"""
        self.exchange = None
        """:type : str"""
        self.correlationID = None
        """:type : str"""
        self.payload = None
        """:type : str"""


class TSTAPIParNewSession:
    def __init__(self):
        self.swaggerTypes = {
            'login': 'str',
            'password': 'str',
            'applicationType': 'str',
            'customerLoginName': 'str'
        }
        self.login = None
        """:type : str"""
        self.password = None
        """:type : str"""
        self.applicationType = None
        """:type : str"""
        self.customerLoginName = None
        """:type : str"""


class TSTAPISoftwarePackageInfo:
    def __init__(self):
        self.swaggerTypes = {
            'name': 'str',
            'version': 'str'
        }
        self.name = None
        """:type : str"""
        self.version = None
        """:type : str"""


class TSTAPIError:
    def __init__(self):
        self.swaggerTypes = {
            'code': 'int',
            'errorText': 'str',
            'textPattern': 'str',
            'patternValues': 'list[str]'
        }
        self.code = None
        """:type : int"""
        self.errorText = None
        """:type : str"""
        self.textPattern = None
        """:type : str"""
        self.patternValues = []
        """:type : str"""


class TSTAPIAppProject:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'name': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.name = None
        """:type : str"""


class TSTAPIAppUserGroupMembership:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'userGroupGop': 'int',
            'userGroupName': 'str',
            'userLogin': 'str',
            'userGop': 'int'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.userGroupGop = None
        """:type : int"""
        self.userGroupName = None
        """:type : str"""
        self.userLogin = None
        """:type : str"""
        self.userGop = None
        """:type : int"""


class TSTAPIServerDefinition:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'dbName': 'str',
            'port': 'int',
            'apiKey': 'str',
            'vHost': 'str',
            'name': 'str',
            'serverAddress': 'str',
            'type': 'str',
            'enabled': 'bool',
            'hint': 'str',
            'description': 'str',
            'login': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.dbName = None
        """:type : str"""
        self.port = None
        """:type : int"""
        self.apiKey = None
        """:type : str"""
        self.vHost = None
        """:type : str"""
        self.name = None
        """:type : str"""
        self.serverAddress = None
        """:type : str"""
        self.type = None
        """:type : str"""
        self.enabled = None
        """:type : bool"""
        self.hint = None
        """:type : str"""
        self.description = None
        """:type : str"""
        self.login = None
        """:type : str"""


class TSTAPIAppUserGroup:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'name': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.name = None
        """:type : str"""


class TSTAPIAppSession:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'applicationType': 'str',
            'createdTS': 'datetime',
            'vHost': 'str',
            'replyExchange': 'str',
            'enteredTS': 'datetime',
            'expiration': 'datetime',
            'wsPassword': 'str',
            'currentLocale': 'str',
            'replyRoutingKey': 'str',
            'wsLogin': 'str',
            'defaultTimeout': 'int',
            'location': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.applicationType = None
        """:type : str"""
        self.createdTS = None
        """:type : datetime"""
        self.vHost = None
        """:type : str"""
        self.replyExchange = None
        """:type : str"""
        self.enteredTS = None
        """:type : datetime"""
        self.expiration = None
        """:type : datetime"""
        self.wsPassword = None
        """:type : str"""
        self.currentLocale = None
        """:type : str"""
        self.replyRoutingKey = None
        """:type : str"""
        self.wsLogin = None
        """:type : str"""
        self.defaultTimeout = None
        """:type : int"""
        self.location = None
        """:type : str"""


class TSTAPIAppUser:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'login': 'str',
            'personalName': 'str',
            'userRole': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.login = None
        """:type : str"""
        self.personalName = None
        """:type : str"""
        self.userRole = None
        """:type : str"""


class TSTAPIAppCustomer:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'cAndETimeoutS': 'int',
            'loginName': 'str',
            'name': 'str',
            'personalName': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.cAndETimeoutS = None
        """:type : int"""
        self.loginName = None
        """:type : str"""
        self.name = None
        """:type : str"""
        self.personalName = None
        """:type : str"""


class TSTAPIProjectUserMembership:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'userLogin': 'str',
            'userGop': 'int',
            'projectGop': 'int',
            'projectName': 'str',
            'userRole': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.userLogin = None
        """:type : str"""
        self.userGop = None
        """:type : int"""
        self.projectGop = None
        """:type : int"""
        self.projectName = None
        """:type : str"""
        self.userRole = None
        """:type : str"""


class TSTAPILogNotice:
    def __init__(self):
        self.swaggerTypes = {
            'syscid': 'str',
            'gop': 'int',
            'sysrev': 'int',
            'createdTS': 'datetime',
            'creator': 'str',
            'logType': 'str'
        }
        self.syscid = None
        """:type : str"""
        self.gop = None
        """:type : int"""
        self.sysrev = None
        """:type : int"""
        self.createdTS = None
        """:type : datetime"""
        self.creator = None
        """:type : str"""
        self.logType = None
        """:type : str"""


class TSTAPIGeneralResult:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""


class TSTAPIResSingleSession:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'session': 'TSTAPIAppSession'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.session = None
        """:type : TSTAPIAppSession"""


class TSTAPIVisInfoCustomerListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPICustomerVisualInfo]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPICustomerVisualInfo]"""


class TSTAPICustomerUserGroupListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIAppUserGroup]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIAppUserGroup]"""


class TSTAPISoftwarePackageListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'softwareInfo': 'list[TSTAPISoftwarePackageInfo]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.softwareInfo = []
        """:type : list[TSTAPISoftwarePackageInfo]"""


class TSTAPILogNoticeListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPILogNotice]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPILogNotice]"""


class TSTAPIUserUserGroupMembershipListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIAppUserGroup]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIAppUserGroup]"""


class TSTAPILogListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIPayloadLog]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIPayloadLog]"""


class TSTAPIUserListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIAppUser]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIAppUser]"""


class TSTAPILicenseListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'licenseInfo': 'list[TSTAPILicenseInfo]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.licenseInfo = []
        """:type : list[TSTAPILicenseInfo]"""


class TSTAPIUserProjectMembershipListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIProjectUserMembership]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIProjectUserMembership]"""


class TSTAPISessionListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIAppSession]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIAppSession]"""


class TSTAPIServerListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'server': 'list[TSTAPIServerDefinition]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.server = []
        """:type : list[TSTAPIServerDefinition]"""


class TSTAPIProjectMembershipListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIProjectUserMembership]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIProjectUserMembership]"""


class TSTAPIGSStatisticListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIGSStatisticInfo]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIGSStatisticInfo]"""


class TSTAPICustomerListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIAppCustomer]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIAppCustomer]"""


class TSTAPIUserGroupMembershipListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIAppUserGroup]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIAppUserGroup]"""


class TSTAPICustomerProjectListStoreRL:
    def __init__(self):
        self.swaggerTypes = {
            'dbgapi': 'str',
            'dbgloc': 'str',
            'dbgss': 'int',
            'dbgms': 'int',
            'dbts': 'datetime',
            'success': 'bool',
            'error': 'TSTAPIError',
            'total': 'int',
            'items': 'list[TSTAPIAppProject]'
        }
        self.dbgapi = None
        """:type : str"""
        self.dbgloc = None
        """:type : str"""
        self.dbgss = None
        """:type : int"""
        self.dbgms = None
        """:type : int"""
        self.dbts = None
        """:type : datetime"""
        self.success = None
        """:type : bool"""
        self.error = None
        """:type : TSTAPIError"""
        self.total = None
        """:type : int"""
        self.items = []
        """:type : list[TSTAPIAppProject]"""


TSTENUMAPPTYPE_ALL_VALUES = ['undefined']
TSTENUMAPPTYPE_UNDEFINED = 'undefined'

TSTENUMSERVERAPPTYPE_ALL_VALUES = ['undefined']
TSTENUMSERVERAPPTYPE_UNDEFINED = 'undefined'

TSTENUMERRORDEFINITION_ALL_VALUES = ['errCodeAccessDenied', 'errCodeGeneralError', 'errCodeMethodNotImplemented', 'errCodeParameterNotDefined', 'errCodeParameterWrongValue', 'errCodeRevisionConflict', 'errCodeSearchObjectNotFound', 'errCodeSearchObjectWrongClass', 'errCodeWrongUserOrLoginName']
TSTENUMERRORDEFINITION_ERRCODEACCESSDENIED = 'errCodeAccessDenied'
TSTENUMERRORDEFINITION_ERRCODEGENERALERROR = 'errCodeGeneralError'
TSTENUMERRORDEFINITION_ERRCODEMETHODNOTIMPLEMENTED = 'errCodeMethodNotImplemented'
TSTENUMERRORDEFINITION_ERRCODEPARAMETERNOTDEFINED = 'errCodeParameterNotDefined'
TSTENUMERRORDEFINITION_ERRCODEPARAMETERWRONGVALUE = 'errCodeParameterWrongValue'
TSTENUMERRORDEFINITION_ERRCODEREVISIONCONFLICT = 'errCodeRevisionConflict'
TSTENUMERRORDEFINITION_ERRCODESEARCHOBJECTNOTFOUND = 'errCodeSearchObjectNotFound'
TSTENUMERRORDEFINITION_ERRCODESEARCHOBJECTWRONGCLASS = 'errCodeSearchObjectWrongClass'
TSTENUMERRORDEFINITION_ERRCODEWRONGUSERORLOGINNAME = 'errCodeWrongUserOrLoginName'

TSTENUMMQTARGETDEFINITION_ALL_VALUES = ['eventBus', 'log', 'serverEventBus', 'sessionActivity', 'undefined']
TSTENUMMQTARGETDEFINITION_EVENTBUS = 'eventBus'
TSTENUMMQTARGETDEFINITION_LOG = 'log'
TSTENUMMQTARGETDEFINITION_SERVEREVENTBUS = 'serverEventBus'
TSTENUMMQTARGETDEFINITION_SESSIONACTIVITY = 'sessionActivity'
TSTENUMMQTARGETDEFINITION_UNDEFINED = 'undefined'

TSTENUMMQEVENTDEFINITION_ALL_VALUES = ['evChangedSession', 'evCloseSession', 'evEnterSession', 'evLog', 'evNewSessionRequest', 'evSessionActivity']
TSTENUMMQEVENTDEFINITION_EVCHANGEDSESSION = 'evChangedSession'
TSTENUMMQEVENTDEFINITION_EVCLOSESESSION = 'evCloseSession'
TSTENUMMQEVENTDEFINITION_EVENTERSESSION = 'evEnterSession'
TSTENUMMQEVENTDEFINITION_EVLOG = 'evLog'
TSTENUMMQEVENTDEFINITION_EVNEWSESSIONREQUEST = 'evNewSessionRequest'
TSTENUMMQEVENTDEFINITION_EVSESSIONACTIVITY = 'evSessionActivity'

TSTENUMPROJECTUSERROLE_ALL_VALUES = ['admin', 'user']
TSTENUMPROJECTUSERROLE_ADMIN = 'admin'
TSTENUMPROJECTUSERROLE_USER = 'user'

TSTENUMCLIENTSTARTTYPE_ALL_VALUES = ['fork', 'replace']
TSTENUMCLIENTSTARTTYPE_FORK = 'fork'
TSTENUMCLIENTSTARTTYPE_REPLACE = 'replace'

TSTENUMSIMPLEUSERROLE_ALL_VALUES = ['admin', 'customerAdmin', 'user']
TSTENUMSIMPLEUSERROLE_ADMIN = 'admin'
TSTENUMSIMPLEUSERROLE_CUSTOMERADMIN = 'customerAdmin'
TSTENUMSIMPLEUSERROLE_USER = 'user'

TSTENUMMQEXCHANGEDEFINITION_ALL_VALUES = ['amqDirect', 'amqFanout', 'amqHeaders', 'amqTopic']
TSTENUMMQEXCHANGEDEFINITION_AMQDIRECT = 'amqDirect'
TSTENUMMQEXCHANGEDEFINITION_AMQFANOUT = 'amqFanout'
TSTENUMMQEXCHANGEDEFINITION_AMQHEADERS = 'amqHeaders'
TSTENUMMQEXCHANGEDEFINITION_AMQTOPIC = 'amqTopic'

TSTENUMGEMSTONESTATISTIC_ALL_VALUES = ['clientVersion', 'gemConfig', 'process', 'stoneConfig', 'stoneVersion', 'system']
TSTENUMGEMSTONESTATISTIC_CLIENTVERSION = 'clientVersion'
TSTENUMGEMSTONESTATISTIC_GEMCONFIG = 'gemConfig'
TSTENUMGEMSTONESTATISTIC_PROCESS = 'process'
TSTENUMGEMSTONESTATISTIC_STONECONFIG = 'stoneConfig'
TSTENUMGEMSTONESTATISTIC_STONEVERSION = 'stoneVersion'
TSTENUMGEMSTONESTATISTIC_SYSTEM = 'system'

TSTENUMAPPLOGLEVEL_ALL_VALUES = ['logLevelDebug', 'logLevelError', 'logLevelInfo', 'logLevelWarning']
TSTENUMAPPLOGLEVEL_LOGLEVELDEBUG = 'logLevelDebug'
TSTENUMAPPLOGLEVEL_LOGLEVELERROR = 'logLevelError'
TSTENUMAPPLOGLEVEL_LOGLEVELINFO = 'logLevelInfo'
TSTENUMAPPLOGLEVEL_LOGLEVELWARNING = 'logLevelWarning'

TSTENUMSERVERTYPE_ALL_VALUES = ['imap', 'pop3', 'psql', 'rabbitmq', 'smtp', 'unknown']
TSTENUMSERVERTYPE_IMAP = 'imap'
TSTENUMSERVERTYPE_POP3 = 'pop3'
TSTENUMSERVERTYPE_PSQL = 'psql'
TSTENUMSERVERTYPE_RABBITMQ = 'rabbitmq'
TSTENUMSERVERTYPE_SMTP = 'smtp'
TSTENUMSERVERTYPE_UNKNOWN = 'unknown'

TSTENUMLOGNOTICETYPE_ALL_VALUES = ['info']
TSTENUMLOGNOTICETYPE_INFO = 'info'


class RESTApi(object):
    def __init__(self, apiclient ):
        self.apiClient = apiclient
        self.RequestSessionID = 'DUMMY'
        self.BaseURL = apiclient.apiServer

    #
    # The constant  "CustomerProjectListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerProjectList"
    #
    CustomerProjectListCreateBaseURL = "/tst/v1/normal/a/CustomerProjectListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerProjectList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerProjectListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerProjectListCreateBaseURL  + str(self.RequestSessionID)
    def CustomerProjectListCreate(self, body: TSTAPICustomerProjectListStorePL, **kwargs) -> TSTAPICustomerProjectListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerProjectListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerProjectListStoreRL')
        return response_object

    def customer_project_list_create(self, body: TSTAPICustomerProjectListStorePL, **kwargs) -> TSTAPICustomerProjectListStoreRL:
        return self.CustomerProjectListCreate(body, **kwargs)

    #
    # The constant  "CustomerProjectListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerProjectList"
    #
    CustomerProjectListDestroyBaseURL = "/tst/v1/normal/a/CustomerProjectListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerProjectList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerProjectListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerProjectListDestroyBaseURL  + str(self.RequestSessionID)
    def CustomerProjectListDestroy(self, body: TSTAPICustomerProjectListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerProjectListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def customer_project_list_destroy(self, body: TSTAPICustomerProjectListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.CustomerProjectListDestroy(body, **kwargs)

    #
    # The constant  "CustomerProjectListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerProjectList"
    #
    CustomerProjectListUpdateBaseURL = "/tst/v1/normal/a/CustomerProjectListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerProjectList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerProjectListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerProjectListUpdateBaseURL  + str(self.RequestSessionID)
    def CustomerProjectListUpdate(self, body: TSTAPICustomerProjectListStorePL, **kwargs) -> TSTAPICustomerProjectListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerProjectListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerProjectListStoreRL')
        return response_object

    def customer_project_list_update(self, body: TSTAPICustomerProjectListStorePL, **kwargs) -> TSTAPICustomerProjectListStoreRL:
        return self.CustomerProjectListUpdate(body, **kwargs)

    #
    # The constant  "CustomerProjectListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerProjectList"
    #
    CustomerProjectListReadBaseURL = "/tst/v1/normal/a/CustomerProjectListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerProjectList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerProjectListReadURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerProjectListReadBaseURL  + str(self.RequestSessionID)
    def CustomerProjectListRead(self, body: TSTAPIPRCustomerProjectListStore, **kwargs) -> TSTAPICustomerProjectListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerProjectListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerProjectListStoreRL')
        return response_object

    def customer_project_list_read(self, body: TSTAPIPRCustomerProjectListStore, **kwargs) -> TSTAPICustomerProjectListStoreRL:
        return self.CustomerProjectListRead(body, **kwargs)

    #
    # The constant  "ProjectMembershipListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ProjectMembershipList"
    #
    ProjectMembershipListCreateBaseURL = "/tst/v1/normal/a/ProjectMembershipListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def ProjectMembershipListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.ProjectMembershipListCreateBaseURL  + str(self.RequestSessionID)
    def ProjectMembershipListCreate(self, body: TSTAPIProjectMembershipListStorePL, **kwargs) -> TSTAPIProjectMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ProjectMembershipListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIProjectMembershipListStoreRL')
        return response_object

    def project_membership_list_create(self, body: TSTAPIProjectMembershipListStorePL, **kwargs) -> TSTAPIProjectMembershipListStoreRL:
        return self.ProjectMembershipListCreate(body, **kwargs)

    #
    # The constant  "ProjectMembershipListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ProjectMembershipList"
    #
    ProjectMembershipListDestroyBaseURL = "/tst/v1/normal/a/ProjectMembershipListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def ProjectMembershipListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.ProjectMembershipListDestroyBaseURL  + str(self.RequestSessionID)
    def ProjectMembershipListDestroy(self, body: TSTAPIProjectMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ProjectMembershipListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def project_membership_list_destroy(self, body: TSTAPIProjectMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.ProjectMembershipListDestroy(body, **kwargs)

    #
    # The constant  "ProjectMembershipListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ProjectMembershipList"
    #
    ProjectMembershipListUpdateBaseURL = "/tst/v1/normal/a/ProjectMembershipListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def ProjectMembershipListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.ProjectMembershipListUpdateBaseURL  + str(self.RequestSessionID)
    def ProjectMembershipListUpdate(self, body: TSTAPIProjectMembershipListStorePL, **kwargs) -> TSTAPIProjectMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ProjectMembershipListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIProjectMembershipListStoreRL')
        return response_object

    def project_membership_list_update(self, body: TSTAPIProjectMembershipListStorePL, **kwargs) -> TSTAPIProjectMembershipListStoreRL:
        return self.ProjectMembershipListUpdate(body, **kwargs)

    #
    # The constant  "ProjectMembershipListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ProjectMembershipList"
    #
    ProjectMembershipListReadBaseURL = "/tst/v1/normal/a/ProjectMembershipListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def ProjectMembershipListReadURL(self) -> str:
        return self.BaseURL + RESTApi.ProjectMembershipListReadBaseURL  + str(self.RequestSessionID)
    def ProjectMembershipListRead(self, body: TSTAPIPRProjectMembershipListStore, **kwargs) -> TSTAPIProjectMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ProjectMembershipListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIProjectMembershipListStoreRL')
        return response_object

    def project_membership_list_read(self, body: TSTAPIPRProjectMembershipListStore, **kwargs) -> TSTAPIProjectMembershipListStoreRL:
        return self.ProjectMembershipListRead(body, **kwargs)

    #
    # The constant  "UserProjectMembershipListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserProjectMembershipList"
    #
    UserProjectMembershipListCreateBaseURL = "/tst/v1/normal/a/UserProjectMembershipListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserProjectMembershipListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.UserProjectMembershipListCreateBaseURL  + str(self.RequestSessionID)
    def UserProjectMembershipListCreate(self, body: TSTAPIUserProjectMembershipListStorePL, **kwargs) -> TSTAPIUserProjectMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserProjectMembershipListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserProjectMembershipListStoreRL')
        return response_object

    def user_project_membership_list_create(self, body: TSTAPIUserProjectMembershipListStorePL, **kwargs) -> TSTAPIUserProjectMembershipListStoreRL:
        return self.UserProjectMembershipListCreate(body, **kwargs)

    #
    # The constant  "UserProjectMembershipListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserProjectMembershipList"
    #
    UserProjectMembershipListDestroyBaseURL = "/tst/v1/normal/a/UserProjectMembershipListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserProjectMembershipListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.UserProjectMembershipListDestroyBaseURL  + str(self.RequestSessionID)
    def UserProjectMembershipListDestroy(self, body: TSTAPIUserProjectMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserProjectMembershipListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def user_project_membership_list_destroy(self, body: TSTAPIUserProjectMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.UserProjectMembershipListDestroy(body, **kwargs)

    #
    # The constant  "UserProjectMembershipListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserProjectMembershipList"
    #
    UserProjectMembershipListUpdateBaseURL = "/tst/v1/normal/a/UserProjectMembershipListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserProjectMembershipListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.UserProjectMembershipListUpdateBaseURL  + str(self.RequestSessionID)
    def UserProjectMembershipListUpdate(self, body: TSTAPIUserProjectMembershipListStorePL, **kwargs) -> TSTAPIUserProjectMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserProjectMembershipListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserProjectMembershipListStoreRL')
        return response_object

    def user_project_membership_list_update(self, body: TSTAPIUserProjectMembershipListStorePL, **kwargs) -> TSTAPIUserProjectMembershipListStoreRL:
        return self.UserProjectMembershipListUpdate(body, **kwargs)

    #
    # The constant  "UserProjectMembershipListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserProjectMembershipList"
    #
    UserProjectMembershipListReadBaseURL = "/tst/v1/normal/a/UserProjectMembershipListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserProjectMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserProjectMembershipListReadURL(self) -> str:
        return self.BaseURL + RESTApi.UserProjectMembershipListReadBaseURL  + str(self.RequestSessionID)
    def UserProjectMembershipListRead(self, body: TSTAPIPRUserProjectMembershipListStore, **kwargs) -> TSTAPIUserProjectMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserProjectMembershipListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserProjectMembershipListStoreRL')
        return response_object

    def user_project_membership_list_read(self, body: TSTAPIPRUserProjectMembershipListStore, **kwargs) -> TSTAPIUserProjectMembershipListStoreRL:
        return self.UserProjectMembershipListRead(body, **kwargs)

    #
    # The constant  "SendAppMessageURL" holds the base URL - with session parameter, but exluding the session information - for the API call "SendAppMessage"
    #
    SendAppMessageBaseURL = "/tst/v1/normal/a/SendAppMessage?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "SendAppMessage"
    #
    # @return string - containing the URL for this API call
    #
    def SendAppMessageURL(self) -> str:
        return self.BaseURL + RESTApi.SendAppMessageBaseURL  + str(self.RequestSessionID)
    def SendAppMessage(self, body: TSTAPIParMessage, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.SendAppMessageURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def send_app_message(self, body: TSTAPIParMessage, **kwargs) -> TSTAPIGeneralResult:
        return self.SendAppMessage(body, **kwargs)

    #
    # The constant  "ServerListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ServerList"
    #
    ServerListCreateBaseURL = "/tst/v1/normal/a/ServerListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ServerList"
    #
    # @return string - containing the URL for this API call
    #
    def ServerListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.ServerListCreateBaseURL  + str(self.RequestSessionID)
    def ServerListCreate(self, body: TSTAPIServerListStorePL, **kwargs) -> TSTAPIServerListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ServerListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIServerListStoreRL')
        return response_object

    def server_list_create(self, body: TSTAPIServerListStorePL, **kwargs) -> TSTAPIServerListStoreRL:
        return self.ServerListCreate(body, **kwargs)

    #
    # The constant  "ServerListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ServerList"
    #
    ServerListDestroyBaseURL = "/tst/v1/normal/a/ServerListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ServerList"
    #
    # @return string - containing the URL for this API call
    #
    def ServerListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.ServerListDestroyBaseURL  + str(self.RequestSessionID)
    def ServerListDestroy(self, body: TSTAPIServerListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ServerListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def server_list_destroy(self, body: TSTAPIServerListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.ServerListDestroy(body, **kwargs)

    #
    # The constant  "ServerListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ServerList"
    #
    ServerListUpdateBaseURL = "/tst/v1/normal/a/ServerListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ServerList"
    #
    # @return string - containing the URL for this API call
    #
    def ServerListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.ServerListUpdateBaseURL  + str(self.RequestSessionID)
    def ServerListUpdate(self, body: TSTAPIServerListStorePL, **kwargs) -> TSTAPIServerListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ServerListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIServerListStoreRL')
        return response_object

    def server_list_update(self, body: TSTAPIServerListStorePL, **kwargs) -> TSTAPIServerListStoreRL:
        return self.ServerListUpdate(body, **kwargs)

    #
    # The constant  "ServerListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ServerList"
    #
    ServerListReadBaseURL = "/tst/v1/normal/a/ServerListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ServerList"
    #
    # @return string - containing the URL for this API call
    #
    def ServerListReadURL(self) -> str:
        return self.BaseURL + RESTApi.ServerListReadBaseURL  + str(self.RequestSessionID)
    def ServerListRead(self, body: TSTAPIPRServerListStore, **kwargs) -> TSTAPIServerListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.ServerListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIServerListStoreRL')
        return response_object

    def server_list_read(self, body: TSTAPIPRServerListStore, **kwargs) -> TSTAPIServerListStoreRL:
        return self.ServerListRead(body, **kwargs)

    #
    # The constant  "ChangeServerPasswordURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ChangeServerPassword"
    #
    ChangeServerPasswordBaseURL = "/tst/v1/normal/a/ChangeServerPassword?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ChangeServerPassword"
    #
    # @return string - containing the URL for this API call
    #
    def ChangeServerPasswordURL(self) -> str:
        return self.BaseURL + RESTApi.ChangeServerPasswordBaseURL  + str(self.RequestSessionID)
    def ChangeServerPassword(self, body: TSTAPIChangeServerPasswordParameter, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.ChangeServerPasswordURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def change_server_password(self, body: TSTAPIChangeServerPasswordParameter, **kwargs) -> TSTAPIGeneralResult:
        return self.ChangeServerPassword(body, **kwargs)

    #
    # The constant  "CustomerListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerList"
    #
    CustomerListCreateBaseURL = "/tst/v1/normal/a/CustomerListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerListCreateBaseURL  + str(self.RequestSessionID)
    def CustomerListCreate(self, body: TSTAPICustomerListStorePL, **kwargs) -> TSTAPICustomerListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerListStoreRL')
        return response_object

    def customer_list_create(self, body: TSTAPICustomerListStorePL, **kwargs) -> TSTAPICustomerListStoreRL:
        return self.CustomerListCreate(body, **kwargs)

    #
    # The constant  "CustomerListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerList"
    #
    CustomerListDestroyBaseURL = "/tst/v1/normal/a/CustomerListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerListDestroyBaseURL  + str(self.RequestSessionID)
    def CustomerListDestroy(self, body: TSTAPICustomerListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def customer_list_destroy(self, body: TSTAPICustomerListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.CustomerListDestroy(body, **kwargs)

    #
    # The constant  "CustomerListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerList"
    #
    CustomerListUpdateBaseURL = "/tst/v1/normal/a/CustomerListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerListUpdateBaseURL  + str(self.RequestSessionID)
    def CustomerListUpdate(self, body: TSTAPICustomerListStorePL, **kwargs) -> TSTAPICustomerListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerListStoreRL')
        return response_object

    def customer_list_update(self, body: TSTAPICustomerListStorePL, **kwargs) -> TSTAPICustomerListStoreRL:
        return self.CustomerListUpdate(body, **kwargs)

    #
    # The constant  "CustomerListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerList"
    #
    CustomerListReadBaseURL = "/tst/v1/normal/a/CustomerListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerListReadURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerListReadBaseURL  + str(self.RequestSessionID)
    def CustomerListRead(self, body: TSTAPIPRCustomerListStore, **kwargs) -> TSTAPICustomerListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerListStoreRL')
        return response_object

    def customer_list_read(self, body: TSTAPIPRCustomerListStore, **kwargs) -> TSTAPICustomerListStoreRL:
        return self.CustomerListRead(body, **kwargs)

    #
    # The constant  "VisInfoCustomerListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "VisInfoCustomerList"
    #
    VisInfoCustomerListReadBaseURL = "/tst/v1/normal/a/VisInfoCustomerListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "VisInfoCustomerList"
    #
    # @return string - containing the URL for this API call
    #
    def VisInfoCustomerListReadURL(self) -> str:
        return self.BaseURL + RESTApi.VisInfoCustomerListReadBaseURL  + str(self.RequestSessionID)
    def VisInfoCustomerListRead(self, body: TSTAPIPRVisInfoCustomerListStore, **kwargs) -> TSTAPIVisInfoCustomerListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.VisInfoCustomerListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIVisInfoCustomerListStoreRL')
        return response_object

    def vis_info_customer_list_read(self, body: TSTAPIPRVisInfoCustomerListStore, **kwargs) -> TSTAPIVisInfoCustomerListStoreRL:
        return self.VisInfoCustomerListRead(body, **kwargs)

    #
    # The constant  "CustomerUserGroupListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerUserGroupList"
    #
    CustomerUserGroupListCreateBaseURL = "/tst/v1/normal/a/CustomerUserGroupListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerUserGroupList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerUserGroupListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerUserGroupListCreateBaseURL  + str(self.RequestSessionID)
    def CustomerUserGroupListCreate(self, body: TSTAPICustomerUserGroupListStorePL, **kwargs) -> TSTAPICustomerUserGroupListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerUserGroupListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerUserGroupListStoreRL')
        return response_object

    def customer_user_group_list_create(self, body: TSTAPICustomerUserGroupListStorePL, **kwargs) -> TSTAPICustomerUserGroupListStoreRL:
        return self.CustomerUserGroupListCreate(body, **kwargs)

    #
    # The constant  "CustomerUserGroupListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerUserGroupList"
    #
    CustomerUserGroupListDestroyBaseURL = "/tst/v1/normal/a/CustomerUserGroupListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerUserGroupList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerUserGroupListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerUserGroupListDestroyBaseURL  + str(self.RequestSessionID)
    def CustomerUserGroupListDestroy(self, body: TSTAPICustomerUserGroupListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerUserGroupListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def customer_user_group_list_destroy(self, body: TSTAPICustomerUserGroupListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.CustomerUserGroupListDestroy(body, **kwargs)

    #
    # The constant  "CustomerUserGroupListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerUserGroupList"
    #
    CustomerUserGroupListUpdateBaseURL = "/tst/v1/normal/a/CustomerUserGroupListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerUserGroupList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerUserGroupListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerUserGroupListUpdateBaseURL  + str(self.RequestSessionID)
    def CustomerUserGroupListUpdate(self, body: TSTAPICustomerUserGroupListStorePL, **kwargs) -> TSTAPICustomerUserGroupListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerUserGroupListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerUserGroupListStoreRL')
        return response_object

    def customer_user_group_list_update(self, body: TSTAPICustomerUserGroupListStorePL, **kwargs) -> TSTAPICustomerUserGroupListStoreRL:
        return self.CustomerUserGroupListUpdate(body, **kwargs)

    #
    # The constant  "CustomerUserGroupListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CustomerUserGroupList"
    #
    CustomerUserGroupListReadBaseURL = "/tst/v1/normal/a/CustomerUserGroupListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CustomerUserGroupList"
    #
    # @return string - containing the URL for this API call
    #
    def CustomerUserGroupListReadURL(self) -> str:
        return self.BaseURL + RESTApi.CustomerUserGroupListReadBaseURL  + str(self.RequestSessionID)
    def CustomerUserGroupListRead(self, body: TSTAPIPRCustomerUserGroupListStore, **kwargs) -> TSTAPICustomerUserGroupListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.CustomerUserGroupListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPICustomerUserGroupListStoreRL')
        return response_object

    def customer_user_group_list_read(self, body: TSTAPIPRCustomerUserGroupListStore, **kwargs) -> TSTAPICustomerUserGroupListStoreRL:
        return self.CustomerUserGroupListRead(body, **kwargs)

    #
    # The constant  "UserUserGroupMembershipListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserUserGroupMembershipList"
    #
    UserUserGroupMembershipListCreateBaseURL = "/tst/v1/normal/a/UserUserGroupMembershipListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserUserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserUserGroupMembershipListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.UserUserGroupMembershipListCreateBaseURL  + str(self.RequestSessionID)
    def UserUserGroupMembershipListCreate(self, body: TSTAPIUserUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserUserGroupMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserUserGroupMembershipListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserUserGroupMembershipListStoreRL')
        return response_object

    def user_user_group_membership_list_create(self, body: TSTAPIUserUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserUserGroupMembershipListStoreRL:
        return self.UserUserGroupMembershipListCreate(body, **kwargs)

    #
    # The constant  "UserUserGroupMembershipListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserUserGroupMembershipList"
    #
    UserUserGroupMembershipListDestroyBaseURL = "/tst/v1/normal/a/UserUserGroupMembershipListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserUserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserUserGroupMembershipListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.UserUserGroupMembershipListDestroyBaseURL  + str(self.RequestSessionID)
    def UserUserGroupMembershipListDestroy(self, body: TSTAPIUserUserGroupMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserUserGroupMembershipListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def user_user_group_membership_list_destroy(self, body: TSTAPIUserUserGroupMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.UserUserGroupMembershipListDestroy(body, **kwargs)

    #
    # The constant  "UserUserGroupMembershipListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserUserGroupMembershipList"
    #
    UserUserGroupMembershipListUpdateBaseURL = "/tst/v1/normal/a/UserUserGroupMembershipListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserUserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserUserGroupMembershipListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.UserUserGroupMembershipListUpdateBaseURL  + str(self.RequestSessionID)
    def UserUserGroupMembershipListUpdate(self, body: TSTAPIUserUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserUserGroupMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserUserGroupMembershipListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserUserGroupMembershipListStoreRL')
        return response_object

    def user_user_group_membership_list_update(self, body: TSTAPIUserUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserUserGroupMembershipListStoreRL:
        return self.UserUserGroupMembershipListUpdate(body, **kwargs)

    #
    # The constant  "UserUserGroupMembershipListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserUserGroupMembershipList"
    #
    UserUserGroupMembershipListReadBaseURL = "/tst/v1/normal/a/UserUserGroupMembershipListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserUserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserUserGroupMembershipListReadURL(self) -> str:
        return self.BaseURL + RESTApi.UserUserGroupMembershipListReadBaseURL  + str(self.RequestSessionID)
    def UserUserGroupMembershipListRead(self, body: TSTAPIPRUserUserGroupMembershipListStore, **kwargs) -> TSTAPIUserUserGroupMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserUserGroupMembershipListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserUserGroupMembershipListStoreRL')
        return response_object

    def user_user_group_membership_list_read(self, body: TSTAPIPRUserUserGroupMembershipListStore, **kwargs) -> TSTAPIUserUserGroupMembershipListStoreRL:
        return self.UserUserGroupMembershipListRead(body, **kwargs)

    #
    # The constant  "UserGroupMembershipListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserGroupMembershipList"
    #
    UserGroupMembershipListCreateBaseURL = "/tst/v1/normal/a/UserGroupMembershipListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserGroupMembershipListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.UserGroupMembershipListCreateBaseURL  + str(self.RequestSessionID)
    def UserGroupMembershipListCreate(self, body: TSTAPIUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserGroupMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserGroupMembershipListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserGroupMembershipListStoreRL')
        return response_object

    def user_group_membership_list_create(self, body: TSTAPIUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserGroupMembershipListStoreRL:
        return self.UserGroupMembershipListCreate(body, **kwargs)

    #
    # The constant  "UserGroupMembershipListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserGroupMembershipList"
    #
    UserGroupMembershipListDestroyBaseURL = "/tst/v1/normal/a/UserGroupMembershipListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserGroupMembershipListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.UserGroupMembershipListDestroyBaseURL  + str(self.RequestSessionID)
    def UserGroupMembershipListDestroy(self, body: TSTAPIUserGroupMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserGroupMembershipListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def user_group_membership_list_destroy(self, body: TSTAPIUserGroupMembershipListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.UserGroupMembershipListDestroy(body, **kwargs)

    #
    # The constant  "UserGroupMembershipListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserGroupMembershipList"
    #
    UserGroupMembershipListUpdateBaseURL = "/tst/v1/normal/a/UserGroupMembershipListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserGroupMembershipListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.UserGroupMembershipListUpdateBaseURL  + str(self.RequestSessionID)
    def UserGroupMembershipListUpdate(self, body: TSTAPIUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserGroupMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserGroupMembershipListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserGroupMembershipListStoreRL')
        return response_object

    def user_group_membership_list_update(self, body: TSTAPIUserGroupMembershipListStorePL, **kwargs) -> TSTAPIUserGroupMembershipListStoreRL:
        return self.UserGroupMembershipListUpdate(body, **kwargs)

    #
    # The constant  "UserGroupMembershipListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserGroupMembershipList"
    #
    UserGroupMembershipListReadBaseURL = "/tst/v1/normal/a/UserGroupMembershipListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserGroupMembershipList"
    #
    # @return string - containing the URL for this API call
    #
    def UserGroupMembershipListReadURL(self) -> str:
        return self.BaseURL + RESTApi.UserGroupMembershipListReadBaseURL  + str(self.RequestSessionID)
    def UserGroupMembershipListRead(self, body: TSTAPIPRUserGroupMembershipListStore, **kwargs) -> TSTAPIUserGroupMembershipListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserGroupMembershipListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserGroupMembershipListStoreRL')
        return response_object

    def user_group_membership_list_read(self, body: TSTAPIPRUserGroupMembershipListStore, **kwargs) -> TSTAPIUserGroupMembershipListStoreRL:
        return self.UserGroupMembershipListRead(body, **kwargs)

    #
    # The constant  "GSStatisticListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "GSStatisticList"
    #
    GSStatisticListReadBaseURL = "/tst/v1/normal/a/GSStatisticListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "GSStatisticList"
    #
    # @return string - containing the URL for this API call
    #
    def GSStatisticListReadURL(self) -> str:
        return self.BaseURL + RESTApi.GSStatisticListReadBaseURL  + str(self.RequestSessionID)
    def GSStatisticListRead(self, body: TSTAPIPRGSStatisticListStore, **kwargs) -> TSTAPIGSStatisticListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.GSStatisticListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGSStatisticListStoreRL')
        return response_object

    def g_s_statistic_list_read(self, body: TSTAPIPRGSStatisticListStore, **kwargs) -> TSTAPIGSStatisticListStoreRL:
        return self.GSStatisticListRead(body, **kwargs)

    #
    # The constant  "SoftwarePackageListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "SoftwarePackageList"
    #
    SoftwarePackageListReadBaseURL = "/tst/v1/normal/a/SoftwarePackageListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "SoftwarePackageList"
    #
    # @return string - containing the URL for this API call
    #
    def SoftwarePackageListReadURL(self) -> str:
        return self.BaseURL + RESTApi.SoftwarePackageListReadBaseURL  + str(self.RequestSessionID)
    def SoftwarePackageListRead(self, body: TSTAPIPRSoftwarePackageListStore, **kwargs) -> TSTAPISoftwarePackageListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.SoftwarePackageListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPISoftwarePackageListStoreRL')
        return response_object

    def software_package_list_read(self, body: TSTAPIPRSoftwarePackageListStore, **kwargs) -> TSTAPISoftwarePackageListStoreRL:
        return self.SoftwarePackageListRead(body, **kwargs)

    #
    # The constant  "LicenseListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "LicenseList"
    #
    LicenseListReadBaseURL = "/tst/v1/normal/a/LicenseListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "LicenseList"
    #
    # @return string - containing the URL for this API call
    #
    def LicenseListReadURL(self) -> str:
        return self.BaseURL + RESTApi.LicenseListReadBaseURL  + str(self.RequestSessionID)
    def LicenseListRead(self, body: TSTAPIPRLicenseListStore, **kwargs) -> TSTAPILicenseListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.LicenseListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPILicenseListStoreRL')
        return response_object

    def license_list_read(self, body: TSTAPIPRLicenseListStore, **kwargs) -> TSTAPILicenseListStoreRL:
        return self.LicenseListRead(body, **kwargs)

    #
    # The constant  "SendAppLogMessageURL" holds the base URL - with session parameter, but exluding the session information - for the API call "SendAppLogMessage"
    #
    SendAppLogMessageBaseURL = "/tst/v1/normal/a/SendAppLogMessage?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "SendAppLogMessage"
    #
    # @return string - containing the URL for this API call
    #
    def SendAppLogMessageURL(self) -> str:
        return self.BaseURL + RESTApi.SendAppLogMessageBaseURL  + str(self.RequestSessionID)
    def SendAppLogMessage(self, body: TSTAPIPayloadLog, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.SendAppLogMessageURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def send_app_log_message(self, body: TSTAPIPayloadLog, **kwargs) -> TSTAPIGeneralResult:
        return self.SendAppLogMessage(body, **kwargs)

    #
    # The constant  "LogListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "LogList"
    #
    LogListReadBaseURL = "/tst/v1/normal/a/LogListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "LogList"
    #
    # @return string - containing the URL for this API call
    #
    def LogListReadURL(self) -> str:
        return self.BaseURL + RESTApi.LogListReadBaseURL  + str(self.RequestSessionID)
    def LogListRead(self, body: TSTAPIPRLogListStore, **kwargs) -> TSTAPILogListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.LogListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPILogListStoreRL')
        return response_object

    def log_list_read(self, body: TSTAPIPRLogListStore, **kwargs) -> TSTAPILogListStoreRL:
        return self.LogListRead(body, **kwargs)

    #
    # The constant  "LogListGCURL" holds the base URL - with session parameter, but exluding the session information - for the API call "LogListGC"
    #
    LogListGCBaseURL = "/tst/v1/normal/a/LogListGC?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "LogListGC"
    #
    # @return string - containing the URL for this API call
    #
    def LogListGCURL(self) -> str:
        return self.BaseURL + RESTApi.LogListGCBaseURL  + str(self.RequestSessionID)
    def LogListGC(self, body: TSTAPIParLogListGC, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.LogListGCURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def log_list_g_c(self, body: TSTAPIParLogListGC, **kwargs) -> TSTAPIGeneralResult:
        return self.LogListGC(body, **kwargs)

    #
    # The constant  "LogNoticeListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "LogNoticeList"
    #
    LogNoticeListCreateBaseURL = "/tst/v1/normal/a/LogNoticeListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "LogNoticeList"
    #
    # @return string - containing the URL for this API call
    #
    def LogNoticeListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.LogNoticeListCreateBaseURL  + str(self.RequestSessionID)
    def LogNoticeListCreate(self, body: TSTAPILogNoticeListStorePL, **kwargs) -> TSTAPILogNoticeListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.LogNoticeListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPILogNoticeListStoreRL')
        return response_object

    def log_notice_list_create(self, body: TSTAPILogNoticeListStorePL, **kwargs) -> TSTAPILogNoticeListStoreRL:
        return self.LogNoticeListCreate(body, **kwargs)

    #
    # The constant  "LogNoticeListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "LogNoticeList"
    #
    LogNoticeListDestroyBaseURL = "/tst/v1/normal/a/LogNoticeListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "LogNoticeList"
    #
    # @return string - containing the URL for this API call
    #
    def LogNoticeListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.LogNoticeListDestroyBaseURL  + str(self.RequestSessionID)
    def LogNoticeListDestroy(self, body: TSTAPILogNoticeListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.LogNoticeListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def log_notice_list_destroy(self, body: TSTAPILogNoticeListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.LogNoticeListDestroy(body, **kwargs)

    #
    # The constant  "LogNoticeListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "LogNoticeList"
    #
    LogNoticeListUpdateBaseURL = "/tst/v1/normal/a/LogNoticeListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "LogNoticeList"
    #
    # @return string - containing the URL for this API call
    #
    def LogNoticeListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.LogNoticeListUpdateBaseURL  + str(self.RequestSessionID)
    def LogNoticeListUpdate(self, body: TSTAPILogNoticeListStorePL, **kwargs) -> TSTAPILogNoticeListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.LogNoticeListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPILogNoticeListStoreRL')
        return response_object

    def log_notice_list_update(self, body: TSTAPILogNoticeListStorePL, **kwargs) -> TSTAPILogNoticeListStoreRL:
        return self.LogNoticeListUpdate(body, **kwargs)

    #
    # The constant  "LogNoticeListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "LogNoticeList"
    #
    LogNoticeListReadBaseURL = "/tst/v1/normal/a/LogNoticeListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "LogNoticeList"
    #
    # @return string - containing the URL for this API call
    #
    def LogNoticeListReadURL(self) -> str:
        return self.BaseURL + RESTApi.LogNoticeListReadBaseURL  + str(self.RequestSessionID)
    def LogNoticeListRead(self, body: TSTAPIPRLogNoticeListStore, **kwargs) -> TSTAPILogNoticeListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.LogNoticeListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPILogNoticeListStoreRL')
        return response_object

    def log_notice_list_read(self, body: TSTAPIPRLogNoticeListStore, **kwargs) -> TSTAPILogNoticeListStoreRL:
        return self.LogNoticeListRead(body, **kwargs)

    #
    # The constant  "ExportOpenAPISpecificationURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ExportOpenAPISpecification"
    #
    ExportOpenAPISpecificationBaseURL = "/tst/v1/normal/a/ExportOpenAPISpecification?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ExportOpenAPISpecification"
    #
    # @return string - containing the URL for this API call
    #
    def ExportOpenAPISpecificationURL(self) -> str:
        return self.BaseURL + RESTApi.ExportOpenAPISpecificationBaseURL  + str(self.RequestSessionID)
    def ExportOpenAPISpecification(self, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.ExportOpenAPISpecificationURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def export_open_a_p_i_specification(self, **kwargs) -> TSTAPIGeneralResult:
        return self.ExportOpenAPISpecification(**kwargs)

    #
    # The constant  "UserListCreateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserList"
    #
    UserListCreateBaseURL = "/tst/v1/normal/a/UserListCreate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserList"
    #
    # @return string - containing the URL for this API call
    #
    def UserListCreateURL(self) -> str:
        return self.BaseURL + RESTApi.UserListCreateBaseURL  + str(self.RequestSessionID)
    def UserListCreate(self, body: TSTAPIUserListStorePL, **kwargs) -> TSTAPIUserListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserListCreateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserListStoreRL')
        return response_object

    def user_list_create(self, body: TSTAPIUserListStorePL, **kwargs) -> TSTAPIUserListStoreRL:
        return self.UserListCreate(body, **kwargs)

    #
    # The constant  "UserListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserList"
    #
    UserListDestroyBaseURL = "/tst/v1/normal/a/UserListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserList"
    #
    # @return string - containing the URL for this API call
    #
    def UserListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.UserListDestroyBaseURL  + str(self.RequestSessionID)
    def UserListDestroy(self, body: TSTAPIUserListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def user_list_destroy(self, body: TSTAPIUserListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.UserListDestroy(body, **kwargs)

    #
    # The constant  "UserListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserList"
    #
    UserListUpdateBaseURL = "/tst/v1/normal/a/UserListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserList"
    #
    # @return string - containing the URL for this API call
    #
    def UserListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.UserListUpdateBaseURL  + str(self.RequestSessionID)
    def UserListUpdate(self, body: TSTAPIUserListStorePL, **kwargs) -> TSTAPIUserListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserListStoreRL')
        return response_object

    def user_list_update(self, body: TSTAPIUserListStorePL, **kwargs) -> TSTAPIUserListStoreRL:
        return self.UserListUpdate(body, **kwargs)

    #
    # The constant  "UserListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UserList"
    #
    UserListReadBaseURL = "/tst/v1/normal/a/UserListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UserList"
    #
    # @return string - containing the URL for this API call
    #
    def UserListReadURL(self) -> str:
        return self.BaseURL + RESTApi.UserListReadBaseURL  + str(self.RequestSessionID)
    def UserListRead(self, body: TSTAPIPRUserListStore, **kwargs) -> TSTAPIUserListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.UserListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIUserListStoreRL')
        return response_object

    def user_list_read(self, body: TSTAPIPRUserListStore, **kwargs) -> TSTAPIUserListStoreRL:
        return self.UserListRead(body, **kwargs)

    #
    # The constant  "ChangePasswordURL" holds the base URL - with session parameter, but exluding the session information - for the API call "ChangePassword"
    #
    ChangePasswordBaseURL = "/tst/v1/normal/a/ChangePassword?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "ChangePassword"
    #
    # @return string - containing the URL for this API call
    #
    def ChangePasswordURL(self) -> str:
        return self.BaseURL + RESTApi.ChangePasswordBaseURL  + str(self.RequestSessionID)
    def ChangePassword(self, body: TSTAPIParChangePassword, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.ChangePasswordURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def change_password(self, body: TSTAPIParChangePassword, **kwargs) -> TSTAPIGeneralResult:
        return self.ChangePassword(body, **kwargs)

    #
    # The constant  "CheckPasswordURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CheckPassword"
    #
    CheckPasswordBaseURL = "/tst/v1/normal/a/CheckPassword?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CheckPassword"
    #
    # @return string - containing the URL for this API call
    #
    def CheckPasswordURL(self) -> str:
        return self.BaseURL + RESTApi.CheckPasswordBaseURL  + str(self.RequestSessionID)
    def CheckPassword(self, body: TSTAPIParCheckPassword, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.CheckPasswordURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def check_password(self, body: TSTAPIParCheckPassword, **kwargs) -> TSTAPIGeneralResult:
        return self.CheckPassword(body, **kwargs)

    #
    # The constant  "SessionListDestroyURL" holds the base URL - with session parameter, but exluding the session information - for the API call "SessionList"
    #
    SessionListDestroyBaseURL = "/tst/v1/normal/a/SessionListDestroy?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "SessionList"
    #
    # @return string - containing the URL for this API call
    #
    def SessionListDestroyURL(self) -> str:
        return self.BaseURL + RESTApi.SessionListDestroyBaseURL  + str(self.RequestSessionID)
    def SessionListDestroy(self, body: TSTAPISessionListStorePL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.SessionListDestroyURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def session_list_destroy(self, body: TSTAPISessionListStorePL, **kwargs) -> TSTAPIGeneralResult:
        return self.SessionListDestroy(body, **kwargs)

    #
    # The constant  "SessionListUpdateURL" holds the base URL - with session parameter, but exluding the session information - for the API call "SessionList"
    #
    SessionListUpdateBaseURL = "/tst/v1/normal/a/SessionListUpdate?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "SessionList"
    #
    # @return string - containing the URL for this API call
    #
    def SessionListUpdateURL(self) -> str:
        return self.BaseURL + RESTApi.SessionListUpdateBaseURL  + str(self.RequestSessionID)
    def SessionListUpdate(self, body: TSTAPISessionListStorePL, **kwargs) -> TSTAPISessionListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.SessionListUpdateURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPISessionListStoreRL')
        return response_object

    def session_list_update(self, body: TSTAPISessionListStorePL, **kwargs) -> TSTAPISessionListStoreRL:
        return self.SessionListUpdate(body, **kwargs)

    #
    # The constant  "SessionListReadURL" holds the base URL - with session parameter, but exluding the session information - for the API call "SessionList"
    #
    SessionListReadBaseURL = "/tst/v1/normal/a/SessionListRead?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "SessionList"
    #
    # @return string - containing the URL for this API call
    #
    def SessionListReadURL(self) -> str:
        return self.BaseURL + RESTApi.SessionListReadBaseURL  + str(self.RequestSessionID)
    def SessionListRead(self, body: TSTAPIPRSessionListStore, **kwargs) -> TSTAPISessionListStoreRL:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI( self.SessionListReadURL(), 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPISessionListStoreRL')
        return response_object

    def session_list_read(self, body: TSTAPIPRSessionListStore, **kwargs) -> TSTAPISessionListStoreRL:
        return self.SessionListRead(body, **kwargs)

    #
    # The constant  "NewSessionURL" holds the base URL - with session parameter, but exluding the session information - for the API call "NewSession"
    #
    NewSessionBaseURL = "/tst/v1/normal/a/NewSession?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "NewSession"
    #
    # @return string - containing the URL for this API call
    #
    def NewSessionURL(self) -> str:
        return self.BaseURL + RESTApi.NewSessionBaseURL  + str(self.RequestSessionID)
    def NewSession(self, body: TSTAPIParNewSession, **kwargs) -> TSTAPIResSingleSession:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.NewSessionURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIResSingleSession')
        return response_object

    def new_session(self, body: TSTAPIParNewSession, **kwargs) -> TSTAPIResSingleSession:
        return self.NewSession(body, **kwargs)

    #
    # The constant  "EnterSessionURL" holds the base URL - with session parameter, but exluding the session information - for the API call "EnterSession"
    #
    EnterSessionBaseURL = "/tst/v1/normal/a/EnterSession?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "EnterSession"
    #
    # @return string - containing the URL for this API call
    #
    def EnterSessionURL(self) -> str:
        return self.BaseURL + RESTApi.EnterSessionBaseURL  + str(self.RequestSessionID)
    def EnterSession(self, body: TSTAPIParEnterSession, **kwargs) -> TSTAPIResSingleSession:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.EnterSessionURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIResSingleSession')
        return response_object

    def enter_session(self, body: TSTAPIParEnterSession, **kwargs) -> TSTAPIResSingleSession:
        return self.EnterSession(body, **kwargs)

    #
    # The constant  "RequestPendingSessionURL" holds the base URL - with session parameter, but exluding the session information - for the API call "RequestPendingSession"
    #
    RequestPendingSessionBaseURL = "/tst/v1/normal/a/RequestPendingSession?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "RequestPendingSession"
    #
    # @return string - containing the URL for this API call
    #
    def RequestPendingSessionURL(self) -> str:
        return self.BaseURL + RESTApi.RequestPendingSessionBaseURL  + str(self.RequestSessionID)
    def RequestPendingSession(self, body: TSTAPIParRequestPendingSession, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.RequestPendingSessionURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def request_pending_session(self, body: TSTAPIParRequestPendingSession, **kwargs) -> TSTAPIGeneralResult:
        return self.RequestPendingSession(body, **kwargs)

    #
    # The constant  "CurrentSessionURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CurrentSession"
    #
    CurrentSessionBaseURL = "/tst/v1/normal/a/CurrentSession?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CurrentSession"
    #
    # @return string - containing the URL for this API call
    #
    def CurrentSessionURL(self) -> str:
        return self.BaseURL + RESTApi.CurrentSessionBaseURL  + str(self.RequestSessionID)
    def CurrentSession(self, **kwargs) -> TSTAPIResSingleSession:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.CurrentSessionURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIResSingleSession')
        return response_object

    def current_session(self, **kwargs) -> TSTAPIResSingleSession:
        return self.CurrentSession(**kwargs)

    #
    # The constant  "CloseSessionURL" holds the base URL - with session parameter, but exluding the session information - for the API call "CloseSession"
    #
    CloseSessionBaseURL = "/tst/v1/normal/a/CloseSession?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "CloseSession"
    #
    # @return string - containing the URL for this API call
    #
    def CloseSessionURL(self) -> str:
        return self.BaseURL + RESTApi.CloseSessionBaseURL  + str(self.RequestSessionID)
    def CloseSession(self, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.CloseSessionURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def close_session(self, **kwargs) -> TSTAPIGeneralResult:
        return self.CloseSession(**kwargs)

    #
    # The constant  "TerminateSessionURL" holds the base URL - with session parameter, but exluding the session information - for the API call "TerminateSession"
    #
    TerminateSessionBaseURL = "/tst/v1/normal/a/TerminateSession?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "TerminateSession"
    #
    # @return string - containing the URL for this API call
    #
    def TerminateSessionURL(self) -> str:
        return self.BaseURL + RESTApi.TerminateSessionBaseURL  + str(self.RequestSessionID)
    def TerminateSession(self, body: TSTAPIParTerminateSession, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.TerminateSessionURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def terminate_session(self, body: TSTAPIParTerminateSession, **kwargs) -> TSTAPIGeneralResult:
        return self.TerminateSession(body, **kwargs)

    #
    # The constant  "SessionListGCURL" holds the base URL - with session parameter, but exluding the session information - for the API call "SessionListGC"
    #
    SessionListGCBaseURL = "/tst/v1/normal/a/SessionListGC?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "SessionListGC"
    #
    # @return string - containing the URL for this API call
    #
    def SessionListGCURL(self) -> str:
        return self.BaseURL + RESTApi.SessionListGCBaseURL  + str(self.RequestSessionID)
    def SessionListGC(self, body: TSTAPIParSessionListGC, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.SessionListGCURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def session_list_g_c(self, body: TSTAPIParSessionListGC, **kwargs) -> TSTAPIGeneralResult:
        return self.SessionListGC(body, **kwargs)

    #
    # The constant  "UpdateSessionActivityURL" holds the base URL - with session parameter, but exluding the session information - for the API call "UpdateSessionActivity"
    #
    UpdateSessionActivityBaseURL = "/tst/v1/normal/a/UpdateSessionActivity?sessionID="
    #
    # Builds the complete URL - including the current session information - for the API call "UpdateSessionActivity"
    #
    # @return string - containing the URL for this API call
    #
    def UpdateSessionActivityURL(self) -> str:
        return self.BaseURL + RESTApi.UpdateSessionActivityBaseURL  + str(self.RequestSessionID)
    def UpdateSessionActivity(self, body: TSTAPIUpdateSessionActivityPL, **kwargs) -> TSTAPIGeneralResult:
        params = locals()
        post_data = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.UpdateSessionActivityURL() , 'POST', {}, post_data, {})
        if not response:
            return None
        response_object = self.apiClient.deserialize(response, 'TSTAPIGeneralResult')
        return response_object

    def update_session_activity(self, body: TSTAPIUpdateSessionActivityPL, **kwargs) -> TSTAPIGeneralResult:
        return self.UpdateSessionActivity(body, **kwargs)
