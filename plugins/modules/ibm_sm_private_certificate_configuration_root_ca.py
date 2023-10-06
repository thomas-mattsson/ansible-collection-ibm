#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_sm_private_certificate_configuration_root_ca
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_private_certificate_configuration_root_ca

short_description: Configure IBM Cloud 'ibm_sm_private_certificate_configuration_root_ca' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_sm_private_certificate_configuration_root_ca' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.51.0
    - Terraform v0.12.20

options:
    ip_sans:
        description:
            - The IP Subject Alternative Names to define for the CA certificate, in a comma-delimited list.
        required: False
        type: str
    other_sans:
        description:
            - The custom Object Identifier (OID) or UTF8-string Subject Alternative Names to define for the CA certificate.The alternative names must match the values that are specified in the `allowed_other_sans` field in the associated certificate template. The format is the same as OpenSSL: `<oid>:<type>:<value>` where the current valid type is `UTF8`.
        required: False
        type: list
        elements: str
    private_key_format:
        description:
            - The format of the generated private key.
        required: False
        type: str
        default: der
    region:
        description:
            - The region of the Secrets Manager instance.
        required: False
        type: str
    issuing_certificates_urls_encoded:
        description:
            - Determines whether to encode the URL of the issuing certificate in the certificates that are issued by this certificate authority.
        required: False
        type: bool
    crl_expiry:
        description:
            - The time until the certificate revocation list (CRL) expires.The value can be supplied as a string representation of a duration in hours, such as `48h`. The default is 72 hours. In the API response, this value is returned in seconds (integer).**Note:** The CRL is rotated automatically before it expires.
        required: False
        type: str
    exclude_cn_from_sans:
        description:
            - Controls whether the common name is excluded from Subject Alternative Names (SANs).If the common name set to `true`, it is not included in DNS or Email SANs if they apply. This field can be useful if the common name is a human-readable identifier, instead of a hostname or an email address.
        required: False
        type: bool
    ou:
        description:
            - The Organizational Unit (OU) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    province:
        description:
            - The Province (ST) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    postal_code:
        description:
            - The postal code values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    uri_sans:
        description:
            - The URI Subject Alternative Names to define for the CA certificate, in a comma-delimited list.
        required: False
        type: str
    crl_disable:
        description:
            - Disables or enables certificate revocation list (CRL) building.If CRL building is disabled, a signed but zero-length CRL is returned when downloading the CRL. If CRL building is enabled, it will rebuild the CRL.
        required: False
        type: bool
    key_bits:
        description:
            - The number of bits to use to generate the private key.Allowable values for RSA keys are: `2048` and `4096`. Allowable values for EC keys are: `224`, `256`, `384`, and `521`. The default for RSA keys is `2048`. The default for EC keys is `256`.
        required: False
        type: int
    name:
        description:
            - (Required for new resource) A human-readable unique name to assign to your configuration.To protect your privacy, do not use personal data, such as your name or location, as an name for your secret.
        required: True
        type: str
    locality:
        description:
            - The Locality (L) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    endpoint_type:
        description:
            - public or private.
        required: False
        type: str
    organization:
        description:
            - The Organization (O) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    format:
        description:
            - The format of the returned data.
        required: False
        type: str
    max_path_length:
        description:
            - The maximum path length to encode in the generated certificate. `-1` means no limit.If the signing certificate has a maximum path length set, the path length is set to one less than that of the signing certificate. A limit of `0` means a literal path length of zero.
        required: False
        type: int
    permitted_dns_domains:
        description:
            - The allowed DNS domains or subdomains for the certificates that are to be signed and issued by this CA certificate.
        required: False
        type: list
        elements: str
    instance_id:
        description:
            - (Required for new resource) The ID of the Secrets Manager instance.
        required: True
        type: str
    common_name:
        description:
            - (Required for new resource) The Common Name (AKA CN) represents the server name that is protected by the SSL certificate.
        required: True
        type: str
    max_ttl:
        description:
            - (Required for new resource) The maximum time-to-live (TTL) for certificates that are created by this CA.The value can be supplied as a string representation of a duration in hours, for example '8760h'. In the API response, this value is returned in seconds (integer).Minimum value is one hour (`1h`). Maximum value is 100 years (`876000h`).
        required: True
        type: str
    alt_names:
        description:
            - With the Subject Alternative Name field, you can specify additional host names to be protected by a single SSL certificate.
        required: False
        type: list
        elements: str
    country:
        description:
            - The Country (C) values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    ttl:
        description:
            - The requested time-to-live (TTL) for certificates that are created by this CA. This field's value cannot be longer than the `max_ttl` limit.The value can be supplied as a string representation of a duration in hours, for example '8760h'. In the API response, this value is returned in seconds (integer).
        required: False
        type: str
    key_type:
        description:
            - The type of private key to generate.
        required: False
        type: str
    street_address:
        description:
            - The street address values to define in the subject field of the resulting certificate.
        required: False
        type: list
        elements: str
    serial_number:
        description:
            - The serial number to assign to the generated certificate. To assign a random serial number, you can omit this field.
        required: False
        type: str
    crl_distribution_points_encoded:
        description:
            - Determines whether to encode the certificate revocation list (CRL) distribution points in the certificates that are issued by this certificate authority.
        required: False
        type: bool
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
    ('name', 'str'),
    ('instance_id', 'str'),
    ('common_name', 'str'),
    ('max_ttl', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'ip_sans',
    'other_sans',
    'private_key_format',
    'region',
    'issuing_certificates_urls_encoded',
    'crl_expiry',
    'exclude_cn_from_sans',
    'ou',
    'province',
    'postal_code',
    'uri_sans',
    'crl_disable',
    'key_bits',
    'name',
    'locality',
    'endpoint_type',
    'organization',
    'format',
    'max_path_length',
    'permitted_dns_domains',
    'instance_id',
    'common_name',
    'max_ttl',
    'alt_names',
    'country',
    'ttl',
    'key_type',
    'street_address',
    'serial_number',
    'crl_distribution_points_encoded',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
    ('instance_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'endpoint_type',
    'instance_id',
    'region',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ip_sans=dict(
        required=False,
        type='str'),
    other_sans=dict(
        required=False,
        elements='',
        type='list'),
    private_key_format=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    issuing_certificates_urls_encoded=dict(
        required=False,
        type='bool'),
    crl_expiry=dict(
        required=False,
        type='str'),
    exclude_cn_from_sans=dict(
        required=False,
        type='bool'),
    ou=dict(
        required=False,
        elements='',
        type='list'),
    province=dict(
        required=False,
        elements='',
        type='list'),
    postal_code=dict(
        required=False,
        elements='',
        type='list'),
    uri_sans=dict(
        required=False,
        type='str'),
    crl_disable=dict(
        required=False,
        type='bool'),
    key_bits=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    locality=dict(
        required=False,
        elements='',
        type='list'),
    endpoint_type=dict(
        required=False,
        type='str'),
    organization=dict(
        required=False,
        elements='',
        type='list'),
    format=dict(
        required=False,
        type='str'),
    max_path_length=dict(
        required=False,
        type='int'),
    permitted_dns_domains=dict(
        required=False,
        elements='',
        type='list'),
    instance_id=dict(
        required=False,
        type='str'),
    common_name=dict(
        required=False,
        type='str'),
    max_ttl=dict(
        required=False,
        type='str'),
    alt_names=dict(
        required=False,
        elements='',
        type='list'),
    country=dict(
        required=False,
        elements='',
        type='list'),
    ttl=dict(
        required=False,
        type='str'),
    key_type=dict(
        required=False,
        type='str'),
    street_address=dict(
        required=False,
        elements='',
        type='list'),
    serial_number=dict(
        required=False,
        type='str'),
    crl_distribution_points_encoded=dict(
        required=False,
        type='bool'),
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
        resource_type='ibm_sm_private_certificate_configuration_root_ca',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.51.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_sm_private_certificate_configuration_root_ca',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.51.0',
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
