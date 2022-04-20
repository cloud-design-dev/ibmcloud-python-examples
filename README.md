# ibmcloud-python-examples
IBM Cloud Python examples for Classic and PaaS resources.

## Classic Infrastructure

All Classic Infrastructure examples are located in the [classic](classic/) directory. The [README](classic/README.md) outlines what tools need to be installed as well as how to set up authentication for interacting with the Python API Client.

## Cloud Resources

The Cloud Resource examples are broken up by their respective API. Currently the this includes:

    ```
    vpc:
     - Create a VPC, Public, Gateway, and Subnet
     - List all VPC related resources in the targetted region 

    tag and search:
     - Get all attached tags across Classic Infrastructure and Cloud Resources
     - Get all resources attached to a specific tag
     - Find all VPC instances attached to a specific tag

    containers:
     - Get a Vulnerability advisor scan for all images in the IBM Container Registry
    ```

See the main [README](cloud/README.md) for configuring the most common Environment variables and information on the various python modules that need to be installed. 