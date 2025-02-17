# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class BackupPlanOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BACKUP_DELAY_OPTION_ASC = "backup_delay_option_ASC"
    BACKUP_DELAY_OPTION_DESC = "backup_delay_option_DESC"
    BACKUP_RESTORE_POINT_COUNT_ASC = "backup_restore_point_count_ASC"
    BACKUP_RESTORE_POINT_COUNT_DESC = "backup_restore_point_count_DESC"
    BACKUP_TOTAL_SIZE_ASC = "backup_total_size_ASC"
    BACKUP_TOTAL_SIZE_DESC = "backup_total_size_DESC"
    COMPRESSION_ASC = "compression_ASC"
    COMPRESSION_DESC = "compression_DESC"
    COMPRESSION_RATIO_ASC = "compression_ratio_ASC"
    COMPRESSION_RATIO_DESC = "compression_ratio_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DELETE_STRATEGY_ASC = "delete_strategy_ASC"
    DELETE_STRATEGY_DESC = "delete_strategy_DESC"
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    ENABLE_WINDOW_ASC = "enable_window_ASC"
    ENABLE_WINDOW_DESC = "enable_window_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    FULL_INTERVAL_ASC = "full_interval_ASC"
    FULL_INTERVAL_DESC = "full_interval_DESC"
    FULL_PERIOD_ASC = "full_period_ASC"
    FULL_PERIOD_DESC = "full_period_DESC"
    FULL_TIME_POINT_ASC = "full_time_point_ASC"
    FULL_TIME_POINT_DESC = "full_time_point_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    INCREMENTAL_INTERVAL_ASC = "incremental_interval_ASC"
    INCREMENTAL_INTERVAL_DESC = "incremental_interval_DESC"
    INCREMENTAL_PERIOD_ASC = "incremental_period_ASC"
    INCREMENTAL_PERIOD_DESC = "incremental_period_DESC"
    INCREMENTAL_TIME_POINTS_ASC = "incremental_time_points_ASC"
    INCREMENTAL_TIME_POINTS_DESC = "incremental_time_points_DESC"
    KEEP_POLICY_ASC = "keep_policy_ASC"
    KEEP_POLICY_DESC = "keep_policy_DESC"
    KEEP_POLICY_VALUE_ASC = "keep_policy_value_ASC"
    KEEP_POLICY_VALUE_DESC = "keep_policy_value_DESC"
    LAST_EXECUTE_STATUS_ASC = "last_execute_status_ASC"
    LAST_EXECUTE_STATUS_DESC = "last_execute_status_DESC"
    LAST_EXECUTE_STATUS_MESSAGE_ASC = "last_execute_status_message_ASC"
    LAST_EXECUTE_STATUS_MESSAGE_DESC = "last_execute_status_message_DESC"
    LAST_EXECUTE_SUCCESS_JOB_COUNT_ASC = "last_execute_success_job_count_ASC"
    LAST_EXECUTE_SUCCESS_JOB_COUNT_DESC = "last_execute_success_job_count_DESC"
    LAST_EXECUTE_TOTAL_JOB_COUNT_ASC = "last_execute_total_job_count_ASC"
    LAST_EXECUTE_TOTAL_JOB_COUNT_DESC = "last_execute_total_job_count_DESC"
    LAST_EXECUTED_AT_ASC = "last_executed_at_ASC"
    LAST_EXECUTED_AT_DESC = "last_executed_at_DESC"
    LAST_MANUAL_EXECUTE_STATUS_ASC = "last_manual_execute_status_ASC"
    LAST_MANUAL_EXECUTE_STATUS_DESC = "last_manual_execute_status_DESC"
    LAST_MANUAL_EXECUTE_STATUS_MESSAGE_ASC = "last_manual_execute_status_message_ASC"
    LAST_MANUAL_EXECUTE_STATUS_MESSAGE_DESC = "last_manual_execute_status_message_DESC"
    LAST_MANUAL_EXECUTE_SUCCESS_JOB_COUNT_ASC = "last_manual_execute_success_job_count_ASC"
    LAST_MANUAL_EXECUTE_SUCCESS_JOB_COUNT_DESC = "last_manual_execute_success_job_count_DESC"
    LAST_MANUAL_EXECUTE_TOTAL_JOB_COUNT_ASC = "last_manual_execute_total_job_count_ASC"
    LAST_MANUAL_EXECUTE_TOTAL_JOB_COUNT_DESC = "last_manual_execute_total_job_count_DESC"
    LAST_MANUAL_EXECUTED_AT_ASC = "last_manual_executed_at_ASC"
    LAST_MANUAL_EXECUTED_AT_DESC = "last_manual_executed_at_DESC"
    LOGICAL_SIZE_ASC = "logical_size_ASC"
    LOGICAL_SIZE_DESC = "logical_size_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    NEXT_EXECUTE_TIME_ASC = "next_execute_time_ASC"
    NEXT_EXECUTE_TIME_DESC = "next_execute_time_DESC"
    PHASE_ASC = "phase_ASC"
    PHASE_DESC = "phase_DESC"
    PHYSICAL_SIZE_ASC = "physical_size_ASC"
    PHYSICAL_SIZE_DESC = "physical_size_DESC"
    SNAPSHOT_CONSISTENT_TYPE_ASC = "snapshot_consistent_type_ASC"
    SNAPSHOT_CONSISTENT_TYPE_DESC = "snapshot_consistent_type_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    VALID_SIZE_OF_BACKUP_OBJECT_ASC = "valid_size_of_backup_object_ASC"
    VALID_SIZE_OF_BACKUP_OBJECT_DESC = "valid_size_of_backup_object_DESC"
    VALID_SIZE_OF_RESTORE_POINT_ASC = "valid_size_of_restore_point_ASC"
    VALID_SIZE_OF_RESTORE_POINT_DESC = "valid_size_of_restore_point_DESC"
    WINDOW_END_ASC = "window_end_ASC"
    WINDOW_END_DESC = "window_end_DESC"
    WINDOW_START_ASC = "window_start_ASC"
    WINDOW_START_DESC = "window_start_DESC"

    allowable_values = [BACKUP_DELAY_OPTION_ASC, BACKUP_DELAY_OPTION_DESC, BACKUP_RESTORE_POINT_COUNT_ASC, BACKUP_RESTORE_POINT_COUNT_DESC, BACKUP_TOTAL_SIZE_ASC, BACKUP_TOTAL_SIZE_DESC, COMPRESSION_ASC, COMPRESSION_DESC, COMPRESSION_RATIO_ASC, COMPRESSION_RATIO_DESC, CREATEDAT_ASC, CREATEDAT_DESC, DELETE_STRATEGY_ASC, DELETE_STRATEGY_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, ENABLE_WINDOW_ASC, ENABLE_WINDOW_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, FULL_INTERVAL_ASC, FULL_INTERVAL_DESC, FULL_PERIOD_ASC, FULL_PERIOD_DESC, FULL_TIME_POINT_ASC, FULL_TIME_POINT_DESC, ID_ASC, ID_DESC, INCREMENTAL_INTERVAL_ASC, INCREMENTAL_INTERVAL_DESC, INCREMENTAL_PERIOD_ASC, INCREMENTAL_PERIOD_DESC, INCREMENTAL_TIME_POINTS_ASC, INCREMENTAL_TIME_POINTS_DESC, KEEP_POLICY_ASC, KEEP_POLICY_DESC, KEEP_POLICY_VALUE_ASC, KEEP_POLICY_VALUE_DESC, LAST_EXECUTE_STATUS_ASC, LAST_EXECUTE_STATUS_DESC, LAST_EXECUTE_STATUS_MESSAGE_ASC, LAST_EXECUTE_STATUS_MESSAGE_DESC, LAST_EXECUTE_SUCCESS_JOB_COUNT_ASC, LAST_EXECUTE_SUCCESS_JOB_COUNT_DESC, LAST_EXECUTE_TOTAL_JOB_COUNT_ASC, LAST_EXECUTE_TOTAL_JOB_COUNT_DESC, LAST_EXECUTED_AT_ASC, LAST_EXECUTED_AT_DESC, LAST_MANUAL_EXECUTE_STATUS_ASC, LAST_MANUAL_EXECUTE_STATUS_DESC, LAST_MANUAL_EXECUTE_STATUS_MESSAGE_ASC, LAST_MANUAL_EXECUTE_STATUS_MESSAGE_DESC, LAST_MANUAL_EXECUTE_SUCCESS_JOB_COUNT_ASC, LAST_MANUAL_EXECUTE_SUCCESS_JOB_COUNT_DESC, LAST_MANUAL_EXECUTE_TOTAL_JOB_COUNT_ASC, LAST_MANUAL_EXECUTE_TOTAL_JOB_COUNT_DESC, LAST_MANUAL_EXECUTED_AT_ASC, LAST_MANUAL_EXECUTED_AT_DESC, LOGICAL_SIZE_ASC, LOGICAL_SIZE_DESC, NAME_ASC, NAME_DESC, NEXT_EXECUTE_TIME_ASC, NEXT_EXECUTE_TIME_DESC, PHASE_ASC, PHASE_DESC, PHYSICAL_SIZE_ASC, PHYSICAL_SIZE_DESC, SNAPSHOT_CONSISTENT_TYPE_ASC, SNAPSHOT_CONSISTENT_TYPE_DESC, STATUS_ASC, STATUS_DESC, VALID_SIZE_OF_BACKUP_OBJECT_ASC, VALID_SIZE_OF_BACKUP_OBJECT_DESC, VALID_SIZE_OF_RESTORE_POINT_ASC, VALID_SIZE_OF_RESTORE_POINT_DESC, WINDOW_END_ASC, WINDOW_END_DESC, WINDOW_START_ASC, WINDOW_START_DESC]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BackupPlanOrderByInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())
        self.discriminator = None

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
        if not isinstance(other, BackupPlanOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupPlanOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
