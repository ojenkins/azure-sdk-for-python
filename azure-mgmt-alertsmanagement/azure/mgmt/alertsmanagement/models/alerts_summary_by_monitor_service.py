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

from msrest.serialization import Model


class AlertsSummaryByMonitorService(Model):
    """Summary of the alerts by monitor service.

    :param platform: Count of alerts of "Platform"
    :type platform: int
    :param application_insights: Count of alerts of "Application Insights"
    :type application_insights: int
    :param log_analytics: Count of alerts of "Log Analytics"
    :type log_analytics: int
    :param zabbix: Count of alerts of "Zabbix"
    :type zabbix: int
    :param scom: Count of alerts of "SCOM"
    :type scom: int
    :param nagios: Count of alerts of "Nagios"
    :type nagios: int
    :param infrastructure_insights: Count of alerts of "Infrastructure
     Insights"
    :type infrastructure_insights: int
    :param activity_log_administrative: Count of alerts of "ActivityLog
     Administrative"
    :type activity_log_administrative: int
    :param activity_log_security: Count of alerts of "ActivityLog Security"
    :type activity_log_security: int
    :param activity_log_recommendation: Count of alerts of "ActivityLog
     Recommendation"
    :type activity_log_recommendation: int
    :param activity_log_policy: Count of alerts of "ActivityLog Policy"
    :type activity_log_policy: int
    :param activity_log_autoscale: Count of alerts of "ActivityLog Autoscale"
    :type activity_log_autoscale: int
    :param service_health: Count of alerts of "ServiceHealth"
    :type service_health: int
    :param smart_detector: Count of alerts of "Smart Detector"
    :type smart_detector: int
    """

    _attribute_map = {
        'platform': {'key': 'platform', 'type': 'int'},
        'application_insights': {'key': 'application Insights', 'type': 'int'},
        'log_analytics': {'key': 'log Analytics', 'type': 'int'},
        'zabbix': {'key': 'zabbix', 'type': 'int'},
        'scom': {'key': 'scom', 'type': 'int'},
        'nagios': {'key': 'nagios', 'type': 'int'},
        'infrastructure_insights': {'key': 'infrastructure Insights', 'type': 'int'},
        'activity_log_administrative': {'key': 'activityLog Administrative', 'type': 'int'},
        'activity_log_security': {'key': 'activityLog Security', 'type': 'int'},
        'activity_log_recommendation': {'key': 'activityLog Recommendation', 'type': 'int'},
        'activity_log_policy': {'key': 'activityLog Policy', 'type': 'int'},
        'activity_log_autoscale': {'key': 'activityLog Autoscale', 'type': 'int'},
        'service_health': {'key': 'serviceHealth', 'type': 'int'},
        'smart_detector': {'key': 'smartDetector', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AlertsSummaryByMonitorService, self).__init__(**kwargs)
        self.platform = kwargs.get('platform', None)
        self.application_insights = kwargs.get('application_insights', None)
        self.log_analytics = kwargs.get('log_analytics', None)
        self.zabbix = kwargs.get('zabbix', None)
        self.scom = kwargs.get('scom', None)
        self.nagios = kwargs.get('nagios', None)
        self.infrastructure_insights = kwargs.get('infrastructure_insights', None)
        self.activity_log_administrative = kwargs.get('activity_log_administrative', None)
        self.activity_log_security = kwargs.get('activity_log_security', None)
        self.activity_log_recommendation = kwargs.get('activity_log_recommendation', None)
        self.activity_log_policy = kwargs.get('activity_log_policy', None)
        self.activity_log_autoscale = kwargs.get('activity_log_autoscale', None)
        self.service_health = kwargs.get('service_health', None)
        self.smart_detector = kwargs.get('smart_detector', None)
