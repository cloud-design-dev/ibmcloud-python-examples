import os
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_platform_services import GlobalTaggingV1, ResourceManagerV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

vpcService = VpcV1(authenticator=authenticator)
vpcServiceRegion = 'https://' + (os.environ.get('VPC_REGION')) + '.iaas.cloud.ibm.com/v1'
vpcService.set_service_url(vpcServiceRegion)


region = os.environ.get('VPC_REGION')

zones = vpcService.list_region_zones(region).get_result()['zones']

print("Listing Zones in region " + region + ": ")
for zone in zones:
    print(zone['name'])
