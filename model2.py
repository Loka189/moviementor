import numpy as np
import pandas as pd 
import requests as req
import json
# Importing the dataset
movies=pd.read_csv('tmdb5kPrePData.csv')

with open('confidential.json') as f:
    data = json.load(f)
    ApiKey=data['api_key']
    Headers=data['headers']
class ImageFetcher:
    def __init__(self):
        self.movieList=[]
        self.movieData=pd.DataFrame({'title':self.movieList})
    def fetchImage1(self,name):
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
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000)

vectorized_array = cv.fit_transform(movies['tags']).toarray()
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectorized_array)

titleList = movies['title'].tolist()



def recommedate(movie):#movie is a string which is coming from the user

    # If the movie user entered is in the list of movies we have then we will not have to do all the api calls and all that stuff we will just have to find the index of that movie and then find the similarity of that movie with all the other movies and then sort them and then return the top 5 movies
    if movie in titleList:
       movies=pd.read_csv('tmdb5kPrePData.csv')
       mainlist=[]
       movie_index = movies[movies['title'] == movie].index[0]
       distances = similarity[movie_index]
       similar_movies_with_scores = list(enumerate(distances))
       top_similar_movies = sorted(similar_movies_with_scores, reverse=True, key=lambda x: x[1])[1:6]
    
    
       for i in top_similar_movies:
          mainlist.append(movies.iloc[i[0]].title)

        
       #return mainlist
       movieData=pd.DataFrame({'title':mainlist})
              
       object1=ImageFetcher()
       movieData['imageurl']=movieData['title'].apply(object1.fetchImage1)
       # Now return the mmoviedata as Dictionary
       return movieData.to_dict('records')
       
    else:
        # so we are in this else block means that the movie user entered is not in the list of movies we have so we will have to do all the api calls and all that stuff

        # first we will have to find the movie id of the movie user entered by movie name using the api call
        movies=pd.read_csv('tmdb5kPrePData.csv')
        base_url = "https://api.themoviedb.org/3/search/movie"
        api_key = ApiKey
        query = movie

        url = f"{base_url}?query={query}&api_key={api_key}"
        response=req.get(url)
        if response.status_code==200:
            mainJSON=response.json()
            resultList=mainJSON['results']
            if len(resultList)!=0:
                
                movie_id=resultList[0]['id']
                # here we got the movie id but we can also get the title and overview of the movie but not the genres , keywords , cast and crew
                title=resultList[0]['title']
                overview=[resultList[0]['overview']]
                genres=[]
                keywords=[]
                cast=[]
                crew=[]

                # Lets get the genres of the movie
                base_url_for_genres="https://api.themoviedb.org/3/movie/"
                main_url_for_genres=f"{base_url_for_genres}{movie_id}?api_key={api_key}" 
                response_for_genres=req.get(main_url_for_genres) 
                if response_for_genres.status_code==200:
                    json_for_genres=response_for_genres.json()
                    gen=json_for_genres['genres']
                    for i in gen:
                        genres.append(i['name'])
                # we got the genres now lets get the keywords of the movie
                

                base_url_for_keywords="https://api.themoviedb.org/3/movie/" 
                main_url_for_keywords=f"{base_url_for_keywords}{movie_id}/keywords" 
                headers = Headers
                response_for_keywords = req.get(main_url_for_keywords, headers=headers)
                if response_for_keywords.status_code==200:
                    jsonfk=response_for_keywords.json()
                    keyWL=jsonfk['keywords']
                    keywords=[i['name'] for i in keyWL]
                    
                base_url_for_credits="https://api.themoviedb.org/3/movie/"
                main_url_for_credits=f"{base_url_for_credits}{movie_id}/credits?language=en-US"
                headers2 = Headers
                resfcast=req.get(main_url_for_credits,headers=headers2)
                if resfcast.status_code==200:
                    json=resfcast.json()
                    allcast=json['cast']
                    allcrew=json['crew']
                    cast=[i['name'] for i in allcast[:4]]
                    crew=[i['name'] for i in allcrew if i['job']=='Director']

                # Got all columns first i have to create that god damn tag
                remSpace=(lambda x:[i.replace(" ","") for i in x])
                cast=remSpace(cast)
                crew=remSpace(crew)
                genres=remSpace(genres)
                keywords=remSpace(keywords)
                tags=overview+genres+keywords+cast+crew
                tags=' '.join(tags).lower()

                import nltk
                from nltk.corpus import stopwords
                from nltk.tokenize import word_tokenize
                from nltk.stem.porter import PorterStemmer
                
                ps=PorterStemmer()
                stop_words=set(stopwords.words('english'))
                
                wordTokens=word_tokenize(tags)
                filterWords=[w for w in wordTokens if not w.lower() in stop_words]
                remov_d_text=[ps.stem(w) for w in filterWords]
                filterText=' '.join(remov_d_text)

                # now have to create new row and add to existing data hen process
                newRow={'movie_id':movie_id,'title':title,'tags':filterText}
                newMovieData=pd.Series(newRow)
                movies.loc[len(movies)]=newMovieData
                movies=movies.drop_duplicates()
                movies.to_csv('tmdb5kPrePData.csv',index=False)
                vectorized_array = cv.fit_transform(movies['tags']).toarray()
                simi=cosine_similarity(vectorized_array)
                mainList=[]
                movieIn=movies[movies['title'] == movie].index[0]
                dist=simi[movieIn]
                similar_movies_with_scores = list(enumerate(dist))
                top_similar_movies = sorted(similar_movies_with_scores, reverse=True, key=lambda x: x[1])[1:6]
            
                for i in top_similar_movies:
                    mainList.append(movies.iloc[i[0]].title)

                #return mainList
                movieData=pd.DataFrame({'title':mainList})
                # def fetchImage(name):
                #     url='https://api.themoviedb.org/3/search/movie?query='+name+'&api_key=32d52a38f77b039c8394a09b7e1b67d3'
                #     response=req.get(url)
                #     if response.status_code==200:
                #         json=response.json()
                #         results=json['results']
                #         poster_path=results[0]['poster_path']
                #         imageurl='https://image.tmdb.org/t/p/w342'+poster_path
                #         return imageurl
                object1=ImageFetcher()
                movieData['imageurl']=movieData['title'].apply(object1.fetchImage1)
                return movieData.to_dict('records')
            else:
                return "Movie not found"
        else:
            return "Check your internet connection"


x=recommedate('Oppenheimer')
print(x)


