# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class GetSCVMDiskMetricInput(object):
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
        'range': 'str',
        'disks': 'DiskWhereInput',
        'metrics': 'list[str]'
    }

    attribute_map = {
        'range': 'range',
        'disks': 'disks',
        'metrics': 'metrics'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GetSCVMDiskMetricInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._range = None
        self._disks = None
        self._metrics = None
        self.discriminator = None

        if "range" in kwargs:
            self.range = kwargs["range"]
        if "disks" in kwargs:
            self.disks = kwargs["disks"]
        if "metrics" in kwargs:
            self.metrics = kwargs["metrics"]

    @property
    def range(self):
        """Gets the range of this GetSCVMDiskMetricInput.  # noqa: E501


        :return: The range of this GetSCVMDiskMetricInput.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetSCVMDiskMetricInput.


        :param range: The range of this GetSCVMDiskMetricInput.  # noqa: E501
        :type range: str
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def disks(self):
        """Gets the disks of this GetSCVMDiskMetricInput.  # noqa: E501


        :return: The disks of this GetSCVMDiskMetricInput.  # noqa: E501
        :rtype: DiskWhereInput
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this GetSCVMDiskMetricInput.


        :param disks: The disks of this GetSCVMDiskMetricInput.  # noqa: E501
        :type disks: DiskWhereInput
        """
        if self.local_vars_configuration.client_side_validation and disks is None:  # noqa: E501
            raise ValueError("Invalid value for `disks`, must not be `None`")  # noqa: E501

        self._disks = disks

    @property
    def metrics(self):
        """Gets the metrics of this GetSCVMDiskMetricInput.  # noqa: E501


        :return: The metrics of this GetSCVMDiskMetricInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GetSCVMDiskMetricInput.


        :param metrics: The metrics of this GetSCVMDiskMetricInput.  # noqa: E501
        :type metrics: list[str]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

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
        if not isinstance(other, GetSCVMDiskMetricInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSCVMDiskMetricInput):
            return True

        return self.to_dict() != other.to_dict()
