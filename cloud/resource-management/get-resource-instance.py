import os
import json
from ibm_platform_services import ResourceControllerV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

resourceService = ResourceControllerV2(authenticator=authenticator)

resourceName = "vault-secret-manager-rt"

resource_instances_list = resourceService.list_resource_instances(
    name=resourceName
).get_result().get("resources")

sm_instance = resource_instances_list[0]['guid']
print(sm_instance)