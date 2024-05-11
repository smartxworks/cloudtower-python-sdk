# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class MaintenanceModeVmInfo(object):
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
        'vm_uuid': 'str',
        'vm_state': 'str',
        'vm_name': 'str',
        'vm_ha': 'bool',
        'verify': 'MaintenanceModeVerify',
        'target_host_name': 'str',
        'state': 'str'
    }

    attribute_map = {
        'vm_uuid': 'vm_uuid',
        'vm_state': 'vm_state',
        'vm_name': 'vm_name',
        'vm_ha': 'vm_ha',
        'verify': 'verify',
        'target_host_name': 'target_host_name',
        'state': 'state'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """MaintenanceModeVmInfo - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._vm_uuid = None
        self._vm_state = None
        self._vm_name = None
        self._vm_ha = None
        self._verify = None
        self._target_host_name = None
        self._state = None
        self.discriminator = None

        self.vm_uuid = kwargs.get("vm_uuid", None)
        self.vm_state = kwargs.get("vm_state", None)
        self.vm_name = kwargs.get("vm_name", None)
        self.vm_ha = kwargs.get("vm_ha", None)
        self.verify = kwargs.get("verify", None)
        self.target_host_name = kwargs.get("target_host_name", None)
        self.state = kwargs.get("state", None)

    @property
    def vm_uuid(self):
        """Gets the vm_uuid of this MaintenanceModeVmInfo.  # noqa: E501


        :return: The vm_uuid of this MaintenanceModeVmInfo.  # noqa: E501
        :rtype: str
        """
        return self._vm_uuid

    @vm_uuid.setter
    def vm_uuid(self, vm_uuid):
        """Sets the vm_uuid of this MaintenanceModeVmInfo.


        :param vm_uuid: The vm_uuid of this MaintenanceModeVmInfo.  # noqa: E501
        :type vm_uuid: str
        """

        self._vm_uuid = vm_uuid

    @property
    def vm_state(self):
        """Gets the vm_state of this MaintenanceModeVmInfo.  # noqa: E501


        :return: The vm_state of this MaintenanceModeVmInfo.  # noqa: E501
        :rtype: str
        """
        return self._vm_state

    @vm_state.setter
    def vm_state(self, vm_state):
        """Sets the vm_state of this MaintenanceModeVmInfo.


        :param vm_state: The vm_state of this MaintenanceModeVmInfo.  # noqa: E501
        :type vm_state: str
        """

        self._vm_state = vm_state

    @property
    def vm_name(self):
        """Gets the vm_name of this MaintenanceModeVmInfo.  # noqa: E501


        :return: The vm_name of this MaintenanceModeVmInfo.  # noqa: E501
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this MaintenanceModeVmInfo.


        :param vm_name: The vm_name of this MaintenanceModeVmInfo.  # noqa: E501
        :type vm_name: str
        """

        self._vm_name = vm_name

    @property
    def vm_ha(self):
        """Gets the vm_ha of this MaintenanceModeVmInfo.  # noqa: E501


        :return: The vm_ha of this MaintenanceModeVmInfo.  # noqa: E501
        :rtype: bool
        """
        return self._vm_ha

    @vm_ha.setter
    def vm_ha(self, vm_ha):
        """Sets the vm_ha of this MaintenanceModeVmInfo.


        :param vm_ha: The vm_ha of this MaintenanceModeVmInfo.  # noqa: E501
        :type vm_ha: bool
        """

        self._vm_ha = vm_ha

    @property
    def verify(self):
        """Gets the verify of this MaintenanceModeVmInfo.  # noqa: E501


        :return: The verify of this MaintenanceModeVmInfo.  # noqa: E501
        :rtype: MaintenanceModeVerify
        """
        return self._verify

    @verify.setter
    def verify(self, verify):
        """Sets the verify of this MaintenanceModeVmInfo.


        :param verify: The verify of this MaintenanceModeVmInfo.  # noqa: E501
        :type verify: MaintenanceModeVerify
        """

        self._verify = verify

    @property
    def target_host_name(self):
        """Gets the target_host_name of this MaintenanceModeVmInfo.  # noqa: E501


        :return: The target_host_name of this MaintenanceModeVmInfo.  # noqa: E501
        :rtype: str
        """
        return self._target_host_name

    @target_host_name.setter
    def target_host_name(self, target_host_name):
        """Sets the target_host_name of this MaintenanceModeVmInfo.


        :param target_host_name: The target_host_name of this MaintenanceModeVmInfo.  # noqa: E501
        :type target_host_name: str
        """

        self._target_host_name = target_host_name

    @property
    def state(self):
        """Gets the state of this MaintenanceModeVmInfo.  # noqa: E501


        :return: The state of this MaintenanceModeVmInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MaintenanceModeVmInfo.


        :param state: The state of this MaintenanceModeVmInfo.  # noqa: E501
        :type state: str
        """

        self._state = state

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
        if not isinstance(other, MaintenanceModeVmInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaintenanceModeVmInfo):
            return True

        return self.to_dict() != other.to_dict()