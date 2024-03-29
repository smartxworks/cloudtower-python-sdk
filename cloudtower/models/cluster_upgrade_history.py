# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ClusterUpgradeHistory(object):
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
        'cluster': 'NestedCluster',
        'date': 'str',
        'id': 'str',
        'local_id': 'str',
        'progress': 'object',
        'result': 'str',
        'task_uuid': 'str',
        'version': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'date': 'date',
        'id': 'id',
        'local_id': 'local_id',
        'progress': 'progress',
        'result': 'result',
        'task_uuid': 'task_uuid',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ClusterUpgradeHistory - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._date = None
        self._id = None
        self._local_id = None
        self._progress = None
        self._result = None
        self._task_uuid = None
        self._version = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "date" in kwargs:
            self.date = kwargs["date"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "progress" in kwargs:
            self.progress = kwargs["progress"]
        if "result" in kwargs:
            self.result = kwargs["result"]
        if "task_uuid" in kwargs:
            self.task_uuid = kwargs["task_uuid"]
        if "version" in kwargs:
            self.version = kwargs["version"]

    @property
    def cluster(self):
        """Gets the cluster of this ClusterUpgradeHistory.  # noqa: E501


        :return: The cluster of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ClusterUpgradeHistory.


        :param cluster: The cluster of this ClusterUpgradeHistory.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def date(self):
        """Gets the date of this ClusterUpgradeHistory.  # noqa: E501


        :return: The date of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ClusterUpgradeHistory.


        :param date: The date of this ClusterUpgradeHistory.  # noqa: E501
        :type date: str
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def id(self):
        """Gets the id of this ClusterUpgradeHistory.  # noqa: E501


        :return: The id of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterUpgradeHistory.


        :param id: The id of this ClusterUpgradeHistory.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this ClusterUpgradeHistory.  # noqa: E501


        :return: The local_id of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this ClusterUpgradeHistory.


        :param local_id: The local_id of this ClusterUpgradeHistory.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def progress(self):
        """Gets the progress of this ClusterUpgradeHistory.  # noqa: E501


        :return: The progress of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: object
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ClusterUpgradeHistory.


        :param progress: The progress of this ClusterUpgradeHistory.  # noqa: E501
        :type progress: object
        """
        if self.local_vars_configuration.client_side_validation and progress is None:  # noqa: E501
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def result(self):
        """Gets the result of this ClusterUpgradeHistory.  # noqa: E501


        :return: The result of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ClusterUpgradeHistory.


        :param result: The result of this ClusterUpgradeHistory.  # noqa: E501
        :type result: str
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def task_uuid(self):
        """Gets the task_uuid of this ClusterUpgradeHistory.  # noqa: E501


        :return: The task_uuid of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._task_uuid

    @task_uuid.setter
    def task_uuid(self, task_uuid):
        """Sets the task_uuid of this ClusterUpgradeHistory.


        :param task_uuid: The task_uuid of this ClusterUpgradeHistory.  # noqa: E501
        :type task_uuid: str
        """
        if self.local_vars_configuration.client_side_validation and task_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `task_uuid`, must not be `None`")  # noqa: E501

        self._task_uuid = task_uuid

    @property
    def version(self):
        """Gets the version of this ClusterUpgradeHistory.  # noqa: E501


        :return: The version of this ClusterUpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterUpgradeHistory.


        :param version: The version of this ClusterUpgradeHistory.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, ClusterUpgradeHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterUpgradeHistory):
            return True

        return self.to_dict() != other.to_dict()
