import sys
sys.path.insert(0, './api')
sys.path.insert(1, './constants')
sys.path.insert(2, './utils')

from api import Api
from requestconfig import HLTVRequestConfig, DEFAULT_CONFIG
from playerstats import PlayerStats

class Player(Api):
  player: str
  
  def __init__(self, player: str):
    self.player = player
  
  def get_stats(self, 
                config: HLTVRequestConfig | None = DEFAULT_CONFIG) -> PlayerStats:
    super.get()