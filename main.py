import numpy as np
import pandas as pd

movies=pd.read_csv('tmdb_5000_movies.csv')
credits=pd.read_csv('tmdb_5000_credits.csv')

movies=movies.merge(credits,on='title')
movies=movies[['movie_id','title','keywords','genres','overview','cast','crew']]

movies.dropna(inplace=True)


import ast
movies['keywords']=movies['keywords'].apply(lambda x:ast.literal_eval(x))
movies['genres']=movies['genres'].apply(lambda x:ast.literal_eval(x))
movies['cast']=movies['cast'].apply(lambda x:ast.literal_eval(x))
movies['crew']=movies['crew'].apply(lambda x:ast.literal_eval(x))


def convert(List):
    L=[]
    for i in List:
        L.append(i['name'])
        
    return L


movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)


def castCon(list1):
    c=0
    L=[]
    for i in list1:
        if c!=4:
            L.append(i['name'])
            c=c+1
        else:
            break
            
    return L


movies['cast']=movies['cast'].apply(castCon)
print(movies['cast'])