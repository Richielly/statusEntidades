from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://sites.google.com/view/entidade/p%C3%A1gina-inicial?authuser=0'
urls=[]
entidades=[]
def pagina():
    global url
    response = urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    all_links = soup.find_all("a")
    for link in all_links:
        linha = link.get("href")
        url = str(linha).split("%3A%2F%2F")
        try:
            urls.append((url[1].split("%3A7474%2F")[0]))
        except:
            "Não encontado"
    for item in soup.select("small"):
        entidades.append(item.get_text())

    entidade_url = dict(zip(entidades, urls))
    return entidade_url
