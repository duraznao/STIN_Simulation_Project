# Modelado Matemático y Evaluación Computacional de la Propagación de Canal en Redes Integradas Terrestre-Satelitales para 6G

Proyecto de Python para simulación de redes STIN (Space-Terrestrial Integrated Networks) y análisis de Path Loss.

## Disponible en GitHub

[https://github.com/duraznao/STIN_Simulation_Project](https://github.com/duraznao/STIN_Simulation_Project.git)

## Estructura del Directorio del Proyecto

Código organizado en módulos

```text
STIN_Project/
├── main.py                # Orquestador del experimento
├── requirements.txt       # Dependencias (numpy, pandas, matplotlib)
├── data/                  # Salida: Archivos CSV
├── plots/                 # Salida: Gráficos científicos
└── src/                   # Módulos internos
    ├── __init__.py        # Indica que src es un paquete
    ├── constants.py       # Parámetros físicos constantes
    ├── physics.py         # Ecuaciones de propagación de canal
    ├── scenarios.py       # Configuración de entornos y órbitas
    └── visualizer.py      # Motor de generación de gráficos

```

---

## Creación y activación del Entorno Virtual de Python

Asegurar que el proyecto implemente las librerías necesarias. Utilizaremos un entorno virtual (`venv`).

#### Instrucciones de despliegue 

Para ejecutar este proyecto ejecute los siguientes comandos en su terminal:

1. **Clonar/Entrar en la carpeta:** `cd STIN_Simulation_Project`
2. **Crear entorno virtual:** 
* Windows: `python -m venv venv`
* Linux/Mac: `python3 -m venv venv`


3. **Activar entorno:**
* Windows: `.\venv\Scripts\activate`
* Linux/Mac: `source venv/bin/activate`


4. **Instalar dependencias:** `pip install -r requirements.txt`
5. **Ejecutar simulación:** `python main.py`

---

### Justificación de esta Estructura

* **Modularidad:** Si mañana se decide cambiar el modelo de pérdida satelital por uno de la **ITU-R P.618** (para lluvia), solo se requiere modificar `src/physics.py` sin romper los gráficos ni la lógica de `main.py`.
* **Reproducibilidad:** El uso de `requirements.txt` elimina el error "ModuleNotFoundError".
* **Escalabilidad:** Esta estructura es compatible con el entrenamiento de los agentes de **Deep Reinforcement Learning (DRL)**  permitiendo añadir una carpeta `src/agents/` en el futuro.