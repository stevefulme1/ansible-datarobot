"""Unit tests for stevefulme1.datarobot.model module."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from unittest.mock import MagicMock, patch

import pytest

MODULE_PATH = "ansible_collections.stevefulme1.datarobot.plugins.modules.model"
CLIENT_PATH = "ansible_collections.stevefulme1.datarobot.plugins.module_utils.api_client"


def _build_model(**kwargs):
    """Return a mock model dict."""
    defaults = {"id": "test-id", "name": "test-model"}
    defaults.update(kwargs)
    return defaults


class TestCreate:
    """Test model creation."""

    @patch(f"{CLIENT_PATH}.requests")
    def test_create_model(self, mock_requests, module_args):
        """Creating a model sends POST request."""
        mock_response = MagicMock()
        created = _build_model()
        mock_response.json.return_value = created
        mock_response.raise_for_status.return_value = None
        mock_response.content = b'{"id":"test-id"}'

        list_response = MagicMock()
        list_response.json.return_value = []
        list_response.raise_for_status.return_value = None
        list_response.content = b'[]'

        session = MagicMock()
        session.request.side_effect = [list_response, mock_response]
        mock_requests.Session.return_value = session

        from ansible_collections.stevefulme1.datarobot.plugins.module_utils.api_client import ApiClient

        mock_module = MagicMock()
        mock_module.params = module_args
        client = ApiClient(mock_module)
        result = client.post("/api/v1/models", data={"name": "test"})
        assert result is not None
