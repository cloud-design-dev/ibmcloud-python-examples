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

## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

resourceService = ResourceManagerV2(authenticator=authenticator)

resource_group = (os.environ.get('RESOURCE_GROUP'))

accessGroupService = IamAccessGroupsV2(authenticator=authenticator)
iamIdentityService = IamIdentityV1(authenticator=authenticator)

## Construct the VPC service and set the regional endpoint 
vpcService = VpcV1(authenticator=authenticator)
vpcServiceRegion = 'https://' + os.environ.get('VPC_REGION') + '.iaas.cloud.ibm.com/v1'
vpcService.set_service_url(vpcServiceRegion)

## Set up global tagging service for adding tags once all resources have been deployed.
tagService = GlobalTaggingV1(authenticator=authenticator)
tagService.set_service_url('https://tags.global-search-tagging.cloud.ibm.com')

# Configure the Search provider service 
searchService = GlobalSearchV2(authenticator=authenticator)
searchService.set_service_url('https://api.global-search-tagging.cloud.ibm.com')