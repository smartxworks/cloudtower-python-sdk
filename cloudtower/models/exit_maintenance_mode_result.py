# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ExitMaintenanceModeResult(object):
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
        'offline_migrate_vms': 'list[MaintenanceModeVmInfo]',
        'live_migrate_vms': 'list[MaintenanceModeVmInfo]',
        'shut_down_vms': 'list[MaintenanceModeVmInfo]'
    }

    attribute_map = {
        'offline_migrate_vms': 'offlineMigrateVms',
        'live_migrate_vms': 'liveMigrateVms',
        'shut_down_vms': 'shutDownVms'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ExitMaintenanceModeResult - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._offline_migrate_vms = None
        self._live_migrate_vms = None
        self._shut_down_vms = None
        self.discriminator = None

        if "offline_migrate_vms" in kwargs:
            self.offline_migrate_vms = kwargs["offline_migrate_vms"]
        if "live_migrate_vms" in kwargs:
            self.live_migrate_vms = kwargs["live_migrate_vms"]
        if "shut_down_vms" in kwargs:
            self.shut_down_vms = kwargs["shut_down_vms"]

    @property
    def offline_migrate_vms(self):
        """Gets the offline_migrate_vms of this ExitMaintenanceModeResult.  # noqa: E501


        :return: The offline_migrate_vms of this ExitMaintenanceModeResult.  # noqa: E501
        :rtype: list[MaintenanceModeVmInfo]
        """
        return self._offline_migrate_vms

    @offline_migrate_vms.setter
    def offline_migrate_vms(self, offline_migrate_vms):
        """Sets the offline_migrate_vms of this ExitMaintenanceModeResult.


        :param offline_migrate_vms: The offline_migrate_vms of this ExitMaintenanceModeResult.  # noqa: E501
        :type offline_migrate_vms: list[MaintenanceModeVmInfo]
        """
        if self.local_vars_configuration.client_side_validation and offline_migrate_vms is None:  # noqa: E501
            raise ValueError("Invalid value for `offline_migrate_vms`, must not be `None`")  # noqa: E501

        self._offline_migrate_vms = offline_migrate_vms

    @property
    def live_migrate_vms(self):
        """Gets the live_migrate_vms of this ExitMaintenanceModeResult.  # noqa: E501


        :return: The live_migrate_vms of this ExitMaintenanceModeResult.  # noqa: E501
        :rtype: list[MaintenanceModeVmInfo]
        """
        return self._live_migrate_vms

    @live_migrate_vms.setter
    def live_migrate_vms(self, live_migrate_vms):
        """Sets the live_migrate_vms of this ExitMaintenanceModeResult.


        :param live_migrate_vms: The live_migrate_vms of this ExitMaintenanceModeResult.  # noqa: E501
        :type live_migrate_vms: list[MaintenanceModeVmInfo]
        """
        if self.local_vars_configuration.client_side_validation and live_migrate_vms is None:  # noqa: E501
            raise ValueError("Invalid value for `live_migrate_vms`, must not be `None`")  # noqa: E501

        self._live_migrate_vms = live_migrate_vms

    @property
    def shut_down_vms(self):
        """Gets the shut_down_vms of this ExitMaintenanceModeResult.  # noqa: E501


        :return: The shut_down_vms of this ExitMaintenanceModeResult.  # noqa: E501
        :rtype: list[MaintenanceModeVmInfo]
        """
        return self._shut_down_vms

    @shut_down_vms.setter
    def shut_down_vms(self, shut_down_vms):
        """Sets the shut_down_vms of this ExitMaintenanceModeResult.


        :param shut_down_vms: The shut_down_vms of this ExitMaintenanceModeResult.  # noqa: E501
        :type shut_down_vms: list[MaintenanceModeVmInfo]
        """
        if self.local_vars_configuration.client_side_validation and shut_down_vms is None:  # noqa: E501
            raise ValueError("Invalid value for `shut_down_vms`, must not be `None`")  # noqa: E501

        self._shut_down_vms = shut_down_vms

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
        if not isinstance(other, ExitMaintenanceModeResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExitMaintenanceModeResult):
            return True

        return self.to_dict() != other.to_dict()
