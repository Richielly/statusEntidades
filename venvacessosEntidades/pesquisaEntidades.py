import streamlit as st
import requests
import scraping
import webbrowser

from time import sleep as t

st.set_page_config(
    page_title='Pesquisa de entidades',
    page_icon='🏦'
)

sistemas = ['esadmin','stp','scf','srh','stm']
col1, col2, col3 = st.columns(3)
page_urls_prefeituras = scraping.pesquisa_prefeituras()
page_urls_camaras = scraping.pesquisa_camaras()
page_urls_outras = scraping.pesquisa_outras()
st.sidebar.title("Pesquise a entidade pelo número ou nome.")
search = st.sidebar.text_input("Pesquisar")

with col1:
    st.header('Prefeituras')
    if (search != ''):
        for entidade, url in page_urls_prefeituras.items():
            nome = str(entidade)

            with open("urls.txt","a") as arquivo:
                arquivo.write(nome + ' : ' + url+'\n')
                arquivo.close()
            if search.upper() in nome.upper():
                link = '['+entidade+']'+'('+'http://'+url+')'
                try:
                    versao = scraping.versao('http://' + url)
                except : versao = 'não informada.'
                st.markdown(str(link) + ' versão ' +str(versao), unsafe_allow_html=True)

with col2:
    st.header('Câmaras')
    if (search != ''):
        for camara, url_camara in page_urls_camaras.items():
            nome_camara = str(camara)
            if search.upper() in nome_camara.upper():
                link2 = '[' + camara + ']' + '(' + 'http://' + url_camara + ')'
                try:
                    versao = scraping.versao('http://' + url_camara)
                except : versao = 'não informada.'
                st.markdown(str(link2) + ' versão ' +str(versao), unsafe_allow_html=True)
with col3:
    st.header('Outras')
    if (search != ''):
        for outras, url_outras in page_urls_outras.items():
            nome_outras = str(outras)
            if search.upper() in nome_outras.upper():
                link3 = '[' + outras + ']' + '(' + 'http://' + url_outras + ')'
                try:
                    versao = scraping.versao('http://' + url_outras)
                except : versao = 'não informada.'
                st.markdown(str(link3) + ' versão ' +str(versao), unsafe_allow_html=True)
