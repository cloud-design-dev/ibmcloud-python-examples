import os
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from haikunator import Haikunator

authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))
service = VpcV1(version='2022-03-29', authenticator=authenticator)
service.set_service_url('https://jp-tok.iaas.cloud.ibm.com/v1')
haikunator = Haikunator()

basename = haikunator.haikunate(token_length=0, delimiter='')
resource_group = os.environ.get('RESOURCE_GROUP')
vpc_name = basename + "-vpc"

print("Creating VPC")
new_vpc = service.create_vpc(
    address_prefix_management = 'auto',
    name = vpc_name,
    resource_group =resource_group
    ).get_result()

pprint(new_vpc)

# def vpc_create(service):
#     print("Creating VPC")
    
#     name = basename + "-vpc"

#     vpc = service.create_vpc(
#     address_prefix_management='auto',
#     classic_access=False,
#     name=name,
#     resource_group=resource_group
#     ).get_result()

#     return vpc

# try:
#     vpc = vpc_create(service)
#     print("Created VPC: " + vpc['name'] + " || ID: " + vpc['id'])
# except ApiException as e:
#     print("VPC creation failed with status code " + str(e.code) + ": " + e.message)

