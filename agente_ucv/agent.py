"""Agente académico desarrollado con Google ADK."""

from google.adk import Agent


CONCEPTOS = {
    "api": "Una API permite la comunicación entre diferentes sistemas.",
    "algoritmo": "Un algoritmo es una secuencia ordenada de pasos.",
    "base de datos": "Una base de datos almacena información organizada.",
    "inteligencia artificial": (
        "La inteligencia artificial permite que una máquina realice "
        "tareas que requieren razonamiento o aprendizaje."
    ),
    "variable": "Una variable almacena un valor que puede cambiar.",
    "función": "Una función agrupa instrucciones que realizan una tarea.",
    "git": "Git permite registrar y controlar los cambios de un proyecto.",
    "poetry": (
        "Poetry permite administrar dependencias y entornos de Python."
    ),
}


def explicar_concepto(concepto: str) -> dict:
    """Devuelve una explicación sencilla de un concepto técnico."""
    if not isinstance(concepto, str):
        return {
            "status": "error",
            "explicacion": "El concepto debe ser un texto.",
        }

    concepto_normalizado = concepto.lower().strip()

    if not concepto_normalizado:
        return {
            "status": "error",
            "explicacion": "Debe ingresar un concepto.",
        }

    if concepto_normalizado in CONCEPTOS:
        return {
            "status": "success",
            "explicacion": CONCEPTOS[concepto_normalizado],
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado.",
    }


def calcular_promedio(numeros: list[float]) -> dict:
    """Calcula el promedio de una lista de números."""
    if not isinstance(numeros, list) or not numeros:
        return {
            "status": "error",
            "mensaje": "Debe ingresar una lista con números.",
        }

    if any(
        isinstance(numero, bool)
        or not isinstance(numero, (int, float))
        for numero in numeros
    ):
        return {
            "status": "error",
            "mensaje": "Todos los valores deben ser numéricos.",
        }

    promedio = sum(numeros) / len(numeros)

    return {
        "status": "success",
        "cantidad": len(numeros),
        "promedio": round(promedio, 2),
    }


root_agent = Agent(
    model="gemini-flash-latest",
    name="agente_ucv",
    description="Agente académico de la Universidad César Vallejo",
    instruction=(
        "Eres un asistente académico. Responde siempre en español, "
        "usa lenguaje sencillo y utiliza las herramientas disponibles "
        "cuando el usuario solicite conceptos o promedios."
    ),
    tools=[explicar_concepto, calcular_promedio],
)