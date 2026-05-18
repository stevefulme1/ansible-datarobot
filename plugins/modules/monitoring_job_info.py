# -*- coding: utf-8 -*-
# Copyright (c) 2025, Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to query DataRobot monitoring_job resources."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: monitoring_job_info
short_description: List or retrieve DataRobot monitoring jobs
description:
    - Retrieve information about DataRobot monitoring_job resources.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    deployment_id:
        description:
            - The deployment id for the DataRobot resource.
        type: str
    job_id:
        description:
            - The job id for the DataRobot resource.
        type: str
extends_documentation_fragment:
    - stevefulme1.datarobot.common
requirements:
    - "python >= 3.9"
    - "requests"
"""

EXAMPLES = r"""
- name: List all monitoring_jobs
  stevefulme1.datarobot.monitoring_job_info:
    api_url: "https://app.datarobot.com"
    api_key: "my-api-key"
"""

RETURN = r"""
monitoring_jobs:
    description: List of monitoring_job resources.
    returned: always
    type: list
    elements: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.stevefulme1.datarobot.plugins.module_utils.api_client import (
    COMMON_ARGS,
    ApiClient,
    HAS_REQUESTS,
)


def main():
    argument_spec = dict(
        deployment_id=dict(type="str"),
        job_id=dict(type="str"),
    )
    argument_spec.update(COMMON_ARGS)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if not HAS_REQUESTS:
        module.fail_json(msg="The 'requests' library is required. Install with: pip install requests")

    client = ApiClient(module)
    params = module.params

    if params.get("deployment_id"):
        result = client.get(f"/api/v1/monitoring_jobs/{params['deployment_id']}")
        module.exit_json(changed=False, monitoring_jobs=[result] if result else [])
    else:
        result = client.get("/api/v1/monitoring_jobs")
        items = result if isinstance(result, list) else result.get("data", result.get("items", []))
        module.exit_json(changed=False, monitoring_jobs=items)


if __name__ == "__main__":
    main()
