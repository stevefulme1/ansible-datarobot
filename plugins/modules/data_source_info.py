# -*- coding: utf-8 -*-
# Copyright (c) 2025, Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to query DataRobot data_source resources."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: data_source_info
short_description: List or retrieve DataRobot data sources
description:
    - Retrieve information about DataRobot data_source resources.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    data_source_id:
        description:
            - The data source id for the DataRobot resource.
        type: str
extends_documentation_fragment:
    - stevefulme1.datarobot.common
requirements:
    - "python >= 3.9"
    - "requests"
"""

EXAMPLES = r"""
- name: List all data_sources
  stevefulme1.datarobot.data_source_info:
    api_url: "https://app.datarobot.com"
    api_key: "my-api-key"
"""

RETURN = r"""
data_sources:
    description: List of data_source resources.
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
        data_source_id=dict(type="str"),
    )
    argument_spec.update(COMMON_ARGS)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if not HAS_REQUESTS:
        module.fail_json(msg="The 'requests' library is required. Install with: pip install requests")

    client = ApiClient(module)

    result = client.get("/api/v1/data_sources")
    items = result if isinstance(result, list) else result.get("data", result.get("items", []))
    module.exit_json(changed=False, data_sources=items)


if __name__ == "__main__":
    main()
