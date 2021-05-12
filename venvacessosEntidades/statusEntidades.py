import requests
import streamlit as st
from time import sleep as s

#with st.form(key='my_form'):
 #   text_input = st.text_input(label='Enter your name')
  #  submit_button = st.form_submit_button(label='Submit')

urls =[]
sistemas = ['esadmin','stp','scf','srh','stm']
with st.beta_expander("Cadastrar Url"):
    urls = st.text_area('Informe a Url')
    if st.button("Gravar"):
        if urls != "":
            arquivo = open('urls.txt','r')
            # historico = open('urls.txt','r')

            for line in arquivo:
                if urls in line:
                    st.warning('Url já cadastrada, verifique a lista de entidades.')
                    break
                else:
                    arquivo = open('urls.txt', 'a')
                    arquivo.write(urls + "\n")
                    arquivo.close()
                    break
            arquivo.close()

if st.sidebar.checkbox("Cadastrados"):
    st.header('Lista de entidades cadastradas:')
    urls = open('urls.txt', 'r')
    for url in urls:
        label = url.split('//')
        if st.sidebar.checkbox(str(label[1].split('.')[0].upper())):
            for sistema in sistemas:
                resposta = requests.get(str(url.strip('\n')) + sistema)
                if (resposta.status_code == 200):
                    st.success("Sistema " + sistema.upper() + " no Ar.")
                else:
                    st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")

if st.button("Verificação Geral") :
    urls = open('urls.txt', 'r')
    for url in urls:
        resposta = requests.get(str(url.strip('\n'))+'esadmin')
        if (resposta.status_code == 200):
            st.success("Entidade: " + url + " no Ar.")
        else:
            st.error("Entidade: " + url + " fora do Ar ou sem licença encontrada.")
