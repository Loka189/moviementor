import numpy as np
import pandas as pd 
import warnings
warnings.filterwarnings("ignore")

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

def convertCrew(list2):
    L=[]
    for i in list2:
        if i['job']=='Director':
            L.append(i['name'])
            break
            
    return L

movies['crew']=movies['crew'].apply(convertCrew)

movies['overview']=movies['overview'].apply(lambda x:[x])

movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","")for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","")for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","")for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","")for i in x])

movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']
new_df=movies[['movie_id','title','tags']]

new_df['tags']=new_df['tags'].apply(lambda x:x[0])
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
stop_words=set(stopwords.words('english'))

def removingSWandDual(obj):
    word_tokens=word_tokenize(obj)
    filter_sen=[w for w in word_tokens if not w.lower() in stop_words]
    remov_d_text=[ps.stem(w) for w in filter_sen]
    return ' '.join(remov_d_text)


new_df['tags'] = new_df['tags'].apply(lambda x: removingSWandDual(x) if isinstance(x, str) else x)



import sklearn
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000)

vectorized_array = cv.fit_transform(new_df['tags']).toarray()
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectorized_array)

def recommedate(movie):
    mainlist=[]
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    similar_movies_with_scores = list(enumerate(distances))
    top_similar_movies = sorted(similar_movies_with_scores, reverse=True, key=lambda x: x[1])[1:6]
    
    
    for i in top_similar_movies:
        mainlist.append(new_df.iloc[i[0]].title)

    return mainlist

x=recommedate('Avatar')
print(x)