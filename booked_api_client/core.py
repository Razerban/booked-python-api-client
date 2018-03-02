# -*- coding: utf-8 -*-

from .helpers import is_url_valid, parse_date, make_api_call
from .config import TIMEZONE, Route, Attribute, Method
from .classes import CustomAttribute, Reservation
from typing import Dict


class Client(object):
    def __init__(self, web_service_url: str, username: str, password: str, timezone: str = None):
        if is_url_valid(web_service_url) is True:
            self.web_service_url: str = web_service_url
        else:
            raise ValueError('Please make sure that the URL that you provided is in the right format.')

        if timezone is not None:
            from pytz import all_timezones
            if timezone not in all_timezones:
                raise ValueError('Please make sure that the timezone you provided is right.')
            else:
                self.timezone = timezone
        else:
            self.timezone = TIMEZONE
        self.username: str = username
        self.password: str = password
        self.is_authenticated: bool = False
        self._session: dict = {  # To keep it coherent with _make_api_call method
            'sessionToken': None,
            'sessionExpires': None,
            'userId': None
        }

    def _create_session(self, session_token: str, session_expiration_date: str, user_id: str):
        self._session['sessionToken'] = session_token
        self._session['sessionExpires'] = session_expiration_date
        self._session['userId'] = user_id

    def _has_session_expired(self):
        if self.is_authenticated is True:
            if self._session['sessionExpires'] is not None:
                from pytz import timezone as tz
                from datetime import datetime

                timezone = tz(self.timezone)
                current_date = timezone.localize(datetime.now())
                session_expiration_date = parse_date(self._session['sessionExpires'])

                if session_expiration_date >= current_date:
                    return False
            else:
                self.is_authenticated = False
        return True

    def _ensure_session_has_not_expired(self):
        if self._has_session_expired() is True:
            self.authenticate()

    def _make_api_call(self, route: str, method: Method, post_authentication: bool = True, data: Dict = None):
        self._ensure_session_has_not_expired()
        return make_api_call(route=route, method=method, post_authentication=post_authentication, data=data,
                             session_token=self._session['session_token'], user_id=self._session['session_token'])

    def get_accessories(self):
        route = '{0}{1}'.format(self.web_service_url, Route.GET_ALL_ACCESSORIES.value)
        return self._make_api_call(route=route, method=Method.GET)

    def get_accessory(self, accessory_id: int):
        route = ('{0}{1}'.format(self.web_service_url, Route.GET_ACCESSORY.value)).replace(':accessoryId',
                                                                                           str(accessory_id))
        return self._make_api_call(route=route, method=Method.GET)

    def create_custom_attribute(self, custom_attribute: CustomAttribute):
        route = '{0}{1}'.format(self.web_service_url, Route.CREATE_CUSTOM_ATTRIBUTE.value)
        return self._make_api_call(route=route, method=Method.GET, data=custom_attribute.to_dict())

    def update_custom_attribute(self, attribute_id: int, custom_attribute: CustomAttribute):
        route = ('{0}{1}'.format(self.web_service_url, Route.UPDATE_CUSTOM_ATTRIBUTE.value)).replace(':attributeId',
                                                                                                     str(attribute_id))
        return self._make_api_call(route=route, method=Method.POST, data=custom_attribute.to_dict())

    def get_attributes_by_category(self, category: Attribute.Category):
        route = ('{0}{1}'.format(self.web_service_url, Route.GET_ATTRIBUTES_BY_CATEGORY.value)).replace(':categoryId',
                                                                                                        str(category))
        return self._make_api_call(route=route, method=Method.GET)

    def get_attribute(self, attribute_id: int):
        route = ('{0}{1}'.format(self.web_service_url, Route.GET_ATTRIBUTE.value)).replace(':attributeId',
                                                                                           str(attribute_id))
        return self._make_api_call(route=route, method=Method.GET)

    def delete_custom_attribute(self, attribute_id: int):
        route = ('{0}{1}'.format(self.web_service_url, Route.DELETE_CUSTOM_ATTRIBUTE.Value)).replace(':attributeId',
                                                                                                     str(attribute_id))
        return self._make_api_call(route=route, method=Method.DELETE)

    def sign_out(self):
        try:
            route = '{0}{1}'.format(self.web_service_url, Route.SIGN_OUT.value)
            data = {'userId': self._session['userId'], 'sessionToken': self._session['sessionToken']}
            response = self._make_api_call(route=route, method=Method.POST, data=data)
        except Exception:
            raise

        if response is None:
            self.is_authenticated = True

    def authenticate(self, force: bool = False):
        if not self._has_session_expired() and not force:
            return True

        route = "{0}{1}".format(self.web_service_url, Route.AUTHENTICATE.value)
        auth_data = {'username': self.username, 'password': self.password}
        response = self._make_api_call(route=route, data=auth_data, method=Method.POST, post_authentication=False)

        if response is False:
            from .exceptions import AuthenticationError
            raise AuthenticationError('Not being able to authenticate to the server.')
        else:
            for key in ['sessionToken', 'sessionExpires', 'userId']:
                if key not in response:
                    raise ValueError('{0} not found in the response body.')
            self._create_session(response['sessionToken'], response['sessionExpires'],
                                 response['userId'])

        self.is_authenticated = True

    def get_all_users_groups(self):
        route = "{0}{1}".format(self.web_service_url, Route.GET_ALL_USERS_GROUPS.value)
        return self._make_api_call(route=route, method=Method.GET)

    def get_users_group(self, group_id: int):
        route = ("{0}{1}".format(self.web_service_url, Route.GET_USERS_GROUPS.value)).replace(':groupId', str(group_id))
        return self._make_api_call(route=route, method=Method.GET)

    def create_reservation(self, reservation: Reservation):
        route = "{0}{1}".format(self.web_service_url, Route.CREATE_RESERVATION.value)
        return self._make_api_call(route=route, method=Method.POST, data=reservation.to_dict())

    def update_reservation(self, reference_number: int, reservation: Reservation):
        route = ("{0}{1}".format(self.web_service_url, Route.UPDATE_RESERVATION.value)).replace(':referenceNumber',
                                                                                                str(reference_number))
        return self._make_api_call(route=route, method=Method.POST, data=reservation.to_dict())
