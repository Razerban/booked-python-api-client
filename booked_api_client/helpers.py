# from requests import Session

# session = Session()


def validate_url(url: str):
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


def make_api_call(endpoint: str, method: str, data: dict = None, post_authentication: bool = False, session_token: str = None, user_id: str = None):
    """
    Make an API call with retries if the calls fails.
    :param endpoint: The endpoint we wish to connect to
    :param data: The request parameters
    :param method: POST/GET
    :param post_authentication: Whether this call is made after beeing authenticated
    :param session_token: The session token if the client has already been authenticated
    :param user_id: The user identifier
    :return: False if session_token is None or user_id is None. False if method is not port, get or delete.
    Else, json encoded body of the response.
    """

    def api_call(endpoint: str, method: str, data: dict = None, post_authentication: bool = False,
                 session_token: str = None, user_id: str = None):
        """
        Make an API call
        :param endpoint: The endpoint we wish to connect to
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
                return False
            headers['X-Booked-SessionToken'] = session_token
            headers['X-Booked-UserId'] = user_id

        from requests import get, post, delete
        from config import TIMEOUT

        method = method.lower()
        if method == 'get':
            # response = session.get(endpoint, headers=headers, timeout=TIMEOUT)
            response = get(endpoint, headers=headers, timeout=TIMEOUT)
        elif method == 'post':
            headers['Content-Type'] = 'application/json'
            # response = session.post(endpoint, headers=headers, json=data, timeout=TIMEOUT)
            response = post(endpoint, headers=headers, json=data, timeout=TIMEOUT)
        elif method == 'delete':
            # response = session.delete(endpoint, headers=headers, timeout=TIMEOUT)
            response = delete(endpoint, headers=headers, timeout=TIMEOUT)
        else:
            return False

        response.raise_for_status()

        return response.json()

    from config import TIME_BETWEEN_RETRIES, NUMBER_OF_RETRIES
    from requests import RequestException
    from time import sleep

    retries = NUMBER_OF_RETRIES

    while retries:
        try:
            retries = retries - 1
            return api_call(endpoint=endpoint, method=method, data=data, post_authentication=post_authentication,
                            session_token=session_token, user_id=user_id)
        except RequestException:
            if retries == 1:  # The last call
                raise
            sleep(TIME_BETWEEN_RETRIES)
            continue
