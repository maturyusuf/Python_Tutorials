from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('https://www.rottentomatoes.com').text
soup = BeautifulSoup(source,'lxml')

header_texts = soup.find_all('div',class_ = 'dynamic-poster-list__header-container--hide-h3')
headers = []
for i in header_texts:
    header_name = i.h2.text
    headers.append(header_name)
pop_in_theaters =soup.find('div',class_ = 'dynamic-poster-list__header-container')
headers.insert(1,pop_in_theaters.h2.text)
#print(headers)

movie_text = soup.find_all('span',class_ = 'p--small')
movies = []
for i in movie_text:
    movies.append(i.text)
 
#New Upcoming Movies
new_upcoming_movies = movies[0:13]


#popular_in_theaters
popular_in_theaters = movies[13:23]

#celebrating 10th anniversaries in 2021
celeb_ann = movies[23:43]


#BEST SERIES ON NETFLIX
best_series_netflix = movies[43:54]

#award winners
award_wins = movies[54:63]

#PAST JANUARY BOX OFFICE WINNERS
jan_bow = movies[63:81]

#NEWLY CERTIFIED FRESH CLASSICS
fresh_classics =  movies[81:99]

#writing to excel
df = pd.DataFrame([new_upcoming_movies,popular_in_theaters,celeb_ann,best_series_netflix,award_wins,jan_bow,fresh_classics])
df.head()
new_df = df.T
rotten_tomatoes = new_df.to_excel('Rotten_Tomatoes.xlsx',index = False,header=headers)

