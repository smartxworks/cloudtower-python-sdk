# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class BackupRestoreExecutionNetworkMapping(object):
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
        'target': 'BackupRestoreExecutionNetworkInformation',
        'src_vlan_id': 'str',
        'source': 'BackupRestoreExecutionNetworkInformation',
        'dst_vlan_id': 'str',
        'typename': 'str'
    }

    attribute_map = {
        'target': 'target',
        'src_vlan_id': 'src_vlan_id',
        'source': 'source',
        'dst_vlan_id': 'dst_vlan_id',
        'typename': '__typename'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BackupRestoreExecutionNetworkMapping - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._target = None
        self._src_vlan_id = None
        self._source = None
        self._dst_vlan_id = None
        self._typename = None
        self.discriminator = None

        self.target = kwargs.get("target", None)
        if "src_vlan_id" in kwargs:
            self.src_vlan_id = kwargs["src_vlan_id"]
        self.source = kwargs.get("source", None)
        if "dst_vlan_id" in kwargs:
            self.dst_vlan_id = kwargs["dst_vlan_id"]
        if "typename" in kwargs:
            self.typename = kwargs["typename"]

    @property
    def target(self):
        """Gets the target of this BackupRestoreExecutionNetworkMapping.  # noqa: E501


        :return: The target of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :rtype: BackupRestoreExecutionNetworkInformation
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this BackupRestoreExecutionNetworkMapping.


        :param target: The target of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :type target: BackupRestoreExecutionNetworkInformation
        """

        self._target = target

    @property
    def src_vlan_id(self):
        """Gets the src_vlan_id of this BackupRestoreExecutionNetworkMapping.  # noqa: E501


        :return: The src_vlan_id of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :rtype: str
        """
        return self._src_vlan_id

    @src_vlan_id.setter
    def src_vlan_id(self, src_vlan_id):
        """Sets the src_vlan_id of this BackupRestoreExecutionNetworkMapping.


        :param src_vlan_id: The src_vlan_id of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :type src_vlan_id: str
        """
        if self.local_vars_configuration.client_side_validation and src_vlan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `src_vlan_id`, must not be `None`")  # noqa: E501

        self._src_vlan_id = src_vlan_id

    @property
    def source(self):
        """Gets the source of this BackupRestoreExecutionNetworkMapping.  # noqa: E501


        :return: The source of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :rtype: BackupRestoreExecutionNetworkInformation
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BackupRestoreExecutionNetworkMapping.


        :param source: The source of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :type source: BackupRestoreExecutionNetworkInformation
        """

        self._source = source

    @property
    def dst_vlan_id(self):
        """Gets the dst_vlan_id of this BackupRestoreExecutionNetworkMapping.  # noqa: E501


        :return: The dst_vlan_id of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :rtype: str
        """
        return self._dst_vlan_id

    @dst_vlan_id.setter
    def dst_vlan_id(self, dst_vlan_id):
        """Sets the dst_vlan_id of this BackupRestoreExecutionNetworkMapping.


        :param dst_vlan_id: The dst_vlan_id of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :type dst_vlan_id: str
        """
        if self.local_vars_configuration.client_side_validation and dst_vlan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dst_vlan_id`, must not be `None`")  # noqa: E501

        self._dst_vlan_id = dst_vlan_id

    @property
    def typename(self):
        """Gets the typename of this BackupRestoreExecutionNetworkMapping.  # noqa: E501


        :return: The typename of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        """Sets the typename of this BackupRestoreExecutionNetworkMapping.


        :param typename: The typename of this BackupRestoreExecutionNetworkMapping.  # noqa: E501
        :type typename: str
        """
        allowed_values = ["BackupRestoreExecutionNetworkMapping"]  # noqa: E501
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
        if not isinstance(other, BackupRestoreExecutionNetworkMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupRestoreExecutionNetworkMapping):
            return True

        return self.to_dict() != other.to_dict()
