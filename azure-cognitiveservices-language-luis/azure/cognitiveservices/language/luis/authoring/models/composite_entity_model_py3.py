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


class CompositeEntityModel(Model):
    """A composite entity.

    :param children: Child entities.
    :type children: list[str]
    :param name: Entity name.
    :type name: str
    """

    _attribute_map = {
        'children': {'key': 'children', 'type': '[str]'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, children=None, name: str=None, **kwargs) -> None:
        super(CompositeEntityModel, self).__init__(**kwargs)
        self.children = children
        self.name = name
