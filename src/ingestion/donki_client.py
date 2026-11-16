import requests
import os
from dotenv import load_dotenv

load_dotenv()

API = os.getenv("NASA_API_KEY")

def buscar_eventos_flr(data_inicio , data_fim):
    url = "https://ccmc.gsfc.nasa.gov/DONKI-API/get/FLR"

    params = {
        "startDate":data_inicio,
        "endDate":data_fim,
        "api_key": API
    }

    resposta = requests.get(url, params=params, timeout=10)

    return resposta.json()

if __name__ == "__main__":
    eventos = buscar_eventos_flr("2026-11-01", "2026-11-05")
    print(eventos)