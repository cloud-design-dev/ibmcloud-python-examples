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

# Retrieve GUID of instance
secretsManagerInstanceLookup = resourceService.list_resource_instances(
    name=resourceName
).get_result().get("resources")

secretsManagerInstance = secretsManagerInstanceLookup[0]['guid']

# Construct Secrets Manager service. The endpoint is specific to your Secrets Manager instance. 
secretsManagerService = SecretsManagerV1(authenticator=authenticator)
secretsManagerServiceUrl = 'https://' + str(secretsManagerInstance) + "." + os.environ.get('SECRET_INSTANCE_REGION') + '.secrets-manager.appdomain.cloud'
secretsManagerService.set_service_url(secretsManagerServiceUrl)

# Name of an existing Secret Group to use with `get_secret_group`
existingGroup = "91b75586-1c38-bff0-7733-c05c692cc5a9"

# Name of a new group to create if using `create_secret_group`
newGroup = "python-sg-rt-test-v1"

def list_secret_groups(secretsManagerService):

    secretGroups = secretsManagerService.list_secret_groups().get_result().get("resources")

    print("Listing Secret Group Names, IDs, and Descriptions:")
    for group in secretGroups:
        print("Name: " + group['name'] + "\nID: " + group['id'] + "\nDescription: " + group['description'] + "\n")

    print("Returning JSON dump of Secret Groups:")
    print(json.dumps(secretGroups, indent=2) + "\n")


def get_secret_group(secretsManagerService, group):

    secretGroup = secretsManagerService.get_secret_group(
        id=group
    ).get_result().get("resources")

    print("Returning JSON dump of Secret Group:")
    print(json.dumps(secretGroup, indent=2) + "\n")


def create_secret_group(secretsManagerService, newGroup):
    collection_metadata_model = {
        'collection_type': 'application/vnd.ibm.secrets-manager.secret.group+json',
        'collection_total': 1,
    }

    secret_group_resource_model = {
        'name': newGroup,
        'description': 'Extended description for this group.',
    }

    createSecretGroup = secretsManagerService.create_secret_group(
        metadata=collection_metadata_model,
        resources=[secret_group_resource_model]
    ).get_result().get("resources")


    print("Created new Secret Group:\n" + json.dumps(createSecretGroup, indent=2))


try:
  #list_secret_groups(secretsManagerService)
  get_secret_group(secretsManagerService, group=existingGroup)
  create_secret_group(secretsManagerService, newGroup=newGroup)
except ApiException as ae:
  print("Method failed")
  print(" - status code: " + str(ae.code))
  print(" - error message: " + ae.message)
  if ("reason" in ae.http_response.json()):
    print(" - reason: " + ae.http_response.json()["reason"])
 
