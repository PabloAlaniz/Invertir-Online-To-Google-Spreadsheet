"""Pytest configuration and fixtures."""

import pytest
from unittest.mock import Mock, patch
import datetime


@pytest.fixture
def mock_auth_response():
    """Mock successful authentication response."""
    return {
        'access_token': 'test_access_token',
        'refresh_token': 'test_refresh_token',
        'expires_in': 3600,
        '.expires': (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat()
    }


@pytest.fixture
def mock_requests(mock_auth_response):
    """Mock requests module."""
    with patch('iol.requests') as mock:
        # Setup auth response
        auth_response = Mock()
        auth_response.status_code = 200
        auth_response.json.return_value = mock_auth_response
        mock.post.return_value = auth_response
        
        yield mock
