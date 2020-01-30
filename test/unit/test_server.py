import unittest
from unittest.mock import patch

from robotframework_rest_listener import server


class TestServer(unittest.TestCase):
    def setUp(self):
        self.client = server.app.test_client()

    def tearDown(self):
        pass

    def test_should_start_new_robot_instance(self):
        start_request = {
            ''
        }

    def test_should_digest_start_suite_event_request(self):
        # Given
        start_suite_event = {
            'event': 'start_suite',
            'name': 'Suite 1',
            'attributes': {},
        }
        # When
        response = self.client.post('event', json=start_suite_event)
        # Then
        self.

