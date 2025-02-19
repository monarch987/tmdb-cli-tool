import requests
from creds import api_key

def now_playing_movies():

    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1"

    headers = {
    "accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()
        movies = data.get('results',[])
  
        for movie in movies:
            print(movie['title'])           

    elif response.status_code == 401:
        
        print("Invalid Api Key") 

    elif response.status_code == 429:
        
        print("Api limit exceeded") 
    
    else:
        print(response.status_code)

def popular_movies():

    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"

    headers = {
    "accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()
        movies = data.get('results',[])
  
        for movie in movies:
            print(movie['title'])           
    
    elif response.status_code == 401:
        
        print("Invalid Api Key") 

    elif response.status_code == 429:
        
        print("Api limit exceeded") 
    
    else:
        print(response.status_code) 


def top_movies():

    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1"

    headers = {
    "accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()
        movies = data.get('results',[])
  
        for movie in movies:
            print(movie['title'])           
   
    elif response.status_code == 401:
        
        print("Invalid Api Key") 

    elif response.status_code == 429:
        
        print("Api limit exceeded") 
    
    else:
        print(response.status_code)


def upcoming_movies():

    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=1"

    headers = {
    "accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()
        movies = data.get('results',[])
  
        for movie in movies:
            print(movie['title'])    
    
    elif response.status_code == 401:
        
        print("Invalid Api Key") 

    elif response.status_code == 429:
        
        print("Api limit exceeded") 
    
    else:
        print(response.status_code)


def display_movies():

    print(f" tmdb-app --type 'playing'\n tmdb-app --type 'popular'\n tmdb-app --type 'top'\n tmdb-app --type 'upcoming'")
    
    print('\n')
    selected = input(str("Enter the type from above: "))
    print('\n')

    if selected.lower() == 'playing':

        now_playing_movies()

    elif selected.lower() == 'popular':

        popular_movies()

    elif selected.lower() == 'top':

        top_movies()


    elif selected.lower() == 'upcoming':

        upcoming_movies()


if __name__ == '__main__':
    
    display_movies()