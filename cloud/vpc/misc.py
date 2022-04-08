
# def pubgw_create(service, vpc_id=vpc_id, zone_name='jp-tok-1', resource_group_id=(os.environ.get('RESOURCE_GROUP'))):
#     print("Creating Public gateway in jp-tok-1")
#     vpc_identity_model = {}
#     vpc_identity_model['id'] = vpc_id
#     zone_identity_model = {}
#     zone_identity_model['name'] = zone_name
#     public_gateway_prototype_floating_ip_model = {}
#     public_gateway_prototype_floating_ip_model['id'] = None

#     resource_group_identity_model = {}
#     resource_group_identity_model['id'] = resource_group_id

#     vpc = vpc_identity_model
#     zone = zone_identity_model
#     floating_ip = public_gateway_prototype_floating_ip_model
#     name = basename + "-pubgw",
#     resource_group = resource_group_identity_model

#     pubgw = service.create_public_gateway(
#         vpc,
#         zone,
#         floating_ip=floating_ip,
#         name=name,
#         resource_group=resource_group,
#     ).get_result()

#     return pubgw

# try:
#     pubgw = pubgw_create(service)
#     print("Created Public gateway: " + pubgw['name'] + " || ID: " + pubgw['id'])
# except ApiException as e:
#     print("Public gateway creation failed with status code " + str(e.code) + ": " + e.message)




# # print("Creating Subnet in zone 1")
# # def subnet_create(service, vpc):
# #     network_acl_identity_model = {}
# #     network_acl_identity_model['id'] = vpc['default_network_acl']

# #     resource_group_identity_model = {}
# #     resource_group_identity_model['id'] = (os.environ.get('RESOUCE_GROUP'))

# #     vpc_identity_model = {}
# #     vpc_identity_model['id'] = vpc['id']

# #     zone_identity_model = {}
# #     zone_identity_model['name'] = 'jp-tok-1'

# #     subnet_prototype_model = {}
# #     subnet_prototype_model['ip_version'] = 'ipv4'
# #     subnet_prototype_model['name'] = basename + "-subnet-z1",
# #     subnet_prototype_model['network_acl'] = network_acl_identity_model
# #     subnet_prototype_model['resource_group'] = resource_group_identity_model
# #     subnet_prototype_model['vpc'] = vpc_identity_model
# #     subnet_prototype_model['total_ipv4_address_count'] = 256
# #     subnet_prototype_model['zone'] = zone_identity_model

# #     subnet_prototype = subnet_prototype_model

# #     subnet = service.create_subnet(subnet_prototype
# #     ).get_result()
    
# #     return subnet

# # try:
# #     subnet_create(service, vpc)
# #     print("Created Subnet: " + subnet['name'] + " || ID: " + subnet['id'] + " in jp-tok-1 zone")
# # except ApiException as e:
# #     print("Create Subnet failed with status code " + str(e.code) + ": " + e.message)
