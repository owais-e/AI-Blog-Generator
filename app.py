import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# function to get response from llama 2 model

def getLLamaResponse(input_text, no_words, blog_style):

    # LLAma model
    llm = CTransformers(model='D:\BlogGenerator\models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens': 256,
                              'temperature': 0.01})

    # prompt template

    template = """
    Write a blog for {blog_style}  job profile 
    for a topic {input_text} within {no_words} words.
    """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)

    # generate the response from model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response






st.set_page_config(page_title="Blog Generator",
                   layout='centered',
                   initial_sidebar_state='collapsed')


st.header('AI Blog Writer')

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the Blg for ',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")


# final response

if submit:
    with st.spinner("Generating the Blog...."):
        st.write(getLLamaResponse(input_text, no_words, blog_style))