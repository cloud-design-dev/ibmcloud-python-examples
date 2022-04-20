# Classic Infrastructure Python Examples

The following directories provide Python SDK examples for interacting with the [Classic Infrastructure API][classi-api] on IBM Cloud.

## Authentication

The python client can use its built in [create_client_from_env][auth-env] option to pull the credentials from our environment and use them in our calls. This can be done using:

- Local exported [environment variables](#environment-variables)
- The SoftLayer [`slcli`](#softlayer-command-line-client) command line client

### Gathering Classic Infrastructure Credentials

If you are unsure of your Classic Infrastructure username, go to the [IAM Users][iam-users] page in the portal, click on your username and look under the section that says **VPN password**.

To get your Classic Infrastructure API key use the following steps:

1. Go to [API Keys][api-keys]
2. From the drop down select 'Classic Infrastructure API Keys' and copy the key

![Retrieve Classic API Keys](https://dsc.cloud/quickshare/retrieve-classic-key.png)

If you do not have a Classic Infrastructure API Key you will need to generate one from the [API Keys][api-keys] page in the portal:

1. Go to [API Keys][api-keys]
2. From the drop down select 'Classic Infrastructure API Keys' and click `Create a Classic Infrastructure API key`

![Create Classic API Key](https://dsc.cloud/quickshare/create-classic-key.png)

## Environment variables

Export the following environment variables with your Classic Infrastructure credentials. 
With the credentials gathered, we can now export these variables for use with our Python examples:

```shell
export SL_USERNAME="YOUR_USERNAME"
export SL_API_KEY="YOUR_API_KEY"
```

## SoftLayer Command Line Client

Another option is to configure the `slcli` command line utility, which the python client can also use for authentication. To configure the `slcli` client run the command `slcli config setup` and when prompted provide your username and API key. To test that the `slcli` is configured properly you can run the command `slcli vs list`.

[classic-api]: https://github.com/softlayer/softlayer-python
[auth-env]: https://softlayer-python.readthedocs.io/en/latest/api/client/#getting-started
[iam-users]: https://cloud.ibm.com/iam/users
[api-keys]: https://cloud.ibm.com/iam/apikeys
