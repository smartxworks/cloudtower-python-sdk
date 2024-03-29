# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class SnmpTrapReceiver(object):
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
        'auth_pass_phrase': 'str',
        'auth_protocol': 'SnmpAuthProtocol',
        'cluster': 'NestedCluster',
        'community': 'str',
        'disabled': 'bool',
        'engine_id': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'host': 'str',
        'id': 'str',
        'inform': 'bool',
        'language_code': 'SnmpLanguageCode',
        'local_id': 'str',
        'name': 'str',
        'port': 'int',
        'privacy_pass_phrase': 'str',
        'privacy_protocol': 'SnmpPrivacyProtocol',
        'protocol': 'SnmpProtocol',
        'username': 'str',
        'version': 'SnmpVersion'
    }

    attribute_map = {
        'auth_pass_phrase': 'auth_pass_phrase',
        'auth_protocol': 'auth_protocol',
        'cluster': 'cluster',
        'community': 'community',
        'disabled': 'disabled',
        'engine_id': 'engine_id',
        'entity_async_status': 'entityAsyncStatus',
        'host': 'host',
        'id': 'id',
        'inform': 'inform',
        'language_code': 'language_code',
        'local_id': 'local_id',
        'name': 'name',
        'port': 'port',
        'privacy_pass_phrase': 'privacy_pass_phrase',
        'privacy_protocol': 'privacy_protocol',
        'protocol': 'protocol',
        'username': 'username',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SnmpTrapReceiver - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._auth_pass_phrase = None
        self._auth_protocol = None
        self._cluster = None
        self._community = None
        self._disabled = None
        self._engine_id = None
        self._entity_async_status = None
        self._host = None
        self._id = None
        self._inform = None
        self._language_code = None
        self._local_id = None
        self._name = None
        self._port = None
        self._privacy_pass_phrase = None
        self._privacy_protocol = None
        self._protocol = None
        self._username = None
        self._version = None
        self.discriminator = None

        self.auth_pass_phrase = kwargs.get("auth_pass_phrase", None)
        self.auth_protocol = kwargs.get("auth_protocol", None)
        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        self.community = kwargs.get("community", None)
        if "disabled" in kwargs:
            self.disabled = kwargs["disabled"]
        self.engine_id = kwargs.get("engine_id", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "host" in kwargs:
            self.host = kwargs["host"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "inform" in kwargs:
            self.inform = kwargs["inform"]
        if "language_code" in kwargs:
            self.language_code = kwargs["language_code"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "port" in kwargs:
            self.port = kwargs["port"]
        self.privacy_pass_phrase = kwargs.get("privacy_pass_phrase", None)
        self.privacy_protocol = kwargs.get("privacy_protocol", None)
        if "protocol" in kwargs:
            self.protocol = kwargs["protocol"]
        self.username = kwargs.get("username", None)
        if "version" in kwargs:
            self.version = kwargs["version"]

    @property
    def auth_pass_phrase(self):
        """Gets the auth_pass_phrase of this SnmpTrapReceiver.  # noqa: E501


        :return: The auth_pass_phrase of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._auth_pass_phrase

    @auth_pass_phrase.setter
    def auth_pass_phrase(self, auth_pass_phrase):
        """Sets the auth_pass_phrase of this SnmpTrapReceiver.


        :param auth_pass_phrase: The auth_pass_phrase of this SnmpTrapReceiver.  # noqa: E501
        :type auth_pass_phrase: str
        """

        self._auth_pass_phrase = auth_pass_phrase

    @property
    def auth_protocol(self):
        """Gets the auth_protocol of this SnmpTrapReceiver.  # noqa: E501


        :return: The auth_protocol of this SnmpTrapReceiver.  # noqa: E501
        :rtype: SnmpAuthProtocol
        """
        return self._auth_protocol

    @auth_protocol.setter
    def auth_protocol(self, auth_protocol):
        """Sets the auth_protocol of this SnmpTrapReceiver.


        :param auth_protocol: The auth_protocol of this SnmpTrapReceiver.  # noqa: E501
        :type auth_protocol: SnmpAuthProtocol
        """

        self._auth_protocol = auth_protocol

    @property
    def cluster(self):
        """Gets the cluster of this SnmpTrapReceiver.  # noqa: E501


        :return: The cluster of this SnmpTrapReceiver.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this SnmpTrapReceiver.


        :param cluster: The cluster of this SnmpTrapReceiver.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def community(self):
        """Gets the community of this SnmpTrapReceiver.  # noqa: E501


        :return: The community of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this SnmpTrapReceiver.


        :param community: The community of this SnmpTrapReceiver.  # noqa: E501
        :type community: str
        """

        self._community = community

    @property
    def disabled(self):
        """Gets the disabled of this SnmpTrapReceiver.  # noqa: E501


        :return: The disabled of this SnmpTrapReceiver.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SnmpTrapReceiver.


        :param disabled: The disabled of this SnmpTrapReceiver.  # noqa: E501
        :type disabled: bool
        """
        if self.local_vars_configuration.client_side_validation and disabled is None:  # noqa: E501
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def engine_id(self):
        """Gets the engine_id of this SnmpTrapReceiver.  # noqa: E501


        :return: The engine_id of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this SnmpTrapReceiver.


        :param engine_id: The engine_id of this SnmpTrapReceiver.  # noqa: E501
        :type engine_id: str
        """

        self._engine_id = engine_id

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this SnmpTrapReceiver.  # noqa: E501


        :return: The entity_async_status of this SnmpTrapReceiver.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this SnmpTrapReceiver.


        :param entity_async_status: The entity_async_status of this SnmpTrapReceiver.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def host(self):
        """Gets the host of this SnmpTrapReceiver.  # noqa: E501


        :return: The host of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SnmpTrapReceiver.


        :param host: The host of this SnmpTrapReceiver.  # noqa: E501
        :type host: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def id(self):
        """Gets the id of this SnmpTrapReceiver.  # noqa: E501


        :return: The id of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnmpTrapReceiver.


        :param id: The id of this SnmpTrapReceiver.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def inform(self):
        """Gets the inform of this SnmpTrapReceiver.  # noqa: E501


        :return: The inform of this SnmpTrapReceiver.  # noqa: E501
        :rtype: bool
        """
        return self._inform

    @inform.setter
    def inform(self, inform):
        """Sets the inform of this SnmpTrapReceiver.


        :param inform: The inform of this SnmpTrapReceiver.  # noqa: E501
        :type inform: bool
        """
        if self.local_vars_configuration.client_side_validation and inform is None:  # noqa: E501
            raise ValueError("Invalid value for `inform`, must not be `None`")  # noqa: E501

        self._inform = inform

    @property
    def language_code(self):
        """Gets the language_code of this SnmpTrapReceiver.  # noqa: E501


        :return: The language_code of this SnmpTrapReceiver.  # noqa: E501
        :rtype: SnmpLanguageCode
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this SnmpTrapReceiver.


        :param language_code: The language_code of this SnmpTrapReceiver.  # noqa: E501
        :type language_code: SnmpLanguageCode
        """
        if self.local_vars_configuration.client_side_validation and language_code is None:  # noqa: E501
            raise ValueError("Invalid value for `language_code`, must not be `None`")  # noqa: E501

        self._language_code = language_code

    @property
    def local_id(self):
        """Gets the local_id of this SnmpTrapReceiver.  # noqa: E501


        :return: The local_id of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this SnmpTrapReceiver.


        :param local_id: The local_id of this SnmpTrapReceiver.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this SnmpTrapReceiver.  # noqa: E501


        :return: The name of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnmpTrapReceiver.


        :param name: The name of this SnmpTrapReceiver.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def port(self):
        """Gets the port of this SnmpTrapReceiver.  # noqa: E501


        :return: The port of this SnmpTrapReceiver.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SnmpTrapReceiver.


        :param port: The port of this SnmpTrapReceiver.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def privacy_pass_phrase(self):
        """Gets the privacy_pass_phrase of this SnmpTrapReceiver.  # noqa: E501


        :return: The privacy_pass_phrase of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._privacy_pass_phrase

    @privacy_pass_phrase.setter
    def privacy_pass_phrase(self, privacy_pass_phrase):
        """Sets the privacy_pass_phrase of this SnmpTrapReceiver.


        :param privacy_pass_phrase: The privacy_pass_phrase of this SnmpTrapReceiver.  # noqa: E501
        :type privacy_pass_phrase: str
        """

        self._privacy_pass_phrase = privacy_pass_phrase

    @property
    def privacy_protocol(self):
        """Gets the privacy_protocol of this SnmpTrapReceiver.  # noqa: E501


        :return: The privacy_protocol of this SnmpTrapReceiver.  # noqa: E501
        :rtype: SnmpPrivacyProtocol
        """
        return self._privacy_protocol

    @privacy_protocol.setter
    def privacy_protocol(self, privacy_protocol):
        """Sets the privacy_protocol of this SnmpTrapReceiver.


        :param privacy_protocol: The privacy_protocol of this SnmpTrapReceiver.  # noqa: E501
        :type privacy_protocol: SnmpPrivacyProtocol
        """

        self._privacy_protocol = privacy_protocol

    @property
    def protocol(self):
        """Gets the protocol of this SnmpTrapReceiver.  # noqa: E501


        :return: The protocol of this SnmpTrapReceiver.  # noqa: E501
        :rtype: SnmpProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SnmpTrapReceiver.


        :param protocol: The protocol of this SnmpTrapReceiver.  # noqa: E501
        :type protocol: SnmpProtocol
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def username(self):
        """Gets the username of this SnmpTrapReceiver.  # noqa: E501


        :return: The username of this SnmpTrapReceiver.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SnmpTrapReceiver.


        :param username: The username of this SnmpTrapReceiver.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def version(self):
        """Gets the version of this SnmpTrapReceiver.  # noqa: E501


        :return: The version of this SnmpTrapReceiver.  # noqa: E501
        :rtype: SnmpVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SnmpTrapReceiver.


        :param version: The version of this SnmpTrapReceiver.  # noqa: E501
        :type version: SnmpVersion
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, SnmpTrapReceiver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnmpTrapReceiver):
            return True

        return self.to_dict() != other.to_dict()
