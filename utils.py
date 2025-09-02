import requests
from bs4 import BeautifulSoup as BS


async def ottieniSanti(full: bool):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get("https://www.santodelgiorno.it/",
                     headers = headers)

    url = "https://www.santodelgiorno.it/"
    result = {'santodelgiorno': {}}
    soup = BS(r.text, 'html.parser')

    if not full:
        sdg_div = soup.find("div", class_="SantoDiOggi")
        if sdg_div:
            sdg_name_div = sdg_div.find("div", class_="NomeSantoDiOggi")
            if sdg_name_div:
                sdg_name = sdg_name_div.text.strip()
                sdg_img_tag = soup.find("img", alt=sdg_name)
                if sdg_img_tag and sdg_img_tag.get('src'):
                    sdg_img = url + sdg_img_tag['src'].replace("small", "big")
                    result['santodelgiorno'] = {'name': sdg_name, 'img': sdg_img}
    else:
        sdg_div = soup.find("div", class_="SantoDiOggi")
        if sdg_div:
            sdg_name_div = sdg_div.find("div", class_="NomeSantoDiOggi")
            if sdg_name_div:
                sdg_name = sdg_name_div.text.strip()
                sdg_img_tag = soup.find("img", alt=sdg_name)
                if sdg_img_tag and sdg_img_tag.get('src'):
                    sdg_img = url + sdg_img_tag['src']
                    result['santodelgiorno'][sdg_name] = {'img': sdg_img}

        for altri_santi_div in soup.find_all("div", class_="giornocarosel"):
            try:
                santi = altri_santi_div.find_all("div", class_="ElencoSanto")
                for santo in santi:
                    nome_santo = santo.find("a")
                    img_tag = altri_santi_div.find("img", class_="lazy")
                    if nome_santo and img_tag and img_tag.get('data-src'):
                        nome_santo = nome_santo.text.strip()
                        img_url = url + img_tag['data-src']
                        result['santodelgiorno'][nome_santo] = {'img': img_url}
            except AttributeError:
                pass

    return result
