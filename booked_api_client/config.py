"""
Title: booked-php-api-client
Ver: v0.1.0
By: Ahmed Abdelkafi
Email: abdelkafiahmed@yahoo.fr

This file is part of Booked Python Client Library.
There are other files that make up the whole library
and that are dependent on this file or that this file is dependent on.
"""

from enum import Enum

TIMEZONE = 'Europe/Paris'
BOOKED_WEB_SERVICE_URL = ''
TIMEOUT = 600
NUMBER_OF_RETRIES = 3
TIME_BETWEEN_RETRIES = 5


class Method(Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'


class Route(Enum):
    GET_ALL_ACCESSORIES = '/Accessories/'
    GET_ACCESSORY = '/Accessories/:accessoryId'
    CREATE_CUSTOM_ATTRIBUTE = '/Attributes/'
    UPDATE_CUSTOM_ATTRIBUTE = '/Attributes/:attributeId'
    GET_ATTRIBUTES_BY_CATEGORY = '/Attributes/Category/:categoryId'  # RESERVATION = 1, USER = 2, RESOURCE = 4
    GET_ATTRIBUTE = '/Attributes/:attributeId'
    DELETE_CUSTOM_ATTRIBUTE = '/Attributes/:attributeId'
    SIGN_OUT = '/Authentication/SignOut'
    AUTHENTICATE = '/Authentication/Authenticate'
    GET_ALL_USERS_GROUPS = '/Groups/'
    GET_USERS_GROUP = '/Groups/:groupId'
    CREATE_RESERVATION = '/Reservations/'
    UPDATE_RESERVATION = '/Reservations/:referenceNumber'
    APPROVE_RESERVATION = '/Reservations/:referenceNumber/Approval'
    CHECK_IN_RESERVATION = '/Reservations/:referenceNumber/CheckIn'
    CHECK_OUT_RESERVATION = '/Reservations/:referenceNumber/CheckOut'
    GET_ALL_RESERVATIONS = '/Reservations/'
    GET_RESERVATION = '/Reservations/:referenceNumber'
    DELETE_RESERVATION = '/Reservations/:referenceNumber'
    CREATE_RESOURCE = '/Resources/'
    UPDATE_RESOURCE = '/Resources/:resourceId'
    GET_STATUSES = '/Resources/Status'
    GET_ALL_RESOURCES = '/Resources/'
    GET_STATUS_REASONS = '/Resources/Status/Reasons'
    GET_RESOURCES_AVAILABILITY = '/Resources/Availability'
    GET_RESOURCES_GROUPS = '/Resources/Groups'
    GET_RESOURCE = '/Resources/:resourceId'
    GET_RESOURCE_AVAILABILITY = '/Resources/:resourceId/Availability'  # Create an issue on Booked git repository
    DELETE_RESOURCE = '/Resources/:resourceId'
    GET_ALL_SCHEDULES = '/Schedules/'
    GET_SCHEDULE = '/Schedules/:scheduleId'
    GET_SCHEDULE_SLOTS = '/Schedules/:scheduleId/Slots'
    CREATE_USER = '/Users/'  # This service is only available to application administrators
    UPDATE_USER = '/Users/:userId'  # This service is only available to application administrators
    UPDATE_USER_PASSWORD = '/Users/:userId/Password'  # This service is only available to application administrators
    GET_ALL_USERS = '/Users/'
    GET_USER = '/Users/:userId'
    DELETE_USER = '/Users/:userId'  # This service is only available to application administrators

# TODO: Create an issue on Booked to correct their API documentation


class Attribute(Enum):
    class Type(Enum):
        CHECK_BOX = 4
        MULTI_LINE = 2
        SELECT_LIST = 3
        SINGLE_LINE = 1

    class Category(Enum):
        RESERVATION = 1
        USER = 2
        RESOURCE = 4
        RESOURCE_TYPE = 5


class ReccurenceRule(Enum):
    class Type(Enum):
        DAILY = 'daily'
        MONTHLY = 'monthly'
        NONE = 'none'
        WEEKLY = 'weekly'
        YEARLY = 'yearly'

    class MonthlyType(Enum):
        DAY_OF_MONTH = 'dayOfMonth'
        DAY_OF_WEEK = 'dayOfWeek'
        NULL = 'null'

    class WeekDay(Enum):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 0

    class ReminderInterval(Enum):
        HOURS = 'hours'
        MINUTES = 'minutes'
        DAYS = 'days'


class UpdateScope(Enum):
    THIS = 'this'
    FULL = 'full'
    FUTURE = 'future'
