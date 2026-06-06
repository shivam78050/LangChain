from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Assistant")

user_input = st.text_input("Ask me anything")
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
if st.button("Generate Response"):
    result = model.invoke(user_input)
    st.text("Generating response...")
    st.write(result.content)
