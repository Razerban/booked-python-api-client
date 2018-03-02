# coding: utf8

from typing import List, Dict
from .config import Attribute


class CustomAttribute(object):
    def __init__(self, label: str, type: Attribute.Type, category: Attribute.Category, regex: str, required: bool,
                 sort_order: int, applies_to_ids: List[int], admin_only: bool, is_private: bool,
                 possible_values: List[str] = None):
        self.label = label
        self.type = type
        self.category = category
        from re import compile, error
        try:
            compile(regex)
        except error:
            raise ValueError('Please make sure that the regular expression provided is valid')
        self.regex = regex
        self.required = required
        self.sort_order = sort_order
        self.applies_to_ids = applies_to_ids
        self.admin_only = admin_only
        self.is_private = is_private
        if type == Attribute.Type.SELECT_LIST:
            if possible_values is None:
                raise ValueError('possible_values cannot be none when type is SELECT_LIST')
            if len(possible_values) < 2:
                raise ValueError('possible_values should contain at least one value when type is SELECT_LIST')
        else:
            if possible_values is not None:
                pass  # Log a warning about non relevant attribute
        self.possible_values = possible_values

    def to_dict(self):
        dictionary = {'label': self.label, 'type': self.type.value, 'categoryId': self.category, 'regex': self.regex,
                      'required': self.required, 'sortOrder': self.sort_order,
                      'appliesToIds': self.applies_to_ids, 'adminOnly': self.admin_only, 'isPrivate': self.is_private}
        if self.type == Attribute.Type.SELECT_LIST:
            dictionary['possibleValues'] = self.possible_values
        return dictionary


class Link(object):
    def __init__(self, href: str, title: str):
        from .helpers import is_url_valid
        if is_url_valid(href) is True:
            self.href = href
        else:
            raise ValueError('Please make sure that the URL that you provided is in the right format.')
        self.title = title

    def to_dict(self):
        return {'href': self.href, 'title': self.title}


class Reservation(object):  # TODO Reimplement the Reservation class
    def __init__(self, reference_name: str, is_pending_approval: bool, links: List[Link], message: str):
        self.reference_number: str = reference_name
        self.is_pending_approval: bool = is_pending_approval
        self.links: List[Link] = links
        self.message: str = message

    def to_dict(self):
        pass


class Period(object):
    def __init__(self, start: str, end: str, label: str, start_time: str, end_time: str, is_reservable: bool):
        self.start: str = start
        self.end: str = end
        self.label: str = label
        self.start_time: str = start_time
        self.end_time: str = end_time
        self.is_reservable: bool = is_reservable


class Schedule(object):
    def __init__(self, id: str, name: str, timezone: str, weekday_start: str, ics_url: str, days_visible: int,
                 is_visible: bool, periods: List[Link]):
        self.id: str = id
        self.name: str = name

        from pytz import all_timezones
        if timezone in all_timezones:
            self.timezone: str = timezone
        else:
            raise ValueError('Please make sure that the timezone you provided is right.')
        self.weekday_start: int = weekday_start

        from .helpers import is_url_valid
        if is_url_valid(ics_url) is True:
            self.ics_url: str = ics_url
        else:
            raise ValueError('Please make sure that the URL that you provided is in the right format.')
        self.days_visible: int = days_visible
        self.is_visible: bool = is_visible
        self.periods: List[Link] = periods


class Slot(object):
    def __init__(self):
        pass
