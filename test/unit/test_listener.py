import unittest
from unittest.mock import patch

from robot_webserver_listener import listener


class TestLiveListener(unittest.TestCase):
    def setUp(self):
        self.post = patch('requests.post').start()
        self.robot_listener = listener.LiveListener('host', 1234)

    def tearDown(self):
        patch.stopall()

    def test_should_forward_to_web_server_a_start_suite_event_in_json_format(self):
        # When
        self.robot_listener.start_suite('Suite1', {'dummy': None})
        # Then
        self.post.assert_called_with(
            'http://host:1234/event',
            json={
                'event': 'start_suite',
                'name': 'Suite1',
                'attributes': {
                    'dummy': None
                }
            }
        )

    def test_should_forward_to_web_server_a_end_suite_event_in_json_format(self):
        # When
        self.robot_listener.end_suite('Suite1', {'a': 1})
        # Then
        self.post.assert_called_with(
            'http://host:1234/event',
            json={
                'event': 'end_suite',
                'name': 'Suite1',
                'attributes': {
                    'a': 1
                }
            }
        )

    def test_should_forward_to_web_server_a_start_test_event_in_json_format(self):
        # When
        self.robot_listener.start_test('Test 1', {'critical': False})
        # Then
        self.post.assert_called_with(
            'http://host:1234/event',
            json={
                'event': 'start_test',
                'name': 'Test 1',
                'attributes': {
                    'critical': False
                }
            }
        )

    def test_should_forward_to_web_server_a_end_test_event_in_json_format(self):
        # When
        self.robot_listener.end_test('Test 1', {'critical': False})
        # Then
        self.post.assert_called_with(
            'http://host:1234/event',
            json={
                'event': 'end_test',
                'name': 'Test 1',
                'attributes': {
                    'critical': False
                }
            }
        )

    def test_should_forward_to_web_server_a_start_keyword_event_in_json_format(self):
        # When
        self.robot_listener.start_keyword('Keyword 5', {'magic_level': 99})
        # Then
        self.post.assert_called_with(
            'http://host:1234/event',
            json={
                'event': 'start_keyword',
                'name': 'Keyword 5',
                'attributes': {
                    'magic_level': 99
                }
            }
        )

    def test_should_forward_to_web_server_a_end_keyword_event_in_json_format(self):
        # When
        self.robot_listener.end_keyword('Keyword 5', {'duration': 120})
        # Then
        self.post.assert_called_with(
            'http://host:1234/event',
            json={
                'event': 'end_keyword',
                'name': 'Keyword 5',
                'attributes': {
                    'duration': 120
                }
            }
        )
