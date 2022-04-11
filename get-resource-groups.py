import os
import json 
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from haikunator import Haikunator
from ibm_platform_services import ResourceManagerV2


authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))
resource_group = os.environ.get('RESOURCE_GROUP')
service = ResourceManagerV2(authenticator=authenticator)

resource_group_list = service.list_resource_groups(
  account_id=(os.environ.get('IBM_ACCOUNT')),
  include_deleted=False,
).get_result()

pprint("Listing Account Resource Groups:")
for rg in resource_group_list['resources']:
   print( rg['id'], "\t",  rg['name'])


print(json.dumps(resource_group_list))



data=[]
for rg in resource_group_list['resources']:
    data.append({
        "name": rg.get('name'),
        "id": rg.get('id'),
        "crn": rg.get('crn')
    })

pprint(data)
# print("Getting details of env rg")

# resource_group_get = service.get_resource_group(
#   id=id
# ).get_result()