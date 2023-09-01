# import requests

# url = "https://api.themoviedb.org/3/movie/19995/keywords"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMmQ1MmEzOGY3N2IwMzljODM5NGEwOWI3ZTFiNjdkMyIsInN1YiI6IjY0ZWZhMjRlZjAzMTc0MDEzODNjMzE5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9oLIDLZwJKOZPKpgq0RaXmRbgkFvm97gDiX-aN9YxTk"
# }

# response = requests.get(url, headers=headers)

# mainJSON=response.json()
# keywords=mainJSON['keywords']
# keywords1=[]
# keywords1.append(keywords[i]['name'] for i in range(len(keywords)))
# keywords1=[i['name'] for i in keywords]
#print(keywords1)

#print(response.text)


# url2 = "https://api.themoviedb.org/3/movie/199956969/credits?language=en-US"



# response2 = requests.get(url2, headers=headers)
# if response2.status_code==200:
#     JSONforCredits=response2.json()
#     allcast=JSONforCredits['cast']
#     allcrew=JSONforCredits['crew']
#     top4cast=[i['name'] for i in allcast[:4]]
#     director=[i['name'] for i in allcrew if i['job']=='Director']

#     print(director)
# else:
#     print("error")


# error handling
# url3='https://api.themoviedb.org/3/search/movie?query=Oppenheimerxxx&api_key=32d52a38f77b039c8394a09b7e1b67d3'

# response3=requests.get(url3)
# if response3.status_code==200:
#     json=response3.json()
#     results=json['results']
#     if len(results)!=0:
#         print(json)
#     else:
#         print("no movie found")
# else:
#     print("check your internet connection")

#image getting
import numpy as np
import pandas as pd
import requests as req
movieList=['Avatar','The Avengers','Titanic','Jurassic World','The Lion King']
movieData=pd.DataFrame({'title':movieList})

def fetchImage(name):
    url='https://api.themoviedb.org/3/search/movie?query='+name+'&api_key=32d52a38f77b039c8394a09b7e1b67d3'
    response=req.get(url)
    if response.status_code==200:
        json=response.json()
        results=json['results']
        poster_path=results[0]['poster_path']
        imageurl='https://image.tmdb.org/t/p/w342'+poster_path
        return imageurl
    else:
        return "error"
    

movieData['imageurl']=movieData['title'].apply(fetchImage)
