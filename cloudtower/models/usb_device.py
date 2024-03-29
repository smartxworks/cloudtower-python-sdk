# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class UsbDevice(object):
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
        'binded': 'bool',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'host': 'NestedHost',
        'id': 'str',
        'local_created_at': 'str',
        'local_id': 'str',
        'manufacturer': 'str',
        'name': 'str',
        'size': 'int',
        'status': 'UsbDeviceStatus',
        'usb_type': 'str',
        'vms': 'list[NestedVm]',
        'vm': 'NestedVm'
    }

    attribute_map = {
        'binded': 'binded',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'host': 'host',
        'id': 'id',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'manufacturer': 'manufacturer',
        'name': 'name',
        'size': 'size',
        'status': 'status',
        'usb_type': 'usb_type',
        'vms': 'vms',
        'vm': 'vm'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """UsbDevice - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._binded = None
        self._description = None
        self._entity_async_status = None
        self._host = None
        self._id = None
        self._local_created_at = None
        self._local_id = None
        self._manufacturer = None
        self._name = None
        self._size = None
        self._status = None
        self._usb_type = None
        self._vms = None
        self._vm = None
        self.discriminator = None

        if "binded" in kwargs:
            self.binded = kwargs["binded"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "host" in kwargs:
            self.host = kwargs["host"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_created_at" in kwargs:
            self.local_created_at = kwargs["local_created_at"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "manufacturer" in kwargs:
            self.manufacturer = kwargs["manufacturer"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "status" in kwargs:
            self.status = kwargs["status"]
        if "usb_type" in kwargs:
            self.usb_type = kwargs["usb_type"]
        self.vms = kwargs.get("vms", None)
        self.vm = kwargs.get("vm", None)

    @property
    def binded(self):
        """Gets the binded of this UsbDevice.  # noqa: E501


        :return: The binded of this UsbDevice.  # noqa: E501
        :rtype: bool
        """
        return self._binded

    @binded.setter
    def binded(self, binded):
        """Sets the binded of this UsbDevice.


        :param binded: The binded of this UsbDevice.  # noqa: E501
        :type binded: bool
        """
        if self.local_vars_configuration.client_side_validation and binded is None:  # noqa: E501
            raise ValueError("Invalid value for `binded`, must not be `None`")  # noqa: E501

        self._binded = binded

    @property
    def description(self):
        """Gets the description of this UsbDevice.  # noqa: E501


        :return: The description of this UsbDevice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UsbDevice.


        :param description: The description of this UsbDevice.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this UsbDevice.  # noqa: E501


        :return: The entity_async_status of this UsbDevice.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this UsbDevice.


        :param entity_async_status: The entity_async_status of this UsbDevice.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def host(self):
        """Gets the host of this UsbDevice.  # noqa: E501


        :return: The host of this UsbDevice.  # noqa: E501
        :rtype: NestedHost
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this UsbDevice.


        :param host: The host of this UsbDevice.  # noqa: E501
        :type host: NestedHost
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def id(self):
        """Gets the id of this UsbDevice.  # noqa: E501


        :return: The id of this UsbDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UsbDevice.


        :param id: The id of this UsbDevice.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_created_at(self):
        """Gets the local_created_at of this UsbDevice.  # noqa: E501


        :return: The local_created_at of this UsbDevice.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this UsbDevice.


        :param local_created_at: The local_created_at of this UsbDevice.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this UsbDevice.  # noqa: E501


        :return: The local_id of this UsbDevice.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this UsbDevice.


        :param local_id: The local_id of this UsbDevice.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def manufacturer(self):
        """Gets the manufacturer of this UsbDevice.  # noqa: E501


        :return: The manufacturer of this UsbDevice.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this UsbDevice.


        :param manufacturer: The manufacturer of this UsbDevice.  # noqa: E501
        :type manufacturer: str
        """
        if self.local_vars_configuration.client_side_validation and manufacturer is None:  # noqa: E501
            raise ValueError("Invalid value for `manufacturer`, must not be `None`")  # noqa: E501

        self._manufacturer = manufacturer

    @property
    def name(self):
        """Gets the name of this UsbDevice.  # noqa: E501


        :return: The name of this UsbDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UsbDevice.


        :param name: The name of this UsbDevice.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this UsbDevice.  # noqa: E501


        :return: The size of this UsbDevice.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UsbDevice.


        :param size: The size of this UsbDevice.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def status(self):
        """Gets the status of this UsbDevice.  # noqa: E501


        :return: The status of this UsbDevice.  # noqa: E501
        :rtype: UsbDeviceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UsbDevice.


        :param status: The status of this UsbDevice.  # noqa: E501
        :type status: UsbDeviceStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def usb_type(self):
        """Gets the usb_type of this UsbDevice.  # noqa: E501


        :return: The usb_type of this UsbDevice.  # noqa: E501
        :rtype: str
        """
        return self._usb_type

    @usb_type.setter
    def usb_type(self, usb_type):
        """Sets the usb_type of this UsbDevice.


        :param usb_type: The usb_type of this UsbDevice.  # noqa: E501
        :type usb_type: str
        """
        if self.local_vars_configuration.client_side_validation and usb_type is None:  # noqa: E501
            raise ValueError("Invalid value for `usb_type`, must not be `None`")  # noqa: E501

        self._usb_type = usb_type

    @property
    def vms(self):
        """Gets the vms of this UsbDevice.  # noqa: E501


        :return: The vms of this UsbDevice.  # noqa: E501
        :rtype: list[NestedVm]
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this UsbDevice.


        :param vms: The vms of this UsbDevice.  # noqa: E501
        :type vms: list[NestedVm]
        """

        self._vms = vms

    @property
    def vm(self):
        """Gets the vm of this UsbDevice.  # noqa: E501


        :return: The vm of this UsbDevice.  # noqa: E501
        :rtype: NestedVm
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this UsbDevice.


        :param vm: The vm of this UsbDevice.  # noqa: E501
        :type vm: NestedVm
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
        if not isinstance(other, UsbDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsbDevice):
            return True

        return self.to_dict() != other.to_dict()
