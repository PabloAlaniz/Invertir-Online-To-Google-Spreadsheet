import requests
import datetime

class InvertirOnlineAPI:
    def __init__(self, username, password):
        self.base_url = "https://api.invertironline.com"
        self.username = username
        self.password = password
        self.access_token = None
        self.refresh_token = None
        self.token_expires = datetime.datetime.now()
        self.authenticate()

    def authenticate(self):
        data = {
            'username': self.username,
            'password': self.password,
            'grant_type': 'password'
        }
        response = requests.post(f"{self.base_url}/token", data=data)
        if response.status_code == 200:
            self._update_tokens(response.json())

    def _update_tokens(self, token_response):
        self.access_token = token_response['access_token']
        self.refresh_token = token_response['refresh_token']
        expires_in = token_response['expires_in']
        self.token_expires = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)

    def _process_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def is_token_expired(self):
        return datetime.datetime.now() >= self.token_expires

    def refresh_access_token(self):
        if self.refresh_token:
            data = {
                'refresh_token': self.refresh_token,
                'grant_type': 'refresh_token'
            }
            response = requests.post(f"{self.base_url}/token", data=data)
            if response.status_code == 200:
                self._update_tokens(response.json())
            else:
                self.authenticate()
        else:
            raise Exception("No refresh token available. Please authenticate again.")

    def get_estado_cuenta(self):
        if self.is_token_expired():
            self.refresh_access_token()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(f"{self.base_url}/api/v2/estadocuenta", headers=headers)
        return self._process_response(response)

    def get_portfolio(self, pais):
        if self.is_token_expired():
            self.refresh_access_token()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(f"{self.base_url}/api/v2/portafolio/{pais}", headers=headers)
        return self._process_response(response)