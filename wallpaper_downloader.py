import requests
import urllib.request
import shutil

from bs4 import BeautifulSoup

base_url = "http://earthview.withgoogle.com"
current = "/tiris-zemmour-mauritania-14074"
file_name = "wallpapers"

for i in range(1,2000):
    response = requests.get(base_url+current)
    page_html = response.text
    soup = BeautifulSoup(page_html, "lxml")

    download = soup.findAll('a', {'class': 'menu__download icon-button'})[0]['href']
    next = soup.findAll('a', {'class': 'pagination__link pagination__link--next'})[0]['href']
    print(download + " " + next)


    with urllib.request.urlopen(base_url+download) as page, open(file_name+current+".jpg", 'wb') as out_file:
        shutil.copyfileobj(page, out_file)

    current = next;

