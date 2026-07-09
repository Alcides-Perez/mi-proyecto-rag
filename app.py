import os
import streamlit as st
import cohere
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma

# --- CONFIGURACIÓN DE LA INTERFAZ WEB ---
st.set_page_config(page_title="Asistente de Políticas de la Empresa", page_icon="🤖")
st.title("🤖 Asistente Virtual de Políticas Internas")
st.write("Hacé tus preguntas sobre los manuales y políticas de la empresa.")

# --- CONFIGURACIÓN DE COHERE ---
# En producción, es mejor leer la API Key desde variables de entorno
COHERE_API_KEY = os.environ.get("COHERE_API_KEY", "Y8mmhK3VIDC64x8cJqsmdy4HDWoP4QccqgPXsFha")
cohere_client = cohere.ClientV2(api_key=COHERE_API_KEY)

# --- PROCESAMIENTO DEL DOCUMENTO (Se ejecuta una sola vez para ahorrar recursos) ---
@st.cache_resource
def inicializar_base_datos():
    # Cargar el PDF
    loader = PyPDFLoader("politicas_empresa.pdf")
    documentos_completos = loader.load()
    
    # Fragmentar
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    fragmentos = text_splitter.split_documents(documentos_completos)
    
    # Crear base de datos vectorial
    embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")
    db_vectorial = Chroma.from_documents(fragmentos, embeddings)
    return db_vectorial.as_retriever(search_kwargs={"k": 3})

# Inicializamos el buscador
buscador = inicializar_base_datos()

# --- CHAT / INTERACCIÓN ---
# Campo de texto para que el usuario escriba en la web
pregunta_usuario = st.text_input("Escribí tu consulta acá:", placeholder="Ej: ¿Cuántos días me corresponden por estudio?")

if pregunta_usuario:
    with st.spinner("Buscando en el documento..."):
        try:
            # 1. Buscar fragmentos relevantes
            documentos_encontrados = buscador.invoke(pregunta_usuario)
            contexto_pdf = "\n\n".join(doc.page_content for doc in documentos_encontrados)
            
            # 2. Definir Prompts
            system_prompt = (
                "Sos un asistente virtual experto en las políticas internas de la empresa.\n"
                "Tu único objetivo es responder las preguntas de los empleados usando "
                "estrictamente el contexto provisto a continuación. Si la respuesta no está "
                "en el contexto, decí amablemente: 'Lo siento, no encontré esa información en las políticas actuales.'\n"
                "Mantené un tono profesional, claro y servicial."
            )
            user_prompt = f"Contexto extraído del PDF:\n{contexto_pdf}\n\nPregunta del empleado: {pregunta_usuario}"
            
            # 3. Llamar a Cohere
            response = cohere_client.chat(
                model="command-r-08-2024",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.0
            )
            
            # 4. Mostrar respuesta en la web
            st.subheader("🤖 Respuesta del Agente:")
            st.write(response.message.content[0].text)
            
        except Exception as e:
            st.error(f"Hubo un problema con la API de Cohere: {e}")