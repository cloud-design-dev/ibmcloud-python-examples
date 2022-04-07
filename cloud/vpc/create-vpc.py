import os
import sys
import json 
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibm_platform_services import ResourceManagerV2

account = (os.environ.get('IBM_ACCOUNT'))
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))
service = VpcV1(authenticator=authenticator)
service.set_service_url('https://us-east.iaas.cloud.ibm.com/v1')

