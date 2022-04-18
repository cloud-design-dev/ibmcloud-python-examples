import os
import json
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_platform_services import GlobalTaggingV1, ResourceManagerV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from haikunator import Haikunator
from datetime import datetime, timedelta

## Used in the construction of the VPC API client which can be versioned.
## Requests to the VPC API require a major version as the first segment of the request path (/v1/) 
## and a date-based version as a query parameter in the format version=YYYY-MM-DD
## For safety I set this to one day behind the current date 
today = datetime.now()
date = today + timedelta(days = -1)
version_date = date.strftime("%Y-%m-%d")


## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

## Pull resource group ID from RESOURCE_GROUP_ID Environment variable
## Todo: Pull all rgs based on name and filter to the one I want, return ID and set
## as var for future calls
resourceService = ResourceManagerV2(authenticator=authenticator)

resource_group = (os.environ.get('RESOURCE_GROUP'))
resource_group_list = resourceService.list_resource_groups(
  account_id=(os.environ.get('IBM_ACCOUNT')),
  include_deleted=False,
).get_result()


rglist = resource_group_list['resources']
rg_id = rglist['name' == resource_group]['id']


## Construct the VPC service and set the regional endpoint 
vpcService = VpcV1(authenticator=authenticator)
vpcServiceRegion = 'https://' + os.environ.get('VPC_REGION') + '.iaas.cloud.ibm.com/v1'
vpcService.set_service_url(vpcServiceRegion)

## Pull zones based on region. Set deployment zone to first in region by default. 
## Todo: based on length of zones returned, create that number of pubgws and subnets
zones = vpcService.list_region_zones(os.environ.get('VPC_REGION')).get_result()['zones']
deployment_zone = zones[0]['name']

## Set up global tagging service for adding tags once all resources have been deployed.
tagService = GlobalTaggingV1(authenticator=authenticator)
tagService.set_service_url('https://tags.global-search-tagging.cloud.ibm.com')

## Use Haikunator to generate a unique heroku like base name for resources.
## Handy while testing 
haikunator = Haikunator()
basename = haikunator.haikunate(token_length=0, delimiter='')

## Set up some parameters that will be used by multiple functions 
resource_group_identity_model = {}
resource_group_identity_model['id'] = rg_id
resource_group_id = resource_group_identity_model

zone_identity_model = {}
zone_identity_model['name'] = deployment_zone
zone = zone_identity_model

def create_vpc(vpcService):

    address_prefix_management = 'auto'
    classic_access = False
    name = (basename + "-vpc")
    
    new_vpc = vpcService.create_vpc(
        classic_access=classic_access,
        address_prefix_management=address_prefix_management,
        name=name,
        resource_group=resource_group_id
    ).get_result()
    
    return new_vpc

try:
    print("\nCreating IBM Cloud VPC in " + os.environ.get('VPC_REGION') + " ----\n")
    newVpc = create_vpc(vpcService)
    print("Creation Complete. VPC Info: ----\nName: " + newVpc['name'] + "\nID: " + newVpc['id'] + "\nCRN: " + newVpc['crn'] + " ----\n----\n")
    print(newVpc['default_network_acl']['id'])
except ApiException as e:
     print("VPC creation failed with status code " + str(e.code) + ": " + e.message)


def create_pubgw(vpcService):
    vpc_identity_model = {'id': newVpc['id']}
    vpc = vpc_identity_model
    zone = zone_identity_model
    name = (basename + "-" + deployment_zone + "-gw")

    new_pubgw = vpcService.create_public_gateway(
        vpc,
        zone,
        name=name,
        floating_ip={},
        resource_group=resource_group_id
    ).get_result()

    return new_pubgw

try:
    print("\nCreating VPC Public gateway in " + os.environ.get('VPC_REGION') + "-1 ----\n")
    newPubGw = create_pubgw(vpcService)
    print("Creation Complete. Pubgw Info: ----\nName: " + newPubGw['name'] + "\nID: " + newPubGw['id'] + "\nCRN: " + newPubGw['crn'])
except ApiException as e:
     print("Public Gareway creation failed with status code " + str(e.code) + ": " + e.message)

def create_subnet(vpcService):
    vpc_identity_model = {'id': newVpc['id']}
    vpc = vpc_identity_model
    zone = zone_identity_model
    name = (basename + "-" + deployment_zone + "-subnet")
    network_acl_identity_model = {}
    network_acl_identity_model['id'] = newVpc['default_network_acl']['id']

    public_gateway_identity_model = {}
    public_gateway_identity_model['id'] = newPubGw['id']

    subnet_prototype_model = {}
    subnet_prototype_model['ip_version'] = 'ipv4'
    subnet_prototype_model['name'] = name
    subnet_prototype_model['network_acl'] = network_acl_identity_model
    subnet_prototype_model['public_gateway'] = public_gateway_identity_model
    subnet_prototype_model['resource_group'] = resource_group_identity_model
    subnet_prototype_model['vpc'] =  vpc
    subnet_prototype_model['total_ipv4_address_count'] = 256
    subnet_prototype_model['zone'] = zone

    subnet_prototype = subnet_prototype_model
    new_subnet = vpcService.create_subnet(subnet_prototype).get_result()

    return new_subnet

try:
    print("\nCreating VPC Subnet in " + deployment_zone +" ----\n")
    #print(subnet_prototype_model)
    newSubnet = create_subnet(vpcService)
    print("Creation Complete. Subnet Info: ----\nName: " + newSubnet['name'] + "\nID: " + newSubnet['id'] + "\nCRN: " + newSubnet['crn'])
except ApiException as e:
     print("Subnet creation failed with status code " + str(e.code) + ": " + e.message)