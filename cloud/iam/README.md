# IAM Examples

The examples in this directory use the following APIs:
- https://cloud.ibm.com/apidocs/iam-access-groups?code=python
- https://cloud.ibm.com/apidocs/iam-identity-token-api?code=python

## Configuring Environment

To use these examples please ensure you have installed the IBM Cloud Platform python module:

```
pip install --upgrade "ibm-platform-services"
```

You will also need to export the following environment variables if they are not already set:

```shell
export ACCOUNT_ID='YOUR ACCOUNT ID'
export IBMCLOUD_API_KEY='YOUR IBM CLOUD API KEY ' 
```

### Create New Access Group

The following example will create a new Access Group named `python-test-access-group`:

```python
import os
import json
from ibm_platform_services import IamAccessGroupsV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from datetime import datetime, timedelta

## Pull Account ID from Environment variable
account_id = os.environ.get('ACCOUNT_ID')

## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get(''))
accessGroupService = IamAccessGroupsV2(authenticator=authenticator)

def create_access_group(accessGroupService):
    print("Creating new access group:")
    acessGroup = accessGroupService.create_access_group(
        name='python-test-access-group',
        account_id=account_id,
        description='Example Access Group created using the Python SDK'
    ).get_result()

    newAccessGroup = acessGroup
    print(json.dumps(newAccessGroup, indent=2))

try:
  list_access_groups(accessGroupService)
  get_access_group(accessGroupService, access_group_id=access_group_id)
  create_access_group(accessGroupService)
except ApiException as ae:
  print("Method failed")
  print(" - status code: " + str(ae.code))
  print(" - error message: " + ae.message)
  if ("reason" in ae.http_response.json()):
    print(" - reason: " + ae.http_response.json()["reason"])
```

#### Example Output

```shell
Creating new access group:
{
  "id": "AccessGroupId-xxxxxxx-2d2f-4e30-xxxxxxx-bca01772f49a",
  "name": "cool-project-access-group",
  "description": "Example Access Group created using the Python SDK for our cool new project",
  "account_id": "xxxxxxx",
  "created_at": "2022-04-25T21:07:07Z",
  "created_by_id": "IBMid-xxxxxxx",
  "last_modified_at": "2022-04-25T21:07:07Z",
  "last_modified_by_id": "IBMid-xxxxxxx"
}
```

## Examples

- Access groups
 - list_access_groups
 - get_access_group
 - create_access_group