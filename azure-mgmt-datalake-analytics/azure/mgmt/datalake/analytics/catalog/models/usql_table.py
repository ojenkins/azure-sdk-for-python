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

from .catalog_item import CatalogItem


class USqlTable(CatalogItem):
    """A Data Lake Analytics catalog U-SQL table item.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param schema_name: the name of the schema associated with this table and
     database.
    :type schema_name: str
    :param name: the name of the table.
    :type name: str
    :param column_list: the list of columns in this table
    :type column_list:
     list[~azure.mgmt.datalake.analytics.catalog.models.USqlTableColumn]
    :param index_list: the list of indices in this table
    :type index_list:
     list[~azure.mgmt.datalake.analytics.catalog.models.USqlIndex]
    :param partition_key_list: the list of partition keys in the table
    :type partition_key_list: list[str]
    :param external_table: the external table associated with the table.
    :type external_table:
     ~azure.mgmt.datalake.analytics.catalog.models.ExternalTable
    :param distribution_info: the distributions info of the table
    :type distribution_info:
     ~azure.mgmt.datalake.analytics.catalog.models.USqlDistributionInfo
    """

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'schema_name': {'key': 'schemaName', 'type': 'str'},
        'name': {'key': 'tableName', 'type': 'str'},
        'column_list': {'key': 'columnList', 'type': '[USqlTableColumn]'},
        'index_list': {'key': 'indexList', 'type': '[USqlIndex]'},
        'partition_key_list': {'key': 'partitionKeyList', 'type': '[str]'},
        'external_table': {'key': 'externalTable', 'type': 'ExternalTable'},
        'distribution_info': {'key': 'distributionInfo', 'type': 'USqlDistributionInfo'},
    }

    def __init__(self, **kwargs):
        super(USqlTable, self).__init__(**kwargs)
        self.database_name = kwargs.get('database_name', None)
        self.schema_name = kwargs.get('schema_name', None)
        self.name = kwargs.get('name', None)
        self.column_list = kwargs.get('column_list', None)
        self.index_list = kwargs.get('index_list', None)
        self.partition_key_list = kwargs.get('partition_key_list', None)
        self.external_table = kwargs.get('external_table', None)
        self.distribution_info = kwargs.get('distribution_info', None)
