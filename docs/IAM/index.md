# Configuring Environment

The examples in this IAM section use the IBM Cloud Platform Services Python SDK which can be installed using the command:

```shell
pip install --upgrade "ibm-platform-services"
```

## APIs used in these examples

- [IAM Access Groups][access-groups]
- [Service IDs][service-ids]

## Endpoints

The IAM APIs uses the following public global endpoint URL:

```shell
https://iam.cloud.ibm.com
```

If you enabled service endpoints in your account, you can send API requests over the IBM Cloud private network at the following base endpoint URLs.

Private endpoint URL for VPC infrastructure:

```shell
https://private.iam.cloud.ibm.com
```

Private endpoint URLs for classic infrastructure:

```shell
Dallas: https://private.us-south.iam.cloud.ibm.com
Washington DC: https://private.us-east.iam.cloud.ibm.com
```

[access-groups]: https://cloud.ibm.com/apidocs/iam-access-groups?code=python
[service-ids]: https://example.com