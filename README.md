# ibmcloud-python-examples
IBM Cloud Python examples for Classic and PaaS resources.

## Classic Infrastructure

All Classic Infrastructure examples are located in the [classic](classic/) directory. The [README](classic/README.md) outlines what tools need to be installed as well as how to set up authentication for interacting with the Python API Client.

## Cloud Resources

The Cloud Resource examples are broken up by their respective API. Currently the this includes:

    ```
     - containers/registry
    │       ├── cloud/containers/registry/get-va-image-reports.py
    │       └── cloud/containers/registry/va-scan-example.py
     - iam
    │   ├── cloud/iam/access-groups.py
    │   └── cloud/iam/servide-ids.py
    ├── cloud/interconnectivity
    │   ├── cloud/interconnectivity/direct-link
    │   │   └── cloud/interconnectivity/direct-link/dl.py
    │   └── cloud/interconnectivity/transit-gateway
    │       ├── cloud/interconnectivity/transit-gateway/list-tgw-connections.py
    │       └── cloud/interconnectivity/transit-gateway/list-tgws.py
    ├── cloud/resource-management
    ├── cloud/schematics
    │   ├── cloud/schematics/README.md
    │   ├── cloud/schematics/get-workspace-output.py
    │   ├── cloud/schematics/get-workspace-resources.py
    │   └── cloud/schematics/list-workspaces.py
    ├── cloud/tagging-and-search
    │   ├── cloud/tagging-and-search/find-by-tag.py
    │   └── cloud/tagging-and-search/get-all-tags.py
    ├── cloud/template-service.py
    └── cloud/vpc
        ├── cloud/vpc/create-vpc.py
        ├── cloud/vpc/get-regional-zones.py
        └── cloud/vpc/list-vpc-resources.py

    ```

See the main [README](cloud/README.md) for configuring the most common Environment variables and information on the various python modules that need to be installed. 
