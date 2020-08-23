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


class SyncListPermissionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, list_sid):
        """
        Initialize the SyncListPermissionList

        :param Version version: Version that contains the resource
        :param service_sid: Sync Service Instance SID.
        :param list_sid: Sync List SID.

        :returns: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionList
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionList
        """
        super(SyncListPermissionList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'list_sid': list_sid, }
        self._uri = '/Services/{service_sid}/Lists/{list_sid}/Permissions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams SyncListPermissionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncListPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SyncListPermissionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return SyncListPermissionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncListPermissionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SyncListPermissionPage(self._version, response, self._solution)

    def get(self, identity):
        """
        Constructs a SyncListPermissionContext

        :param identity: Identity of the user to whom the Sync List Permission applies.

        :returns: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionContext
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionContext
        """
        return SyncListPermissionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            identity=identity,
        )

    def __call__(self, identity):
        """
        Constructs a SyncListPermissionContext

        :param identity: Identity of the user to whom the Sync List Permission applies.

        :returns: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionContext
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionContext
        """
        return SyncListPermissionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            identity=identity,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncListPermissionList>'


class SyncListPermissionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the SyncListPermissionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Sync Service Instance SID.
        :param list_sid: Sync List SID.

        :returns: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionPage
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionPage
        """
        super(SyncListPermissionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncListPermissionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        """
        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncListPermissionPage>'


class SyncListPermissionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, list_sid, identity):
        """
        Initialize the SyncListPermissionContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param list_sid: Sync List SID or unique name.
        :param identity: Identity of the user to whom the Sync List Permission applies.

        :returns: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionContext
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionContext
        """
        super(SyncListPermissionContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'list_sid': list_sid, 'identity': identity, }
        self._uri = '/Services/{service_sid}/Lists/{list_sid}/Permissions/{identity}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the SyncListPermissionInstance

        :returns: The fetched SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            identity=self._solution['identity'],
        )

    def delete(self):
        """
        Deletes the SyncListPermissionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def update(self, read, write, manage):
        """
        Update the SyncListPermissionInstance

        :param bool read: Read access.
        :param bool write: Write access.
        :param bool manage: Manage access.

        :returns: The updated SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        """
        data = values.of({'Read': read, 'Write': write, 'Manage': manage, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return SyncListPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            list_sid=self._solution['list_sid'],
            identity=self._solution['identity'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncListPermissionContext {}>'.format(context)


class SyncListPermissionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, service_sid, list_sid, identity=None):
        """
        Initialize the SyncListPermissionInstance

        :returns: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        """
        super(SyncListPermissionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'list_sid': payload.get('list_sid'),
            'identity': payload.get('identity'),
            'read': payload.get('read'),
            'write': payload.get('write'),
            'manage': payload.get('manage'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'list_sid': list_sid,
            'identity': identity or self._properties['identity'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SyncListPermissionContext for this SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionContext
        """
        if self._context is None:
            self._context = SyncListPermissionContext(
                self._version,
                service_sid=self._solution['service_sid'],
                list_sid=self._solution['list_sid'],
                identity=self._solution['identity'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: Twilio Account SID.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: Sync Service Instance SID.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def list_sid(self):
        """
        :returns: Sync List SID.
        :rtype: unicode
        """
        return self._properties['list_sid']

    @property
    def identity(self):
        """
        :returns: Identity of the user to whom the Sync List Permission applies.
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def read(self):
        """
        :returns: Read access.
        :rtype: bool
        """
        return self._properties['read']

    @property
    def write(self):
        """
        :returns: Write access.
        :rtype: bool
        """
        return self._properties['write']

    @property
    def manage(self):
        """
        :returns: Manage access.
        :rtype: bool
        """
        return self._properties['manage']

    @property
    def url(self):
        """
        :returns: URL of this Sync List Permission.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the SyncListPermissionInstance

        :returns: The fetched SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SyncListPermissionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, read, write, manage):
        """
        Update the SyncListPermissionInstance

        :param bool read: Read access.
        :param bool write: Write access.
        :param bool manage: Manage access.

        :returns: The updated SyncListPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.sync_list_permission.SyncListPermissionInstance
        """
        return self._proxy.update(read, write, manage, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncListPermissionInstance {}>'.format(context)
