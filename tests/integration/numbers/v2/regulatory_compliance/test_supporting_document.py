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


class SupportingDocumentTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .supporting_documents.create(friendly_name="friendly_name", type="type")

        values = {'FriendlyName': "friendly_name", 'Type': "type", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "mime_type": "mime_type",
                "status": "draft",
                "type": "type",
                "attributes": {
                    "first_name": "foo",
                    "last_name": "bar"
                },
                "date_created": "2019-07-31T02:11:52Z",
                "date_updated": "2019-07-31T02:11:52Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .supporting_documents.create(friendly_name="friendly_name", type="type")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .supporting_documents.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments',
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
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .supporting_documents.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [
                    {
                        "sid": "RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "friendly_name",
                        "mime_type": "mime_type",
                        "status": "draft",
                        "type": "type",
                        "attributes": {
                            "first_name": "foo",
                            "last_name": "bar"
                        },
                        "date_created": "2019-07-31T02:11:52Z",
                        "date_updated": "2019-07-31T02:11:52Z",
                        "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .supporting_documents.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .supporting_documents("RDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/RDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "mime_type": "mime_type",
                "status": "draft",
                "type": "type",
                "attributes": {
                    "first_name": "foo",
                    "last_name": "bar"
                },
                "date_created": "2019-07-31T02:11:52Z",
                "date_updated": "2019-07-31T02:11:52Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .supporting_documents("RDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .supporting_documents("RDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/RDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "mime_type": "mime_type",
                "status": "draft",
                "type": "type",
                "attributes": {
                    "first_name": "foo",
                    "last_name": "bar"
                },
                "date_created": "2019-07-31T02:11:52Z",
                "date_updated": "2019-07-31T02:11:52Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/SupportingDocuments/RDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .supporting_documents("RDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
