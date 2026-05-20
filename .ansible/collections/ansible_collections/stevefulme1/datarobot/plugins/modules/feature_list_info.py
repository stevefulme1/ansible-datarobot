# -*- coding: utf-8 -*-
# Copyright (c) 2025, Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to query DataRobot feature_list resources."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: feature_list_info
short_description: List or retrieve DataRobot feature lists
description:
    - Retrieve information about DataRobot feature_list resources.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    project_id:
        description:
            - The project id for the DataRobot resource.
        type: str
        required: true
    feature_list_id:
        description:
            - The feature list id for the DataRobot resource.
        type: str
extends_documentation_fragment:
    - stevefulme1.datarobot.common
requirements:
    - "python >= 3.9"
    - "requests"
"""

EXAMPLES = r"""
- name: List all feature_lists
  stevefulme1.datarobot.feature_list_info:
    api_url: "https://app.datarobot.com"
    api_key: "my-api-key"
"""

RETURN = r"""
feature_lists:
    description: List of feature_list resources.
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
        project_id=dict(type="str", required=True),
        feature_list_id=dict(type="str"),
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

    if not params.get("project_id"):
        module.fail_json(msg="project_id is required to list feature lists")

    result = client.get(f"/api/v2/projects/{params['project_id']}/featurelists/")
    items = result if isinstance(result, list) else result.get("data", result.get("items", []))
    module.exit_json(changed=False, feature_lists=items)


if __name__ == "__main__":
    main()
