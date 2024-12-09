import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_ai_model():
    """Initialize AI model with error handling"""
    try:
        return ChatOpenAI(
            temperature=0.7,
            model_name="gpt-3.5-turbo"
        )
    except Exception as e:
        st.error(f"Error initializing AI model: {str(e)}")
        return None

def generate_content(prompt, system_prompt=""):
    """Generate content using the AI model"""
    try:
        model = init_ai_model()
        if not model:
            return "Error: Could not initialize AI model"

        template = ChatPromptTemplate.from_template(
            system_prompt + "\n\n" + prompt if system_prompt else prompt
        )
        chain = template | model | StrOutputParser()
        return chain.invoke({})

    except Exception as e:
        return f"Error: {str(e)}"

def load_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: #FF4B4B;
        text-align: center;
        margin: 2rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 500;
        color: #FAFAFA;
        margin: 1rem 0;
    }
    
    .card {
        text-align: center;
        padding: 20px;
        margin: 10px 0;
        background-color: #262730;
        border-radius: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    
    .card img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin: 0 auto 15px auto;
        display: block;
        border: 3px solid #FF4B4B;
        transition: transform 0.3s ease;
    }
    
    .card img:hover {
        transform: scale(1.1);
    }
    
    .card h3 {
        color: #FFFFFF;
        margin: 10px 0;
        font-size: 1.2rem;
    }
    
    .card p {
        color: #B2B2B2;
        margin: 5px 0;
    }
    
    .card a {
        color: #FF4B4B;
        text-decoration: none;
        margin: 0 5px;
        transition: color 0.3s ease;
    }
    
    .card a:hover {
        color: #FF7676;
        text-decoration: underline;
    }
    
    .info-text {
        font-size: 0.9rem;
        color: #B2B2B2;
        font-style: italic;
    }
    </style>
    """

def show_error(message):
    st.error(f"🚨 {message}")

def show_success(message):
    st.success(f"✅ {message}")

def show_info(message):
    st.info(f"ℹ️ {message}")