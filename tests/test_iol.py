"""Tests for InvertirOnlineAPI class."""

import pytest
from unittest.mock import Mock, patch
import datetime


class TestInvertirOnlineAPIInit:
    """Test API initialization and authentication."""

    def test_init_authenticates(self, mock_requests, mock_auth_response):
        """Test that init calls authenticate."""
        from iol import InvertirOnlineAPI
        
        api = InvertirOnlineAPI('testuser', 'testpass')
        
        assert api.username == 'testuser'
        assert api.password == 'testpass'
        assert api.access_token == 'test_access_token'
        mock_requests.post.assert_called()

    def test_auth_failure_no_token(self, mock_requests):
        """Test handling of auth failure."""
        from iol import InvertirOnlineAPI
        
        # Mock failed auth
        failed_response = Mock()
        failed_response.status_code = 401
        mock_requests.post.return_value = failed_response
        
        api = InvertirOnlineAPI('baduser', 'badpass')
        
        assert api.access_token is None


class TestAPIRequests:
    """Test API request methods."""

    def test_get_account_state(self, mock_requests, mock_auth_response):
        """Test get_estado_cuenta method."""
        from iol import InvertirOnlineAPI
        
        api = InvertirOnlineAPI('testuser', 'testpass')
        
        # Mock account state response
        account_response = Mock()
        account_response.status_code = 200
        account_response.json.return_value = {
            'cuentas': [{'moneda': 'peso_Argentino', 'disponible': 1000}]
        }
        mock_requests.get.return_value = account_response
        
        result = api.get_estado_cuenta()
        
        assert result is not None
        mock_requests.get.assert_called()

    def test_get_portfolio(self, mock_requests, mock_auth_response):
        """Test get_portafolio method."""
        from iol import InvertirOnlineAPI
        
        api = InvertirOnlineAPI('testuser', 'testpass')
        
        # Mock portfolio response
        portfolio_response = Mock()
        portfolio_response.status_code = 200
        portfolio_response.json.return_value = {
            'activos': [{'simbolo': 'GGAL', 'cantidad': 100}]
        }
        mock_requests.get.return_value = portfolio_response
        
        result = api.get_portafolio('argentina')
        
        assert result is not None


class TestTokenRefresh:
    """Test token refresh functionality."""

    def test_refresh_token_called_when_expired(self, mock_requests, mock_auth_response):
        """Test that refresh is called when token expires."""
        from iol import InvertirOnlineAPI
        
        api = InvertirOnlineAPI('testuser', 'testpass')
        
        # Expire the token
        api.token_expires = datetime.datetime.now() - datetime.timedelta(hours=1)
        
        # Mock refresh response
        refresh_response = Mock()
        refresh_response.status_code = 200
        refresh_response.json.return_value = mock_auth_response
        mock_requests.post.return_value = refresh_response
        
        # Any API call should trigger refresh
        api._ensure_token_valid()
        
        # Should have called POST again for refresh
        assert mock_requests.post.call_count >= 2
