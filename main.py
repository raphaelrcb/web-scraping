from bs4 import BeautifulSoup
import requests

search = input("O que você quer procurar?\n")
#search = "vox machina"

params = {"q": search}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
r = requests.get("https://www.bing.com/search", params=params, headers=headers)


soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

print(r.headers)
for item in links:
    item_text = item.find("h2").find("a").text
    item_href = item.find("h2").find("a").attrs["href"]

    if item_text and item_href:
        print("text: ", item_text)
        print("href: ", item_href)
        print("Descrição: ", item.find("a").parent.parent.find("p").text)
#        children = item.children
#        for child in children:
#            print("Child: ", child)
        children = item.find("h2")
        print("Irmão anterior = ", children.previous_sibling)
        print("\n")

f = open("arquivo.html", "wb")

f.write(r.content)

f.close()