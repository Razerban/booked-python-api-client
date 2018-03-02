# from requests import Session

# session = Session()

from .config import Method


def is_url_valid(url: str):
    """
    URL validator inspired by Django's URL validator.
    :param url: URL to validate
    :return: True if the URL is in good format, False if it is not
    """
    from re import compile, IGNORECASE, match

    regex = compile(
        r'^(?:http)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', IGNORECASE)

    return True if match(regex, url) is not None else False


def parse_date(date: str, date_format: str = "%Y-%m-%dT%H:%M:%S%z"):
    """
    Parse a date string and return the corresponding datetime object
    :param date: String representing the date
    :param date_format: The format in which the date is written (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
    :return: Corresponding datetime object
    """
    from datetime import datetime

    return datetime.strptime(date, date_format)


def make_api_call(route: str, method: Method.value, data: dict = None, post_authentication: bool = True,
                  session_token: str = None, user_id: str = None):
    """
    Make an API call with retries if the calls fails.
    :param route: The endpoint we wish to connect to
    :param data: The request parameters
    :param method: POST/GET
    :param post_authentication: Whether this call is made after beeing authenticated
    :param session_token: The session token if the client has already been authenticated
    :param user_id: The user identifier
    :return: False if session_token is None or user_id is None. False if method is not port, get or delete.
    Else, json encoded body of the response.
    """

    def _api_call(route: str, method: Method, data: dict = None, post_authentication: bool = True    ,
                  session_token: str = None, user_id: str = None):
        """
        Make an API call
        :param route: The endpoint we wish to connect to
        :param data: The request parameters
        :param method: POST/GET
        :param post_authentication: Whether this call is made after beeing authenticated
        :param session_token: The session token if the client has already been authenticated
        :param user_id: The user identifier
        :return: False if session_token is None or user_id is None. False if method is not port, get or delete.
        Else, json encoded body of the response.
        """
        headers = {}

        if post_authentication is True:
            if session_token is None or user_id is None:
                return None
            headers['X-Booked-SessionToken'] = session_token
            headers['X-Booked-UserId'] = user_id

        from requests import get, post, delete
        from .config import TIMEOUT

        if method.value == 'GET':
            if data is not None:
                pass  # Log a warning about non relevant data
            # response = session.get(endpoint, headers=headers, timeout=TIMEOUT)
            response = get(route, headers=headers, timeout=TIMEOUT)
        elif method.value == 'POST':
            headers['Content-Type'] = 'application/json'
            # response = session.post(endpoint, headers=headers, json=data, timeout=TIMEOUT)
            response = post(route, headers=headers, json=data, timeout=TIMEOUT)
        elif method.value == 'DELETE':
            if data is not None:
                pass  # Log a warning about non relevant data
            # response = session.delete(endpoint, headers=headers, timeout=TIMEOUT)
            response = delete(route, headers=headers, timeout=TIMEOUT)
        else:
            raise ValueError('HTTP method should be one from the following: GET, POST, DELETE.')

        response.raise_for_status()

        return response.json()

    from .config import TIME_BETWEEN_RETRIES, NUMBER_OF_RETRIES
    from requests import RequestException
    from time import sleep

    retries = NUMBER_OF_RETRIES

    while retries:
        try:
            retries = retries - 1
            return _api_call(route=route, method=method, data=data, post_authentication=post_authentication,
                             session_token=session_token, user_id=user_id)
        except RequestException:
            if retries == 1:  # The last call
                raise
            sleep(TIME_BETWEEN_RETRIES)
            continue
