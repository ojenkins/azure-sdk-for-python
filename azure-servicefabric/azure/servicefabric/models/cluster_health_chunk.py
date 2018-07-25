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


class ClusterHealthChunk(Model):
    """Represents the health chunk of the cluster.
    Contains the cluster aggregated health state, and the cluster entities that
    respect the input filter.
    .

    :param health_state: The HealthState representing the aggregated health
     state of the cluster computed by Health Manager.
     The health evaluation of the entity reflects all events reported on the
     entity and its children (if any).
     The aggregation is done by applying the desired cluster health policy and
     the application health policies.
     . Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param node_health_state_chunks: The list of node health state chunks in
     the cluster that respect the filters in the cluster health chunk query
     description.
    :type node_health_state_chunks:
     ~azure.servicefabric.models.NodeHealthStateChunkList
    :param application_health_state_chunks: The list of application health
     state chunks in the cluster that respect the filters in the cluster health
     chunk query description.
    :type application_health_state_chunks:
     ~azure.servicefabric.models.ApplicationHealthStateChunkList
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'node_health_state_chunks': {'key': 'NodeHealthStateChunks', 'type': 'NodeHealthStateChunkList'},
        'application_health_state_chunks': {'key': 'ApplicationHealthStateChunks', 'type': 'ApplicationHealthStateChunkList'},
    }

    def __init__(self, **kwargs):
        super(ClusterHealthChunk, self).__init__(**kwargs)
        self.health_state = kwargs.get('health_state', None)
        self.node_health_state_chunks = kwargs.get('node_health_state_chunks', None)
        self.application_health_state_chunks = kwargs.get('application_health_state_chunks', None)
