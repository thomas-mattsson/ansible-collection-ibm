#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_app
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/app

short_description: Configure IBM Cloud 'ibm_app' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_app' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.38.2
    - Terraform v0.12.20

options:
    memory:
        description:
            - The amount of memory each instance should have. In megabytes.
        required: False
        type: int
    instances:
        description:
            - The number of instances
        required: False
        type: int
        default: 1
    service_instance_guid:
        description:
            - Define the service instance guids that should be bound to this application.
        required: False
        type: list
        elements: str
    app_version:
        description:
            - Version of the application
        required: False
        type: str
    command:
        description:
            - The initial command for the app
        required: False
        type: str
    health_check_http_endpoint:
        description:
            - Endpoint called to determine if the app is healthy.
        required: False
        type: str
    route_guid:
        description:
            - Define the route guids which should be bound to the application.
        required: False
        type: list
        elements: str
    app_path:
        description:
            - (Required for new resource) Define the  path of the zip file of the application.
        required: True
        type: str
    health_check_type:
        description:
            - Type of health check to perform.
        required: False
        type: str
        default: port
    disk_quota:
        description:
            - The maximum amount of disk available to an instance of an app. In megabytes.
        required: False
        type: int
    buildpack:
        description:
            - Buildpack to build the app. 3 options: a) Blank means autodetection; b) A Git Url pointing to a buildpack; c) Name of an installed buildpack.
        required: False
        type: str
    health_check_timeout:
        description:
            - Timeout in seconds for health checking of an staged app when starting up.
        required: False
        type: int
    name:
        description:
            - (Required for new resource) The name for the app
        required: True
        type: str
    space_guid:
        description:
            - (Required for new resource) Define space guid to which app belongs
        required: True
        type: str
    environment_json:
        description:
            - Key/value pairs of all the environment variables to run in your app. Does not include any system or service variables.
        required: False
        type: dict
    wait_time_minutes:
        description:
            - Define timeout to wait for the app instances to start/update/restage etc.
        required: False
        type: int
        default: 20
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('app_path', 'str'),
    ('name', 'str'),
    ('space_guid', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'memory',
    'instances',
    'service_instance_guid',
    'app_version',
    'command',
    'health_check_http_endpoint',
    'route_guid',
    'app_path',
    'health_check_type',
    'disk_quota',
    'buildpack',
    'health_check_timeout',
    'name',
    'space_guid',
    'environment_json',
    'wait_time_minutes',
    'tags',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('space_guid', 'str'),
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'space_guid',
    'name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    memory=dict(
        required=False,
        type='int'),
    instances=dict(
        required=False,
        type='int'),
    service_instance_guid=dict(
        required=False,
        elements='',
        type='list'),
    app_version=dict(
        required=False,
        type='str'),
    command=dict(
        required=False,
        type='str'),
    health_check_http_endpoint=dict(
        required=False,
        type='str'),
    route_guid=dict(
        required=False,
        elements='',
        type='list'),
    app_path=dict(
        required=False,
        type='str'),
    health_check_type=dict(
        required=False,
        type='str'),
    disk_quota=dict(
        required=False,
        type='int'),
    buildpack=dict(
        required=False,
        type='str'),
    health_check_timeout=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    space_guid=dict(
        required=False,
        type='str'),
    environment_json=dict(
        required=False,
        type='dict'),
    wait_time_minutes=dict(
        required=False,
        type='int'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_app',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.38.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_app',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.38.2',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
