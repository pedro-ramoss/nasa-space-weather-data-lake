import requests


def buscar_eventos_flr(data_inicio , data_fim):
    url = "https://ccmc.gsfc.nasa.gov/DONKI-API/get/FLR"

    params = {
        "startDate":data_inicio,
        "endDate":data_fim
    }
    
    resposta = requests.get(url, params=params, timeout=10)
    resposta.raise_for_status()

    return resposta.json()


if __name__ == "__main__":
    eventos = buscar_eventos_flr("2026-11-01", "2026-11-05")
    print(eventos)