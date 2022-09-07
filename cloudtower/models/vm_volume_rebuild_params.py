# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmVolumeRebuildParams(object):
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
        'name': 'str',
        'description': 'str',
        'volume_snapshot_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'volume_snapshot_id': 'volume_snapshot_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmVolumeRebuildParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._name = None
        self._description = None
        self._volume_snapshot_id = None
        self.discriminator = None

        if "name" in kwargs:
            self.name = kwargs["name"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "volume_snapshot_id" in kwargs:
            self.volume_snapshot_id = kwargs["volume_snapshot_id"]

    @property
    def name(self):
        """Gets the name of this VmVolumeRebuildParams.  # noqa: E501


        :return: The name of this VmVolumeRebuildParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmVolumeRebuildParams.


        :param name: The name of this VmVolumeRebuildParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this VmVolumeRebuildParams.  # noqa: E501


        :return: The description of this VmVolumeRebuildParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VmVolumeRebuildParams.


        :param description: The description of this VmVolumeRebuildParams.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def volume_snapshot_id(self):
        """Gets the volume_snapshot_id of this VmVolumeRebuildParams.  # noqa: E501


        :return: The volume_snapshot_id of this VmVolumeRebuildParams.  # noqa: E501
        :rtype: str
        """
        return self._volume_snapshot_id

    @volume_snapshot_id.setter
    def volume_snapshot_id(self, volume_snapshot_id):
        """Sets the volume_snapshot_id of this VmVolumeRebuildParams.


        :param volume_snapshot_id: The volume_snapshot_id of this VmVolumeRebuildParams.  # noqa: E501
        :type volume_snapshot_id: str
        """
        if self.local_vars_configuration.client_side_validation and volume_snapshot_id is None:  # noqa: E501
            raise ValueError("Invalid value for `volume_snapshot_id`, must not be `None`")  # noqa: E501

        self._volume_snapshot_id = volume_snapshot_id

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
        if not isinstance(other, VmVolumeRebuildParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmVolumeRebuildParams):
            return True

        return self.to_dict() != other.to_dict()