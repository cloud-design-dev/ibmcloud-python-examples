import os
import sys
import json 
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))
service = VpcV1(authenticator=authenticator)
service.set_service_url('https://us-east.iaas.cloud.ibm.com/v1')

#  Listing VPCs
print("List VPCs")
try:
    vpcs = service.list_vpcs().get_result()['vpcs']
except ApiException as e:
  print("List VPC failed with status code " + str(e.code) + ": " + e.message)
for vpc in vpcs:
    print(vpc['id'], "\t",  vpc['name'])

#  Listing Subnets
print("List Subnets")
try:
    subnets = service.list_subnets().get_result()['subnets']
except ApiException as e:
  print("List subnets failed with status code " + str(e.code) + ": " + e.message)
for subnet in subnets:
    print(subnet['id'], "\t",  subnet['name'])

# #  Listing Instances
# print("List Instances")
# try:
#     instances = service.list_instances().get_result()['instances']
# except ApiException as e:
#   print("List instances failed with status code " + str(e.code) + ": " + e.message)
# for instance in instances:
#     print(instance['id'], "\t",  instance['name'])

# instanceId = instances[0]['id']
# instanceName = instances[0]['name']

