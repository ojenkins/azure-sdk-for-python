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


class BGPCommunity(Model):
    """Contains bgp community information offered in Service Community resources.

    :param service_supported_region: The region which the service support.
     e.g. For O365, region is Global.
    :type service_supported_region: str
    :param community_name: The name of the bgp community. e.g. Skype.
    :type community_name: str
    :param community_value: The value of the bgp community. For more
     information:
     https://docs.microsoft.com/en-us/azure/expressroute/expressroute-routing.
    :type community_value: str
    :param community_prefixes: The prefixes that the bgp community contains.
    :type community_prefixes: list[str]
    :param is_authorized_to_use: Customer is authorized to use bgp community
     or not.
    :type is_authorized_to_use: bool
    :param service_group: The service group of the bgp community contains.
    :type service_group: str
    """

    _attribute_map = {
        'service_supported_region': {'key': 'serviceSupportedRegion', 'type': 'str'},
        'community_name': {'key': 'communityName', 'type': 'str'},
        'community_value': {'key': 'communityValue', 'type': 'str'},
        'community_prefixes': {'key': 'communityPrefixes', 'type': '[str]'},
        'is_authorized_to_use': {'key': 'isAuthorizedToUse', 'type': 'bool'},
        'service_group': {'key': 'serviceGroup', 'type': 'str'},
    }

    def __init__(self, *, service_supported_region: str=None, community_name: str=None, community_value: str=None, community_prefixes=None, is_authorized_to_use: bool=None, service_group: str=None, **kwargs) -> None:
        super(BGPCommunity, self).__init__(**kwargs)
        self.service_supported_region = service_supported_region
        self.community_name = community_name
        self.community_value = community_value
        self.community_prefixes = community_prefixes
        self.is_authorized_to_use = is_authorized_to_use
        self.service_group = service_group
