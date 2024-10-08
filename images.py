from bs4 import BeautifulSoup
import requests
import json
import re
from PIL import Image
from io import BytesIO
import os

def ImageSearch():

    search = input("Procure por: ")
    #search = "vox machina"
    if search == "":
        quit()
    params = {"q": search}
    r = requests.get("http://www.bing.com/images/search", params=params)

    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.findAll("a", {"class": "iusc"})
    for item in links:
        try:
            m = json.loads(item["m"])
            media_url = m["murl"]
            media_title = m["murl"].split("/")[-1]
            media_title = re.split(r'[/?&.]', media_title)[0]
            print(media_url)
            print(media_title)
            img_obj = requests.get(media_url)
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + media_title + "." + img.format.lower())
        except FileNotFoundError:
            print("Erro em acessar url da imagem")
        except IOError:
            print("Um erro ocorreu ao abrir o arquivo")
        except:
            print("Erro nao identificado")
    ImageSearch()

ImageSearch()
