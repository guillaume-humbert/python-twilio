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


class EndUserTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .end_users.create(friendly_name="friendly_name", type="individual")

        values = {'FriendlyName': "friendly_name", 'Type': "individual", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "type": "individual",
                "attributes": {
                    "email": "foobar@twilio.com"
                },
                "date_created": "2019-07-30T21:57:45Z",
                "date_updated": "2019-07-30T21:57:45Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .end_users.create(friendly_name="friendly_name", type="individual")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .end_users.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .end_users.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [
                    {
                        "sid": "ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "friendly_name",
                        "type": "individual",
                        "attributes": {
                            "email": "foobar@twilio.com"
                        },
                        "date_created": "2019-07-30T21:57:45Z",
                        "date_updated": "2019-07-30T21:57:45Z",
                        "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .end_users.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .end_users("ITXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/ITXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "type": "individual",
                "attributes": {
                    "email": "foobar@twilio.com"
                },
                "date_created": "2019-07-30T21:57:45Z",
                "date_updated": "2019-07-30T21:57:45Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .end_users("ITXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .end_users("ITXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/ITXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "type": "individual",
                "attributes": {
                    "email": "foobar@twilio.com"
                },
                "date_created": "2019-07-30T21:57:45Z",
                "date_updated": "2019-07-30T21:57:45Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/EndUsers/ITaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .end_users("ITXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
