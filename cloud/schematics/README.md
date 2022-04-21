# IBM Cloud Schematics

If you did not use the main [requirements.txt](../../requirements.txt), you can install the modules needed to interact with the Schematics API using the following commands:

```sh
pip install --upgrade "ibm-schematics"
pip install --upgrade "ibm-platform-services"
```

## Environment variables

You will need to export the following environment variables in order to use the examples in this repository.

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| IBMCLOUD\_API\_KEY | IBM Cloud API Key to use for IAM Token Authentication | `string` | n/a | yes |
| IBM\_SCHEMATICS\_URL | The API endpoint where your Schematics actions run and where your workspace data is stored. See the [Schematics API Docs](https://cloud.ibm.com/apidocs/schematics/schematics?code=python#api-endpoints) for available endpoints.  | `string` | n/a | yes |

In this example I am targeting the Public Schematics endpoint in the `us-south` region.

```sh
export IBMCLOUD_API_KEY="Your API Key"
export IBM_SCHEMATICS_URL="https://us.schematics.cloud.ibm.com"
```

## Examples

- list-workspaces: List the workspaces in the specified endpoint
- get-workspace-resources: Retrieve the resources deployed in a specified workspace
- get-workspace-output: Retrive the terraform output from a specified workspace

