# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class AlertNotifier(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'clusters': 'list[NestedCluster]',
        'disabled': 'bool',
        'email_from': 'str',
        'email_tos': 'list[str]',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'language_code': 'NotifierLanguageCode',
        'name': 'str',
        'notice_severities': 'list[str]',
        'security_mode': 'NotifierSecurityMode',
        'smtp_server_config': 'NestedSmtpServer',
        'smtp_server_host': 'str',
        'smtp_server_port': 'int',
        'username': 'str'
    }

    attribute_map = {
        'clusters': 'clusters',
        'disabled': 'disabled',
        'email_from': 'email_from',
        'email_tos': 'email_tos',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'language_code': 'language_code',
        'name': 'name',
        'notice_severities': 'notice_severities',
        'security_mode': 'security_mode',
        'smtp_server_config': 'smtp_server_config',
        'smtp_server_host': 'smtp_server_host',
        'smtp_server_port': 'smtp_server_port',
        'username': 'username'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """AlertNotifier - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._clusters = None
        self._disabled = None
        self._email_from = None
        self._email_tos = None
        self._entity_async_status = None
        self._id = None
        self._language_code = None
        self._name = None
        self._notice_severities = None
        self._security_mode = None
        self._smtp_server_config = None
        self._smtp_server_host = None
        self._smtp_server_port = None
        self._username = None
        self.discriminator = None

        self.clusters = kwargs.get("clusters", None)
        if "disabled" in kwargs:
            self.disabled = kwargs["disabled"]
        self.email_from = kwargs.get("email_from", None)
        if "email_tos" in kwargs:
            self.email_tos = kwargs["email_tos"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.language_code = kwargs.get("language_code", None)
        self.name = kwargs.get("name", None)
        if "notice_severities" in kwargs:
            self.notice_severities = kwargs["notice_severities"]
        self.security_mode = kwargs.get("security_mode", None)
        self.smtp_server_config = kwargs.get("smtp_server_config", None)
        self.smtp_server_host = kwargs.get("smtp_server_host", None)
        self.smtp_server_port = kwargs.get("smtp_server_port", None)
        self.username = kwargs.get("username", None)

    @property
    def clusters(self):
        """Gets the clusters of this AlertNotifier.  # noqa: E501


        :return: The clusters of this AlertNotifier.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this AlertNotifier.


        :param clusters: The clusters of this AlertNotifier.  # noqa: E501
        :type clusters: list[NestedCluster]
        """

        self._clusters = clusters

    @property
    def disabled(self):
        """Gets the disabled of this AlertNotifier.  # noqa: E501


        :return: The disabled of this AlertNotifier.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this AlertNotifier.


        :param disabled: The disabled of this AlertNotifier.  # noqa: E501
        :type disabled: bool
        """
        if self.local_vars_configuration.client_side_validation and disabled is None:  # noqa: E501
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def email_from(self):
        """Gets the email_from of this AlertNotifier.  # noqa: E501


        :return: The email_from of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._email_from

    @email_from.setter
    def email_from(self, email_from):
        """Sets the email_from of this AlertNotifier.


        :param email_from: The email_from of this AlertNotifier.  # noqa: E501
        :type email_from: str
        """

        self._email_from = email_from

    @property
    def email_tos(self):
        """Gets the email_tos of this AlertNotifier.  # noqa: E501


        :return: The email_tos of this AlertNotifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_tos

    @email_tos.setter
    def email_tos(self, email_tos):
        """Sets the email_tos of this AlertNotifier.


        :param email_tos: The email_tos of this AlertNotifier.  # noqa: E501
        :type email_tos: list[str]
        """
        if self.local_vars_configuration.client_side_validation and email_tos is None:  # noqa: E501
            raise ValueError("Invalid value for `email_tos`, must not be `None`")  # noqa: E501

        self._email_tos = email_tos

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this AlertNotifier.  # noqa: E501


        :return: The entity_async_status of this AlertNotifier.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this AlertNotifier.


        :param entity_async_status: The entity_async_status of this AlertNotifier.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this AlertNotifier.  # noqa: E501


        :return: The id of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertNotifier.


        :param id: The id of this AlertNotifier.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def language_code(self):
        """Gets the language_code of this AlertNotifier.  # noqa: E501


        :return: The language_code of this AlertNotifier.  # noqa: E501
        :rtype: NotifierLanguageCode
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this AlertNotifier.


        :param language_code: The language_code of this AlertNotifier.  # noqa: E501
        :type language_code: NotifierLanguageCode
        """

        self._language_code = language_code

    @property
    def name(self):
        """Gets the name of this AlertNotifier.  # noqa: E501


        :return: The name of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertNotifier.


        :param name: The name of this AlertNotifier.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def notice_severities(self):
        """Gets the notice_severities of this AlertNotifier.  # noqa: E501


        :return: The notice_severities of this AlertNotifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._notice_severities

    @notice_severities.setter
    def notice_severities(self, notice_severities):
        """Sets the notice_severities of this AlertNotifier.


        :param notice_severities: The notice_severities of this AlertNotifier.  # noqa: E501
        :type notice_severities: list[str]
        """
        if self.local_vars_configuration.client_side_validation and notice_severities is None:  # noqa: E501
            raise ValueError("Invalid value for `notice_severities`, must not be `None`")  # noqa: E501

        self._notice_severities = notice_severities

    @property
    def security_mode(self):
        """Gets the security_mode of this AlertNotifier.  # noqa: E501


        :return: The security_mode of this AlertNotifier.  # noqa: E501
        :rtype: NotifierSecurityMode
        """
        return self._security_mode

    @security_mode.setter
    def security_mode(self, security_mode):
        """Sets the security_mode of this AlertNotifier.


        :param security_mode: The security_mode of this AlertNotifier.  # noqa: E501
        :type security_mode: NotifierSecurityMode
        """

        self._security_mode = security_mode

    @property
    def smtp_server_config(self):
        """Gets the smtp_server_config of this AlertNotifier.  # noqa: E501


        :return: The smtp_server_config of this AlertNotifier.  # noqa: E501
        :rtype: NestedSmtpServer
        """
        return self._smtp_server_config

    @smtp_server_config.setter
    def smtp_server_config(self, smtp_server_config):
        """Sets the smtp_server_config of this AlertNotifier.


        :param smtp_server_config: The smtp_server_config of this AlertNotifier.  # noqa: E501
        :type smtp_server_config: NestedSmtpServer
        """

        self._smtp_server_config = smtp_server_config

    @property
    def smtp_server_host(self):
        """Gets the smtp_server_host of this AlertNotifier.  # noqa: E501


        :return: The smtp_server_host of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._smtp_server_host

    @smtp_server_host.setter
    def smtp_server_host(self, smtp_server_host):
        """Sets the smtp_server_host of this AlertNotifier.


        :param smtp_server_host: The smtp_server_host of this AlertNotifier.  # noqa: E501
        :type smtp_server_host: str
        """

        self._smtp_server_host = smtp_server_host

    @property
    def smtp_server_port(self):
        """Gets the smtp_server_port of this AlertNotifier.  # noqa: E501


        :return: The smtp_server_port of this AlertNotifier.  # noqa: E501
        :rtype: int
        """
        return self._smtp_server_port

    @smtp_server_port.setter
    def smtp_server_port(self, smtp_server_port):
        """Sets the smtp_server_port of this AlertNotifier.


        :param smtp_server_port: The smtp_server_port of this AlertNotifier.  # noqa: E501
        :type smtp_server_port: int
        """

        self._smtp_server_port = smtp_server_port

    @property
    def username(self):
        """Gets the username of this AlertNotifier.  # noqa: E501


        :return: The username of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AlertNotifier.


        :param username: The username of this AlertNotifier.  # noqa: E501
        :type username: str
        """

        self._username = username

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlertNotifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertNotifier):
            return True

        return self.to_dict() != other.to_dict()
