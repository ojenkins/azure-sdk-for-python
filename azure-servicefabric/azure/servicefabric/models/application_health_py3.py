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

from .entity_health_py3 import EntityHealth


class ApplicationHealth(EntityHealth):
    """Represents the health of the application. Contains the application
    aggregated health state and the service and deployed application health
    states.

    :param aggregated_health_state: The HealthState representing the
     aggregated health state of the entity computed by Health Manager.
     The health evaluation of the entity reflects all events reported on the
     entity and its children (if any).
     The aggregation is done by applying the desired health policy.
     . Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param health_events: The list of health events reported on the entity.
    :type health_events: list[~azure.servicefabric.models.HealthEvent]
    :param unhealthy_evaluations: The unhealthy evaluations that show why the
     current aggregated health state was returned by Health Manager.
    :type unhealthy_evaluations:
     list[~azure.servicefabric.models.HealthEvaluationWrapper]
    :param health_statistics: Shows the health statistics for all children
     types of the queried entity.
    :type health_statistics: ~azure.servicefabric.models.HealthStatistics
    :param name: The name of the application, including the 'fabric:' URI
     scheme.
    :type name: str
    :param service_health_states: Service health states as found in the health
     store.
    :type service_health_states:
     list[~azure.servicefabric.models.ServiceHealthState]
    :param deployed_application_health_states: Deployed application health
     states as found in the health store.
    :type deployed_application_health_states:
     list[~azure.servicefabric.models.DeployedApplicationHealthState]
    """

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'health_events': {'key': 'HealthEvents', 'type': '[HealthEvent]'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'health_statistics': {'key': 'HealthStatistics', 'type': 'HealthStatistics'},
        'name': {'key': 'Name', 'type': 'str'},
        'service_health_states': {'key': 'ServiceHealthStates', 'type': '[ServiceHealthState]'},
        'deployed_application_health_states': {'key': 'DeployedApplicationHealthStates', 'type': '[DeployedApplicationHealthState]'},
    }

    def __init__(self, *, aggregated_health_state=None, health_events=None, unhealthy_evaluations=None, health_statistics=None, name: str=None, service_health_states=None, deployed_application_health_states=None, **kwargs) -> None:
        super(ApplicationHealth, self).__init__(aggregated_health_state=aggregated_health_state, health_events=health_events, unhealthy_evaluations=unhealthy_evaluations, health_statistics=health_statistics, **kwargs)
        self.name = name
        self.service_health_states = service_health_states
        self.deployed_application_health_states = deployed_application_health_states
