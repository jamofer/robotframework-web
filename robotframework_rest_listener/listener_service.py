import requests


EVENT_PATH = '/event'
MESSAGE_PATH = '/message'
INIT_PATH = '/init'
CLOSE_PATH = '/close'


def __build_event_post(event, name, attributes):
    return {
        'event': event,
        'name': name,
        'attributes': attributes
    }


def __build_message_post(content):
    return {
        'message': content
    }


def event(rest_listener, event, name, attributes):
    json_content = __build_event_post(event, name, attributes)

    url = __url(rest_listener.host, rest_listener.port, EVENT_PATH)

    requests.post(url, json=json_content)


def log_message(rest_listener, message):
    json_content = __build_message_post(message)

    url = __url(rest_listener.host, rest_listener.port, MESSAGE_PATH)

    requests.post(url, json=json_content)


def start(rest_listener):
    url = __url(rest_listener.host, rest_listener.port, INIT_PATH)

    requests.post(url)


def end(rest_listener):
    url = __url(rest_listener.host, rest_listener.port, CLOSE_PATH)

    requests.post(url)


def __url(host, port, path):
    return 'http://{host}:{port}{url}'.format(
        host=host,
        port=port,
        url=path
    )
