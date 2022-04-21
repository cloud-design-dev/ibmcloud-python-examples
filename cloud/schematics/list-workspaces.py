import os
import json
from pprint import pprint
from ibm_schematics.schematics_v1 import SchematicsV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

## Construct IAM Authentication using IBMCLOUD_API_KEY Environment variable
authenticator = IAMAuthenticator(os.environ.get('IBMCLOUD_API_KEY'))

schematicsService = SchematicsV1(authenticator=authenticator)

schematicsService.set_service_url(os.environ.get('IBM_SCHEMATICS_URL'))

def list_workspaces(schematicsService):
    workspace_response_list = schematicsService.list_workspaces().get_result()

    print("Listing Workspaces: \n")
    for workspace in workspace_response_list['workspaces']:
        print("Workspace Name: " + workspace['name'] + "\nWorkspace ID: " + workspace['id'] + "\nCurrent Status: " + workspace['status'] + "\n")

try:
  list_workspaces(schematicsService)
except ApiException as ae:
  print("Method failed")
  print(" - status code: " + str(ae.code))
  print(" - error message: " + ae.message)
  if ("reason" in ae.http_response.json()):
    print(" - reason: " + ae.http_response.json()["reason"])
