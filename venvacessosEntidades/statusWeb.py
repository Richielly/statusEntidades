import requests
import streamlit as st
from time import sleep as s
import os.path
from conexao import TransactionObject

dados = TransactionObject()
urls = dados.view()
sistemas = ['esadmin','stp','scf','srh','stm']

if st.sidebar.checkbox("Cadastrar"):
    with st.form(key='cadastrar_entidade'):
        col1, col2 = st.beta_columns(2)
        with col1:
            entidade = st.text_input(label='Código Entidade')
        with col2:
            nome = st.text_input(label='Nome')
        url = st.text_input(label='Url')
        btn_gravar = st.form_submit_button(label='Gravar')

    if btn_gravar:
        if len(dados.search(entidade)) == 0:
            text_url = url.split('/')
            dados.insert(str(entidade), nome, text_url[0] +'//'+ text_url[2] +'/')
            st.success("Registro gravado com sucesso.")
        else:
            st.warning("Entidade já cadastrada.")

if st.sidebar.checkbox("Cadastrados"):
    st.header('Lista de entidades cadastradas:')
    col1, col2 = st.beta_columns(2)
    for url in urls:
        if st.sidebar.checkbox(str(url[1])):
            for sistema in sistemas:
                resposta = requests.get(str(url[3]) + sistema)
                if (resposta.status_code == 200):
                    st.success("Sistema " + sistema.upper() + " no Ar.")
                else:
                    st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")

if st.button("Verificação Geral") :
    for url in urls:
        resposta = requests.get(str(url[3]) +'esadmin')
        if (resposta.status_code == 200):
            st.success("Entidade: " + url[3] + " no Ar.")
        else:
            st.error("Entidade: " + url[3] + " fora do Ar ou sem licença encontrada.")