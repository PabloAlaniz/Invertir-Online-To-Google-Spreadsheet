import requests
import datetime

class InvertirOnlineAPI:
    """
    Clase para interactuar con la API de InvertirOnline.

    Esta clase proporciona métodos para autenticarse en la API de InvertirOnline,
    refrescar tokens de acceso y realizar solicitudes para obtener datos como el estado
    de cuenta y el portafolio por país.

    Attributes:
        username (str): Nombre de usuario para la autenticación en la API.
        password (str): Contraseña para la autenticación en la API.
        access_token (str): Token de acceso obtenido después de la autenticación.
        refresh_token (str): Token de actualización para obtener un nuevo access_token.
        token_expires (datetime): Fecha y hora de expiración del access_token.
    """

    def __init__(self, username, password):
        """
        Constructor para la clase InvertirOnlineAPI.

        Args:
            username (str): Nombre de usuario para la autenticación en la API.
            password (str): Contraseña para la autenticación en la API.
        """
        self.base_url = "https://api.invertironline.com"
        self.username = username
        self.password = password
        self.access_token = None
        self.refresh_token = None
        self.token_expires = datetime.datetime.now()
        self.authenticate()

    def authenticate(self):
        """
        Autentica al usuario en la API de InvertirOnline.

        Realiza una solicitud POST para obtener el access_token y el refresh_token.
        Estos tokens son necesarios para realizar solicitudes posteriores a la API.
        """
        data = {
            'username': self.username,
            'password': self.password,
            'grant_type': 'password'
        }
        response = requests.post(f"{self.base_url}/token", data=data)
        if response.status_code == 200:
            self._update_tokens(response.json())

    def _update_tokens(self, token_response):
        """
        Actualiza los tokens de acceso y refresco basado en la respuesta de la API.

        Args:
            token_response (dict): Respuesta de la API conteniendo los nuevos tokens.
        """
        self.access_token = token_response['access_token']
        self.refresh_token = token_response['refresh_token']
        expires_in = token_response['expires_in']
        self.token_expires = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)

    def _process_response(self, response):
        """
        Procesa la respuesta de la API.

        Args:
            response (requests.Response): Respuesta obtenida de la API.

        Returns:
            dict or str: Contenido de la respuesta en formato JSON si el código de
            estado es 200, de lo contrario, devuelve el texto de la respuesta.
        """
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def is_token_expired(self):
        """
        Comprueba si el token de acceso ha expirado.

        Returns:
            bool: True si el token ha expirado, False en caso contrario.
        """
        return datetime.datetime.now() >= self.token_expires

    def refresh_access_token(self):
        """
        Refresca el access_token utilizando el refresh_token.

        Si el refresh_token no está disponible o la solicitud falla, se intenta
        autenticar de nuevo.
        """
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
        """
        Obtiene el estado de cuenta del usuario.

        Returns:
            dict or str: Estado de cuenta del usuario en formato JSON o un mensaje de error.
        """
        if self.is_token_expired():
            self.refresh_access_token()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(f"{self.base_url}/api/v2/estadocuenta", headers=headers)
        return self._process_response(response)

    def get_portfolio(self, pais):
        """
        Obtiene el portafolio del usuario para un país específico.

        Args:
            pais (str): El país para el cual obtener el portafolio.

        Returns:
            dict or str: Portafolio del usuario en formato JSON o un mensaje de error.
        """
        if self.is_token_expired():
            self.refresh_access_token()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(f"{self.base_url}/api/v2/portafolio/{pais}", headers=headers)
        return self._process_response(response)

    def get_valor_dolar_mep(self, simbolo="AL30"):
        """
        Obtiene el valor del dólar MEP para un símbolo específico.

        Realiza una solicitud GET a la API para obtener la cotización del dólar MEP
        basada en el símbolo proporcionado. Si no se especifica un símbolo, se utiliza
        'AL30' por defecto.

        Args:
            simbolo (str): El símbolo para el cual obtener la cotización del dólar MEP.
                           Por defecto es 'AL30'.

        Returns:
            double: El valor del dólar MEP para el símbolo dado.
        """
        if self.is_token_expired():
            self.refresh_access_token()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(f"{self.base_url}/api/v2/Cotizaciones/MEP/{simbolo}", headers=headers)
        return self._process_response(response)
