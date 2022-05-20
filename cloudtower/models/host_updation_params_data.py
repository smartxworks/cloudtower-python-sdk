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


class HostUpdationParamsData(object):
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
        'ipmi': 'HostBatchCreateIpmiInput',
        'scvm_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'ipmi': 'ipmi',
        'scvm_name': 'scvm_name',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """HostUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._ipmi = None
        self._scvm_name = None
        self._name = None
        self.discriminator = None

        if "ipmi" in kwargs:
            self.ipmi = kwargs["ipmi"]
        if "scvm_name" in kwargs:
            self.scvm_name = kwargs["scvm_name"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def ipmi(self):
        """Gets the ipmi of this HostUpdationParamsData.  # noqa: E501


        :return: The ipmi of this HostUpdationParamsData.  # noqa: E501
        :rtype: HostBatchCreateIpmiInput
        """
        return self._ipmi

    @ipmi.setter
    def ipmi(self, ipmi):
        """Sets the ipmi of this HostUpdationParamsData.


        :param ipmi: The ipmi of this HostUpdationParamsData.  # noqa: E501
        :type ipmi: HostBatchCreateIpmiInput
        """

        self._ipmi = ipmi

    @property
    def scvm_name(self):
        """Gets the scvm_name of this HostUpdationParamsData.  # noqa: E501


        :return: The scvm_name of this HostUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._scvm_name

    @scvm_name.setter
    def scvm_name(self, scvm_name):
        """Sets the scvm_name of this HostUpdationParamsData.


        :param scvm_name: The scvm_name of this HostUpdationParamsData.  # noqa: E501
        :type scvm_name: str
        """

        self._scvm_name = scvm_name

    @property
    def name(self):
        """Gets the name of this HostUpdationParamsData.  # noqa: E501


        :return: The name of this HostUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostUpdationParamsData.


        :param name: The name of this HostUpdationParamsData.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, HostUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()