import os
import json
import sys
from pprint import pprint
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_platform_services.resource_manager_v2 import *

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

account = (os.environ.get('IBM_ACCOUNT'))
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

resource_manager_service = ResourceManagerV2(authenticator=authenticator)

resource_group_list = resource_manager_service.list_resource_groups( 
  account_id=account,
  include_deleted=False,
).get_result()


#print(json.dumps(resource_group_list, indent=2))
pprint(resource_group_list)