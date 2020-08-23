# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SinkTestTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.sinks("DGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .sink_test.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://events.twilio.com/v1/Sinks/DGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Test',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "result": "valid"
            }
            '''
        ))

        actual = self.client.events.v1.sinks("DGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .sink_test.create()

        self.assertIsNotNone(actual)
