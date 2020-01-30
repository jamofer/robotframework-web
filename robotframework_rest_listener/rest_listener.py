from robotframework_rest_listener import listener_service


START_KEYWORD_EVENT = 'start_keyword'
END_KEYWORD_EVENT = 'end_keyword'
START_SUITE_EVENT = 'start_suite'
END_SUITE_EVENT = 'end_suite'
START_TEST_EVENT = 'start_test'
END_TEST_EVENT = 'end_test'


class RestListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, path, robot_options=None, host='localhost', port=5000):
        self.host = host
        self.port = port
        listener_service.start(self)

    def start_keyword(self, name, attributes):
        listener_service.event(self, START_KEYWORD_EVENT, name, attributes)

    def end_keyword(self, name, attributes):
        listener_service.event(self, END_KEYWORD_EVENT, name, attributes)

    def start_suite(self, name, attributes):
        listener_service.event(self, START_SUITE_EVENT, name, attributes)

    def end_suite(self, name, attributes):
        listener_service.event(self, END_SUITE_EVENT, name, attributes)

    def start_test(self, name, attributes):
        listener_service.event(self, START_TEST_EVENT, name, attributes)

    def end_test(self, name, attributes):
        listener_service.event(self, END_TEST_EVENT, name, attributes)

    def message(self, message):
        listener_service.log_message(self, message)

    def close(self):
        listener_service.end(self)
