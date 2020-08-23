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


class DataSessionTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.sims("DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .data_sessions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://wireless.twilio.com/v1/Sims/DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/DataSessions',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "data_sessions": [
                    {
                        "sid": "WNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "radio_link": "LTE",
                        "operator_mcc": "",
                        "operator_mnc": "",
                        "operator_country": "",
                        "operator_name": "",
                        "cell_id": "",
                        "cell_location_estimate": {},
                        "packets_uploaded": 0,
                        "packets_downloaded": 0,
                        "last_updated": "2015-07-30T20:00:00Z",
                        "start": "2015-07-30T20:00:00Z",
                        "end": null,
                        "imei": null
                    },
                    {
                        "sid": "WNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "radio_link": "3G",
                        "operator_mcc": "",
                        "operator_mnc": "",
                        "operator_country": "",
                        "operator_name": "",
                        "cell_id": "",
                        "cell_location_estimate": {},
                        "packets_uploaded": 0,
                        "packets_downloaded": 0,
                        "last_updated": "2015-07-30T20:00:00Z",
                        "start": "2015-07-30T20:00:00Z",
                        "end": "2015-07-30T20:00:00Z",
                        "imei": "014931000129700"
                    }
                ],
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DataSessions?PageSize=50&Page=0",
                    "key": "data_sessions",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DataSessions?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.wireless.v1.sims("DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .data_sessions.list()

        self.assertIsNotNone(actual)
