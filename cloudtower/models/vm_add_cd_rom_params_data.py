# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmAddCdRomParamsData(object):
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
        'vm_cd_roms': 'list[VmCdRomParams]'
    }

    attribute_map = {
        'vm_cd_roms': 'vm_cd_roms'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmAddCdRomParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._vm_cd_roms = None
        self.discriminator = None

        if "vm_cd_roms" in kwargs:
            self.vm_cd_roms = kwargs["vm_cd_roms"]

    @property
    def vm_cd_roms(self):
        """Gets the vm_cd_roms of this VmAddCdRomParamsData.  # noqa: E501


        :return: The vm_cd_roms of this VmAddCdRomParamsData.  # noqa: E501
        :rtype: list[VmCdRomParams]
        """
        return self._vm_cd_roms

    @vm_cd_roms.setter
    def vm_cd_roms(self, vm_cd_roms):
        """Sets the vm_cd_roms of this VmAddCdRomParamsData.


        :param vm_cd_roms: The vm_cd_roms of this VmAddCdRomParamsData.  # noqa: E501
        :type vm_cd_roms: list[VmCdRomParams]
        """
        if self.local_vars_configuration.client_side_validation and vm_cd_roms is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_cd_roms`, must not be `None`")  # noqa: E501

        self._vm_cd_roms = vm_cd_roms

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
        if not isinstance(other, VmAddCdRomParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmAddCdRomParamsData):
            return True

        return self.to_dict() != other.to_dict()
