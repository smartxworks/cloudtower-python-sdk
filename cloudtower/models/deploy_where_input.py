# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class DeployWhereInput(object):
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
        '_and': 'list[DeployWhereInput]',
        '_not': 'list[DeployWhereInput]',
        '_or': 'list[DeployWhereInput]',
        'id': 'str',
        'id_contains': 'str',
        'id_ends_with': 'str',
        'id_gt': 'str',
        'id_gte': 'str',
        'id_in': 'list[str]',
        'id_lt': 'str',
        'id_lte': 'str',
        'id_not': 'str',
        'id_not_contains': 'str',
        'id_not_ends_with': 'str',
        'id_not_in': 'list[str]',
        'id_not_starts_with': 'str',
        'id_starts_with': 'str',
        'license': 'LicenseWhereInput',
        'version': 'str',
        'version_contains': 'str',
        'version_ends_with': 'str',
        'version_gt': 'str',
        'version_gte': 'str',
        'version_in': 'list[str]',
        'version_lt': 'str',
        'version_lte': 'str',
        'version_not': 'str',
        'version_not_contains': 'str',
        'version_not_ends_with': 'str',
        'version_not_in': 'list[str]',
        'version_not_starts_with': 'str',
        'version_starts_with': 'str'
    }

    attribute_map = {
        '_and': 'AND',
        '_not': 'NOT',
        '_or': 'OR',
        'id': 'id',
        'id_contains': 'id_contains',
        'id_ends_with': 'id_ends_with',
        'id_gt': 'id_gt',
        'id_gte': 'id_gte',
        'id_in': 'id_in',
        'id_lt': 'id_lt',
        'id_lte': 'id_lte',
        'id_not': 'id_not',
        'id_not_contains': 'id_not_contains',
        'id_not_ends_with': 'id_not_ends_with',
        'id_not_in': 'id_not_in',
        'id_not_starts_with': 'id_not_starts_with',
        'id_starts_with': 'id_starts_with',
        'license': 'license',
        'version': 'version',
        'version_contains': 'version_contains',
        'version_ends_with': 'version_ends_with',
        'version_gt': 'version_gt',
        'version_gte': 'version_gte',
        'version_in': 'version_in',
        'version_lt': 'version_lt',
        'version_lte': 'version_lte',
        'version_not': 'version_not',
        'version_not_contains': 'version_not_contains',
        'version_not_ends_with': 'version_not_ends_with',
        'version_not_in': 'version_not_in',
        'version_not_starts_with': 'version_not_starts_with',
        'version_starts_with': 'version_starts_with'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DeployWhereInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self.__and = None
        self.__not = None
        self.__or = None
        self._id = None
        self._id_contains = None
        self._id_ends_with = None
        self._id_gt = None
        self._id_gte = None
        self._id_in = None
        self._id_lt = None
        self._id_lte = None
        self._id_not = None
        self._id_not_contains = None
        self._id_not_ends_with = None
        self._id_not_in = None
        self._id_not_starts_with = None
        self._id_starts_with = None
        self._license = None
        self._version = None
        self._version_contains = None
        self._version_ends_with = None
        self._version_gt = None
        self._version_gte = None
        self._version_in = None
        self._version_lt = None
        self._version_lte = None
        self._version_not = None
        self._version_not_contains = None
        self._version_not_ends_with = None
        self._version_not_in = None
        self._version_not_starts_with = None
        self._version_starts_with = None
        self.discriminator = None

        self._and = kwargs.get("_and", None)
        self._not = kwargs.get("_not", None)
        self._or = kwargs.get("_or", None)
        self.id = kwargs.get("id", None)
        self.id_contains = kwargs.get("id_contains", None)
        self.id_ends_with = kwargs.get("id_ends_with", None)
        self.id_gt = kwargs.get("id_gt", None)
        self.id_gte = kwargs.get("id_gte", None)
        self.id_in = kwargs.get("id_in", None)
        self.id_lt = kwargs.get("id_lt", None)
        self.id_lte = kwargs.get("id_lte", None)
        self.id_not = kwargs.get("id_not", None)
        self.id_not_contains = kwargs.get("id_not_contains", None)
        self.id_not_ends_with = kwargs.get("id_not_ends_with", None)
        self.id_not_in = kwargs.get("id_not_in", None)
        self.id_not_starts_with = kwargs.get("id_not_starts_with", None)
        self.id_starts_with = kwargs.get("id_starts_with", None)
        self.license = kwargs.get("license", None)
        self.version = kwargs.get("version", None)
        self.version_contains = kwargs.get("version_contains", None)
        self.version_ends_with = kwargs.get("version_ends_with", None)
        self.version_gt = kwargs.get("version_gt", None)
        self.version_gte = kwargs.get("version_gte", None)
        self.version_in = kwargs.get("version_in", None)
        self.version_lt = kwargs.get("version_lt", None)
        self.version_lte = kwargs.get("version_lte", None)
        self.version_not = kwargs.get("version_not", None)
        self.version_not_contains = kwargs.get("version_not_contains", None)
        self.version_not_ends_with = kwargs.get("version_not_ends_with", None)
        self.version_not_in = kwargs.get("version_not_in", None)
        self.version_not_starts_with = kwargs.get("version_not_starts_with", None)
        self.version_starts_with = kwargs.get("version_starts_with", None)

    @property
    def _and(self):
        """Gets the _and of this DeployWhereInput.  # noqa: E501


        :return: The _and of this DeployWhereInput.  # noqa: E501
        :rtype: list[DeployWhereInput]
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this DeployWhereInput.


        :param _and: The _and of this DeployWhereInput.  # noqa: E501
        :type _and: list[DeployWhereInput]
        """

        self.__and = _and

    @property
    def _not(self):
        """Gets the _not of this DeployWhereInput.  # noqa: E501


        :return: The _not of this DeployWhereInput.  # noqa: E501
        :rtype: list[DeployWhereInput]
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this DeployWhereInput.


        :param _not: The _not of this DeployWhereInput.  # noqa: E501
        :type _not: list[DeployWhereInput]
        """

        self.__not = _not

    @property
    def _or(self):
        """Gets the _or of this DeployWhereInput.  # noqa: E501


        :return: The _or of this DeployWhereInput.  # noqa: E501
        :rtype: list[DeployWhereInput]
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this DeployWhereInput.


        :param _or: The _or of this DeployWhereInput.  # noqa: E501
        :type _or: list[DeployWhereInput]
        """

        self.__or = _or

    @property
    def id(self):
        """Gets the id of this DeployWhereInput.  # noqa: E501


        :return: The id of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeployWhereInput.


        :param id: The id of this DeployWhereInput.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def id_contains(self):
        """Gets the id_contains of this DeployWhereInput.  # noqa: E501


        :return: The id_contains of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_contains

    @id_contains.setter
    def id_contains(self, id_contains):
        """Sets the id_contains of this DeployWhereInput.


        :param id_contains: The id_contains of this DeployWhereInput.  # noqa: E501
        :type id_contains: str
        """

        self._id_contains = id_contains

    @property
    def id_ends_with(self):
        """Gets the id_ends_with of this DeployWhereInput.  # noqa: E501


        :return: The id_ends_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_ends_with

    @id_ends_with.setter
    def id_ends_with(self, id_ends_with):
        """Sets the id_ends_with of this DeployWhereInput.


        :param id_ends_with: The id_ends_with of this DeployWhereInput.  # noqa: E501
        :type id_ends_with: str
        """

        self._id_ends_with = id_ends_with

    @property
    def id_gt(self):
        """Gets the id_gt of this DeployWhereInput.  # noqa: E501


        :return: The id_gt of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gt

    @id_gt.setter
    def id_gt(self, id_gt):
        """Sets the id_gt of this DeployWhereInput.


        :param id_gt: The id_gt of this DeployWhereInput.  # noqa: E501
        :type id_gt: str
        """

        self._id_gt = id_gt

    @property
    def id_gte(self):
        """Gets the id_gte of this DeployWhereInput.  # noqa: E501


        :return: The id_gte of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gte

    @id_gte.setter
    def id_gte(self, id_gte):
        """Sets the id_gte of this DeployWhereInput.


        :param id_gte: The id_gte of this DeployWhereInput.  # noqa: E501
        :type id_gte: str
        """

        self._id_gte = id_gte

    @property
    def id_in(self):
        """Gets the id_in of this DeployWhereInput.  # noqa: E501


        :return: The id_in of this DeployWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_in

    @id_in.setter
    def id_in(self, id_in):
        """Sets the id_in of this DeployWhereInput.


        :param id_in: The id_in of this DeployWhereInput.  # noqa: E501
        :type id_in: list[str]
        """

        self._id_in = id_in

    @property
    def id_lt(self):
        """Gets the id_lt of this DeployWhereInput.  # noqa: E501


        :return: The id_lt of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lt

    @id_lt.setter
    def id_lt(self, id_lt):
        """Sets the id_lt of this DeployWhereInput.


        :param id_lt: The id_lt of this DeployWhereInput.  # noqa: E501
        :type id_lt: str
        """

        self._id_lt = id_lt

    @property
    def id_lte(self):
        """Gets the id_lte of this DeployWhereInput.  # noqa: E501


        :return: The id_lte of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lte

    @id_lte.setter
    def id_lte(self, id_lte):
        """Sets the id_lte of this DeployWhereInput.


        :param id_lte: The id_lte of this DeployWhereInput.  # noqa: E501
        :type id_lte: str
        """

        self._id_lte = id_lte

    @property
    def id_not(self):
        """Gets the id_not of this DeployWhereInput.  # noqa: E501


        :return: The id_not of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not

    @id_not.setter
    def id_not(self, id_not):
        """Sets the id_not of this DeployWhereInput.


        :param id_not: The id_not of this DeployWhereInput.  # noqa: E501
        :type id_not: str
        """

        self._id_not = id_not

    @property
    def id_not_contains(self):
        """Gets the id_not_contains of this DeployWhereInput.  # noqa: E501


        :return: The id_not_contains of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_contains

    @id_not_contains.setter
    def id_not_contains(self, id_not_contains):
        """Sets the id_not_contains of this DeployWhereInput.


        :param id_not_contains: The id_not_contains of this DeployWhereInput.  # noqa: E501
        :type id_not_contains: str
        """

        self._id_not_contains = id_not_contains

    @property
    def id_not_ends_with(self):
        """Gets the id_not_ends_with of this DeployWhereInput.  # noqa: E501


        :return: The id_not_ends_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_ends_with

    @id_not_ends_with.setter
    def id_not_ends_with(self, id_not_ends_with):
        """Sets the id_not_ends_with of this DeployWhereInput.


        :param id_not_ends_with: The id_not_ends_with of this DeployWhereInput.  # noqa: E501
        :type id_not_ends_with: str
        """

        self._id_not_ends_with = id_not_ends_with

    @property
    def id_not_in(self):
        """Gets the id_not_in of this DeployWhereInput.  # noqa: E501


        :return: The id_not_in of this DeployWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_not_in

    @id_not_in.setter
    def id_not_in(self, id_not_in):
        """Sets the id_not_in of this DeployWhereInput.


        :param id_not_in: The id_not_in of this DeployWhereInput.  # noqa: E501
        :type id_not_in: list[str]
        """

        self._id_not_in = id_not_in

    @property
    def id_not_starts_with(self):
        """Gets the id_not_starts_with of this DeployWhereInput.  # noqa: E501


        :return: The id_not_starts_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_starts_with

    @id_not_starts_with.setter
    def id_not_starts_with(self, id_not_starts_with):
        """Sets the id_not_starts_with of this DeployWhereInput.


        :param id_not_starts_with: The id_not_starts_with of this DeployWhereInput.  # noqa: E501
        :type id_not_starts_with: str
        """

        self._id_not_starts_with = id_not_starts_with

    @property
    def id_starts_with(self):
        """Gets the id_starts_with of this DeployWhereInput.  # noqa: E501


        :return: The id_starts_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_starts_with

    @id_starts_with.setter
    def id_starts_with(self, id_starts_with):
        """Sets the id_starts_with of this DeployWhereInput.


        :param id_starts_with: The id_starts_with of this DeployWhereInput.  # noqa: E501
        :type id_starts_with: str
        """

        self._id_starts_with = id_starts_with

    @property
    def license(self):
        """Gets the license of this DeployWhereInput.  # noqa: E501


        :return: The license of this DeployWhereInput.  # noqa: E501
        :rtype: LicenseWhereInput
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this DeployWhereInput.


        :param license: The license of this DeployWhereInput.  # noqa: E501
        :type license: LicenseWhereInput
        """

        self._license = license

    @property
    def version(self):
        """Gets the version of this DeployWhereInput.  # noqa: E501


        :return: The version of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeployWhereInput.


        :param version: The version of this DeployWhereInput.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def version_contains(self):
        """Gets the version_contains of this DeployWhereInput.  # noqa: E501


        :return: The version_contains of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_contains

    @version_contains.setter
    def version_contains(self, version_contains):
        """Sets the version_contains of this DeployWhereInput.


        :param version_contains: The version_contains of this DeployWhereInput.  # noqa: E501
        :type version_contains: str
        """

        self._version_contains = version_contains

    @property
    def version_ends_with(self):
        """Gets the version_ends_with of this DeployWhereInput.  # noqa: E501


        :return: The version_ends_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_ends_with

    @version_ends_with.setter
    def version_ends_with(self, version_ends_with):
        """Sets the version_ends_with of this DeployWhereInput.


        :param version_ends_with: The version_ends_with of this DeployWhereInput.  # noqa: E501
        :type version_ends_with: str
        """

        self._version_ends_with = version_ends_with

    @property
    def version_gt(self):
        """Gets the version_gt of this DeployWhereInput.  # noqa: E501


        :return: The version_gt of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_gt

    @version_gt.setter
    def version_gt(self, version_gt):
        """Sets the version_gt of this DeployWhereInput.


        :param version_gt: The version_gt of this DeployWhereInput.  # noqa: E501
        :type version_gt: str
        """

        self._version_gt = version_gt

    @property
    def version_gte(self):
        """Gets the version_gte of this DeployWhereInput.  # noqa: E501


        :return: The version_gte of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_gte

    @version_gte.setter
    def version_gte(self, version_gte):
        """Sets the version_gte of this DeployWhereInput.


        :param version_gte: The version_gte of this DeployWhereInput.  # noqa: E501
        :type version_gte: str
        """

        self._version_gte = version_gte

    @property
    def version_in(self):
        """Gets the version_in of this DeployWhereInput.  # noqa: E501


        :return: The version_in of this DeployWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._version_in

    @version_in.setter
    def version_in(self, version_in):
        """Sets the version_in of this DeployWhereInput.


        :param version_in: The version_in of this DeployWhereInput.  # noqa: E501
        :type version_in: list[str]
        """

        self._version_in = version_in

    @property
    def version_lt(self):
        """Gets the version_lt of this DeployWhereInput.  # noqa: E501


        :return: The version_lt of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_lt

    @version_lt.setter
    def version_lt(self, version_lt):
        """Sets the version_lt of this DeployWhereInput.


        :param version_lt: The version_lt of this DeployWhereInput.  # noqa: E501
        :type version_lt: str
        """

        self._version_lt = version_lt

    @property
    def version_lte(self):
        """Gets the version_lte of this DeployWhereInput.  # noqa: E501


        :return: The version_lte of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_lte

    @version_lte.setter
    def version_lte(self, version_lte):
        """Sets the version_lte of this DeployWhereInput.


        :param version_lte: The version_lte of this DeployWhereInput.  # noqa: E501
        :type version_lte: str
        """

        self._version_lte = version_lte

    @property
    def version_not(self):
        """Gets the version_not of this DeployWhereInput.  # noqa: E501


        :return: The version_not of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_not

    @version_not.setter
    def version_not(self, version_not):
        """Sets the version_not of this DeployWhereInput.


        :param version_not: The version_not of this DeployWhereInput.  # noqa: E501
        :type version_not: str
        """

        self._version_not = version_not

    @property
    def version_not_contains(self):
        """Gets the version_not_contains of this DeployWhereInput.  # noqa: E501


        :return: The version_not_contains of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_not_contains

    @version_not_contains.setter
    def version_not_contains(self, version_not_contains):
        """Sets the version_not_contains of this DeployWhereInput.


        :param version_not_contains: The version_not_contains of this DeployWhereInput.  # noqa: E501
        :type version_not_contains: str
        """

        self._version_not_contains = version_not_contains

    @property
    def version_not_ends_with(self):
        """Gets the version_not_ends_with of this DeployWhereInput.  # noqa: E501


        :return: The version_not_ends_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_not_ends_with

    @version_not_ends_with.setter
    def version_not_ends_with(self, version_not_ends_with):
        """Sets the version_not_ends_with of this DeployWhereInput.


        :param version_not_ends_with: The version_not_ends_with of this DeployWhereInput.  # noqa: E501
        :type version_not_ends_with: str
        """

        self._version_not_ends_with = version_not_ends_with

    @property
    def version_not_in(self):
        """Gets the version_not_in of this DeployWhereInput.  # noqa: E501


        :return: The version_not_in of this DeployWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._version_not_in

    @version_not_in.setter
    def version_not_in(self, version_not_in):
        """Sets the version_not_in of this DeployWhereInput.


        :param version_not_in: The version_not_in of this DeployWhereInput.  # noqa: E501
        :type version_not_in: list[str]
        """

        self._version_not_in = version_not_in

    @property
    def version_not_starts_with(self):
        """Gets the version_not_starts_with of this DeployWhereInput.  # noqa: E501


        :return: The version_not_starts_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_not_starts_with

    @version_not_starts_with.setter
    def version_not_starts_with(self, version_not_starts_with):
        """Sets the version_not_starts_with of this DeployWhereInput.


        :param version_not_starts_with: The version_not_starts_with of this DeployWhereInput.  # noqa: E501
        :type version_not_starts_with: str
        """

        self._version_not_starts_with = version_not_starts_with

    @property
    def version_starts_with(self):
        """Gets the version_starts_with of this DeployWhereInput.  # noqa: E501


        :return: The version_starts_with of this DeployWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._version_starts_with

    @version_starts_with.setter
    def version_starts_with(self, version_starts_with):
        """Sets the version_starts_with of this DeployWhereInput.


        :param version_starts_with: The version_starts_with of this DeployWhereInput.  # noqa: E501
        :type version_starts_with: str
        """

        self._version_starts_with = version_starts_with

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
        if not isinstance(other, DeployWhereInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeployWhereInput):
            return True

        return self.to_dict() != other.to_dict()
