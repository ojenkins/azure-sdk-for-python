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


class OCR(Model):
    """Contains the text found in image for the language specified.

    :param status: The evaluate status
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.Status
    :param metadata: Array of KeyValue.
    :type metadata:
     list[~azure.cognitiveservices.vision.contentmoderator.models.KeyValuePair]
    :param tracking_id: The tracking id.
    :type tracking_id: str
    :param cache_id: The cache id.
    :type cache_id: str
    :param language: The ISO 639-3 code.
    :type language: str
    :param text: The found text.
    :type text: str
    :param candidates: The list of candidate text.
    :type candidates:
     list[~azure.cognitiveservices.vision.contentmoderator.models.Candidate]
    """

    _attribute_map = {
        'status': {'key': 'Status', 'type': 'Status'},
        'metadata': {'key': 'Metadata', 'type': '[KeyValuePair]'},
        'tracking_id': {'key': 'TrackingId', 'type': 'str'},
        'cache_id': {'key': 'CacheId', 'type': 'str'},
        'language': {'key': 'Language', 'type': 'str'},
        'text': {'key': 'Text', 'type': 'str'},
        'candidates': {'key': 'Candidates', 'type': '[Candidate]'},
    }

    def __init__(self, status=None, metadata=None, tracking_id=None, cache_id=None, language=None, text=None, candidates=None):
        super(OCR, self).__init__()
        self.status = status
        self.metadata = metadata
        self.tracking_id = tracking_id
        self.cache_id = cache_id
        self.language = language
        self.text = text
        self.candidates = candidates
