import re

from bs4 import BeautifulSoup
from urllib import request

movies_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
shows_url = "https://www.imdb.com/chart/toptv"


def get_ratings(url_string: str):
    req = request.urlopen(url_string).read()

    soup = BeautifulSoup(req, 'html.parser')

    results = []
    table = soup.find(attrs={"data-caller-name": re.compile("^chart-*")})
    entries = table.find_all('tr')
    for entry in entries:
        title_col = entry.find(class_='titleColumn')
        rating_col = entry.find(class_='imdbRating')
        if title_col and rating_col:
            title = title_col.a.get_text()
            rating = rating_col.strong.get_text()
            item = {"title": title, "rating": rating}
            results.append(item)

    print(results)


get_ratings(movies_url)
get_ratings(shows_url)
