import streamlit as st
import requests

GROQ_API_KEY = st.secrets["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"]

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Generador SEO + Imagen", page_icon="🧠")
st.title("🧠 Generador de Artículos SEO + Imagen IA")

keyword = st.text_input("🔑 Palabra clave principal", placeholder="Ej: inteligencia artificial")
style = st.selectbox("✍️ Estilo del artículo", ["Informativo", "Persuasivo", "Tutorial"])
length = st.slider("📏 Longitud del artículo (palabras)", 100, 1000, 300)

if st.button("🚀 Generar contenido"):
    with st.spinner("Generando artículo..."):
        prompt = (
            f"Eres un redactor SEO experto. Escribe un artículo de {length} palabras, estilo {style}, "
            f"usando la palabra clave principal: '{keyword}'. Usa subtítulos, sinónimos y palabras relacionadas."
        )

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 2048
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        content = response.json()["choices"][0]["message"]["content"]

        st.subheader("📄 Artículo generado:")
        st.markdown(content)

    with st.spinner("Generando imagen..."):
        image_prompt = f"Ilustración digital realista de {keyword}, fondo claro, sin texto, alta calidad."

        dalle_headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        dalle_payload = {
            "model": "dall-e-3",
            "prompt": image_prompt,
            "n": 1,
            "size": "1024x1024"
        }

        image_response = requests.post("https://api.openai.com/v1/images/generations",
                                       headers=dalle_headers, json=dalle_payload)

        image_url = image_response.json()["data"][0]["url"]

        st.subheader("🖼 Imagen generada:")
        st.image(image_url, caption=keyword, use_column_width=True)
