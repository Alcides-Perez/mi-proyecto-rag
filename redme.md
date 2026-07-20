# 🤖 Agente IA de Políticas Corporativas (RAG)

Este proyecto consiste en un **Agente de Inteligencia Artificial** diseñado para resolver dudas sobre las políticas internas de una empresa de forma directa y en lenguaje natural. Utiliza una arquitectura **RAG (Retrieval-Augmented Generation)** para buscar información precisa dentro de documentos institucionales (PDFs) y responder a través de un modelo de lenguaje avanzado, evitando que los colaboradores pierdan tiempo buscando manualmente en archivos extensos.

---

## ☁️ Evidencia del Deploy en OCI
La aplicación se encuentra completamente desplegada y funcional en la nube a través de **Oracle Cloud Infrastructure (OCI)**.
*   **Enlace Público:** [http://148.116.109.115:8501](http://148.116.109.115:8501)
*   *Nota: Se adjuntan capturas de pantalla de la interfaz ejecutándose en el servidor en la sección de evidencias del repositorio.*
*   Imagen del navegador*
<img width="1459" height="458" alt="image" src="https://github.com/user-attachments/assets/992f6163-a3af-4595-ba3e-16466fb9269f" />


*   Imagen de implementacion en la Nube de OCI*
La siguiente imagen muestra una maquina virtual donde se corre el servicio publicado
<img width="1604" height="869" alt="image" src="https://github.com/user-attachments/assets/8dcb42b2-449c-4397-8a0c-0799da108130" />

*   Instancia del OCI
<img width="1604" height="869" alt="image" src="https://github.com/user-attachments/assets/e8b0cd01-9ae6-40b8-9fee-0fc63fbe1811" />



## 📐 Arquitectura del Sistema

La solución se compone de los siguientes bloques tecnológicos:

1. **Extracción y Procesamiento:** El documento de políticas (`.pdf`) es procesado y fragmentado en bloques de texto mediante `PyPDF` y `LangChain`.
2. **Indexación Vectorial:** Cada fragmento se convierte en un vector numérico utilizando el modelo `embed-multilingual-v3.0` de **Cohere** y se almacena en una base de datos vectorial local con `ChromaDB`.
3. **Buscador (Retriever):** Cuando un usuario hace una pregunta, el sistema busca los 3 fragmentos de texto más relevantes dentro de la base de datos.
4. **Generación (LLM):** Se envía la pregunta junto con el contexto extraído al modelo `command-r-08-2024` de **Cohere** mediante su API oficial v2 para redactar una respuesta exacta, profesional y sin alucinaciones.
5. **Interfaz de Usuario:** Una aplicación web responsiva y ágil montada con **Streamlit**.

---
## 🛠️ Tecnologías y Herramientas Utilizadas
*   **Lenguaje:** Python 3.10+
*   **Framework Web:** Streamlit
*   **Orquestador de IA:** LangChain
*   **Base de Datos Vectorial:** Chroma DB
*   **Modelos de LLM y Embeddings:** Cohere API (`embed-multilingual-v3.0` y `ClientV2`)
*   **Infraestructura:** Oracle Cloud Infrastructure (OCI) - Instancia Compute (Ubuntu Server)

## 🚀 Instrucciones para Ejecución Local

### Prerrequisitos
* Tener instalado Python 3.10 o superior.
* Contar con una API Key (Trial o Production) de [Cohere](https://dashboard.cohere.com/).

### Instalación
1. Clonar este repositorio:
   ```bash
   git clone [https://github.com/](https://github.com/)[TU_USUARIO_DE_GITHUB]/[NOMBRE_DE_TU_REPOSITORIO].git
   cd [NOMBRE_DE_TU_REPOSITORIO]

### Ejemplo de Preguntas que el agente puede responder con sus respuestas 
1. ¿Podrias citarme los valores institucionales de la empresa?
<img width="797" height="767" alt="image" src="https://github.com/user-attachments/assets/75de54d0-cb73-4346-9e80-cd71d5c91441" />

2. Cuales son los valores de la empresa y que mensaje nos da ? 
<img width="596" height="882" alt="image" src="https://github.com/user-attachments/assets/1e3c0c83-c642-4ba9-ac1d-8a8cc469ecd8" />

