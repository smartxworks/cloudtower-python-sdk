# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VcenterAccount(object):
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
        'cluster': 'NestedCluster',
        'id': 'str',
        'ip': 'str',
        'is_valid': 'bool',
        'local_id': 'str',
        'port': 'int',
        'username': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'id': 'id',
        'ip': 'ip',
        'is_valid': 'is_valid',
        'local_id': 'local_id',
        'port': 'port',
        'username': 'username'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VcenterAccount - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._id = None
        self._ip = None
        self._is_valid = None
        self._local_id = None
        self._port = None
        self._username = None
        self.discriminator = None

        self.cluster = kwargs.get("cluster", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "ip" in kwargs:
            self.ip = kwargs["ip"]
        if "is_valid" in kwargs:
            self.is_valid = kwargs["is_valid"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "port" in kwargs:
            self.port = kwargs["port"]
        if "username" in kwargs:
            self.username = kwargs["username"]

    @property
    def cluster(self):
        """Gets the cluster of this VcenterAccount.  # noqa: E501


        :return: The cluster of this VcenterAccount.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this VcenterAccount.


        :param cluster: The cluster of this VcenterAccount.  # noqa: E501
        :type cluster: NestedCluster
        """

        self._cluster = cluster

    @property
    def id(self):
        """Gets the id of this VcenterAccount.  # noqa: E501


        :return: The id of this VcenterAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcenterAccount.


        :param id: The id of this VcenterAccount.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this VcenterAccount.  # noqa: E501


        :return: The ip of this VcenterAccount.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this VcenterAccount.


        :param ip: The ip of this VcenterAccount.  # noqa: E501
        :type ip: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def is_valid(self):
        """Gets the is_valid of this VcenterAccount.  # noqa: E501


        :return: The is_valid of this VcenterAccount.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this VcenterAccount.


        :param is_valid: The is_valid of this VcenterAccount.  # noqa: E501
        :type is_valid: bool
        """
        if self.local_vars_configuration.client_side_validation and is_valid is None:  # noqa: E501
            raise ValueError("Invalid value for `is_valid`, must not be `None`")  # noqa: E501

        self._is_valid = is_valid

    @property
    def local_id(self):
        """Gets the local_id of this VcenterAccount.  # noqa: E501


        :return: The local_id of this VcenterAccount.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VcenterAccount.


        :param local_id: The local_id of this VcenterAccount.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def port(self):
        """Gets the port of this VcenterAccount.  # noqa: E501


        :return: The port of this VcenterAccount.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VcenterAccount.


        :param port: The port of this VcenterAccount.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def username(self):
        """Gets the username of this VcenterAccount.  # noqa: E501


        :return: The username of this VcenterAccount.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this VcenterAccount.


        :param username: The username of this VcenterAccount.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, VcenterAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VcenterAccount):
            return True

        return self.to_dict() != other.to_dict()
