import os
import json
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_platform_services import ResourceManagerV2, GlobalSearchV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

# Configure the Search provider service 
searchService = GlobalSearchV2(authenticator=authenticator)
searchService.set_service_url('https://api.global-search-tagging.cloud.ibm.com')

def getVpcInstances(searchService):
    tagQuery = '(region:*) AND (family:is AND type:instance) AND (tags:"owner:ryantiffany")'
    search = searchService.search(query=tagQuery,
                        fields=['*'],limit=100)
    scan_result = search.get_result()

    resources = scan_result['items']

    for resource in resources:
        print("VPC Instance: " + resource['name'] + " is located in zone " + resource['region'])

getVpcInstances(searchService)


def getAllInstances(searchService):
    tagQuery = '(region:*) AND (tags:"owner:ryantiffany")'
    search = searchService.search(query=tagQuery,
                        fields=['*'],limit=100)
    scan_result = search.get_result()

    resources = scan_result['items']

    for resource in resources:
        print("Resource Instance: " + resource['name'] + " of type " + resource['service_name'] + " is located in " + resource['region'])
        #print(resource)

getAllInstances(searchService)