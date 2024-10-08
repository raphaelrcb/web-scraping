from bs4 import BeautifulSoup
import requests
import json
import re
from PIL import Image
from io import BytesIO

from main import item_href

search = input("Procure por: ")
#search = "vox machina"
params = {"q": search}
r = requests.get("http://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

links = soup.findAll("a", {"class": "iusc"})
#print(links)
for item in links:
    print("\n")
    try:
        m = json.loads(item["m"])
        media_url = m["murl"]
        media_title = m["murl"].split("/")[-1]
        media_title = re.split(r'[/?&.]', media_title)[0]
        print(item)
        print(media_url)
        print(media_title)
        img_obj = requests.get(media_url)
        img = Image.open(BytesIO(img_obj.content))
        print(img.format)
        img.save("./scraped_images/" + media_title + "." + img.format.lower())
    except FileNotFoundError:
        print("Erro em acessar url da imagem")
    except IOError:
        print("Um erro ocorreu ao abrir o arquivo")


