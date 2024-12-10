import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def get_page_links(url):
  if url.endswith('/'):
    url = url[:-1]
  response = requests.get(url, headers = headers)
  soup = BeautifulSoup(response.text, 'html.parser')
  raw = [link['href'] for link in soup.find_all('a', href = True)]
  links = []
  for link in raw:
    if link.startswith('/'):
      link = url+link
    links.append(link)
  links = list(set(links))
  
  return links
