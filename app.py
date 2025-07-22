import streamlit as st
import requests

st.set_page_config(page_title="Generador de Artículos SEO", page_icon="🧠")
st.title("🧠 Generador de Artículos con Hugging Face")

# Entrada del usuario
keyword = st.text_input("🔑 Palabra clave principal", placeholder="Ej: inteligencia artificial")
style = st.selectbox("✍️ Estilo del artículo", ["Informativo", "Persuasivo", "Tutorial"])
length = st.slider("📏 Longitud del artículo (palabras)", 100, 1000, 300)

if st.button("🚀 Generar artículo"):
    with st.spinner("Generando artículo..."):
        # Token desde secrets.toml
        headers = {
            "Authorization": f"Bearer {st.secrets['HF_TOKEN']}"
        }

        # Construimos el prompt
        prompt = (
            f"Eres un redactor SEO experto. Escribe un artículo de {length} palabras, estilo {style}, "
            f"usando la palabra clave principal: '{keyword}'. Usa subtítulos y lenguaje claro."
        )

        payload = {
            "inputs": prompt
        }

        # Modelo Hugging Face (gratis y público)
        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
            headers=headers,
            json=payload
        )

        # Resultado
        if response.status_code == 200:
            result = response.json()
            st.subheader("📄 Artículo generado:")
            st.write(result[0]["generated_text"])
        else:
            st.error(f"Error {response.status_code}: No se pudo generar el artículo.")
