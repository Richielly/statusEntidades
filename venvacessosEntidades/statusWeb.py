import requests
import scraping
import streamlit as st
import time as t
from time import sleep as s
import os.path
from streamlit_folium import folium_static
import folium
from conexao import TransactionObject


dados = TransactionObject()
urls = dados.view()
sistemas = ['esadmin','stp','scf','srh','stm']

# if st.sidebar.checkbox("Pagina"):
#
#     text = scraping.pagina()
#     st.write(text)

if st.sidebar.checkbox("Cadastrados "):
    page_urls = scraping.pagina()
    st.header('Lista de entidades cadastradas:')
    st.markdown("Total de Entidades na nuvem: " + str(len(page_urls)))
    #col1, col2 = st.beta_columns(2)
    for entidade, url in page_urls.items():
        if st.sidebar.checkbox(str(entidade)):
            for sistema in sistemas:
                try:
                    resposta = requests.get(str('http://'+url) +':7474/'+ sistema)
                except:
                    resposta = requests.get(str('http://' + url) + ':8080/' + sistema)
                if (resposta.status_code == 200):
                    st.success("Sistema " + sistema.upper() + " no Ar.")
                elif(resposta == 404):
                    st.warning("Url entidade não encontrado.")
                else:
                    st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")
if st.button("Verificação Geral.") :
    page_urls = scraping.pagina()
    st.header('Lista de entidades cadastradas:')
    st.markdown("Total de Entidades na nuvem: "+str(len(page_urls)))

    for entidade, url in page_urls.items():
        start = t.time()
        try:
            resposta = requests.get(str('http://' + url) + ':7474/' + 'esadmin')
            if (resposta.status_code == 200):
                st.success('http://' + url + ':7474/' + 'esadmin' + " ~ Ativa,  consulta feita em - " + str(round((t.time() - start),2)) + " segundos.")
            else:
                st.error('http://' + url + ':7474/' + 'esadmin' + " ~ Inativa,  consulta feita em - " + str(round((t.time() - start),2)) + " segundos.")
        except:
            start = t.time()
            resposta = requests.get(str('http://' + url) + ':8080/' + 'esadmin')
            if (resposta.status_code == 200):
                st.success("Entidade " + 'http://' + url + ':8080/' +'esadmin' + " ~ Ativa,  consulta feita em - " + str(round((t.time() - start),2)) + " segundos.")
            else:
                st.error("Entidade " + 'http://' + url + ':8080/' +'esadmin' + " ~ Inativa,  consulta feita em - " + str(round((t.time() - start),2)) + " segundos.")

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
        [-25.7498, -53.0534], popup="Prefeitura", tooltip="Dois Vizinhos", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.573069989004992, -51.07780581690882], popup="Prefeitura", tooltip="Inácio Martins", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.9863, -50.1959], popup="Prefeitura", tooltip="Antônio Olinto", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.1896, -50.8085], popup="Prefeitura\nFundo", tooltip="Guamiranga", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.4113, -50.5492], popup="Prefeitura", tooltip="Fernandes Pinheiros", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-24.950803145273827, -50.114852503388995], popup="Câmara", tooltip="Carambei", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.708780063474983, -52.916441581452716], popup="Prefeitura", tooltip="São Jorge D'Oeste", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.87649901729939, -48.57793803182175], popup="GuaraPrev", tooltip="Guaratuba",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.184630724854035, -49.312935989490356], popup="Câmara", tooltip="Rio Branco do Sul",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.308400787562828, -52.53645081738991], popup="Câmara", tooltip="Nova Laranjeiras",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.7182, -53.7672], popup="Fundo", tooltip="Planalto",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-23.594164466704818, -50.760430603712], popup="Câmara", tooltip="Nova Santa Barbara",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.573220969641085, -51.07583650076976], popup="Câmara", tooltip="Inácio Martins",icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-22.78106273417823, -51.2312464908427], popup="Prefeitura", tooltip="Alvorada do Sul", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-24.247088185940257, -49.705674574292246], popup="Câmara", tooltip="Jaguariaiva", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.614349027655123, -53.12813936099656], popup="Prefeitura", tooltip="Cruzeiro do Iguaçu", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-23.535456915206044, -52.58865267421556], popup="Prefeitura", tooltip="São Tomé", icon=folium.Icon(icon="cloud")).add_to(m)
    folium.Marker(
        [-25.4622, -50.6335], popup="Conder", tooltip="Irati", icon=folium.Icon(icon="cloud")).add_to(m)
#

    # folium.Marker(
    #     [-25.7086, -52.9190], popup="Prefeitura", tooltip="São Jorge D'Oeste", icon=folium.Icon(icon="cloud")).add_to(m)

    # Criando o mapa
    folium_static(m)
    # Salvando o mapa em html
    #if st.button("Salvar"):
    #m.save('mapa-nuvens-equiplano_19102021.html')
