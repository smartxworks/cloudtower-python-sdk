# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Contact: info@smartx.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class SnmpTrapReceiverCreationParams(object):
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
        'disabled': 'bool',
        'inform': 'bool',
        'engine_id': 'str',
        'privacy_protocol': 'SnmpPrivacyProtocol',
        'privacy_pass_phrase': 'str',
        'auth_protocol': 'SnmpAuthProtocol',
        'auth_pass_phrase': 'str',
        'username': 'str',
        'community': 'str',
        'language_code': 'SnmpLanguageCode',
        'port': 'int',
        'host': 'str',
        'protocol': 'SnmpProtocol',
        'version': 'SnmpVersion',
        'name': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'disabled': 'disabled',
        'inform': 'inform',
        'engine_id': 'engine_id',
        'privacy_protocol': 'privacy_protocol',
        'privacy_pass_phrase': 'privacy_pass_phrase',
        'auth_protocol': 'auth_protocol',
        'auth_pass_phrase': 'auth_pass_phrase',
        'username': 'username',
        'community': 'community',
        'language_code': 'language_code',
        'port': 'port',
        'host': 'host',
        'protocol': 'protocol',
        'version': 'version',
        'name': 'name',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SnmpTrapReceiverCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._disabled = None
        self._inform = None
        self._engine_id = None
        self._privacy_protocol = None
        self._privacy_pass_phrase = None
        self._auth_protocol = None
        self._auth_pass_phrase = None
        self._username = None
        self._community = None
        self._language_code = None
        self._port = None
        self._host = None
        self._protocol = None
        self._version = None
        self._name = None
        self._cluster_id = None
        self.discriminator = None

        if "disabled" in kwargs:
            self.disabled = kwargs["disabled"]
        if "inform" in kwargs:
            self.inform = kwargs["inform"]
        if "engine_id" in kwargs:
            self.engine_id = kwargs["engine_id"]
        if "privacy_protocol" in kwargs:
            self.privacy_protocol = kwargs["privacy_protocol"]
        if "privacy_pass_phrase" in kwargs:
            self.privacy_pass_phrase = kwargs["privacy_pass_phrase"]
        if "auth_protocol" in kwargs:
            self.auth_protocol = kwargs["auth_protocol"]
        if "auth_pass_phrase" in kwargs:
            self.auth_pass_phrase = kwargs["auth_pass_phrase"]
        if "username" in kwargs:
            self.username = kwargs["username"]
        if "community" in kwargs:
            self.community = kwargs["community"]
        if "language_code" in kwargs:
            self.language_code = kwargs["language_code"]
        if "port" in kwargs:
            self.port = kwargs["port"]
        if "host" in kwargs:
            self.host = kwargs["host"]
        if "protocol" in kwargs:
            self.protocol = kwargs["protocol"]
        if "version" in kwargs:
            self.version = kwargs["version"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]

    @property
    def disabled(self):
        """Gets the disabled of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The disabled of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SnmpTrapReceiverCreationParams.


        :param disabled: The disabled of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def inform(self):
        """Gets the inform of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The inform of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._inform

    @inform.setter
    def inform(self, inform):
        """Sets the inform of this SnmpTrapReceiverCreationParams.


        :param inform: The inform of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type inform: bool
        """

        self._inform = inform

    @property
    def engine_id(self):
        """Gets the engine_id of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The engine_id of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this SnmpTrapReceiverCreationParams.


        :param engine_id: The engine_id of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type engine_id: str
        """

        self._engine_id = engine_id

    @property
    def privacy_protocol(self):
        """Gets the privacy_protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The privacy_protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: SnmpPrivacyProtocol
        """
        return self._privacy_protocol

    @privacy_protocol.setter
    def privacy_protocol(self, privacy_protocol):
        """Sets the privacy_protocol of this SnmpTrapReceiverCreationParams.


        :param privacy_protocol: The privacy_protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type privacy_protocol: SnmpPrivacyProtocol
        """

        self._privacy_protocol = privacy_protocol

    @property
    def privacy_pass_phrase(self):
        """Gets the privacy_pass_phrase of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The privacy_pass_phrase of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._privacy_pass_phrase

    @privacy_pass_phrase.setter
    def privacy_pass_phrase(self, privacy_pass_phrase):
        """Sets the privacy_pass_phrase of this SnmpTrapReceiverCreationParams.


        :param privacy_pass_phrase: The privacy_pass_phrase of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type privacy_pass_phrase: str
        """

        self._privacy_pass_phrase = privacy_pass_phrase

    @property
    def auth_protocol(self):
        """Gets the auth_protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The auth_protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: SnmpAuthProtocol
        """
        return self._auth_protocol

    @auth_protocol.setter
    def auth_protocol(self, auth_protocol):
        """Sets the auth_protocol of this SnmpTrapReceiverCreationParams.


        :param auth_protocol: The auth_protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type auth_protocol: SnmpAuthProtocol
        """

        self._auth_protocol = auth_protocol

    @property
    def auth_pass_phrase(self):
        """Gets the auth_pass_phrase of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The auth_pass_phrase of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._auth_pass_phrase

    @auth_pass_phrase.setter
    def auth_pass_phrase(self, auth_pass_phrase):
        """Sets the auth_pass_phrase of this SnmpTrapReceiverCreationParams.


        :param auth_pass_phrase: The auth_pass_phrase of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type auth_pass_phrase: str
        """

        self._auth_pass_phrase = auth_pass_phrase

    @property
    def username(self):
        """Gets the username of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The username of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SnmpTrapReceiverCreationParams.


        :param username: The username of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def community(self):
        """Gets the community of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The community of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this SnmpTrapReceiverCreationParams.


        :param community: The community of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type community: str
        """

        self._community = community

    @property
    def language_code(self):
        """Gets the language_code of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The language_code of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: SnmpLanguageCode
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this SnmpTrapReceiverCreationParams.


        :param language_code: The language_code of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type language_code: SnmpLanguageCode
        """
        if self.local_vars_configuration.client_side_validation and language_code is None:  # noqa: E501
            raise ValueError("Invalid value for `language_code`, must not be `None`")  # noqa: E501

        self._language_code = language_code

    @property
    def port(self):
        """Gets the port of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The port of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SnmpTrapReceiverCreationParams.


        :param port: The port of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def host(self):
        """Gets the host of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The host of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SnmpTrapReceiverCreationParams.


        :param host: The host of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type host: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def protocol(self):
        """Gets the protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: SnmpProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SnmpTrapReceiverCreationParams.


        :param protocol: The protocol of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type protocol: SnmpProtocol
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def version(self):
        """Gets the version of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The version of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: SnmpVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SnmpTrapReceiverCreationParams.


        :param version: The version of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type version: SnmpVersion
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def name(self):
        """Gets the name of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The name of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnmpTrapReceiverCreationParams.


        :param name: The name of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this SnmpTrapReceiverCreationParams.  # noqa: E501


        :return: The cluster_id of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this SnmpTrapReceiverCreationParams.


        :param cluster_id: The cluster_id of this SnmpTrapReceiverCreationParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

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
        if not isinstance(other, SnmpTrapReceiverCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnmpTrapReceiverCreationParams):
            return True

        return self.to_dict() != other.to_dict()
