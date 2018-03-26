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

from .proxy_resource import ProxyResource


class DscNode(ProxyResource):
    """Definition of the dsc node type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param last_seen: Gets or sets the last seen time of the node.
    :type last_seen: datetime
    :param registration_time: Gets or sets the registration time of the node.
    :type registration_time: datetime
    :param ip: Gets or sets the ip of the node.
    :type ip: str
    :param account_id: Gets or sets the account id of the node.
    :type account_id: str
    :param node_configuration: Gets or sets the configuration of the node.
    :type node_configuration:
     ~azure.mgmt.automation.models.DscNodeConfigurationAssociationProperty
    :param status: Gets or sets the status of the node.
    :type status: str
    :param node_id: Gets or sets the node id.
    :type node_id: str
    :param etag: Gets or sets the etag of the resource.
    :type etag: str
    :param extension_handler: Gets or sets the list of extensionHandler
     properties for a Node.
    :type extension_handler:
     list[~azure.mgmt.automation.models.DscNodeExtensionHandlerAssociationProperty]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'last_seen': {'key': 'lastSeen', 'type': 'iso-8601'},
        'registration_time': {'key': 'registrationTime', 'type': 'iso-8601'},
        'ip': {'key': 'ip', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'node_configuration': {'key': 'nodeConfiguration', 'type': 'DscNodeConfigurationAssociationProperty'},
        'status': {'key': 'status', 'type': 'str'},
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'extension_handler': {'key': 'extensionHandler', 'type': '[DscNodeExtensionHandlerAssociationProperty]'},
    }

    def __init__(self, last_seen=None, registration_time=None, ip=None, account_id=None, node_configuration=None, status=None, node_id=None, etag=None, extension_handler=None):
        super(DscNode, self).__init__()
        self.last_seen = last_seen
        self.registration_time = registration_time
        self.ip = ip
        self.account_id = account_id
        self.node_configuration = node_configuration
        self.status = status
        self.node_id = node_id
        self.etag = etag
        self.extension_handler = extension_handler