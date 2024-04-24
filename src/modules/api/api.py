import requests

class Api:
  def __init__(self):
    self.session = requests.Session()
  
  def get(self, url: str) -> requests.Response:
    return self.session.get(url)
  
  def post(self, url: str, content: any) -> requests.Response:
    return self.session.post(url, data=content)