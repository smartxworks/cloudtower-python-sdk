# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class User(object):
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
        'auth_config_id': 'str',
        'display_username': 'str',
        'email_address': 'str',
        'id': 'str',
        'internal': 'bool',
        'ldap_dn': 'str',
        'mobile_phone': 'str',
        'name': 'str',
        'password_expired': 'bool',
        'password_recover_qa': 'NestedPasswordRecoverQa',
        'password_updated_at': 'str',
        'role': 'UserRole',
        'roles': 'list[NestedUserRoleNext]',
        'source': 'UserSource',
        'username': 'str'
    }

    attribute_map = {
        'auth_config_id': 'auth_config_id',
        'display_username': 'display_username',
        'email_address': 'email_address',
        'id': 'id',
        'internal': 'internal',
        'ldap_dn': 'ldap_dn',
        'mobile_phone': 'mobile_phone',
        'name': 'name',
        'password_expired': 'password_expired',
        'password_recover_qa': 'password_recover_qa',
        'password_updated_at': 'password_updated_at',
        'role': 'role',
        'roles': 'roles',
        'source': 'source',
        'username': 'username'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._auth_config_id = None
        self._display_username = None
        self._email_address = None
        self._id = None
        self._internal = None
        self._ldap_dn = None
        self._mobile_phone = None
        self._name = None
        self._password_expired = None
        self._password_recover_qa = None
        self._password_updated_at = None
        self._role = None
        self._roles = None
        self._source = None
        self._username = None
        self.discriminator = None

        self.auth_config_id = kwargs.get("auth_config_id", None)
        if "display_username" in kwargs:
            self.display_username = kwargs["display_username"]
        self.email_address = kwargs.get("email_address", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "internal" in kwargs:
            self.internal = kwargs["internal"]
        self.ldap_dn = kwargs.get("ldap_dn", None)
        self.mobile_phone = kwargs.get("mobile_phone", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.password_expired = kwargs.get("password_expired", None)
        self.password_recover_qa = kwargs.get("password_recover_qa", None)
        self.password_updated_at = kwargs.get("password_updated_at", None)
        self.role = kwargs.get("role", None)
        self.roles = kwargs.get("roles", None)
        if "source" in kwargs:
            self.source = kwargs["source"]
        if "username" in kwargs:
            self.username = kwargs["username"]

    @property
    def auth_config_id(self):
        """Gets the auth_config_id of this User.  # noqa: E501


        :return: The auth_config_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._auth_config_id

    @auth_config_id.setter
    def auth_config_id(self, auth_config_id):
        """Sets the auth_config_id of this User.


        :param auth_config_id: The auth_config_id of this User.  # noqa: E501
        :type auth_config_id: str
        """

        self._auth_config_id = auth_config_id

    @property
    def display_username(self):
        """Gets the display_username of this User.  # noqa: E501


        :return: The display_username of this User.  # noqa: E501
        :rtype: str
        """
        return self._display_username

    @display_username.setter
    def display_username(self, display_username):
        """Sets the display_username of this User.


        :param display_username: The display_username of this User.  # noqa: E501
        :type display_username: str
        """
        if self.local_vars_configuration.client_side_validation and display_username is None:  # noqa: E501
            raise ValueError("Invalid value for `display_username`, must not be `None`")  # noqa: E501

        self._display_username = display_username

    @property
    def email_address(self):
        """Gets the email_address of this User.  # noqa: E501


        :return: The email_address of this User.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this User.


        :param email_address: The email_address of this User.  # noqa: E501
        :type email_address: str
        """

        self._email_address = email_address

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def internal(self):
        """Gets the internal of this User.  # noqa: E501


        :return: The internal of this User.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this User.


        :param internal: The internal of this User.  # noqa: E501
        :type internal: bool
        """
        if self.local_vars_configuration.client_side_validation and internal is None:  # noqa: E501
            raise ValueError("Invalid value for `internal`, must not be `None`")  # noqa: E501

        self._internal = internal

    @property
    def ldap_dn(self):
        """Gets the ldap_dn of this User.  # noqa: E501


        :return: The ldap_dn of this User.  # noqa: E501
        :rtype: str
        """
        return self._ldap_dn

    @ldap_dn.setter
    def ldap_dn(self, ldap_dn):
        """Sets the ldap_dn of this User.


        :param ldap_dn: The ldap_dn of this User.  # noqa: E501
        :type ldap_dn: str
        """

        self._ldap_dn = ldap_dn

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this User.  # noqa: E501


        :return: The mobile_phone of this User.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this User.


        :param mobile_phone: The mobile_phone of this User.  # noqa: E501
        :type mobile_phone: str
        """

        self._mobile_phone = mobile_phone

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password_expired(self):
        """Gets the password_expired of this User.  # noqa: E501


        :return: The password_expired of this User.  # noqa: E501
        :rtype: bool
        """
        return self._password_expired

    @password_expired.setter
    def password_expired(self, password_expired):
        """Sets the password_expired of this User.


        :param password_expired: The password_expired of this User.  # noqa: E501
        :type password_expired: bool
        """

        self._password_expired = password_expired

    @property
    def password_recover_qa(self):
        """Gets the password_recover_qa of this User.  # noqa: E501


        :return: The password_recover_qa of this User.  # noqa: E501
        :rtype: NestedPasswordRecoverQa
        """
        return self._password_recover_qa

    @password_recover_qa.setter
    def password_recover_qa(self, password_recover_qa):
        """Sets the password_recover_qa of this User.


        :param password_recover_qa: The password_recover_qa of this User.  # noqa: E501
        :type password_recover_qa: NestedPasswordRecoverQa
        """

        self._password_recover_qa = password_recover_qa

    @property
    def password_updated_at(self):
        """Gets the password_updated_at of this User.  # noqa: E501


        :return: The password_updated_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._password_updated_at

    @password_updated_at.setter
    def password_updated_at(self, password_updated_at):
        """Sets the password_updated_at of this User.


        :param password_updated_at: The password_updated_at of this User.  # noqa: E501
        :type password_updated_at: str
        """

        self._password_updated_at = password_updated_at

    @property
    def role(self):
        """Gets the role of this User.  # noqa: E501


        :return: The role of this User.  # noqa: E501
        :rtype: UserRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.


        :param role: The role of this User.  # noqa: E501
        :type role: UserRole
        """

        self._role = role

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501


        :return: The roles of this User.  # noqa: E501
        :rtype: list[NestedUserRoleNext]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.


        :param roles: The roles of this User.  # noqa: E501
        :type roles: list[NestedUserRoleNext]
        """

        self._roles = roles

    @property
    def source(self):
        """Gets the source of this User.  # noqa: E501


        :return: The source of this User.  # noqa: E501
        :rtype: UserSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this User.


        :param source: The source of this User.  # noqa: E501
        :type source: UserSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501


        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.


        :param username: The username of this User.  # noqa: E501
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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
