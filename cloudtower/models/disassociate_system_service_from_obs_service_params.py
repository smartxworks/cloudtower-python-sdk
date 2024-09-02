# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class DisassociateSystemServiceFromObsServiceParams(object):
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
        'system_service_type': 'ObservabilityConnectedSystemServiceType',
        'system_service_id': 'str'
    }

    attribute_map = {
        'system_service_type': 'system_service_type',
        'system_service_id': 'system_service_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DisassociateSystemServiceFromObsServiceParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._system_service_type = None
        self._system_service_id = None
        self.discriminator = None

        if "system_service_type" in kwargs:
            self.system_service_type = kwargs["system_service_type"]
        if "system_service_id" in kwargs:
            self.system_service_id = kwargs["system_service_id"]

    @property
    def system_service_type(self):
        """Gets the system_service_type of this DisassociateSystemServiceFromObsServiceParams.  # noqa: E501


        :return: The system_service_type of this DisassociateSystemServiceFromObsServiceParams.  # noqa: E501
        :rtype: ObservabilityConnectedSystemServiceType
        """
        return self._system_service_type

    @system_service_type.setter
    def system_service_type(self, system_service_type):
        """Sets the system_service_type of this DisassociateSystemServiceFromObsServiceParams.


        :param system_service_type: The system_service_type of this DisassociateSystemServiceFromObsServiceParams.  # noqa: E501
        :type system_service_type: ObservabilityConnectedSystemServiceType
        """

        self._system_service_type = system_service_type

    @property
    def system_service_id(self):
        """Gets the system_service_id of this DisassociateSystemServiceFromObsServiceParams.  # noqa: E501


        :return: The system_service_id of this DisassociateSystemServiceFromObsServiceParams.  # noqa: E501
        :rtype: str
        """
        return self._system_service_id

    @system_service_id.setter
    def system_service_id(self, system_service_id):
        """Sets the system_service_id of this DisassociateSystemServiceFromObsServiceParams.


        :param system_service_id: The system_service_id of this DisassociateSystemServiceFromObsServiceParams.  # noqa: E501
        :type system_service_id: str
        """
        if self.local_vars_configuration.client_side_validation and system_service_id is None:  # noqa: E501
            raise ValueError("Invalid value for `system_service_id`, must not be `None`")  # noqa: E501

        self._system_service_id = system_service_id

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
        if not isinstance(other, DisassociateSystemServiceFromObsServiceParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DisassociateSystemServiceFromObsServiceParams):
            return True

        return self.to_dict() != other.to_dict()