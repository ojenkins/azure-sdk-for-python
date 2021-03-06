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


class OnErrorDeploymentExtended(Model):
    """Deployment on error behavior with additional details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: The state of the provisioning for the on error
     deployment.
    :vartype provisioning_state: str
    :param type: The deployment on error behavior type. Possible values are
     LastSuccessful and SpecificDeployment. Possible values include:
     'LastSuccessful', 'SpecificDeployment'
    :type type: str or
     ~azure.mgmt.resource.resources.v2018_05_01.models.OnErrorDeploymentType
    :param deployment_name: The deployment to be used on error case.
    :type deployment_name: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'type': {'key': 'type', 'type': 'OnErrorDeploymentType'},
        'deployment_name': {'key': 'deploymentName', 'type': 'str'},
    }

    def __init__(self, *, type=None, deployment_name: str=None, **kwargs) -> None:
        super(OnErrorDeploymentExtended, self).__init__(**kwargs)
        self.provisioning_state = None
        self.type = type
        self.deployment_name = deployment_name
