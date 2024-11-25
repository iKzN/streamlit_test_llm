import streamlit as st
from langchain_openai import ChatOpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = ChatOpenAI(
        max_tokens=500 or None,
        # model_kwargs=model_kwargs,
        model='openai/gpt-4o-mini',
        base_url="https://api.vsegpt.ru/v1",
        api_key=openai_api_key,
        temperature=0,
        extra_body = {'X-Title': 'langflow'} # <-- pass the X-Title request header
    )
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
