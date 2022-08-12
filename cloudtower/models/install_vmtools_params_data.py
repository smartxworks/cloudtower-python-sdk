# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.3.0
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


class InstallVmtoolsParamsData(object):
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
        'svt_image_id': 'str',
        'cd_rom_id': 'str'
    }

    attribute_map = {
        'svt_image_id': 'svt_image_id',
        'cd_rom_id': 'cd_rom_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """InstallVmtoolsParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._svt_image_id = None
        self._cd_rom_id = None
        self.discriminator = None

        if "svt_image_id" in kwargs:
            self.svt_image_id = kwargs["svt_image_id"]
        if "cd_rom_id" in kwargs:
            self.cd_rom_id = kwargs["cd_rom_id"]

    @property
    def svt_image_id(self):
        """Gets the svt_image_id of this InstallVmtoolsParamsData.  # noqa: E501


        :return: The svt_image_id of this InstallVmtoolsParamsData.  # noqa: E501
        :rtype: str
        """
        return self._svt_image_id

    @svt_image_id.setter
    def svt_image_id(self, svt_image_id):
        """Sets the svt_image_id of this InstallVmtoolsParamsData.


        :param svt_image_id: The svt_image_id of this InstallVmtoolsParamsData.  # noqa: E501
        :type svt_image_id: str
        """
        if self.local_vars_configuration.client_side_validation and svt_image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `svt_image_id`, must not be `None`")  # noqa: E501

        self._svt_image_id = svt_image_id

    @property
    def cd_rom_id(self):
        """Gets the cd_rom_id of this InstallVmtoolsParamsData.  # noqa: E501


        :return: The cd_rom_id of this InstallVmtoolsParamsData.  # noqa: E501
        :rtype: str
        """
        return self._cd_rom_id

    @cd_rom_id.setter
    def cd_rom_id(self, cd_rom_id):
        """Sets the cd_rom_id of this InstallVmtoolsParamsData.


        :param cd_rom_id: The cd_rom_id of this InstallVmtoolsParamsData.  # noqa: E501
        :type cd_rom_id: str
        """
        if self.local_vars_configuration.client_side_validation and cd_rom_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cd_rom_id`, must not be `None`")  # noqa: E501

        self._cd_rom_id = cd_rom_id

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
        if not isinstance(other, InstallVmtoolsParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstallVmtoolsParamsData):
            return True

        return self.to_dict() != other.to_dict()
