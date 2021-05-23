import streamlit as st
import requests
import scraping
import webbrowser
sistemas = ['esadmin','stp','scf','srh','stm']
col1, col2, col3 = st.beta_columns(3)
page_urls_prefeituras = scraping.pesquisa_prefeituras()
page_urls_camaras = scraping.pesquisa_camaras()
page_urls_outras = scraping.pesquisa_outras()
st.sidebar.title("Pesquise a entidade pelo número ou nome.")
search = st.sidebar.text_input("Pesquisar")

with col1:
    st.header('Prefeituras')
    for entidade, url in page_urls_prefeituras.items():
        nome = str(entidade)
        if search.upper() in nome.upper():
            if st.button(entidade,entidade):
                webbrowser.open_new_tab('http://'+url)
with col2:
    st.header('Câmaras')
    for camara, url_camara in page_urls_camaras.items():
        nome_camara = str(camara)
        if search.upper() in nome_camara.upper():
            if st.button(camara,camara):
                webbrowser.open_new_tab('http://'+url_camara)
with col3:
    st.header('Outras')
    for outras, url_outras in page_urls_outras.items():
        nome_outras = str(outras)
        if search.upper() in nome_outras.upper():
            if st.button(outras,outras):
                webbrowser.open_new_tab('http://'+url_outras)
