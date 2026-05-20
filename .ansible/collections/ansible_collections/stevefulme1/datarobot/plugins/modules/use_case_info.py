# -*- coding: utf-8 -*-
# Copyright (c) 2025, Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to query DataRobot use_case resources."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: use_case_info
short_description: List or retrieve DataRobot use cases
description:
    - Retrieve information about DataRobot use_case resources.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    use_case_id:
        description:
            - The use case id for the DataRobot resource.
        type: str
extends_documentation_fragment:
    - stevefulme1.datarobot.common
requirements:
    - "python >= 3.9"
    - "requests"
"""

EXAMPLES = r"""
- name: List all use_cases
  stevefulme1.datarobot.use_case_info:
    api_url: "https://app.datarobot.com"
    api_key: "my-api-key"
"""

RETURN = r"""
use_cases:
    description: List of use_case resources.
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
        use_case_id=dict(type="str"),
    )
    argument_spec.update(COMMON_ARGS)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if not HAS_REQUESTS:
        module.fail_json(msg="The 'requests' library is required. Install with: pip install requests")

    client = ApiClient(module)

    result = client.get("/api/v2/useCases")
    items = result if isinstance(result, list) else result.get("data", result.get("items", []))
    module.exit_json(changed=False, use_cases=items)


if __name__ == "__main__":
    main()
