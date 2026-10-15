# UI
import streamlit as st
from model import gemini_model

st.header('Gemini LLM')
st.subheader('Version - 3.8 Flash')

text = st.text_area('Enter Prompt:', placeholder='Your Prompt goes here...')

if st.button('Send🦅'):
    if text.strip() =='':
        st.warning('Please enter a valid prompt.')
    else:
        with st.spinner('Generating Content'):
            answer = gemini_model(text)
            st.toast('Content Generated.')
            st.write(answer)
            


# st.header('Streamlit Project')


# # <button type='submit'>Button</button>
# if st.button('Search'):
#     st.text('Hello')
#     st.toast('Sucess')
#     st.success('Success')
#     st.warning('Warning')
#     st.error('Error')

# name_col1, name_col2 = st.columns(2)
# with name_col1:
#     st.text_input('First Name', placeholder='Enter First_Name')
# with name_col2:
#     st.text_input('Last Name', placeholder='Enter Last_Name')

# st.text_area('Enter your prompt', placeholder='Enter Prompt')


