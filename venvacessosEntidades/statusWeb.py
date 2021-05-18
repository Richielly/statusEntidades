import requests
import scraping
import streamlit as st
from streamlit_folium import folium_static
import folium
from time import sleep as s
import os.path
from conexao import TransactionObject

dados = TransactionObject()
urls = dados.view()
sistemas = ['esadmin','stp','scf','srh','stm']


# if st.sidebar.checkbox("Pagina"):
#
#     text = scraping.pagina()
#     st.write(text)


# if st.sidebar.checkbox("Cadastrar"):
#     with st.form(key='cadastrar_entidade'):
#         col1, col2 = st.beta_columns(2)
#         with col1:
#             entidade = st.text_input(label='Código Entidade')
#         with col2:
#             nome = st.text_input(label='Nome')
#         url = st.text_input(label='Url')
#         btn_gravar = st.form_submit_button(label='Gravar')

    # if btn_gravar:
    #     if len(dados.search(entidade)) == 0:
    #         text_url = url.split('/')
    #         dados.insert(str(entidade), nome, text_url[0] +'//'+ text_url[2] +'/')
    #         st.success("Registro gravado com sucesso.")
    #     else:
    #         st.warning("Entidade já cadastrada.")

if st.sidebar.checkbox("Cadastrados"):
    page_urls = scraping.pagina()
    st.header('Lista de entidades cadastradas:')
    st.markdown("Total de Entidades na nuvem: " + str(len(page_urls)))
    #col1, col2 = st.beta_columns(2)
    for entidade, url in page_urls.items():
        if st.sidebar.checkbox(str(entidade)):
            for sistema in sistemas:
                resposta = requests.get(str('http://'+url) +':7474/'+ sistema)
                if (resposta.status_code == 200):
                    st.success("Sistema " + sistema.upper() + " no Ar.")
                else:
                    st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")


if st.button("Verificação Geral") :
    page_urls = scraping.pagina()
    st.header('Lista de entidades cadastradas:')
    st.markdown("Total de Entidades na nuvem: "+str(len(page_urls)))

    for entidade, url in page_urls.items():
        resposta = requests.get(str('http://' + url) + ':7474/' +'esadmin')
        if (resposta.status_code == 200):
            st.success("Entidade " + 'http://' + url + ':7474/' +'esadmin' + " no Ar.")
        else:
            st.error("Entidade " + 'http://' + url + ':7474/' +'esadmin' + " fora do Ar ou sem licença.")

    for url in urls:
        resposta = requests.get(str(url[3]) +'esadmin')
        if (resposta.status_code == 200):
            st.success("Entidade: " + url[3] + " no Ar.")
        else:
            st.error("Entidade: " + url[3] + " fora do Ar ou sem licença encontrada.")


if st.sidebar.checkbox("Mapa"):
    st.header("Previsão do tempo, Nuvens Equiplano no Paraná")
    m = folium.Map(location=[-24.3681, -51.7985], zoom_start=7)  #Parana  Lat: -24.3681 Lon: -51.7985

    folium.Marker(
        [-25.1930, -49.3134], popup="Prefeitura\n Câmara", tooltip="Rio Branco Do Sul",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.5806, -49.6295], popup="Prefeitura", tooltip="Balsa Nova",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.2149, -50.9813], popup="Prefeitura", tooltip="Prudentópolis",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-24.8841, -52.2114], popup="Prefeitura", tooltip="Palmital",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.8207, -52.7261], popup="Prefeitura", tooltip="São João",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.7706, -53.5321], popup="Prefeitura", tooltip="Realeza",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-24.1078, -49.4708], popup="Prefeitura", tooltip="Sengés",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.0884, -54.2471], popup="Câmara", tooltip="Missal",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.7086, -52.9190], popup="Prefeitura", tooltip="São Jorge D'Oeste",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.8798, -48.5751], popup="GuaraPrev", tooltip="Guaratuba",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.3069, -52.5427], popup="Câmara", tooltip="Nova Laranjeiras",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.7182, -53.7672], popup="Fundo", tooltip="Planalto",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.7498, -53.0534], popup="Prefeitura", tooltip="Dois Vizinhos",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.9863, -50.1959], popup="Prefeitura", tooltip="Antônio Olinto",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.1896, -50.8085], popup="Prefeitura\nFundo", tooltip="Guamiranga",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.4113, -50.5492], popup="Prefeitura", tooltip="Fernandes Pinheiros",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-23.5948, -50.7608], popup="Câmara", tooltip="Nova Santa Barbara",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-24.2456, -49.7057], popup="Câmara", tooltip="Jaguariaiva",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.4622, -50.6335], popup="Conder", tooltip="Irati",icon=folium.Icon(icon="cloud")).add_to(m)

    # Criando o mapa
    folium_static(m)
    # Salvando o mapa em html
    #if st.button("Salvar"):
     #   m.save('mapa-nuvens-equiplano.html')
