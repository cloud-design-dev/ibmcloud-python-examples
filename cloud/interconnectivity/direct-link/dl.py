import json
import os
from ibm_cloud_networking_services import DirectLinkV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from datetime import datetime, timedelta

## Used in the construction of the DL API client which can be versioned.
## Requests to the DL API require a major version as the first segment of the request path (/v1/) 
## and a date-based version as a query parameter in the format version=YYYY-MM-DD
## For safety I set this to one day behind the current date 
today = datetime.now()
date = today + timedelta(days = -1)
version_date = date.strftime("%Y-%m-%d")


## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

directLinkService = DirectLinkV1(
    version=version_date,
    authenticator=authenticator
)

# Use only when need to change the endpoint. The default endpoint is directlink.cloud.ibm.com/v1
# directLinkService.set_service_url('https://directlink.cloud.ibm.com/v1')

offeringType = directLinkService.list_offering_type_locations(
   offering_type="connect").get_result()

print("Listing Connect Provider Locations:")
for location in offeringType['locations']:
    print(location['display_name'] + "\nLands in a " + location['location_type'] + "\n")

print(json.dumps(offeringType, indent=2))


ports = directLinkService.list_ports(
    location_name = "dal03"
    ).get_result().get("ports")

print(json.dumps(ports, indent=2))

# def show_dc_locations(directLinkService):


