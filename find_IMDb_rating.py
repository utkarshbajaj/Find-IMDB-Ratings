from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


def get_online_platforms(move_name):
    SEARCH_URL = f'https://www.imdb.com/find?q={move_name}'

    session = requests.session()
    response = session.get(SEARCH_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    first_movie_url = soup.find('td', attrs={'class': 'result_text'}).find('a').get('href')
    # with open('test.html', 'w+') as f: f.write(soup.__str__())
    movie_id = first_movie_url.split('/')[-2]

    PLATFORMS_URL = f"https://www.imdb.com/watch/_ajax/box/{movie_id}"

    response = session.get(PLATFORMS_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_platforms = [div.text for div in soup.find_all('div', attrs={'class': 'watchoption-modal__provider'})]

    return all_platforms if len(all_platforms) > 0 else ["None"]


def find_movie(directory_path):
    # Setting up session
    s = requests.session()

    # List contaiting all the films for which data has to be scraped from IMDB
    films = []

    # Lists contaiting web scraped data
    names = []
    ratings = []
    genres = []
    platforms = []

    # Define path where your films are present
    # For eg: "/Users/utkarsh/Desktop/films"
    path = directory_path

    # Films with extensions
    filmswe = os.listdir(path)

    for film in filmswe:
        # Append into my films list (without extensions)
        films.append(os.path.splitext(film)[0])
        # print(os.path.splitext(film)[0])

    for line in films:
        # x = line.split(", ")
        title = line.lower()
        # Convert all the underscores to whitespaces
        title = title.replace("_", " ")
        # release = x[1]
        query = "+".join(title.split(" "))
        URL = "https://www.imdb.com/search/title/?title=" + query

        # print(release)
        try:
            response = s.get(URL)

            # getting contect from IMDB Website
            content = response.content

            # print(response.status_code)

            soup = BeautifulSoup(content, features="html.parser")
            # searching all films containers found
            containers = soup.find_all("div", class_="lister-item-content")
            for result in containers:
                name1 = result.h3.a.text
                name = result.h3.a.text.lower()

                # Uncomment below lines if you want year specific as well, define year variable before this
                # year = result.h3.find(
                # "span", class_="lister-item-year text-muted unbold"
                # ).text.lower()

                # if film found (searching using name)
                if title in name:
                    # scraping rating
                    rating = result.find(
                        "div", class_="inline-block ratings-imdb-rating")["data-value"]
                    # scraping genre
                    genre = result.p.find("span", class_="genre")
                    genre = genre.contents[0].strip()

                    # appending name, rating and genre to individual lists
                    names.append(name1)
                    ratings.append(rating)
                    genres.append(genre)
                    platforms.append(", ".join(get_online_platforms(name1)))

        except Exception:
            print("Try again with valid combination of tile and release year")

    # storing in pandas dataframe
    df = pd.DataFrame({'Film Name': names, 'Rating': ratings, 'Genre': genres,
                       "Platforms": platforms})
    df = df.sort_values("Rating", ascending=False)

    # making csv using pandas
    df.to_csv('film_ratings.csv', index=False, encoding='utf-8')

    return (names, ratings, genres, platforms)
