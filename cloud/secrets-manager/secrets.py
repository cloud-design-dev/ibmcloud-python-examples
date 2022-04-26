import os
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibm_secrets_manager_sdk.secrets_manager_v1 import *
from ibm_platform_services import ResourceControllerV2

## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

# Contruct the Resource controller API to grab the GUID of our Secrets Manavger instance and pass it on to the set_service_url parameter.
resourceService = ResourceControllerV2(authenticator=authenticator)

resourceName = os.environ.get('SECRET_INSTANCE_NAME')

# ID of secret group for `create_secret` example 
secretGroup = ''

# Retrieve GUID of instance
secretsManagerInstanceLookup = resourceService.list_resource_instances(
    name=resourceName
).get_result().get("resources")

secretsManagerInstance = secretsManagerInstanceLookup[0]['guid']

# Construct Secrets Manager service. The endpoint is specific to your Secrets Manager instance. 
secretsManagerService = SecretsManagerV1(authenticator=authenticator)
secretsManagerServiceUrl = 'https://' + str(secretsManagerInstance) + "." + os.environ.get('SECRET_INSTANCE_REGION') + '.secrets-manager.appdomain.cloud'
secretsManagerService.set_service_url(secretsManagerServiceUrl)

# # Retrieve secrets group to use for test secret
# secretGroupLookup = secretsManagerService.list_secret_groups().get_result().get("resources")

# for group in secretGroupLookup:
#     secretGroup = (secretGroupLookup['resources'][0]['name'] == 'consul-client')
#     secretGroupId = secretGroup['id']
def create_secret(secretsManagerService, secretGroup):

    collection_metadata_model = {
        'collection_type': 'application/vnd.ibm.secrets-manager.config+json',
        'collection_total': 1,
    }

    secret_resource_model = {
        'name': 'cool-new-kv-secret',
        'description': "Extended description about cool new KV secret",
        'secret_group_id': secretGroup,
        'payload': [{
            'key1': 'sampleValue1',
            'key2': 'sampleValue2'
            }]
        }

    create_secret = secretsManagerService.create_secret(
        secret_type='kv',
        metadata=collection_metadata_model,
        resources=[secret_resource_model]
    ).get_result()

    print(json.dumps(create_secret, indent=2))

