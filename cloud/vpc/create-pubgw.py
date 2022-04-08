import os
import sys
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))
service = VpcV1(authenticator=authenticator)
service.set_service_url('https://us-east.iaas.cloud.ibm.com/v1')

resource_group = ''
vpc = ''
zone = 'us-east-1'
floating_ip = None

response = service.create_public_gateway(
    vpc,
    zone,
    floating_ip =floating_ip,
    resource_group=resource_group,
    name="gatewaytest",
).get_result()

pprint(response)