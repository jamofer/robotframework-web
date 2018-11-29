import requests


START_KEYWORD_EVENT = 'start_keyword'
END_KEYWORD_EVENT = 'end_keyword'
START_SUITE_EVENT = 'start_suite'
END_SUITE_EVENT = 'end_suite'
START_TEST_EVENT = 'start_test'
END_TEST_EVENT = 'end_test'
MESSAGE_EVENT = 'message'
INIT_EVENT = 'init'
CLOSE_EVENT = 'finish'

REST_PATH = '/event'


def test_event(event, name, attributes):
    return {
        'event': event,
        'name': name,
        'attributes': attributes
    }


def message_event(message):
    return {
        'event': MESSAGE_EVENT,
        'message': message
    }


def close_event():
    return {'event': CLOSE_EVENT}


def init_event():
    return {'event': INIT_EVENT}


class LiveListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, host, port):
        self.host = host
        self.port = port
        requests.post(self.event_url, json=init_event())

    def start_keyword(self, name, attributes):
        requests.post(self.event_url, json=test_event(START_KEYWORD_EVENT, name, attributes))

    def end_keyword(self, name, attributes):
        requests.post(self.event_url, json=test_event(END_KEYWORD_EVENT, name, attributes))

    def start_suite(self, name, attributes):
        requests.post(self.event_url, json=test_event(START_SUITE_EVENT, name, attributes))

    def end_suite(self, name, attributes):
        requests.post(self.event_url, json=test_event(END_SUITE_EVENT, name, attributes))

    def start_test(self, name, attributes):
        requests.post(self.event_url, json=test_event(START_TEST_EVENT, name, attributes))

    def end_test(self, name, attributes):
        requests.post(self.event_url, json=test_event(END_TEST_EVENT, name, attributes))

    def message(self, message):
        requests.post(self.event_url, json=message_event(message))

    def close(self):
        requests.post(self.event_url, json=close_event())

    @property
    def event_url(self):
        return 'http://{host}:{port}{url}'.format(
            host=self.host,
            port=self.port,
            url=REST_PATH
        )
