import requests
import json
import sys
import time
from bs4 import BeautifulSoup as bs
import signal

playernames_file = "./src/modules/constants/playernames.json"
search_url = "https://www.hltv.org/search"
delay = 6.0
ratelimit_hitcount = 1

mimic_useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
player_result = '<td class="table-header">Player</td>'
jsonfile_path = './src/modules/constants/playerids.json'
last_playername_path = './src/modules/constants/last_playername.json'

def add_filter(playername: str) -> str:
  return "?query=" + playername

def load_playernames(filepath: str) -> list[str]:
  with open(filepath, 'rt') as f:
    return json.load(f)

# get last_player playername
def get_last_player_name():
  dct = dict()
  with open(last_playername_path, 'rt') as f:
    dct = json.load(f)
    
  print(dct)
  return dct["last_player"]
  
playernames = load_playernames(playernames_file)
playerids = {}
last_player = get_last_player_name()
last_player_idx = playernames.index(last_player) + 1

if last_player_idx == None:
  last_player_idx = 0

def save_ids():
  # combine previous list
  previous: dict = {}
  with open(jsonfile_path, 'rt') as f:
    previous = json.load(f)
  
  playerids.update(previous)
  
  with open(jsonfile_path, 'wt') as f:
    json.dump(playerids, f, indent=4)
  
  temp_dict = {"last_player": last_player}
  with open(last_playername_path, 'wt') as f:
    json.dump(temp_dict, f, indent=4)

# register SIGINT handler
def signal_saveids(signal, frame):
  save_ids()
    
  print(f"Saved {len(playerids)} player ID's. Exiting...")
  sys.exit(0x00FF)

signal.signal(signal.SIGINT, signal_saveids)

session = requests.Session()
# for playername in playernames:
print(f"Beginning search from player: {last_player}, list_index: {last_player_idx}")

for i in range(last_player_idx, len(playernames)):
  playername = playernames[i]
  
  print("Searching for player: " + playername)
  try: 
    response = session.get(url=f"{search_url}{add_filter(playername)}", 
                         headers={ 'User-Agent' : mimic_useragent })
  except ConnectionError:
    save_ids()
    sys.exit(0xff)
  
  # rate-limited by cloudflare
  if (response.status_code == 105 or response.status_code == 429):
    time.sleep(ratelimit_hitcount * 60 * 2)
    ratelimit_hitcount += 1
    continue
   
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
  
  last_player = playername
  time.sleep(delay)
