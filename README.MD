# Invertir Online To Google Spreadsheet

## Descripción
"Invertir Online To Google Spreadsheet" es una herramienta que permite a los usuarios de InvertirOnline exportar automáticamente sus datos de estado de cuenta a una hoja de cálculo de Google. Esto facilita el seguimiento y análisis de las inversiones de una manera más accesible y personalizable. En esta primera version, acumula en un spreadsheet la fecha actual y el monto total de la cuenta para poder llevar un control de la evolución

## Instalación

Para usar este proyecto, sigue estos pasos:

1. Clona el repositorio:
```
git clone xxx
```

2. Instala las dependencias necesarias:
```
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar el script, necesitarás configurar tus credenciales y otros parámetros necesarios:

1. Crea un archivo `config.py` con el siguiente contenido:
```python
USERNAME = 'tu_usuario_invertironline'
PASSWORD = 'tu_contraseña_invertironline'
JSON_GOOGLE_FILE = 'ruta_a_tu_archivo_json_de_google'
DOC_NAME = 'nombre_de_tu_documento_google'
```

Asegúrate de tener las credenciales de la API de Google para interactuar con Google Sheets (ver documentación de Google API para más detalles).

## Uso  
```
python main.py
```
Esto actualizará tu hoja de cálculo de Google con los últimos datos de tu cuenta InvertirOnline. Se puede ejecutar de manera automática con un cronjob y así tener actualizado el estado de cuenta en periodos regulares.

## Contribución
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor, haz un fork del repositorio, realiza tus cambios y envía un pull request.

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)

## Contacto
Podes contactarme por mail a [pablo@culturainteractiva.com](mailto:pablo@culturainteractiva.com) o por [Twitter](https://twitter.com/PabloAlaniz).