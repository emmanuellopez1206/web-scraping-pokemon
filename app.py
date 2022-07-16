import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://pokemondb.net/pokedex/all"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
rows = soup.find("table", attrs={"id":"pokedex"}).find("tbody").find_all("tr")

names = []
types = []
total = []
hp = []
attack = []
defense = []
sp_attack = []
sp_defense = []
speed = []

for row in rows:
    names.append(row.find_all("td")[1].get_text())
    types.append(row.find_all("td")[2].get_text())
    total.append(row.find_all("td")[3].get_text())
    hp.append(row.find_all("td")[4].get_text())
    attack.append(row.find_all("td")[5].get_text())
    defense.append(row.find_all("td")[6].get_text())
    sp_attack.append(row.find_all("td")[7].get_text())
    sp_defense.append(row.find_all("td")[8].get_text())
    speed.append(row.find_all("td")[9].get_text())

df = pd.DataFrame({"nombres":names, "types":types, "total":total, "hp":hp, "attack":attack, "defense":defense, "sp_attack":sp_attack, "sp_defense":sp_defense, "speeds":speed})

df.to_csv("Pokemones.csv")
    
