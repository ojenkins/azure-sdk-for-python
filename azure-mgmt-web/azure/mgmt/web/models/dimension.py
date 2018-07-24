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


class Dimension(Model):
    """Dimension of a resource metric. For e.g. instance specific HTTP requests
    for a web app,
    where instance name is dimension of the metric HTTP request.

    :param name:
    :type name: str
    :param display_name:
    :type display_name: str
    :param internal_name:
    :type internal_name: str
    :param to_be_exported_for_shoebox:
    :type to_be_exported_for_shoebox: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'internal_name': {'key': 'internalName', 'type': 'str'},
        'to_be_exported_for_shoebox': {'key': 'toBeExportedForShoebox', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(Dimension, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.internal_name = kwargs.get('internal_name', None)
        self.to_be_exported_for_shoebox = kwargs.get('to_be_exported_for_shoebox', None)
