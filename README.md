# KeleaCare

![KeleaCare](./Captura%20desde%202025-02-22%2016-39-10.png)

## Descripción
KeleaCare es un sistema inteligente de apoyo emocional que interactúa de manera empática con los usuarios, perfilando su personalidad y ofreciendo respuestas personalizadas y objetivos para su crecimiento personal.

Este proyecto fue desarrollado como parte de **HackUDC 2025**, con el objetivo de proporcionar un **chatbot de apoyo emocional** que detecte y responda a emociones de forma adaptativa.

## Características principales
- 🤖 **Chatbot de Apoyo Emocional**: análisis de sentimientos y emociones en tiempo real, con respuestas adaptadas a la emoción detectada.
- 📔 **Diario Emocional Inteligente**: permite registrar emociones y almacenar tendencias a lo largo del tiempo.
- 🎯 **Sistema de Perfilado de Personalidad**: basado en modelos psicológicos como Eneagrama y Big Five.
- 📢 **Coach de Bienestar y Objetivos**: generación de recomendaciones personalizadas según el estado emocional detectado.

## Tecnologías Utilizadas
- **Procesamiento de lenguaje natural (NLP)**: Vader, text2emotion, transformers (GoEmotion), EmoRoBERTa, nltk / spaCy.
- **Modelos de Lenguaje**: Vicuna, LLaMA 2, Mistral, DeepSeek.
- **Almacenamiento**: bases de datos vectoriales (Weaviate, FAISS), JSON, SQL.
- **Interfaz**: Streamlit, FastAPI, React.

## Instalación y Configuración
1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tuusuario/keleacare.git
   cd keleacare
   ```
2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el servidor:
   ```bash
   uvicorn main:app --reload
   ```
4. Abrir la interfaz en el navegador:
   ```
   http://127.0.0.1:8000
   ```

## Estructura del Proyecto
```
keleacare/
│── backend/              # API y procesamiento de datos
│── frontend/             # Interfaz de usuario y componentes visuales
│── models/               # Modelos de NLP y análisis emocional
│── database/             # Almacenamiento de datos
│── README.md             # Documentación
```

## Contribución
Si quieres contribuir a **KeleaCare**, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature-nueva`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía un pull request.

## Contacto
Para cualquier duda o sugerencia, puedes encontrarnos en el stand de **Kelea** en **HackUDC2025**. ¡Esperamos tu participación!

