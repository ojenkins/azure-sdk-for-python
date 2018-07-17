# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .alerts_summary_by_monitor_condition import AlertsSummaryByMonitorCondition


class AlertsSummaryBySeverityAndMonitorConditionSev0(AlertsSummaryByMonitorCondition):
    """Summary of alerts by monitor condition with severity 'Sev0'.

    :param fired: Count of alerts with monitorCondition 'Fired'
    :type fired: int
    :param resolved: Count of alerts with monitorCondition 'Resolved'
    :type resolved: int
    """

    _attribute_map = {
        'fired': {'key': 'fired', 'type': 'int'},
        'resolved': {'key': 'resolved', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AlertsSummaryBySeverityAndMonitorConditionSev0, self).__init__(**kwargs)
