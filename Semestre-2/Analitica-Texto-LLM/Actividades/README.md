# Análisis de Texto - Prácticas y Actividades

Este repositorio contiene apuntes, scripts y actividades para el curso de Análisis de Texto

## 🛠️ Entorno de Trabajo

Para la elaboración de estas actividades se utilizó lo siguiente:
* **IDE:** Visual Studio Code (VS Code)
* **Gestor de entornos:** Anaconda (Conda)
* **Lenguaje:** Python 3.10
* **Librerías principales:** NLTK, spaCy y Stanza

## ⚙️ Configuración del Entorno

Para ejecutar los códigos de este repositorio sin conflictos de dependencias, se recomienda replicar el entorno virtual utilizando `conda`. 

Desde la terminal o Anaconda Prompt, ejecuta el siguiente bloque de comandos para crear el entorno, activarlo e instalar todas las dependencias necesarias:

```bash
# 1. Crear y activar el entorno
conda create --name analisis_texto python=3.10 -y
conda activate analisis_texto

# 2. Instalar NLTK
conda install -c anaconda nltk -y

# 3. Instalar spaCy y modelos de lenguaje (Inglés y Español)
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm

# 4. Instalar Stanza
pip install stanza