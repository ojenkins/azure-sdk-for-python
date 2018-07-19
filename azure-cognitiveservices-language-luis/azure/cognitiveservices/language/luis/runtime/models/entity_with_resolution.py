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

from .entity_model import EntityModel


class EntityWithResolution(EntityModel):
    """EntityWithResolution.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param entity: Required. Name of the entity, as defined in LUIS.
    :type entity: str
    :param type: Required. Type of the entity, as defined in LUIS.
    :type type: str
    :param start_index: Required. The position of the first character of the
     matched entity within the utterance.
    :type start_index: float
    :param end_index: Required. The position of the last character of the
     matched entity within the utterance.
    :type end_index: float
    :param resolution: Required. Resolution values for pre-built LUIS
     entities.
    :type resolution: object
    """

    _validation = {
        'entity': {'required': True},
        'type': {'required': True},
        'start_index': {'required': True},
        'end_index': {'required': True},
        'resolution': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'entity': {'key': 'entity', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'start_index': {'key': 'startIndex', 'type': 'float'},
        'end_index': {'key': 'endIndex', 'type': 'float'},
        'resolution': {'key': 'resolution', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(EntityWithResolution, self).__init__(**kwargs)
        self.resolution = kwargs.get('resolution', None)
