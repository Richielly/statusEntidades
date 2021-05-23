from urllib.request import urlopen
from bs4 import BeautifulSoup
urls=[]
entidades=[]
urls2=[]
entidades2=[]
urls3=[]
entidades3=[]
def pagina(url = 'https://sites.google.com/view/entidade/p%C3%A1gina-inicial?authuser=0'):
    #url = 'https://sites.google.com/view/entidade/p%C3%A1gina-inicial?authuser=0'
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


def pesquisa_prefeituras(url = 'https://sites.google.com/view/entidade/prefeituras?authuser=0'):
    response = urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    all_links = soup.find_all("a")

    for link in all_links:
        entidade = link.get("aria-label")
        linha = link.get("href")
        url = str(linha).split("%3A%2F%2F")
        try:
            if entidade != None:
                entidades.append(entidade)
            urls.append(url[1].split('&sa')[0].replace('%2F','/').replace('%3A',':'))
        except:
            "Não encontado"
    entidade_url = dict(zip(entidades, urls))
    return entidade_url

def pesquisa_camaras(url = 'https://sites.google.com/view/entidade/camaras?authuser=0'):
    response = urlopen(url)
    soup2 = BeautifulSoup(response, "html.parser")
    all_links2 = soup2.find_all("a")

    for link2 in all_links2:
        entidade2 = link2.get("aria-label")
        linha2 = link2.get("href")
        url2 = str(linha2).split("%3A%2F%2F")
        try:
            if entidade2 != None:
                entidades2.append(entidade2)
            urls2.append(url2[1].split('&sa')[0].replace('%2F','/').replace('%3A',':'))
        except:
            "Não encontado"
    entidade_url2 = dict(zip(entidades2, urls2))
    return entidade_url2

def pesquisa_outras(url = 'https://sites.google.com/view/entidade/outras?authuser=0'):
    response = urlopen(url)
    soup3 = BeautifulSoup(response, "html.parser")
    all_links3 = soup3.find_all("a")

    for link3 in all_links3:
        entidade3 = link3.get("aria-label")
        linha3 = link3.get("href")
        url3 = str(linha3).split("%3A%2F%2F")
        try:
            if entidade3 != None:
                entidades3.append(entidade3)
            urls3.append(url3[1].split('&sa')[0].replace('%2F','/').replace('%3A',':'))
        except:
            "Não encontado"
    entidade_url3 = dict(zip(entidades3, urls3))
    return entidade_url3
