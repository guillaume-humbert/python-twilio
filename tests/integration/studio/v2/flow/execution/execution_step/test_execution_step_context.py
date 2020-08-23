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


class ExecutionStepContextTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.studio.v2.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .executions("FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .steps("FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .step_context().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://studio.twilio.com/v2/Flows/FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Executions/FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Steps/FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Context',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "context": {
                    "foo": "bar"
                },
                "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "execution_sid": "FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "step_sid": "FTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://studio.twilio.com/v2/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Executions/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps/FTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Context"
            }
            '''
        ))

        actual = self.client.studio.v2.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .executions("FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .steps("FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .step_context().fetch()

        self.assertIsNotNone(actual)
