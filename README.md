# Invertir Online To Google Spreadsheet

Herramienta para exportar automáticamente datos de tu cuenta de InvertirOnline a Google Sheets. Registra diariamente el estado de tu cuenta, permitiéndote hacer seguimiento histórico de tu portafolio.

## 🚀 Features

- 📊 **Estado de cuenta**: Obtiene el total de tu cuenta en pesos
- 💵 **Cotización MEP**: Calcula automáticamente el valor en USD usando dólar MEP
- 📈 **Tracking histórico**: Guarda fecha, monto en ARS, cotización MEP y equivalente en USD
- ⏰ **Automatizable**: Ejecuta con cron para actualizaciones periódicas
- ☁️ **Google Cloud Functions**: Compatible como Cloud Function

## 📋 Requisitos Previos

Antes de instalar, necesitás:

1. **Cuenta en InvertirOnline**: Usuario y contraseña
2. **Proyecto en Google Cloud**:
   - Habilitar Google Sheets API
   - Crear cuenta de servicio (Service Account)
   - Descargar archivo JSON de credenciales
3. **Google Sheet**: Crear una hoja y compartirla con el email de la service account

### Cómo obtener credenciales de Google

1. Ir a [Google Cloud Console](https://console.cloud.google.com/)
2. Crear proyecto nuevo o seleccionar uno existente
3. Habilitar **Google Sheets API**:
   - APIs & Services → Library → buscar "Google Sheets API" → Enable
4. Crear Service Account:
   - APIs & Services → Credentials → Create Credentials → Service Account
   - Completar nombre y descripción
   - Skip permisos opcionales
5. Crear clave JSON:
   - Click en la service account creada
   - Keys → Add Key → Create new key → JSON
   - Guardar el archivo como `credenciales.json` en la raíz del proyecto
6. Compartir tu Google Sheet:
   - Abrir tu hoja de cálculo
   - Compartir con el email de la service account (está en el JSON: `client_email`)
   - Dar permisos de **Editor**

## 🔧 Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/PabloAlaniz/Invertir-Online-To-Google-Spreadsheet.git
cd Invertir-Online-To-Google-Spreadsheet
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Dependencias principales:**
- `requests`: Interacción con API de InvertirOnline
- `GSpreadManager`: Manejo simplificado de Google Sheets

### 3. Configurar credenciales

Crear archivo `config.py` en la raíz del proyecto:

```python
# config.py

# Credenciales de InvertirOnline
USERNAME = 'tu_usuario_invertironline'
PASSWORD = 'tu_contraseña_invertironline'

# Google Sheets
JSON_GOOGLE_FILE = 'credenciales.json'  # Archivo JSON descargado de Google Cloud
DOC_NAME = 'Mi Portafolio IOL'  # Nombre exacto de tu Google Sheet
```

**⚠️ Importante**: `config.py` está en `.gitignore` para proteger tus credenciales.

## 📂 Estructura del Proyecto

```
.
├── main.py                 # Script principal
├── iol.py                  # Cliente API InvertirOnline
├── config.py               # Configuración (no versionado)
├── credenciales.json       # Credenciales Google (no versionado)
├── requirements.txt        # Dependencias Python
├── tests/                  # Tests unitarios
│   ├── test_iol.py
│   └── test_main.py
├── .github/
│   └── workflows/          # CI/CD workflows
├── ROADMAP.md              # Plan de desarrollo
└── FODA.md                 # Análisis FODA del proyecto
```

## 🎯 Uso

### Ejecución manual

```bash
python main.py
```

Esto agregará una nueva fila a tu Google Sheet con:
- Fecha actual
- Total de cuenta en ARS
- Cotización dólar MEP
- Equivalente en USD

### Automatización con cron

Para ejecutar diariamente a las 18:00:

```bash
crontab -e
```

Agregar:
```
0 18 * * * cd /ruta/al/proyecto && python main.py >> /tmp/iol-sync.log 2>&1
```

### Como Google Cloud Function

El código incluye un punto de entrada para Google Cloud Functions:

```python
def cloud_function_entry_point(event, context):
    main(event, context)
```

Para deployar:
```bash
gcloud functions deploy iol_sync \
  --runtime python39 \
  --trigger-topic daily-sync \
  --entry-point cloud_function_entry_point
```

## 🧪 Testing

El proyecto incluye tests unitarios con `pytest`:

```bash
# Instalar pytest si no lo tenés
pip install pytest pytest-cov

# Correr tests
pytest

# Con coverage
pytest --cov=. --cov-report=html
```

## 🔌 API de InvertirOnline

La clase `InvertirOnlineAPI` proporciona:

- `authenticate()`: Autenticación con usuario/contraseña
- `get_estado_cuenta()`: Obtiene estado de cuenta completo
- `get_portfolio(pais)`: Obtiene portafolio por país
- `get_valor_dolar_mep(simbolo)`: Calcula cotización MEP (default: AL30)
- `refresh_access_token()`: Refresca token expirado automáticamente

## 🐛 Troubleshooting

### Error: "No se puede autenticar"
- Verificar usuario y contraseña de InvertirOnline
- Revisar que la API esté disponible: https://api.invertironline.com

### Error: "Permission denied" en Google Sheets
- Verificar que compartiste la hoja con el email de la service account
- Revisar que el nombre del documento en `config.py` sea exacto

### Error: "Module not found: gspreadmanager"
```bash
pip install --upgrade GSpreadManager
```

## 🗺️ Roadmap

Ver [ROADMAP.md](ROADMAP.md) para features planeadas.

## 🤝 Contribución

Las contribuciones son bienvenidas:

1. Fork del repositorio
2. Crear branch para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit con mensajes descriptivos
4. Push al branch
5. Abrir Pull Request

## 📄 Licencia

[MIT](https://choosealicense.com/licenses/mit/)

## 📧 Contacto

**Pablo Alaniz**
- Email: [pablo@culturainteractiva.com](mailto:pablo@culturainteractiva.com)
- Twitter: [@PabloAlaniz](https://twitter.com/PabloAlaniz)
- GitHub: [PabloAlaniz](https://github.com/PabloAlaniz)

---

⭐ Si te resultó útil, dale una estrella al repo!