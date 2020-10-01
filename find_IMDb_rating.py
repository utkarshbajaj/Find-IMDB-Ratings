from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import os

# Setting up session
s = requests.session()

# List contaiting all the films for which data has to be scraped from IMDB
films = []

# Lists contaiting web scraped data
names = []
ratings = []
genres = []

# Define path where your films are present 
# For eg: "/Users/utkarsh/Desktop/films"
path = input("Enter the path where your films are: ")

# Taking the Genre from user 
filter = input('Do you want a specific genre?(y/n)?')
if(filter.lower() == 'y'):
    genre_user = input("Enter the Genre: ")


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
    print(URL)
    # print(release)
    try:
        response = s.get(URL)

        #getting contect from IMDB Website
        content = response.content

        # print(response.status_code)

        soup = BeautifulSoup(response.content, features="html.parser")
        #searching all films containers found
        containers = soup.find_all("div", class_="lister-item-content")
        for result in containers:
            name1 = result.h3.a.text
            name = result.h3.a.text.lower()


            # Extracting the genere
            genre = result.p.find("span", class_="genre")
           

            
            
            

            # Uncomment below lines if you want year specific as well, define year variable before this 
            # year = result.h3.find(
            # "span", class_="lister-item-year text-muted unbold"
            # ).text.lower() 

            #if film found (searching using name)
            
           
           
       
                
            if title in name:
                if filter == 'y':
                    genre_list = []
                    genre_list = list(genre.stripped_strings)[0].split(',')
                    if genre_user in genre_list:
                        #scraping rating
                        rating = result.find("div",class_="inline-block ratings-imdb-rating")["data-value"]
                        #scraping genre
                        # genre = result.p.find("span", class_="genre")
                        genre = genre.contents[0]

                        #appending name, rating and genre to individual lists
                        names.append(name1)
                        ratings.append(rating)
                        genres.append(genre)
                else:
                    #scraping rating
                    rating = result.find("div",class_="inline-block ratings-imdb-rating")["data-value"]
                    #scraping genre
                    # genre = result.p.find("span", class_="genre")
                    genre = genre.contents[0]
                        
                    #appending name, rating and genre to individual lists
                    names.append(name1)
                    ratings.append(rating)
                    genres.append(genre)
                


    except Exception:
        print("Try again with valid combination of tile and release year")

#storing in pandas dataframe
df = pd.DataFrame({'Film Name':names,'Rating':ratings,'Genre':genres})

#making csv using pandas
df.to_csv('film_ratings.csv', index=False, encoding='utf-8')
