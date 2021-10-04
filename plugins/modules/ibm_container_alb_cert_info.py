#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_alb_cert_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_alb_cert

short_description: Retrieve IBM Cloud 'ibm_container_alb_cert' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_container_alb_cert' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.33.1
    - Terraform v0.12.20

options:
    secret_name:
        description:
            - Secret name
        required: True
        type: str
    namespace:
        description:
            - Namespace of the secret
        required: False
        type: str
        default: ibm-cert-store
    cluster_id:
        description:
            - Cluster ID
        required: True
        type: str
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
    ('secret_name', 'str'),
    ('cluster_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'secret_name',
    'namespace',
    'cluster_id',
]


TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    secret_name=dict(
        required=True,
        type='str'),
    namespace=dict(
        required=False,
        type='str'),
    cluster_id=dict(
        required=True,
        type='str'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_alb_cert',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.33.1',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
