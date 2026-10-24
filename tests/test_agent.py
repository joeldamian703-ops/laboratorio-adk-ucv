import pytest

from agente_ucv.agent import (
    CONCEPTOS,
    calcular_promedio,
    explicar_concepto,
    root_agent,
)


def test_configuracion_del_agente():
    assert root_agent.name == "agente_ucv"
    assert root_agent.model == "gemini-flash-latest"
    assert len(root_agent.tools) == 2


def test_cantidad_de_conceptos():
    assert len(CONCEPTOS) == 8


@pytest.mark.parametrize(
    "concepto",
    [
        "api",
        "algoritmo",
        "base de datos",
        "inteligencia artificial",
        "variable",
        "función",
        "git",
        "poetry",
    ],
)
def test_conceptos_registrados(concepto):
    result = explicar_concepto(concepto)

    assert result["status"] == "success"
    assert result["explicacion"]


def test_normalizacion_del_concepto():
    result = explicar_concepto("  API  ")

    assert result["status"] == "success"


def test_concepto_no_registrado():
    result = explicar_concepto("computación cuántica")

    assert result == {
        "status": "not_found",
        "explicacion": "Concepto no registrado.",
    }


@pytest.mark.parametrize("entrada", ["", "   ", None, 15])
def test_concepto_invalido(entrada):
    result = explicar_concepto(entrada)

    assert result["status"] == "error"


@pytest.mark.parametrize(
    "numeros, esperado",
    [
        ([15, 18, 17], 16.67),
        ([10], 10.0),
        ([-5, 5], 0.0),
        ([10.5, 11.5], 11.0),
    ],
)
def test_calcular_promedio(numeros, esperado):
    result = calcular_promedio(numeros)

    assert result["status"] == "success"
    assert result["promedio"] == esperado
    assert result["cantidad"] == len(numeros)


@pytest.mark.parametrize(
    "entrada",
    [
        [],
        "10, 20",
        [10, "20"],
        [True, 10],
    ],
)
def test_promedio_invalido(entrada):
    result = calcular_promedio(entrada)

    assert result["status"] == "error"