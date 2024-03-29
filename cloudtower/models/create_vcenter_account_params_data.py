# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class CreateVcenterAccountParamsData(object):
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
        'port': 'int',
        'password': 'str',
        'username': 'str',
        'ip': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'port': 'port',
        'password': 'password',
        'username': 'username',
        'ip': 'ip',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateVcenterAccountParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._port = None
        self._password = None
        self._username = None
        self._ip = None
        self._cluster_id = None
        self.discriminator = None

        if "port" in kwargs:
            self.port = kwargs["port"]
        if "password" in kwargs:
            self.password = kwargs["password"]
        if "username" in kwargs:
            self.username = kwargs["username"]
        if "ip" in kwargs:
            self.ip = kwargs["ip"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]

    @property
    def port(self):
        """Gets the port of this CreateVcenterAccountParamsData.  # noqa: E501


        :return: The port of this CreateVcenterAccountParamsData.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateVcenterAccountParamsData.


        :param port: The port of this CreateVcenterAccountParamsData.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def password(self):
        """Gets the password of this CreateVcenterAccountParamsData.  # noqa: E501


        :return: The password of this CreateVcenterAccountParamsData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateVcenterAccountParamsData.


        :param password: The password of this CreateVcenterAccountParamsData.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this CreateVcenterAccountParamsData.  # noqa: E501


        :return: The username of this CreateVcenterAccountParamsData.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateVcenterAccountParamsData.


        :param username: The username of this CreateVcenterAccountParamsData.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def ip(self):
        """Gets the ip of this CreateVcenterAccountParamsData.  # noqa: E501


        :return: The ip of this CreateVcenterAccountParamsData.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CreateVcenterAccountParamsData.


        :param ip: The ip of this CreateVcenterAccountParamsData.  # noqa: E501
        :type ip: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateVcenterAccountParamsData.  # noqa: E501


        :return: The cluster_id of this CreateVcenterAccountParamsData.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateVcenterAccountParamsData.


        :param cluster_id: The cluster_id of this CreateVcenterAccountParamsData.  # noqa: E501
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
        if not isinstance(other, CreateVcenterAccountParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVcenterAccountParamsData):
            return True

        return self.to_dict() != other.to_dict()
