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


class DiagnosticsStorageAccountConfig(Model):
    """Diagnostics storage account config.

    :param storage_account_name: Diagnostics storage account name
    :type storage_account_name: str
    :param protected_account_key_name: Protected Diagnostics storage key name
    :type protected_account_key_name: str
    :param blob_endpoint: Diagnostics storage account blob endpoint
    :type blob_endpoint: str
    :param queue_endpoint: Diagnostics storage account queue endpoint
    :type queue_endpoint: str
    :param table_endpoint: Diagnostics storage account table endpoint
    :type table_endpoint: str
    """

    _validation = {
        'storage_account_name': {'required': True},
        'protected_account_key_name': {'required': True},
        'blob_endpoint': {'required': True},
        'queue_endpoint': {'required': True},
        'table_endpoint': {'required': True},
    }

    _attribute_map = {
        'storage_account_name': {'key': 'storageAccountName', 'type': 'str'},
        'protected_account_key_name': {'key': 'protectedAccountKeyName', 'type': 'str'},
        'blob_endpoint': {'key': 'blobEndpoint', 'type': 'str'},
        'queue_endpoint': {'key': 'queueEndpoint', 'type': 'str'},
        'table_endpoint': {'key': 'tableEndpoint', 'type': 'str'},
    }

    def __init__(self, storage_account_name, protected_account_key_name, blob_endpoint, queue_endpoint, table_endpoint):
        self.storage_account_name = storage_account_name
        self.protected_account_key_name = protected_account_key_name
        self.blob_endpoint = blob_endpoint
        self.queue_endpoint = queue_endpoint
        self.table_endpoint = table_endpoint