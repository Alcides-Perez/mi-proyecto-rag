# 🤖 Agente IA de Políticas Corporativas (RAG)

Este proyecto consiste en un **Agente de Inteligencia Artificial** diseñado para resolver dudas sobre las políticas internas de una empresa de forma directa y en lenguaje natural. Utiliza una arquitectura **RAG (Retrieval-Augmented Generation)** para buscar información precisa dentro de documentos institucionales (PDFs) y responder a través de un modelo de lenguaje avanzado, evitando que los colaboradores pierdan tiempo buscando manualmente en archivos extensos.

---

## 📐 Arquitectura del Sistema

La solución se compone de los siguientes bloques tecnológicos:

1. **Extracción y Procesamiento:** El documento de políticas (`.pdf`) es procesado y fragmentado en bloques de texto mediante `PyPDF` y `LangChain`.
2. **Indexación Vectorial:** Cada fragmento se convierte en un vector numérico utilizando el modelo `embed-multilingual-v3.0` de **Cohere** y se almacena en una base de datos vectorial local con `ChromaDB`.
3. **Buscador (Retriever):** Cuando un usuario hace una pregunta, el sistema busca los 3 fragmentos de texto más relevantes dentro de la base de datos.
4. **Generación (LLM):** Se envía la pregunta junto con el contexto extraído al modelo `command-r-08-2024` de **Cohere** mediante su API oficial v2 para redactar una respuesta exacta, profesional y sin alucinaciones.
5. **Interfaz de Usuario:** Una aplicación web responsiva y ágil montada con **Streamlit**.

---

## 🚀 Instrucciones para Ejecución Local

### Prerrequisitos
* Tener instalado Python 3.10 o superior.
* Contar con una API Key (Trial o Production) de [Cohere](https://dashboard.cohere.com/).

### Instalación
1. Clonar este repositorio:
   ```bash
   git clone [https://github.com/](https://github.com/)[TU_USUARIO_DE_GITHUB]/[NOMBRE_DE_TU_REPOSITORIO].git
   cd [NOMBRE_DE_TU_REPOSITORIO]