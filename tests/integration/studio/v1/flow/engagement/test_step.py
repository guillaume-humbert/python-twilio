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


class StepTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.studio.v1.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .engagements("FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .steps.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://studio.twilio.com/v1/Flows/FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Engagements/FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Steps',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "previous_page_url": null,
                    "next_page_url": null,
                    "url": "https://studio.twilio.com/v1/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps?PageSize=50&Page=0",
                    "page": 0,
                    "first_page_url": "https://studio.twilio.com/v1/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "steps"
                },
                "steps": []
            }
            '''
        ))

        actual = self.client.studio.v1.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .engagements("FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .steps.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.studio.v1.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .engagements("FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .steps("FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://studio.twilio.com/v1/Flows/FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Engagements/FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Steps/FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "FTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "engagement_sid": "FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "name": "incomingRequest",
                "context": {},
                "transitioned_from": "Trigger",
                "transitioned_to": "Ended",
                "date_created": "2017-11-06T12:00:00Z",
                "date_updated": null,
                "url": "https://studio.twilio.com/v1/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps/FTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "step_context": "https://studio.twilio.com/v1/Flows/FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Engagements/FNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Steps/FTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Context"
                }
            }
            '''
        ))

        actual = self.client.studio.v1.flows("FWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .engagements("FNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .steps("FTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
