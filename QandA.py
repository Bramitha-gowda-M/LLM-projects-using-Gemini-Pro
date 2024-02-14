from dotenv import load_dotenv
load_dotenv()  #loading all the environment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initialize our streamlit app
st.set_page_config(page_title="Question and Answer Demo") #title of the streamlit app

st.header("Gemini LLM Application") #header of app

input=st.text_input('Enter your question: ',key='input') #taking input from user
submit = st.button("Ask the question") #submit button

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)