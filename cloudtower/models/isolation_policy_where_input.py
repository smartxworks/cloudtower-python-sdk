# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class IsolationPolicyWhereInput(object):
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
        '_and': 'list[IsolationPolicyWhereInput]',
        '_not': 'list[IsolationPolicyWhereInput]',
        '_or': 'list[IsolationPolicyWhereInput]',
        'everoute_cluster': 'EverouteClusterWhereInput',
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
        'labels_every': 'LabelWhereInput',
        'labels_none': 'LabelWhereInput',
        'labels_some': 'LabelWhereInput',
        'mode': 'IsolationMode',
        'mode_in': 'list[IsolationMode]',
        'mode_not': 'IsolationMode',
        'mode_not_in': 'list[IsolationMode]',
        'vm': 'VmWhereInput'
    }

    attribute_map = {
        '_and': 'AND',
        '_not': 'NOT',
        '_or': 'OR',
        'everoute_cluster': 'everoute_cluster',
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
        'labels_every': 'labels_every',
        'labels_none': 'labels_none',
        'labels_some': 'labels_some',
        'mode': 'mode',
        'mode_in': 'mode_in',
        'mode_not': 'mode_not',
        'mode_not_in': 'mode_not_in',
        'vm': 'vm'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IsolationPolicyWhereInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self.__and = None
        self.__not = None
        self.__or = None
        self._everoute_cluster = None
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
        self._labels_every = None
        self._labels_none = None
        self._labels_some = None
        self._mode = None
        self._mode_in = None
        self._mode_not = None
        self._mode_not_in = None
        self._vm = None
        self.discriminator = None

        self._and = kwargs.get("_and", None)
        self._not = kwargs.get("_not", None)
        self._or = kwargs.get("_or", None)
        self.everoute_cluster = kwargs.get("everoute_cluster", None)
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
        self.labels_every = kwargs.get("labels_every", None)
        self.labels_none = kwargs.get("labels_none", None)
        self.labels_some = kwargs.get("labels_some", None)
        self.mode = kwargs.get("mode", None)
        self.mode_in = kwargs.get("mode_in", None)
        self.mode_not = kwargs.get("mode_not", None)
        self.mode_not_in = kwargs.get("mode_not_in", None)
        self.vm = kwargs.get("vm", None)

    @property
    def _and(self):
        """Gets the _and of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The _and of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: list[IsolationPolicyWhereInput]
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this IsolationPolicyWhereInput.


        :param _and: The _and of this IsolationPolicyWhereInput.  # noqa: E501
        :type _and: list[IsolationPolicyWhereInput]
        """

        self.__and = _and

    @property
    def _not(self):
        """Gets the _not of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The _not of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: list[IsolationPolicyWhereInput]
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this IsolationPolicyWhereInput.


        :param _not: The _not of this IsolationPolicyWhereInput.  # noqa: E501
        :type _not: list[IsolationPolicyWhereInput]
        """

        self.__not = _not

    @property
    def _or(self):
        """Gets the _or of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The _or of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: list[IsolationPolicyWhereInput]
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this IsolationPolicyWhereInput.


        :param _or: The _or of this IsolationPolicyWhereInput.  # noqa: E501
        :type _or: list[IsolationPolicyWhereInput]
        """

        self.__or = _or

    @property
    def everoute_cluster(self):
        """Gets the everoute_cluster of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The everoute_cluster of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: EverouteClusterWhereInput
        """
        return self._everoute_cluster

    @everoute_cluster.setter
    def everoute_cluster(self, everoute_cluster):
        """Sets the everoute_cluster of this IsolationPolicyWhereInput.


        :param everoute_cluster: The everoute_cluster of this IsolationPolicyWhereInput.  # noqa: E501
        :type everoute_cluster: EverouteClusterWhereInput
        """

        self._everoute_cluster = everoute_cluster

    @property
    def id(self):
        """Gets the id of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IsolationPolicyWhereInput.


        :param id: The id of this IsolationPolicyWhereInput.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def id_contains(self):
        """Gets the id_contains of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_contains of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_contains

    @id_contains.setter
    def id_contains(self, id_contains):
        """Sets the id_contains of this IsolationPolicyWhereInput.


        :param id_contains: The id_contains of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_contains: str
        """

        self._id_contains = id_contains

    @property
    def id_ends_with(self):
        """Gets the id_ends_with of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_ends_with of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_ends_with

    @id_ends_with.setter
    def id_ends_with(self, id_ends_with):
        """Sets the id_ends_with of this IsolationPolicyWhereInput.


        :param id_ends_with: The id_ends_with of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_ends_with: str
        """

        self._id_ends_with = id_ends_with

    @property
    def id_gt(self):
        """Gets the id_gt of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_gt of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gt

    @id_gt.setter
    def id_gt(self, id_gt):
        """Sets the id_gt of this IsolationPolicyWhereInput.


        :param id_gt: The id_gt of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_gt: str
        """

        self._id_gt = id_gt

    @property
    def id_gte(self):
        """Gets the id_gte of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_gte of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gte

    @id_gte.setter
    def id_gte(self, id_gte):
        """Sets the id_gte of this IsolationPolicyWhereInput.


        :param id_gte: The id_gte of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_gte: str
        """

        self._id_gte = id_gte

    @property
    def id_in(self):
        """Gets the id_in of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_in of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_in

    @id_in.setter
    def id_in(self, id_in):
        """Sets the id_in of this IsolationPolicyWhereInput.


        :param id_in: The id_in of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_in: list[str]
        """

        self._id_in = id_in

    @property
    def id_lt(self):
        """Gets the id_lt of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_lt of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lt

    @id_lt.setter
    def id_lt(self, id_lt):
        """Sets the id_lt of this IsolationPolicyWhereInput.


        :param id_lt: The id_lt of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_lt: str
        """

        self._id_lt = id_lt

    @property
    def id_lte(self):
        """Gets the id_lte of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_lte of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lte

    @id_lte.setter
    def id_lte(self, id_lte):
        """Sets the id_lte of this IsolationPolicyWhereInput.


        :param id_lte: The id_lte of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_lte: str
        """

        self._id_lte = id_lte

    @property
    def id_not(self):
        """Gets the id_not of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_not of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not

    @id_not.setter
    def id_not(self, id_not):
        """Sets the id_not of this IsolationPolicyWhereInput.


        :param id_not: The id_not of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_not: str
        """

        self._id_not = id_not

    @property
    def id_not_contains(self):
        """Gets the id_not_contains of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_not_contains of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_contains

    @id_not_contains.setter
    def id_not_contains(self, id_not_contains):
        """Sets the id_not_contains of this IsolationPolicyWhereInput.


        :param id_not_contains: The id_not_contains of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_not_contains: str
        """

        self._id_not_contains = id_not_contains

    @property
    def id_not_ends_with(self):
        """Gets the id_not_ends_with of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_not_ends_with of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_ends_with

    @id_not_ends_with.setter
    def id_not_ends_with(self, id_not_ends_with):
        """Sets the id_not_ends_with of this IsolationPolicyWhereInput.


        :param id_not_ends_with: The id_not_ends_with of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_not_ends_with: str
        """

        self._id_not_ends_with = id_not_ends_with

    @property
    def id_not_in(self):
        """Gets the id_not_in of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_not_in of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_not_in

    @id_not_in.setter
    def id_not_in(self, id_not_in):
        """Sets the id_not_in of this IsolationPolicyWhereInput.


        :param id_not_in: The id_not_in of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_not_in: list[str]
        """

        self._id_not_in = id_not_in

    @property
    def id_not_starts_with(self):
        """Gets the id_not_starts_with of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_not_starts_with of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_starts_with

    @id_not_starts_with.setter
    def id_not_starts_with(self, id_not_starts_with):
        """Sets the id_not_starts_with of this IsolationPolicyWhereInput.


        :param id_not_starts_with: The id_not_starts_with of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_not_starts_with: str
        """

        self._id_not_starts_with = id_not_starts_with

    @property
    def id_starts_with(self):
        """Gets the id_starts_with of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The id_starts_with of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_starts_with

    @id_starts_with.setter
    def id_starts_with(self, id_starts_with):
        """Sets the id_starts_with of this IsolationPolicyWhereInput.


        :param id_starts_with: The id_starts_with of this IsolationPolicyWhereInput.  # noqa: E501
        :type id_starts_with: str
        """

        self._id_starts_with = id_starts_with

    @property
    def labels_every(self):
        """Gets the labels_every of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The labels_every of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: LabelWhereInput
        """
        return self._labels_every

    @labels_every.setter
    def labels_every(self, labels_every):
        """Sets the labels_every of this IsolationPolicyWhereInput.


        :param labels_every: The labels_every of this IsolationPolicyWhereInput.  # noqa: E501
        :type labels_every: LabelWhereInput
        """

        self._labels_every = labels_every

    @property
    def labels_none(self):
        """Gets the labels_none of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The labels_none of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: LabelWhereInput
        """
        return self._labels_none

    @labels_none.setter
    def labels_none(self, labels_none):
        """Sets the labels_none of this IsolationPolicyWhereInput.


        :param labels_none: The labels_none of this IsolationPolicyWhereInput.  # noqa: E501
        :type labels_none: LabelWhereInput
        """

        self._labels_none = labels_none

    @property
    def labels_some(self):
        """Gets the labels_some of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The labels_some of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: LabelWhereInput
        """
        return self._labels_some

    @labels_some.setter
    def labels_some(self, labels_some):
        """Sets the labels_some of this IsolationPolicyWhereInput.


        :param labels_some: The labels_some of this IsolationPolicyWhereInput.  # noqa: E501
        :type labels_some: LabelWhereInput
        """

        self._labels_some = labels_some

    @property
    def mode(self):
        """Gets the mode of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The mode of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: IsolationMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this IsolationPolicyWhereInput.


        :param mode: The mode of this IsolationPolicyWhereInput.  # noqa: E501
        :type mode: IsolationMode
        """

        self._mode = mode

    @property
    def mode_in(self):
        """Gets the mode_in of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The mode_in of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: list[IsolationMode]
        """
        return self._mode_in

    @mode_in.setter
    def mode_in(self, mode_in):
        """Sets the mode_in of this IsolationPolicyWhereInput.


        :param mode_in: The mode_in of this IsolationPolicyWhereInput.  # noqa: E501
        :type mode_in: list[IsolationMode]
        """

        self._mode_in = mode_in

    @property
    def mode_not(self):
        """Gets the mode_not of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The mode_not of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: IsolationMode
        """
        return self._mode_not

    @mode_not.setter
    def mode_not(self, mode_not):
        """Sets the mode_not of this IsolationPolicyWhereInput.


        :param mode_not: The mode_not of this IsolationPolicyWhereInput.  # noqa: E501
        :type mode_not: IsolationMode
        """

        self._mode_not = mode_not

    @property
    def mode_not_in(self):
        """Gets the mode_not_in of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The mode_not_in of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: list[IsolationMode]
        """
        return self._mode_not_in

    @mode_not_in.setter
    def mode_not_in(self, mode_not_in):
        """Sets the mode_not_in of this IsolationPolicyWhereInput.


        :param mode_not_in: The mode_not_in of this IsolationPolicyWhereInput.  # noqa: E501
        :type mode_not_in: list[IsolationMode]
        """

        self._mode_not_in = mode_not_in

    @property
    def vm(self):
        """Gets the vm of this IsolationPolicyWhereInput.  # noqa: E501


        :return: The vm of this IsolationPolicyWhereInput.  # noqa: E501
        :rtype: VmWhereInput
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this IsolationPolicyWhereInput.


        :param vm: The vm of this IsolationPolicyWhereInput.  # noqa: E501
        :type vm: VmWhereInput
        """

        self._vm = vm

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
        if not isinstance(other, IsolationPolicyWhereInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IsolationPolicyWhereInput):
            return True

        return self.to_dict() != other.to_dict()
