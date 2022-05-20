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


class VmRemoveCdRomParamsData(object):
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
        'cd_rom_ids': 'list[str]'
    }

    attribute_map = {
        'cd_rom_ids': 'cd_rom_ids'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmRemoveCdRomParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cd_rom_ids = None
        self.discriminator = None

        if "cd_rom_ids" in kwargs:
            self.cd_rom_ids = kwargs["cd_rom_ids"]

    @property
    def cd_rom_ids(self):
        """Gets the cd_rom_ids of this VmRemoveCdRomParamsData.  # noqa: E501


        :return: The cd_rom_ids of this VmRemoveCdRomParamsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._cd_rom_ids

    @cd_rom_ids.setter
    def cd_rom_ids(self, cd_rom_ids):
        """Sets the cd_rom_ids of this VmRemoveCdRomParamsData.


        :param cd_rom_ids: The cd_rom_ids of this VmRemoveCdRomParamsData.  # noqa: E501
        :type cd_rom_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and cd_rom_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `cd_rom_ids`, must not be `None`")  # noqa: E501

        self._cd_rom_ids = cd_rom_ids

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
        if not isinstance(other, VmRemoveCdRomParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmRemoveCdRomParamsData):
            return True

        return self.to_dict() != other.to_dict()
