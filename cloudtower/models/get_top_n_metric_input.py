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


class GetTopNMetricInput(object):
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
        'metrics': 'list[str]',
        'clusters': 'ClusterWhereInput',
        'type': 'str',
        'n': 'int',
        'range': 'str'
    }

    attribute_map = {
        'metrics': 'metrics',
        'clusters': 'clusters',
        'type': 'type',
        'n': 'n',
        'range': 'range'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GetTopNMetricInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._metrics = None
        self._clusters = None
        self._type = None
        self._n = None
        self._range = None
        self.discriminator = None

        if "metrics" in kwargs:
            self.metrics = kwargs["metrics"]
        if "clusters" in kwargs:
            self.clusters = kwargs["clusters"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "n" in kwargs:
            self.n = kwargs["n"]
        if "range" in kwargs:
            self.range = kwargs["range"]

    @property
    def metrics(self):
        """Gets the metrics of this GetTopNMetricInput.  # noqa: E501


        :return: The metrics of this GetTopNMetricInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GetTopNMetricInput.


        :param metrics: The metrics of this GetTopNMetricInput.  # noqa: E501
        :type metrics: list[str]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def clusters(self):
        """Gets the clusters of this GetTopNMetricInput.  # noqa: E501


        :return: The clusters of this GetTopNMetricInput.  # noqa: E501
        :rtype: ClusterWhereInput
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this GetTopNMetricInput.


        :param clusters: The clusters of this GetTopNMetricInput.  # noqa: E501
        :type clusters: ClusterWhereInput
        """
        if self.local_vars_configuration.client_side_validation and clusters is None:  # noqa: E501
            raise ValueError("Invalid value for `clusters`, must not be `None`")  # noqa: E501

        self._clusters = clusters

    @property
    def type(self):
        """Gets the type of this GetTopNMetricInput.  # noqa: E501


        :return: The type of this GetTopNMetricInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetTopNMetricInput.


        :param type: The type of this GetTopNMetricInput.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["top", "bottom"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def n(self):
        """Gets the n of this GetTopNMetricInput.  # noqa: E501


        :return: The n of this GetTopNMetricInput.  # noqa: E501
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this GetTopNMetricInput.


        :param n: The n of this GetTopNMetricInput.  # noqa: E501
        :type n: int
        """
        if self.local_vars_configuration.client_side_validation and n is None:  # noqa: E501
            raise ValueError("Invalid value for `n`, must not be `None`")  # noqa: E501

        self._n = n

    @property
    def range(self):
        """Gets the range of this GetTopNMetricInput.  # noqa: E501


        :return: The range of this GetTopNMetricInput.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetTopNMetricInput.


        :param range: The range of this GetTopNMetricInput.  # noqa: E501
        :type range: str
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

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
        if not isinstance(other, GetTopNMetricInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetTopNMetricInput):
            return True

        return self.to_dict() != other.to_dict()
