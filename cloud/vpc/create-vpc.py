import os
import json
from pprint import pprint
from ibm_vpc import VpcV1
from ibm_platform_services import GlobalTaggingV1, ResourceManagerV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from haikunator import Haikunator
from datetime import datetime, timedelta
import logging
from logdna import LogDNAHandler 

ingestion_key = os.environ.get('LOGDNA_INGESTION_KEY')

# def setup_logging(default_path='logging.json', default_level=logging.info, env_key=ingestion_key):
#     # read logging.json for log parameters to be ued by script
#     path = default_path
#     value = os.getenv(env_key, None)
#     if value:
#         path = value
#     if os.path.exists(path):
#         with open(path, 'rt') as f:
#             config = json.load(f)
#         logging.config.dictConfig(config)
#     else:
#         logging.basicConfig(level=default_level)
log = logging.getLogger('logdna')
log.setLevel(logging.INFO)

options = {
  'hostname': 'europa.local',
  'env': 'Sydney',
  'level': 'Info',
  'index_meta': True,
  'url': 'https://logs.au-syd.logging.cloud.ibm.com/logs/ingest'
}

logger = LogDNAHandler(ingestion_key, options)

log.addHandler(logger)

today = datetime.now()
date = today + timedelta(days = -1)
version_date = date.strftime("%Y-%m-%d")

resource_group = (os.environ.get('RESOURCE_GROUP_ID'))
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

vpcService = VpcV1(authenticator=authenticator)
vpcServiceRegion = 'https://' + (os.environ.get('VPC_REGION')) + '.iaas.cloud.ibm.com/v1'
vpcService.set_service_url(vpcServiceRegion)

tagService = GlobalTaggingV1(authenticator=authenticator)
tagService.set_service_url('https://tags.global-search-tagging.cloud.ibm.com')

haikunator = Haikunator()
basename = haikunator.haikunate(token_length=0, delimiter='')

resource_group_identity_model = {}
resource_group_identity_model['id'] = resource_group
resource_group_id = resource_group_identity_model

zone_identity_model = {}
zone_identity_model['name'] = (os.environ.get('VPC_REGION')) + "-1"
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
    log.info("\nCreating IBM Cloud VPC in " + os.environ.get('VPC_REGION') + " ----\n")
    newVpc = create_vpc(vpcService)
    log.error("Creation Complete. VPC Info: ----\nName: " + newVpc['name'] + "\nID: " + newVpc['id'] + "\nCRN: " + newVpc['crn'] + " ----\n----\n")
except ApiException as e:
     print("VPC creation failed with status code " + str(e.code) + ": " + e.message)


def create_pubgw(vpcService):
    vpc_identity_model = {'id': newVpc['id']}
    vpc = vpc_identity_model
    zone = {'name': (os.environ.get('VPC_REGION')) + "-1"}
    name = (basename + "-z1-pubgw")

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

# def tag_resources():
#     resource_model = {}
#     resource_model = {'resource_id': newVpc['crn']}

#     tag_results = tagService.attach_tag(
#         resources=[resource_model],
#         tag_names=['owner:ryantiffany', 'pythontesttag'],
#         tag_type='user'
#     ).get_result()
