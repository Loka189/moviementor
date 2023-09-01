import requests

url = "https://api.themoviedb.org/3/movie/19995/keywords"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMmQ1MmEzOGY3N2IwMzljODM5NGEwOWI3ZTFiNjdkMyIsInN1YiI6IjY0ZWZhMjRlZjAzMTc0MDEzODNjMzE5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9oLIDLZwJKOZPKpgq0RaXmRbgkFvm97gDiX-aN9YxTk"
}

response = requests.get(url, headers=headers)

mainJSON=response.json()
keywords=mainJSON['keywords']
keywords1=[]
keywords1.append(keywords[i]['name'] for i in range(len(keywords)))
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
url3='https://api.themoviedb.org/3/search/movie?query=Oppenheimerxxx&api_key=32d52a38f77b039c8394a09b7e1b67d3'

response3=requests.get(url3)
if response3.status_code==200:
    json=response3.json()
    results=json['results']
    if len(results)!=0:
        print(json)
    else:
        print("no movie found")
else:
    print("check your internet connection")