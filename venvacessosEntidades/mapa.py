from streamlit_folium import folium_static
import folium

m = folium.Map(location=[-24.3681, -51.7985], zoom_start=7)  #Parana  Lat: -24.3681 Lon: -51.7985

class Mapa():

    def make_map(self, lat, long, popup_msg, tooltip_msg, icon_name):
        global m
        folium.Marker([lat, long], popup=str(popup_msg), tooltip=str(tooltip_msg),icon=folium.Icon(icon=str(icon_name))).add_to(m)

        return m

    def cordenada_file(self, file):
        make = Mapa()
        for linha in file:
            make.make_map(linha[0],linha[1],linha[2],linha[3],linha[4])

    def build_map(self, make_map):
        global m
         # Criando o mapa
        mapa = folium_static(m)
        return mapa

    def html_map(self, nome):
        global m
        # Salvando o mapa em html
        mapa_html = m.save(nome +'.html')

        return mapa_html
