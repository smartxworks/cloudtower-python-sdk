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


class MetricSample(object):
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
        'point': 'DataPoint',
        'labels': 'MetricLabel',
        'typename': 'str'
    }

    attribute_map = {
        'point': 'point',
        'labels': 'labels',
        'typename': '__typename'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """MetricSample - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._point = None
        self._labels = None
        self._typename = None
        self.discriminator = None

        self.point = kwargs.get("point", None)
        if "labels" in kwargs:
            self.labels = kwargs["labels"]
        if "typename" in kwargs:
            self.typename = kwargs["typename"]

    @property
    def point(self):
        """Gets the point of this MetricSample.  # noqa: E501


        :return: The point of this MetricSample.  # noqa: E501
        :rtype: DataPoint
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this MetricSample.


        :param point: The point of this MetricSample.  # noqa: E501
        :type point: DataPoint
        """

        self._point = point

    @property
    def labels(self):
        """Gets the labels of this MetricSample.  # noqa: E501


        :return: The labels of this MetricSample.  # noqa: E501
        :rtype: MetricLabel
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this MetricSample.


        :param labels: The labels of this MetricSample.  # noqa: E501
        :type labels: MetricLabel
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def typename(self):
        """Gets the typename of this MetricSample.  # noqa: E501


        :return: The typename of this MetricSample.  # noqa: E501
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        """Sets the typename of this MetricSample.


        :param typename: The typename of this MetricSample.  # noqa: E501
        :type typename: str
        """
        allowed_values = ["MetricSample"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and typename not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `typename` ({0}), must be one of {1}"  # noqa: E501
                .format(typename, allowed_values)
            )

        self._typename = typename

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
        if not isinstance(other, MetricSample):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricSample):
            return True

        return self.to_dict() != other.to_dict()
