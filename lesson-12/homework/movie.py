import requests

genre = input("Enter the genre of the movie: ")

API_key = "f337b6ad4b3baded747f68943ef5ce67"

url = "https://api.themoviedb.org/3/genre/movie/list"

parameters = {"api_key": API_key}

response = requests.get(url, params=parameters)

response_dict = dict(response.json())
# print(response_dict)

for i in response_dict['genres']:
    if i['name'] == genre:
        genre_id = i['id']
        break


an_url = "https://api.themoviedb.org/3/discover/movie"

an_param = {"api_key": API_key, "with_genres": genre_id}

print([requests.get(an_url, params=an_param).json()['results'][i]['title'] for i in range(0, len(requests.get(an_url, params=an_param).json()['results']))])