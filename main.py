from iol import InvertirOnlineAPI
from gspreadmanager import GoogleSheetConector
from config import USERNAME, PASSWORD, JSON_GOOGLE_FILE, DOC_NAME
import datetime
import logging

logging.basicConfig(level=logging.INFO)

def main(event=None, context=None):
    try:
        api = InvertirOnlineAPI(USERNAME, PASSWORD)
        cuenta = api.get_estado_cuenta()
        if 'totalEnPesos' in cuenta:
            total_cuenta = cuenta['totalEnPesos']

            googlesheet = GoogleSheetConector(doc_name=DOC_NAME, json_google_file=JSON_GOOGLE_FILE)
            today = datetime.datetime.now().strftime("%d/%m/%Y")
            googlesheet.spreadsheet_append([[today, total_cuenta]])
            logging.info(f"Dato agregado con éxito: {today}, {total_cuenta}")
        else:
            logging.error("La respuesta de la API no contiene 'totalEnPesos'")
            logging.debug(f"Respuesta de la API: {cuenta}")
    except Exception as e:
        logging.error(f"Error: {e}")

# Punto de entrada para Google Cloud Functions
def cloud_function_entry_point(event, context):
    main(event, context)

# Punto de entrada para ejecución local
if __name__ == "__main__":
    main()
