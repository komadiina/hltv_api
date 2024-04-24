class Filters:
  # optional filters
  __MATCH_FILTER: str = "matchType"
  __DATE_NOT_BEFORE: str = "startDate"
  __DATE_NOT_AFTER: str = "endDate"
  __RANKING_FILTER: str = "rankingFilter"
  __MAP_FILTER: str = "maps" # stackable / multi-instance
  
  # match filter constants
  MAJORS: str = "Majors"
  BIG_EVENTS: str = "BigEvents"
  LANS: str = "Lan"
  ONLINE: str = "Online"
  
  # time filter constants
  LAST_MONTH: str = "" # TODO
  LAST_3_MONTHS: str = "" # TODO
  LAST_6_MONTHS: str = "" # TODO
  LAST_12_MONTHS: str = "" # TODO
  LAST_YEAR: str = LAST_12_MONTHS
  DATE_ALL: str = "all"
  
  # player ranking filter constants
  TOP_5: str = "Top5"
  TOP_10: str = "Top10" 
  TOP_20: str = "Top20"
  TOP_30: str = "Top30"
  TOP_50: str = "Top50"
  
  # map filter constants
  ANCIENT: str = "de_ancient"
  ANUBIS: str = "de_anubis"
  INFERNO: str = "de_inferno"
  MIRAGE: str = "de_mirage"
  NUKE: str = "de_nuke"
  OVERPASS: str = "de_overpass"
  VERTIGO: str = "de_vertigo"
  CACHE: str = "de_cache"
  COBBLESTONE: str = "de_cobblestone"
  DUST2: str = "de_dust2"
  SEASON: str = "de_season"
  TRAIN: str = "de_train"
  TUSCAN: str = "de_tuscan"
  
