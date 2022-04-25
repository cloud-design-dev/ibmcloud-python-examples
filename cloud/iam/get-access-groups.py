import os
import json
from pprint import pprint
from ibm_vpc import VpcV1
## Strip out services that are not needed 
from ibm_platform_services import GlobalTaggingV1, ResourceManagerV2, IamAccessGroupsV2, GlobalSearchV2, IamIdentityV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from datetime import datetime, timedelta

## Used in the construction of many of the IBM Cloud API endpoints, which can be versioned.
## Requests to these APIs require a major version as the first segment of the request path (ex. /v1/) 
## and a date-based version as a query parameter in the format version=YYYY-MM-DD
## For safety I set this to one day behind the current date 
today = datetime.now()
date = today + timedelta(days = -1)
version_date = date.strftime("%Y-%m-%d")

account_id = os.environ.get('ACCOUNT_ID')

## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

resourceService = ResourceManagerV2(authenticator=authenticator)

resource_group = (os.environ.get('RESOURCE_GROUP'))

accessGroupService = IamAccessGroupsV2(authenticator=authenticator)
iamIdentityService = IamIdentityV1(authenticator=authenticator)

groupsList = accessGroupService.list_access_groups(
    account_id=account_id,
    limit=100
).get_result().get("groups")


for group in groupsList:
    group_members_list = accessGroupService.list_access_group_members(
        access_group_id=group['id']
    ).get_result().get("members")
    print("Name: " + group['name'] + "\nID: " + group['id'] + "\nDescription: " + group['description'] + "\nMembers: " + str(group_members_list[0]['iam_id']))