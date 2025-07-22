import streamlit as st
import requests

# Clave API de Groq almacenada en secretos
GROQ_API_KEY = "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"

st.set_page_config(page_title="Generador SEO con Groq", page_icon="🧠")
st.title("🧠 Generador de Artículos SEO usando Groq (sin OpenAI)")

keyword = st.text_input("🔑 Palabra clave principal", placeholder="Ej: inteligencia artificial")
style = st.selectbox("✍️ Estilo del artículo", ["Informativo", "Persuasivo", "Tutorial"])
length = st.slider("📏 Longitud del artículo (palabras)", 100, 1000, 300)

if st.button("🚀 Generar artículo"):
    with st.spinner("Generando artículo con Groq..."):

        prompt = (
            f"Eres un redactor SEO experto. Escribe un artículo de {length} palabras, estilo {style}, "
            f"usando la palabra clave principal: '{keyword}'. Usa subtítulos, sinónimos y palabras relacionadas."
        )

        headers = {
    "Authorization": f"Bearer {st.secrets['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']}"
}

payload = {
    "inputs": "Escribe un artículo sobre inteligencia artificial."
}

response = requests.post(
    "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
    headers=headers,
    json=payload
)

        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            st.subheader("📄 Artículo generado:")
            st.markdown(content)
        else:
            st.error(f"Error {response.status_code}: {response.text}")
