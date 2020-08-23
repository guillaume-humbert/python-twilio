# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.preview.trusted_comms.business.brand import BrandList
from twilio.rest.preview.trusted_comms.business.insights import InsightsList


class BusinessList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the BusinessList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.business.BusinessList
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessList
        """
        super(BusinessList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, sid):
        """
        Constructs a BusinessContext

        :param sid: A string that uniquely identifies this Business.

        :returns: twilio.rest.preview.trusted_comms.business.BusinessContext
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessContext
        """
        return BusinessContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a BusinessContext

        :param sid: A string that uniquely identifies this Business.

        :returns: twilio.rest.preview.trusted_comms.business.BusinessContext
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessContext
        """
        return BusinessContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.BusinessList>'


class BusinessPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the BusinessPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.trusted_comms.business.BusinessPage
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessPage
        """
        super(BusinessPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BusinessInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.business.BusinessInstance
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessInstance
        """
        return BusinessInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.BusinessPage>'


class BusinessContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the BusinessContext

        :param Version version: Version that contains the resource
        :param sid: A string that uniquely identifies this Business.

        :returns: twilio.rest.preview.trusted_comms.business.BusinessContext
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessContext
        """
        super(BusinessContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Businesses/{sid}'.format(**self._solution)

        # Dependents
        self._brands = None
        self._insights = None

    def fetch(self):
        """
        Fetch the BusinessInstance

        :returns: The fetched BusinessInstance
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BusinessInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def brands(self):
        """
        Access the brands

        :returns: twilio.rest.preview.trusted_comms.business.brand.BrandList
        :rtype: twilio.rest.preview.trusted_comms.business.brand.BrandList
        """
        if self._brands is None:
            self._brands = BrandList(self._version, business_sid=self._solution['sid'], )
        return self._brands

    @property
    def insights(self):
        """
        Access the insights

        :returns: twilio.rest.preview.trusted_comms.business.insights.InsightsList
        :rtype: twilio.rest.preview.trusted_comms.business.insights.InsightsList
        """
        if self._insights is None:
            self._insights = InsightsList(self._version, business_sid=self._solution['sid'], )
        return self._insights

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.BusinessContext {}>'.format(context)


class BusinessInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the BusinessInstance

        :returns: twilio.rest.preview.trusted_comms.business.BusinessInstance
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessInstance
        """
        super(BusinessInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: BusinessContext for this BusinessInstance
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessContext
        """
        if self._context is None:
            self._context = BusinessContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Business.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the BusinessInstance

        :returns: The fetched BusinessInstance
        :rtype: twilio.rest.preview.trusted_comms.business.BusinessInstance
        """
        return self._proxy.fetch()

    @property
    def brands(self):
        """
        Access the brands

        :returns: twilio.rest.preview.trusted_comms.business.brand.BrandList
        :rtype: twilio.rest.preview.trusted_comms.business.brand.BrandList
        """
        return self._proxy.brands

    @property
    def insights(self):
        """
        Access the insights

        :returns: twilio.rest.preview.trusted_comms.business.insights.InsightsList
        :rtype: twilio.rest.preview.trusted_comms.business.insights.InsightsList
        """
        return self._proxy.insights

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.BusinessInstance {}>'.format(context)
