# -*- coding: utf-8 -*-

from helpers import validate_url, parse_date, make_api_call
from config import TIMEZONE, ROUTES


class Client(object):
    def __init__(self, web_service_url: str, username: str, password: str, timezone: str = None):
        if validate_url(web_service_url) is True:
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
        self.session: dict = {}

        if self._has_session_expired():
            self.authenticate()
            self.is_authenticated = True

    def _create_session(self, session_token: str, session_expiration_date: str, user_id: str):
        self.session = {
            'sessionToken': session_token,
            'sessionExpires': session_expiration_date,
            'userId': user_id
        }

    def _has_session_expired(self):
        if 'bookedapi_sessionExpires' not in self.session or self.session['bookedapi_sessionExpires'] is None:
            return True

        from pytz import timezone as tz
        from datetime import datetime

        timezone = tz(self.timezone)
        current_date = timezone.localize(datetime.now())
        session_expiration_date = parse_date(self.session['bookedapi_sessionExpires'])

        if session_expiration_date >= current_date:
            return False

        return True

    def authenticate(self, force: bool = False):
        if not self._has_session_expired() and not force:
            return True

        endpoint = "{0}{1}".format(self.web_service_url, ROUTES['authenticate'])

        data = {
            'username': self.username,
            'password': self.password
        }

        response = make_api_call(endpoint=endpoint, data=data, method='POST')
        if response is False:
            from .exceptions import AuthenticationError
            raise AuthenticationError('Not being able to authenticate to the server.')
        else:
            for key in ['sessionToken', 'sessionExpires', 'userId']:
                if key not in response:
                    raise ValueError('{0} not found in the response body.')
            self._create_session(response['sessionToken'], response['sessionExpires'],
                                 response['userId'])
