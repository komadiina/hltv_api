import requests
import json
import time
from bs4 import BeautifulSoup as bs

playernames_file = "./src/modules/constants/playernames.json"
search_url = "https://www.hltv.org/search"
delay = 3.0

mimic_useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
player_result = '<td class="table-header">Player</td>'

def add_filter(playername: str) -> str:
  return "?query=" + playername

def load_playernames(filepath: str) -> list[str]:
  with open(filepath, 'rt') as f:
    return json.load(f)

playernames = load_playernames(playernames_file)
playerids = {}

session = requests.Session()
for playername in playernames:
  print("Searching for player: " + playername)
  
  response = session.get(url=f"{search_url}{add_filter(playername)}", 
                         headers={ 'User-Agent' : mimic_useragent })
   
  if response.text.find(player_result) != -1:
    print(f"[o] Player found: {playername}")
    
    soup = bs(response.text, 'html.parser')
    a_tag = soup.select_one(selector='div.colCon div.contentCol div.search table.table tr td a')
  
    if a_tag is not None:
      href = a_tag.get('href')[1:]
      id = href.split('/')[1]
      
      playerids[playername] = id
  else:
    print("[x] Player not found.")
  
  time.sleep(delay)
  
with open('./src/modules/constants/playerids.json', 'wt') as f:
  json.dump(playerids, f, indent=4)