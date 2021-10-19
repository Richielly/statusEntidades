import streamlit as st
import requests
import scraping
import webbrowser

st.set_page_config(
    page_title='Pesquisa de entidades',
    page_icon='🏦'
)


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
            link = '['+entidade+']'+'('+'http://'+url+')'
            st.markdown(str(link), unsafe_allow_html=True)
            # if st.button(entidade,entidade):
            #     webbrowser.open_new_tab('http://'+url)
with col2:
    st.header('Câmaras')
    for camara, url_camara in page_urls_camaras.items():
        nome_camara = str(camara)
        if search.upper() in nome_camara.upper():
            link2 = '[' + camara + ']' + '(' + 'http://' + url_camara + ')'
            st.markdown(str(link2), unsafe_allow_html=True)
with col3:
    st.header('Outras')
    for outras, url_outras in page_urls_outras.items():
        nome_outras = str(outras)
        if search.upper() in nome_outras.upper():
            link3 = '[' + outras + ']' + '(' + 'http://' + url_outras + ')'
            st.markdown(str(link3), unsafe_allow_html=True)
