# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class IpAccessControlListTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "http://www.example.com"
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists.create(ip_access_control_list_sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        values = {'IpAccessControlListSid': "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",}

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "http://www.example.com"
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists.create(ip_access_control_list_sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .ip_access_control_lists.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "ip_access_control_lists": [],
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists?Page=0&PageSize=50",
                    "key": "ip_access_control_lists",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 0,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists"
                }
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "ip_access_control_lists": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "friendly_name": "friendly_name",
                        "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "trunk_sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "http://www.example.com"
                    }
                ],
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists?Page=0&PageSize=50",
                    "key": "ip_access_control_lists",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists"
                }
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .ip_access_control_lists.list()

        self.assertIsNotNone(actual)
