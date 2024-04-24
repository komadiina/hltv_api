from filters import Filters

class HLTVRequestConfig:
  match_type: str
  date_constraint: str
  top_ranks: str
  maps: str
  
  def __init__(self, 
               match_type: str | None, 
               date_constraint: str | None, 
               top_ranks: str | None, 
               maps: str | list[str]):
    self.match_type = match_type
    self.date_constraint = date_constraint
    self.top_ranks = top_ranks
    self.maps = maps
    

DEFAULT_CONFIG = HLTVRequestConfig(None, Filters.DATE_ALL, None, None)