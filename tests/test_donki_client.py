
import pytest
from unittest.mock import patch, Mock
from requests.exceptions import HTTPError

from src.ingestion.donki_client import buscar_eventos_flr


def test_buscar_eventos_flr_sucesso():
    resposta_mock = Mock()
    resposta_mock.status_code = 200
    resposta_mock.json.return_value = [
        {
            "flrID": "2026-11-05T18:21:00-FLR-001",
            "classType": "M3.5"
        }
    ]

    with patch(
        "src.ingestion.donki_client.requests.get",
        return_value=resposta_mock
    ) as mock_get:
        eventos = buscar_eventos_flr("2026-11-01", "2026-11-05")

    assert eventos == resposta_mock.json.return_value
    mock_get.assert_called_once()
    resposta_mock.raise_for_status.assert_called_once()


def test_buscar_eventos_flr_lista_vazia():
    resposta_mock = Mock()
    resposta_mock.status_code = 200
    resposta_mock.json.return_value = []

    with patch(
        "src.ingestion.donki_client.requests.get",
        return_value=resposta_mock
    ):
        eventos = buscar_eventos_flr("2026-11-01", "2026-11-05")

    assert eventos == []
    resposta_mock.raise_for_status.assert_called_once()


def test_buscar_eventos_flr_http_404():
    resposta_mock = Mock()
    resposta_mock.status_code = 404
    resposta_mock.raise_for_status.side_effect = HTTPError(
        "404 Client Error: Not Found"
    )

    with patch(
        "src.ingestion.donki_client.requests.get",
        return_value=resposta_mock
    ):
        with pytest.raises(HTTPError):
            buscar_eventos_flr("2026-11-01", "2026-11-05")

    resposta_mock.json.assert_not_called()


def test_buscar_eventos_flr_http_500():
    resposta_mock = Mock()
    resposta_mock.status_code = 500
    resposta_mock.raise_for_status.side_effect = HTTPError(
        "500 Server Error: Internal Server Error"
    )

    with patch(
        "src.ingestion.donki_client.requests.get",
        return_value=resposta_mock
    ):
        with pytest.raises(HTTPError):
            buscar_eventos_flr("2026-11-01", "2026-11-05")

    resposta_mock.json.assert_not_called()
