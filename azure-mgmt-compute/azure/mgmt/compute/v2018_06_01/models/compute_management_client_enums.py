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

from enum import Enum


class OperatingSystemTypes(str, Enum):

    windows = "Windows"
    linux = "Linux"


class OperatingSystemStateTypes(str, Enum):

    generalized = "Generalized"
    specialized = "Specialized"


class ScaleTier(str, Enum):

    s30 = "S30"
    s100 = "S100"


class AggregatedReplicationState(str, Enum):

    unknown = "Unknown"
    in_progress = "InProgress"
    completed = "Completed"
    failed = "Failed"


class ReplicationState(str, Enum):

    unknown = "Unknown"
    replicating = "Replicating"
    completed = "Completed"
    failed = "Failed"


class HostCaching(str, Enum):

    none = "None"
    read_only = "ReadOnly"
    read_write = "ReadWrite"


class ReplicationStatusTypes(str, Enum):

    replication_status = "ReplicationStatus"