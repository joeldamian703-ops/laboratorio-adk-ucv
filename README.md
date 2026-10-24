# Laboratorio 8: Agente académico con Google ADK

Proyecto desarrollado para el curso de Sistemas Inteligentes de la Universidad César Vallejo.

## Descripción

Este proyecto implementa un monoagente académico utilizando Google ADK y el modelo Gemini. El agente responde en español y dispone de herramientas personalizadas para explicar conceptos técnicos y calcular promedios.

## Funcionalidades

- Explicación de conceptos técnicos.
- Ocho conceptos registrados:
  - API
  - Algoritmo
  - Base de datos
  - Inteligencia artificial
  - Variable
  - Función
  - Git
  - Poetry
- Cálculo del promedio de una lista de números.
- Validación de entradas vacías o incorrectas.
- Ejecución mediante terminal e interfaz web de Google ADK.
- Pruebas automatizadas con Pytest.
- Medición de cobertura del código.

## Tecnologías utilizadas

- Python 3.14
- Google ADK
- Gemini
- Poetry
- Pytest
- Pytest-cov
- GitHub Actions
- SonarQube Cloud

## Estructura del proyecto

```text
laboratorio-adk-ucv/
├── agente_ucv/
│   ├── __init__.py
│   ├── agent.py
│   └── .env
├── tests/
│   ├── __init__.py
│   └── test_agent.py
├── .github/
│   └── workflows/
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Instalación

```powershell
poetry install --no-root
```

## Configuración

Crear el archivo `agente_ucv/.env` con las siguientes variables:

```env
GOOGLE_GENAI_USE_ENTERPRISE=FALSE
GOOGLE_API_KEY=TU_CLAVE_PRIVADA
```

La clave real no debe subirse al repositorio.

## Ejecución en terminal

```powershell
poetry run adk run agente_ucv
```

## Ejecución de la interfaz web

```powershell
poetry run adk web
```

Luego abrir:

```text
http://127.0.0.1:8000
```

## Pruebas y cobertura

```powershell
poetry run pytest -v --cov=agente_ucv --cov-report=term-missing --cov-report=xml
```

El proyecto cuenta con 24 pruebas automatizadas aprobadas y una cobertura del 100 % del código del agente.

## Reflexión

### ¿Cuál es la diferencia entre un chatbot y un agente?

Un chatbot responde mensajes siguiendo instrucciones o conversaciones definidas. Un agente también puede analizar la solicitud, seleccionar herramientas y ejecutar acciones para cumplir un objetivo.

### ¿Qué beneficios ofrece Poetry?

Poetry administra las dependencias, crea un entorno virtual aislado y registra versiones en un archivo de bloqueo. Esto facilita que el proyecto funcione de la misma manera en diferentes equipos.

### ¿Para qué se utiliza GitHub Actions?

GitHub Actions permite ejecutar automáticamente las pruebas y el análisis del proyecto cuando se suben cambios al repositorio. De esta forma se detectan errores antes de integrar el código.

### ¿Qué aporta SonarQube al proyecto?

SonarQube analiza la calidad del código y ayuda a encontrar errores, vulnerabilidades, duplicaciones y problemas de mantenimiento.

### ¿Qué mejoras podrían implementarse?

Se podrían agregar más herramientas académicas, guardar el historial de consultas, conectar una base de datos, incorporar autenticación y desarrollar una interfaz personalizada para estudiantes.

## Autor

Cesar Joel Sirlopu Damian  
Ingeniería de Sistemas — Universidad César Vallejo