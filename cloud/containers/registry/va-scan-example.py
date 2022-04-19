import os
import json
from pprint import pprint
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_container_registry.vulnerability_advisor_v3 import *
## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable

authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))
imageName =  "us.icr.io/aamir-namespace/hello-world:2"
account = os.environ.get('ACCOUNT_ID')
accept_language = 'en_US'
vulnerability_advisor_service = VulnerabilityAdvisorV3(
    authenticator=authenticator,
    account=account
    )

scanreport = vulnerability_advisor_service.account_status_query_path().get_result()

image_report = scanreport['images']
for image in image_report:
    print("Image: " + image['name'] + " is marked as " + image['status'])

scan_report = vulnerability_advisor_service.image_report_query_path(
  name=imageName
).get_result()

print(json.dumps(scan_report, indent=2))