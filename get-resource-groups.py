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
  account_id=(os.environ.get('IBMCLOUD_ACCOUNT_ID')),
  include_deleted=True,
).get_result()['id']

print(resource_group_list)