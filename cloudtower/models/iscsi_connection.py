# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class IscsiConnection(object):
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
        'client_port': 'int',
        'cluster': 'NestedCluster',
        'host': 'NestedHost',
        'id': 'str',
        'initiator_ip': 'str',
        'iscsi_target': 'NestedIscsiTarget',
        'nvmf_subsystem': 'NestedNvmfSubsystem',
        'tr_type': 'StoreTransportType',
        'type': 'StoreConnectionType'
    }

    attribute_map = {
        'client_port': 'client_port',
        'cluster': 'cluster',
        'host': 'host',
        'id': 'id',
        'initiator_ip': 'initiator_ip',
        'iscsi_target': 'iscsi_target',
        'nvmf_subsystem': 'nvmf_subsystem',
        'tr_type': 'tr_type',
        'type': 'type'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IscsiConnection - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._client_port = None
        self._cluster = None
        self._host = None
        self._id = None
        self._initiator_ip = None
        self._iscsi_target = None
        self._nvmf_subsystem = None
        self._tr_type = None
        self._type = None
        self.discriminator = None

        if "client_port" in kwargs:
            self.client_port = kwargs["client_port"]
        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "host" in kwargs:
            self.host = kwargs["host"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "initiator_ip" in kwargs:
            self.initiator_ip = kwargs["initiator_ip"]
        self.iscsi_target = kwargs.get("iscsi_target", None)
        self.nvmf_subsystem = kwargs.get("nvmf_subsystem", None)
        self.tr_type = kwargs.get("tr_type", None)
        if "type" in kwargs:
            self.type = kwargs["type"]

    @property
    def client_port(self):
        """Gets the client_port of this IscsiConnection.  # noqa: E501


        :return: The client_port of this IscsiConnection.  # noqa: E501
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        """Sets the client_port of this IscsiConnection.


        :param client_port: The client_port of this IscsiConnection.  # noqa: E501
        :type client_port: int
        """
        if self.local_vars_configuration.client_side_validation and client_port is None:  # noqa: E501
            raise ValueError("Invalid value for `client_port`, must not be `None`")  # noqa: E501

        self._client_port = client_port

    @property
    def cluster(self):
        """Gets the cluster of this IscsiConnection.  # noqa: E501


        :return: The cluster of this IscsiConnection.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this IscsiConnection.


        :param cluster: The cluster of this IscsiConnection.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def host(self):
        """Gets the host of this IscsiConnection.  # noqa: E501


        :return: The host of this IscsiConnection.  # noqa: E501
        :rtype: NestedHost
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this IscsiConnection.


        :param host: The host of this IscsiConnection.  # noqa: E501
        :type host: NestedHost
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def id(self):
        """Gets the id of this IscsiConnection.  # noqa: E501


        :return: The id of this IscsiConnection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IscsiConnection.


        :param id: The id of this IscsiConnection.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def initiator_ip(self):
        """Gets the initiator_ip of this IscsiConnection.  # noqa: E501


        :return: The initiator_ip of this IscsiConnection.  # noqa: E501
        :rtype: str
        """
        return self._initiator_ip

    @initiator_ip.setter
    def initiator_ip(self, initiator_ip):
        """Sets the initiator_ip of this IscsiConnection.


        :param initiator_ip: The initiator_ip of this IscsiConnection.  # noqa: E501
        :type initiator_ip: str
        """
        if self.local_vars_configuration.client_side_validation and initiator_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `initiator_ip`, must not be `None`")  # noqa: E501

        self._initiator_ip = initiator_ip

    @property
    def iscsi_target(self):
        """Gets the iscsi_target of this IscsiConnection.  # noqa: E501


        :return: The iscsi_target of this IscsiConnection.  # noqa: E501
        :rtype: NestedIscsiTarget
        """
        return self._iscsi_target

    @iscsi_target.setter
    def iscsi_target(self, iscsi_target):
        """Sets the iscsi_target of this IscsiConnection.


        :param iscsi_target: The iscsi_target of this IscsiConnection.  # noqa: E501
        :type iscsi_target: NestedIscsiTarget
        """

        self._iscsi_target = iscsi_target

    @property
    def nvmf_subsystem(self):
        """Gets the nvmf_subsystem of this IscsiConnection.  # noqa: E501


        :return: The nvmf_subsystem of this IscsiConnection.  # noqa: E501
        :rtype: NestedNvmfSubsystem
        """
        return self._nvmf_subsystem

    @nvmf_subsystem.setter
    def nvmf_subsystem(self, nvmf_subsystem):
        """Sets the nvmf_subsystem of this IscsiConnection.


        :param nvmf_subsystem: The nvmf_subsystem of this IscsiConnection.  # noqa: E501
        :type nvmf_subsystem: NestedNvmfSubsystem
        """

        self._nvmf_subsystem = nvmf_subsystem

    @property
    def tr_type(self):
        """Gets the tr_type of this IscsiConnection.  # noqa: E501


        :return: The tr_type of this IscsiConnection.  # noqa: E501
        :rtype: StoreTransportType
        """
        return self._tr_type

    @tr_type.setter
    def tr_type(self, tr_type):
        """Sets the tr_type of this IscsiConnection.


        :param tr_type: The tr_type of this IscsiConnection.  # noqa: E501
        :type tr_type: StoreTransportType
        """

        self._tr_type = tr_type

    @property
    def type(self):
        """Gets the type of this IscsiConnection.  # noqa: E501


        :return: The type of this IscsiConnection.  # noqa: E501
        :rtype: StoreConnectionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IscsiConnection.


        :param type: The type of this IscsiConnection.  # noqa: E501
        :type type: StoreConnectionType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, IscsiConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiConnection):
            return True

        return self.to_dict() != other.to_dict()
