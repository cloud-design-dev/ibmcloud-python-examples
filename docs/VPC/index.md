# Configuring Environment

The examples in this IAM section use the IBM Cloud Platform Services Python SDK which can be installed using the command:

```shell
pip install --upgrade "ibm-vpc"
```

You will also need to export the following environment variables if they are not already set:

```shell
export VPC_REGION='REGION FOR YOUR VPC RESOURCES'
export IBMCLOUD_API_KEY='YOUR IBM CLOUD API KEY'
export RESOURCE_GROUP='NAME OF RESOURCE_GROUP TO USE FOR DEPLOYMENTS"
```

## Endpoints

VPC uses region specific API endpoints:

| Region | Region Name | Endpoint |
|------|-------------|------|:--------:|
| US South | `us-south` | `https://us-south.iaas.cloud.ibm.com/v1` |
| US East  | `us-east` | `https://us-east.iaas.cloud.ibm.com/v1` |
| Toronto  | `ca-tor` | `https://ca-tor.iaas.cloud.ibm.com/v1` |
| United Kingdom | `eu-gb` | `https://eu-gb.iaas.cloud.ibm.com/v1` |
| Germany | `eu-de` | `https://eu-de.iaas.cloud.ibm.com/v1` |
| Tokyo | `jp-tok` | `https://jp-tok.iaas.cloud.ibm.com/v1` |
| Osaka | `jp-osa` | `https://jp-osa.iaas.cloud.ibm.com/v1` |
| Sydney | `au-syd` | `https://au-syd.iaas.cloud.ibm.com/v1` |
| São Paulo | `br-sao` | `https://br-sao.iaas.cloud.ibm.com/v1` |
