"""
Title: booked-php-api-client
Ver: v0.1.0
By: Ahmed Abdelkafi
Email: abdelkafiahmed@yahoo.fr

This file is part of Booked Python Client Library.
There are other files that make up the whole library
and that are dependent on this file or that this file is dependent on.
"""

TIMEZONE = 'Europe/Paris'
BOOKED_WEB_SERVICE_URL = ''

ENDPOINTS = {
    'AUTHENTICATE': '/Authentication/Authenticate',
    'GETRESOURCES': '/Resources/',
    'GETRESERVATIONS': '/Reservations/',
    'FILTERRESERVATION': '/Reservations',
    'GETAVAILABILITY': '/Resources/Availability',
    'GETACCESSORY': '/Accessories',
    'GETCATATTRIBUTE': '/Attributes/Category',
    'GETATTRIBUTE': '/Attributes',
    'GETGROUPS': '/Groups',
    'RESERVATIONS': '/Reservations/',
    'SCHEDULES': '/Schedules/',
    'SLOTS': '/Slots/',
    'STATUS': '/Resources/Status',
    'STATUSREASONS': '/Resources/Status/Reasons',
    'RESOURCETYPES': '/Types/',
    'USERS': '/Users'
}

INTERVALHOURS = 'hours'
INTERVALMINUTES = 'minutes'
INTERVALDAYS = 'days'

UPDATESCOPE_THIS = 'this'
UPDATESCOPE_FULL = 'full'
UPDATESCOPE_FUTURE = 'future'

RECURRENCETYPE_DAILY = 'daily'
RECURRENCETYPE_MONTHLY = 'monthly'
RECURRENCETYPE_NONE = 'none'
RECURRENCETYPE_WEEKLY = 'weekly'
RECURRENCETYPE_YEARLY = 'yearly'
RECURRENCE_MONTHLY_TYPE_DAYOFMONTH = 'dayOfMonth'
RECURRENCE_MONTHLY_TYPE_DAYOFWEEK = 'dayOfWeek'
RECURRENCE_MONTHLY_TYPE_NULL = 'null'
RECURRENCE_WEEKDAY_SUN = 0
RECURRENCE_WEEKDAY_MON = 1
RECURRENCE_WEEKDAY_TUE = 2
RECURRENCE_WEEKDAY_WED = 3
RECURRENCE_WEEKDAY_THR = 4
RECURRENCE_WEEKDAY_FRI = 5
RECURRENCE_WEEKDAY_SAT = 6

ATT_CAT_RESERVATION = 1
ATT_CAT_USER = 2
ATT_CAT_RESOURCE = 4
ATT_CAT_RESOURCE_TYPE = 5

SINGLE_LINE_TEXT = 1
SELECT_LIST = 3
MULTI_LINE_TEXT = 2
CHECK_BOX = 4

TIMEOUT = 600
NUMBER_OF_RETRIES = 3
TIME_BETWEEN_RETRIES = 5

ROUTES = {
    'authenticate': '/Authentication/Authenticate',
    'getAllAccessories': '/Accessories/',
    'createCustomAttribute': '/Attributes/',
    'updateCustomAttribute': '/Attributes/:attributeId',
    'getCategoryAttributes': '/Attributes/Category/:categoryId',  # RESERVATION = 1, USER = 2, RESOURCE = 4
    'getAttribute': '/Attributes/:attributeId',
    'deleteCustomAttribute': '/Attributes/:attributeId',
    'getAllGroups': '/Groups/',
    'getGroup': '/Groups/:groupId',
    'createReservation': '/Reservations/',
    'updateReservation': '/Reservations/:referenceNumber',
    'approveReservation': '/Reservations/:referenceNumber/Approval',
    'checkInReservation': '/Reservations/:referenceNumber/CheckIn',
    'checkOutReservation': '/Reservations/:referenceNumber/CheckOut',
    'getAllReservations': '/Reservations/',
    'getReservation': '/Reservations/:referenceNumber',
    'deleteReservation': '/Reservations/:referenceNumber',
    'createResource': '/Resources/',
    'updateResource': '/Resources/:resourceId',
    'getResourceStatuses': '/Resources/Status',
    'getAllResources': '/Resources/',
    'getResourceStatusReasons': '/Resources/Status/Reasons',
    'getAvailability': '/Resources/Availability',
    'getAllResourceGroups': '/Resources/Groups',
    'getResource': '/Resources/:resourceId',
    'getResourceAvailability': '/Resources/:resourceId/Availability',
    'DeleteResource': '/Resources/:resourceId',
    'getAllSchedules': '/Schedules/',
    'getSchedule': '/Schedules/:scheduleId',
    'getSlots': '/Schedules/:scheduleId/Slots',
    'createUser': '/Users/',  # This service is only available to application administrators
    'updateUser': '/Users/:userId',  # This service is only available to application administrators
    'updatePassword': '/Users/:userId/Password',  # This service is only available to application administrators
    'getAllUsers': '/Users/',
    'getUser': '/Users/:userId',
    'deleteUser': '/Users/:userId'  # This service is only available to application administrators
}