# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class NotificationList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.notify.v1.service.notification.NotificationList
        :rtype: twilio.rest.notify.v1.service.notification.NotificationList
        """
        super(NotificationList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid,}
        self._uri = '/Services/{service_sid}/Notifications'.format(**self._solution)

    def create(self, body=values.unset, priority=values.unset, ttl=values.unset,
               title=values.unset, sound=values.unset, action=values.unset,
               data=values.unset, apn=values.unset, gcm=values.unset,
               sms=values.unset, facebook_messenger=values.unset, fcm=values.unset,
               segment=values.unset, alexa=values.unset, to_binding=values.unset,
               identity=values.unset, tag=values.unset):
        """
        Create a new NotificationInstance

        :param unicode body: The body
        :param NotificationInstance.Priority priority: The priority
        :param unicode ttl: The ttl
        :param unicode title: The title
        :param unicode sound: The sound
        :param unicode action: The action
        :param dict data: The data
        :param dict apn: The apn
        :param dict gcm: The gcm
        :param dict sms: The sms
        :param dict facebook_messenger: The facebook_messenger
        :param dict fcm: The fcm
        :param unicode segment: The segment
        :param dict alexa: The alexa
        :param unicode to_binding: The to_binding
        :param unicode identity: The identity
        :param unicode tag: The tag

        :returns: Newly created NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        data = values.of({
            'Identity': identity,
            'Tag': tag,
            'Body': body,
            'Priority': priority,
            'Ttl': ttl,
            'Title': title,
            'Sound': sound,
            'Action': action,
            'Data': serialize.object(data),
            'Apn': serialize.object(apn),
            'Gcm': serialize.object(gcm),
            'Sms': serialize.object(sms),
            'FacebookMessenger': serialize.object(facebook_messenger),
            'Fcm': serialize.object(fcm),
            'Segment': segment,
            'Alexa': serialize.object(alexa),
            'ToBinding': to_binding,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return NotificationInstance(self._version, payload, service_sid=self._solution['service_sid'],)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.NotificationList>'


class NotificationPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the NotificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.notify.v1.service.notification.NotificationPage
        :rtype: twilio.rest.notify.v1.service.notification.NotificationPage
        """
        super(NotificationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NotificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.notify.v1.service.notification.NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        return NotificationInstance(self._version, payload, service_sid=self._solution['service_sid'],)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.NotificationPage>'


class NotificationInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Priority(object):
        HIGH = "high"
        LOW = "low"

    def __init__(self, version, payload, service_sid):
        """
        Initialize the NotificationInstance

        :returns: twilio.rest.notify.v1.service.notification.NotificationInstance
        :rtype: twilio.rest.notify.v1.service.notification.NotificationInstance
        """
        super(NotificationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'identities': payload['identities'],
            'tags': payload['tags'],
            'segments': payload['segments'],
            'priority': payload['priority'],
            'ttl': deserialize.integer(payload['ttl']),
            'title': payload['title'],
            'body': payload['body'],
            'sound': payload['sound'],
            'action': payload['action'],
            'data': payload['data'],
            'apn': payload['apn'],
            'gcm': payload['gcm'],
            'fcm': payload['fcm'],
            'sms': payload['sms'],
            'facebook_messenger': payload['facebook_messenger'],
            'alexa': payload['alexa'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid,}

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def identities(self):
        """
        :returns: The identities
        :rtype: unicode
        """
        return self._properties['identities']

    @property
    def tags(self):
        """
        :returns: The tags
        :rtype: unicode
        """
        return self._properties['tags']

    @property
    def segments(self):
        """
        :returns: The segments
        :rtype: unicode
        """
        return self._properties['segments']

    @property
    def priority(self):
        """
        :returns: The priority
        :rtype: NotificationInstance.Priority
        """
        return self._properties['priority']

    @property
    def ttl(self):
        """
        :returns: The ttl
        :rtype: unicode
        """
        return self._properties['ttl']

    @property
    def title(self):
        """
        :returns: The title
        :rtype: unicode
        """
        return self._properties['title']

    @property
    def body(self):
        """
        :returns: The body
        :rtype: unicode
        """
        return self._properties['body']

    @property
    def sound(self):
        """
        :returns: The sound
        :rtype: unicode
        """
        return self._properties['sound']

    @property
    def action(self):
        """
        :returns: The action
        :rtype: unicode
        """
        return self._properties['action']

    @property
    def data(self):
        """
        :returns: The data
        :rtype: dict
        """
        return self._properties['data']

    @property
    def apn(self):
        """
        :returns: The apn
        :rtype: dict
        """
        return self._properties['apn']

    @property
    def gcm(self):
        """
        :returns: The gcm
        :rtype: dict
        """
        return self._properties['gcm']

    @property
    def fcm(self):
        """
        :returns: The fcm
        :rtype: dict
        """
        return self._properties['fcm']

    @property
    def sms(self):
        """
        :returns: The sms
        :rtype: dict
        """
        return self._properties['sms']

    @property
    def facebook_messenger(self):
        """
        :returns: The facebook_messenger
        :rtype: dict
        """
        return self._properties['facebook_messenger']

    @property
    def alexa(self):
        """
        :returns: The alexa
        :rtype: dict
        """
        return self._properties['alexa']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.NotificationInstance>'
