# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.2.0
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


class UserCreationParams(object):
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
        'mobile_phone': 'str',
        'email_address': 'str',
        'internal': 'bool',
        'role_id': 'str',
        'name': 'str',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'mobile_phone': 'mobile_phone',
        'email_address': 'email_address',
        'internal': 'internal',
        'role_id': 'role_id',
        'name': 'name',
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """UserCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._mobile_phone = None
        self._email_address = None
        self._internal = None
        self._role_id = None
        self._name = None
        self._password = None
        self._username = None
        self.discriminator = None

        if "mobile_phone" in kwargs:
            self.mobile_phone = kwargs["mobile_phone"]
        if "email_address" in kwargs:
            self.email_address = kwargs["email_address"]
        if "internal" in kwargs:
            self.internal = kwargs["internal"]
        if "role_id" in kwargs:
            self.role_id = kwargs["role_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "password" in kwargs:
            self.password = kwargs["password"]
        if "username" in kwargs:
            self.username = kwargs["username"]

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this UserCreationParams.  # noqa: E501


        :return: The mobile_phone of this UserCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this UserCreationParams.


        :param mobile_phone: The mobile_phone of this UserCreationParams.  # noqa: E501
        :type mobile_phone: str
        """

        self._mobile_phone = mobile_phone

    @property
    def email_address(self):
        """Gets the email_address of this UserCreationParams.  # noqa: E501


        :return: The email_address of this UserCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserCreationParams.


        :param email_address: The email_address of this UserCreationParams.  # noqa: E501
        :type email_address: str
        """

        self._email_address = email_address

    @property
    def internal(self):
        """Gets the internal of this UserCreationParams.  # noqa: E501


        :return: The internal of this UserCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this UserCreationParams.


        :param internal: The internal of this UserCreationParams.  # noqa: E501
        :type internal: bool
        """

        self._internal = internal

    @property
    def role_id(self):
        """Gets the role_id of this UserCreationParams.  # noqa: E501


        :return: The role_id of this UserCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this UserCreationParams.


        :param role_id: The role_id of this UserCreationParams.  # noqa: E501
        :type role_id: str
        """
        if self.local_vars_configuration.client_side_validation and role_id is None:  # noqa: E501
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def name(self):
        """Gets the name of this UserCreationParams.  # noqa: E501


        :return: The name of this UserCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserCreationParams.


        :param name: The name of this UserCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this UserCreationParams.  # noqa: E501


        :return: The password of this UserCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserCreationParams.


        :param password: The password of this UserCreationParams.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this UserCreationParams.  # noqa: E501


        :return: The username of this UserCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserCreationParams.


        :param username: The username of this UserCreationParams.  # noqa: E501
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
        if not isinstance(other, UserCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserCreationParams):
            return True

        return self.to_dict() != other.to_dict()
