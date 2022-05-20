# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class OrganizationWhereInput(object):
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
        '_and': 'list[OrganizationWhereInput]',
        'datacenters_every': 'DatacenterWhereInput',
        'datacenters_none': 'DatacenterWhereInput',
        'datacenters_some': 'DatacenterWhereInput',
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
        'name': 'str',
        'name_contains': 'str',
        'name_ends_with': 'str',
        'name_gt': 'str',
        'name_gte': 'str',
        'name_in': 'list[str]',
        'name_lt': 'str',
        'name_lte': 'str',
        'name_not': 'str',
        'name_not_contains': 'str',
        'name_not_ends_with': 'str',
        'name_not_in': 'list[str]',
        'name_not_starts_with': 'str',
        'name_starts_with': 'str',
        '_not': 'list[OrganizationWhereInput]',
        '_or': 'list[OrganizationWhereInput]'
    }

    attribute_map = {
        '_and': 'AND',
        'datacenters_every': 'datacenters_every',
        'datacenters_none': 'datacenters_none',
        'datacenters_some': 'datacenters_some',
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
        'name': 'name',
        'name_contains': 'name_contains',
        'name_ends_with': 'name_ends_with',
        'name_gt': 'name_gt',
        'name_gte': 'name_gte',
        'name_in': 'name_in',
        'name_lt': 'name_lt',
        'name_lte': 'name_lte',
        'name_not': 'name_not',
        'name_not_contains': 'name_not_contains',
        'name_not_ends_with': 'name_not_ends_with',
        'name_not_in': 'name_not_in',
        'name_not_starts_with': 'name_not_starts_with',
        'name_starts_with': 'name_starts_with',
        '_not': 'NOT',
        '_or': 'OR'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """OrganizationWhereInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self.__and = None
        self._datacenters_every = None
        self._datacenters_none = None
        self._datacenters_some = None
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
        self._name = None
        self._name_contains = None
        self._name_ends_with = None
        self._name_gt = None
        self._name_gte = None
        self._name_in = None
        self._name_lt = None
        self._name_lte = None
        self._name_not = None
        self._name_not_contains = None
        self._name_not_ends_with = None
        self._name_not_in = None
        self._name_not_starts_with = None
        self._name_starts_with = None
        self.__not = None
        self.__or = None
        self.discriminator = None

        self._and = kwargs.get("_and", None)
        self.datacenters_every = kwargs.get("datacenters_every", None)
        self.datacenters_none = kwargs.get("datacenters_none", None)
        self.datacenters_some = kwargs.get("datacenters_some", None)
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
        self.name = kwargs.get("name", None)
        self.name_contains = kwargs.get("name_contains", None)
        self.name_ends_with = kwargs.get("name_ends_with", None)
        self.name_gt = kwargs.get("name_gt", None)
        self.name_gte = kwargs.get("name_gte", None)
        self.name_in = kwargs.get("name_in", None)
        self.name_lt = kwargs.get("name_lt", None)
        self.name_lte = kwargs.get("name_lte", None)
        self.name_not = kwargs.get("name_not", None)
        self.name_not_contains = kwargs.get("name_not_contains", None)
        self.name_not_ends_with = kwargs.get("name_not_ends_with", None)
        self.name_not_in = kwargs.get("name_not_in", None)
        self.name_not_starts_with = kwargs.get("name_not_starts_with", None)
        self.name_starts_with = kwargs.get("name_starts_with", None)
        self._not = kwargs.get("_not", None)
        self._or = kwargs.get("_or", None)

    @property
    def _and(self):
        """Gets the _and of this OrganizationWhereInput.  # noqa: E501


        :return: The _and of this OrganizationWhereInput.  # noqa: E501
        :rtype: list[OrganizationWhereInput]
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this OrganizationWhereInput.


        :param _and: The _and of this OrganizationWhereInput.  # noqa: E501
        :type _and: list[OrganizationWhereInput]
        """

        self.__and = _and

    @property
    def datacenters_every(self):
        """Gets the datacenters_every of this OrganizationWhereInput.  # noqa: E501


        :return: The datacenters_every of this OrganizationWhereInput.  # noqa: E501
        :rtype: DatacenterWhereInput
        """
        return self._datacenters_every

    @datacenters_every.setter
    def datacenters_every(self, datacenters_every):
        """Sets the datacenters_every of this OrganizationWhereInput.


        :param datacenters_every: The datacenters_every of this OrganizationWhereInput.  # noqa: E501
        :type datacenters_every: DatacenterWhereInput
        """

        self._datacenters_every = datacenters_every

    @property
    def datacenters_none(self):
        """Gets the datacenters_none of this OrganizationWhereInput.  # noqa: E501


        :return: The datacenters_none of this OrganizationWhereInput.  # noqa: E501
        :rtype: DatacenterWhereInput
        """
        return self._datacenters_none

    @datacenters_none.setter
    def datacenters_none(self, datacenters_none):
        """Sets the datacenters_none of this OrganizationWhereInput.


        :param datacenters_none: The datacenters_none of this OrganizationWhereInput.  # noqa: E501
        :type datacenters_none: DatacenterWhereInput
        """

        self._datacenters_none = datacenters_none

    @property
    def datacenters_some(self):
        """Gets the datacenters_some of this OrganizationWhereInput.  # noqa: E501


        :return: The datacenters_some of this OrganizationWhereInput.  # noqa: E501
        :rtype: DatacenterWhereInput
        """
        return self._datacenters_some

    @datacenters_some.setter
    def datacenters_some(self, datacenters_some):
        """Sets the datacenters_some of this OrganizationWhereInput.


        :param datacenters_some: The datacenters_some of this OrganizationWhereInput.  # noqa: E501
        :type datacenters_some: DatacenterWhereInput
        """

        self._datacenters_some = datacenters_some

    @property
    def id(self):
        """Gets the id of this OrganizationWhereInput.  # noqa: E501


        :return: The id of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationWhereInput.


        :param id: The id of this OrganizationWhereInput.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def id_contains(self):
        """Gets the id_contains of this OrganizationWhereInput.  # noqa: E501


        :return: The id_contains of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_contains

    @id_contains.setter
    def id_contains(self, id_contains):
        """Sets the id_contains of this OrganizationWhereInput.


        :param id_contains: The id_contains of this OrganizationWhereInput.  # noqa: E501
        :type id_contains: str
        """

        self._id_contains = id_contains

    @property
    def id_ends_with(self):
        """Gets the id_ends_with of this OrganizationWhereInput.  # noqa: E501


        :return: The id_ends_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_ends_with

    @id_ends_with.setter
    def id_ends_with(self, id_ends_with):
        """Sets the id_ends_with of this OrganizationWhereInput.


        :param id_ends_with: The id_ends_with of this OrganizationWhereInput.  # noqa: E501
        :type id_ends_with: str
        """

        self._id_ends_with = id_ends_with

    @property
    def id_gt(self):
        """Gets the id_gt of this OrganizationWhereInput.  # noqa: E501


        :return: The id_gt of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gt

    @id_gt.setter
    def id_gt(self, id_gt):
        """Sets the id_gt of this OrganizationWhereInput.


        :param id_gt: The id_gt of this OrganizationWhereInput.  # noqa: E501
        :type id_gt: str
        """

        self._id_gt = id_gt

    @property
    def id_gte(self):
        """Gets the id_gte of this OrganizationWhereInput.  # noqa: E501


        :return: The id_gte of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gte

    @id_gte.setter
    def id_gte(self, id_gte):
        """Sets the id_gte of this OrganizationWhereInput.


        :param id_gte: The id_gte of this OrganizationWhereInput.  # noqa: E501
        :type id_gte: str
        """

        self._id_gte = id_gte

    @property
    def id_in(self):
        """Gets the id_in of this OrganizationWhereInput.  # noqa: E501


        :return: The id_in of this OrganizationWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_in

    @id_in.setter
    def id_in(self, id_in):
        """Sets the id_in of this OrganizationWhereInput.


        :param id_in: The id_in of this OrganizationWhereInput.  # noqa: E501
        :type id_in: list[str]
        """

        self._id_in = id_in

    @property
    def id_lt(self):
        """Gets the id_lt of this OrganizationWhereInput.  # noqa: E501


        :return: The id_lt of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lt

    @id_lt.setter
    def id_lt(self, id_lt):
        """Sets the id_lt of this OrganizationWhereInput.


        :param id_lt: The id_lt of this OrganizationWhereInput.  # noqa: E501
        :type id_lt: str
        """

        self._id_lt = id_lt

    @property
    def id_lte(self):
        """Gets the id_lte of this OrganizationWhereInput.  # noqa: E501


        :return: The id_lte of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lte

    @id_lte.setter
    def id_lte(self, id_lte):
        """Sets the id_lte of this OrganizationWhereInput.


        :param id_lte: The id_lte of this OrganizationWhereInput.  # noqa: E501
        :type id_lte: str
        """

        self._id_lte = id_lte

    @property
    def id_not(self):
        """Gets the id_not of this OrganizationWhereInput.  # noqa: E501


        :return: The id_not of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not

    @id_not.setter
    def id_not(self, id_not):
        """Sets the id_not of this OrganizationWhereInput.


        :param id_not: The id_not of this OrganizationWhereInput.  # noqa: E501
        :type id_not: str
        """

        self._id_not = id_not

    @property
    def id_not_contains(self):
        """Gets the id_not_contains of this OrganizationWhereInput.  # noqa: E501


        :return: The id_not_contains of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_contains

    @id_not_contains.setter
    def id_not_contains(self, id_not_contains):
        """Sets the id_not_contains of this OrganizationWhereInput.


        :param id_not_contains: The id_not_contains of this OrganizationWhereInput.  # noqa: E501
        :type id_not_contains: str
        """

        self._id_not_contains = id_not_contains

    @property
    def id_not_ends_with(self):
        """Gets the id_not_ends_with of this OrganizationWhereInput.  # noqa: E501


        :return: The id_not_ends_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_ends_with

    @id_not_ends_with.setter
    def id_not_ends_with(self, id_not_ends_with):
        """Sets the id_not_ends_with of this OrganizationWhereInput.


        :param id_not_ends_with: The id_not_ends_with of this OrganizationWhereInput.  # noqa: E501
        :type id_not_ends_with: str
        """

        self._id_not_ends_with = id_not_ends_with

    @property
    def id_not_in(self):
        """Gets the id_not_in of this OrganizationWhereInput.  # noqa: E501


        :return: The id_not_in of this OrganizationWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_not_in

    @id_not_in.setter
    def id_not_in(self, id_not_in):
        """Sets the id_not_in of this OrganizationWhereInput.


        :param id_not_in: The id_not_in of this OrganizationWhereInput.  # noqa: E501
        :type id_not_in: list[str]
        """

        self._id_not_in = id_not_in

    @property
    def id_not_starts_with(self):
        """Gets the id_not_starts_with of this OrganizationWhereInput.  # noqa: E501


        :return: The id_not_starts_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_starts_with

    @id_not_starts_with.setter
    def id_not_starts_with(self, id_not_starts_with):
        """Sets the id_not_starts_with of this OrganizationWhereInput.


        :param id_not_starts_with: The id_not_starts_with of this OrganizationWhereInput.  # noqa: E501
        :type id_not_starts_with: str
        """

        self._id_not_starts_with = id_not_starts_with

    @property
    def id_starts_with(self):
        """Gets the id_starts_with of this OrganizationWhereInput.  # noqa: E501


        :return: The id_starts_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_starts_with

    @id_starts_with.setter
    def id_starts_with(self, id_starts_with):
        """Sets the id_starts_with of this OrganizationWhereInput.


        :param id_starts_with: The id_starts_with of this OrganizationWhereInput.  # noqa: E501
        :type id_starts_with: str
        """

        self._id_starts_with = id_starts_with

    @property
    def name(self):
        """Gets the name of this OrganizationWhereInput.  # noqa: E501


        :return: The name of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationWhereInput.


        :param name: The name of this OrganizationWhereInput.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def name_contains(self):
        """Gets the name_contains of this OrganizationWhereInput.  # noqa: E501


        :return: The name_contains of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """Sets the name_contains of this OrganizationWhereInput.


        :param name_contains: The name_contains of this OrganizationWhereInput.  # noqa: E501
        :type name_contains: str
        """

        self._name_contains = name_contains

    @property
    def name_ends_with(self):
        """Gets the name_ends_with of this OrganizationWhereInput.  # noqa: E501


        :return: The name_ends_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_ends_with

    @name_ends_with.setter
    def name_ends_with(self, name_ends_with):
        """Sets the name_ends_with of this OrganizationWhereInput.


        :param name_ends_with: The name_ends_with of this OrganizationWhereInput.  # noqa: E501
        :type name_ends_with: str
        """

        self._name_ends_with = name_ends_with

    @property
    def name_gt(self):
        """Gets the name_gt of this OrganizationWhereInput.  # noqa: E501


        :return: The name_gt of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_gt

    @name_gt.setter
    def name_gt(self, name_gt):
        """Sets the name_gt of this OrganizationWhereInput.


        :param name_gt: The name_gt of this OrganizationWhereInput.  # noqa: E501
        :type name_gt: str
        """

        self._name_gt = name_gt

    @property
    def name_gte(self):
        """Gets the name_gte of this OrganizationWhereInput.  # noqa: E501


        :return: The name_gte of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_gte

    @name_gte.setter
    def name_gte(self, name_gte):
        """Sets the name_gte of this OrganizationWhereInput.


        :param name_gte: The name_gte of this OrganizationWhereInput.  # noqa: E501
        :type name_gte: str
        """

        self._name_gte = name_gte

    @property
    def name_in(self):
        """Gets the name_in of this OrganizationWhereInput.  # noqa: E501


        :return: The name_in of this OrganizationWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_in

    @name_in.setter
    def name_in(self, name_in):
        """Sets the name_in of this OrganizationWhereInput.


        :param name_in: The name_in of this OrganizationWhereInput.  # noqa: E501
        :type name_in: list[str]
        """

        self._name_in = name_in

    @property
    def name_lt(self):
        """Gets the name_lt of this OrganizationWhereInput.  # noqa: E501


        :return: The name_lt of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_lt

    @name_lt.setter
    def name_lt(self, name_lt):
        """Sets the name_lt of this OrganizationWhereInput.


        :param name_lt: The name_lt of this OrganizationWhereInput.  # noqa: E501
        :type name_lt: str
        """

        self._name_lt = name_lt

    @property
    def name_lte(self):
        """Gets the name_lte of this OrganizationWhereInput.  # noqa: E501


        :return: The name_lte of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_lte

    @name_lte.setter
    def name_lte(self, name_lte):
        """Sets the name_lte of this OrganizationWhereInput.


        :param name_lte: The name_lte of this OrganizationWhereInput.  # noqa: E501
        :type name_lte: str
        """

        self._name_lte = name_lte

    @property
    def name_not(self):
        """Gets the name_not of this OrganizationWhereInput.  # noqa: E501


        :return: The name_not of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not

    @name_not.setter
    def name_not(self, name_not):
        """Sets the name_not of this OrganizationWhereInput.


        :param name_not: The name_not of this OrganizationWhereInput.  # noqa: E501
        :type name_not: str
        """

        self._name_not = name_not

    @property
    def name_not_contains(self):
        """Gets the name_not_contains of this OrganizationWhereInput.  # noqa: E501


        :return: The name_not_contains of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not_contains

    @name_not_contains.setter
    def name_not_contains(self, name_not_contains):
        """Sets the name_not_contains of this OrganizationWhereInput.


        :param name_not_contains: The name_not_contains of this OrganizationWhereInput.  # noqa: E501
        :type name_not_contains: str
        """

        self._name_not_contains = name_not_contains

    @property
    def name_not_ends_with(self):
        """Gets the name_not_ends_with of this OrganizationWhereInput.  # noqa: E501


        :return: The name_not_ends_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not_ends_with

    @name_not_ends_with.setter
    def name_not_ends_with(self, name_not_ends_with):
        """Sets the name_not_ends_with of this OrganizationWhereInput.


        :param name_not_ends_with: The name_not_ends_with of this OrganizationWhereInput.  # noqa: E501
        :type name_not_ends_with: str
        """

        self._name_not_ends_with = name_not_ends_with

    @property
    def name_not_in(self):
        """Gets the name_not_in of this OrganizationWhereInput.  # noqa: E501


        :return: The name_not_in of this OrganizationWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_not_in

    @name_not_in.setter
    def name_not_in(self, name_not_in):
        """Sets the name_not_in of this OrganizationWhereInput.


        :param name_not_in: The name_not_in of this OrganizationWhereInput.  # noqa: E501
        :type name_not_in: list[str]
        """

        self._name_not_in = name_not_in

    @property
    def name_not_starts_with(self):
        """Gets the name_not_starts_with of this OrganizationWhereInput.  # noqa: E501


        :return: The name_not_starts_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not_starts_with

    @name_not_starts_with.setter
    def name_not_starts_with(self, name_not_starts_with):
        """Sets the name_not_starts_with of this OrganizationWhereInput.


        :param name_not_starts_with: The name_not_starts_with of this OrganizationWhereInput.  # noqa: E501
        :type name_not_starts_with: str
        """

        self._name_not_starts_with = name_not_starts_with

    @property
    def name_starts_with(self):
        """Gets the name_starts_with of this OrganizationWhereInput.  # noqa: E501


        :return: The name_starts_with of this OrganizationWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_starts_with

    @name_starts_with.setter
    def name_starts_with(self, name_starts_with):
        """Sets the name_starts_with of this OrganizationWhereInput.


        :param name_starts_with: The name_starts_with of this OrganizationWhereInput.  # noqa: E501
        :type name_starts_with: str
        """

        self._name_starts_with = name_starts_with

    @property
    def _not(self):
        """Gets the _not of this OrganizationWhereInput.  # noqa: E501


        :return: The _not of this OrganizationWhereInput.  # noqa: E501
        :rtype: list[OrganizationWhereInput]
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this OrganizationWhereInput.


        :param _not: The _not of this OrganizationWhereInput.  # noqa: E501
        :type _not: list[OrganizationWhereInput]
        """

        self.__not = _not

    @property
    def _or(self):
        """Gets the _or of this OrganizationWhereInput.  # noqa: E501


        :return: The _or of this OrganizationWhereInput.  # noqa: E501
        :rtype: list[OrganizationWhereInput]
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this OrganizationWhereInput.


        :param _or: The _or of this OrganizationWhereInput.  # noqa: E501
        :type _or: list[OrganizationWhereInput]
        """

        self.__or = _or

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
        if not isinstance(other, OrganizationWhereInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationWhereInput):
            return True

        return self.to_dict() != other.to_dict()