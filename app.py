from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('API_KEY'))


model = genai.GenerativeModel('gemini-pro')
img_model = genai.GenerativeModel('gemini-pro-vision')
def getResponce(title):
    prompt = f"You`re a content writer, Your job is to write Youtube Description from given video summary which is delimited by three backticks write brief description also include subscribe request ```{title}``` "
    res = model.generate_content(prompt,stream=True)
    return res

# def getResponceImage(title):
#     img =img_model.generate_content(title)
#     return img

st.title("🔥 YT Description & Thumbnail Generator")

st.divider()
title = st.text_area('Enter Summary of a Video!',height=100)
txt = st.checkbox('Text',value=True)
img = st.checkbox('Image')
btn = st.button("Generate", type="primary")

tab1, tab2 = st.tabs(["Description", "Image"])

with tab1:
    container = st.container(border=True)
    if (btn or title) and txt :
        if title :
            container.text("The Description is: ")
            res = getResponce(title)
            for r in res:
                container.markdown(r.text)
    else:
        container.write("Nothing To do")

with tab2:
    container2 = st.container(border=True)
    if (btn or title) and img :
        if title :
            container2.text("Your Thumbnail is: ")
            container2.text("Coming Soon... ")
            # res = getResponceImage(title)

    else:
        container2.write("Nothing To do")