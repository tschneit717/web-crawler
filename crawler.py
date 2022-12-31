from bs4 import BeautifulSoup
from urllib import request

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


def get_movies(url_string: str):
    req = request.urlopen(url_string).read()

    soup = BeautifulSoup(req, 'html.parser')

    movies = []
    table = soup.find(attrs={"data-caller-name": "chart-top250movie"})
    entries = table.find_all('tr')
    for entry in entries:
        title_col = entry.find(class_='titleColumn')
        rating_col = entry.find(class_='imdbRating')
        if title_col and rating_col:
            title = title_col.a.get_text()
            rating = rating_col.strong.get_text()
            movie = {"title": title, "rating": rating}
            movies.append(movie)

    print(movies)


get_movies(url)
