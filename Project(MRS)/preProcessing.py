# Preprocessing of Data
import ast
import numpy as np
import pandas as pd
from nltk.stem.porter import PorterStemmer # this is for natural language processing module
from sklearn.metrics.pairwise import cosine_similarity # for comparing the value and give them num btwnn (0->1) 0 means and match low-level and 1 means match high-level
from sklearn.feature_extraction.text import CountVectorizer

movies_df = pd.read_csv("F:/github/python/Project(MRS)/tmdb_5000_movies.csv")
credits_df = pd.read_csv("F:/github/python/Project(MRS)/tmdb_5000_credits.csv")
# print(movies_df)
# print(credits_df)

# print(movies_df.shape) # the shape of movies_df before merge
movies_df = movies_df.merge(credits_df, on='title') # Here we add cast and crew column in movies_df
# print(movies_df.shape) # the shape of movies_df after merge

# print(movies_df.info())
# We take only esssential columns -> genres, id, keywords, overview, movie_id, title, cast, crew in movies_df
movies_df = movies_df[['genres','id','keywords','overview','movie_id','title','cast','crew']]

# print(movies_df.head(1))

# Now check null values
# print(movies_df.isnull().sum())
movies_df.dropna(inplace=True)
# print(movies_df.isnull().sum())

# Check duplicated values
print("Check for duplicated:- ",movies_df.duplicated().sum()) # No duplicated values

# In genres columnn we need on movies names so we put of the movies names in a list and store it
# For that we have created a function called {convert()}
def convert(obj):
    L = []
    for i in ast.literal_eval(obj): # this ast_literal_eval convert the string in list for looping
        L.append(i['name'])
    return L

# Apply this convert function to the genres col
movies_df['genres'] = movies_df['genres'].apply(convert) # can print also in output
movies_df['keywords'] = movies_df['keywords'].apply(convert)

# Fuction for Cast conversion select only top 3 actors
def convertCast(obj):
    L = []
    count = 0
    for i in ast.literal_eval(obj): # this ast_literal_eval convert the string in list for looping
        if count != 3:
            L.append(i['name'])
            count += 1
        else:
            break
    return L

movies_df['cast'] = movies_df['cast'].apply(convertCast)

# A fuction to Select only Director name from the list
def convertCrew(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

movies_df['crew'] = movies_df['crew'].apply(convertCrew)
print(movies_df.head())

# Convert the Overview Col of string in a list use lambda function
movies_df['overview'] = movies_df['overview'].apply(lambda x : x.split())

# print(movies_df['overview'].head(1))

movies_df['tags'] = movies_df['genres'] + movies_df['overview'] + movies_df['keywords'] + movies_df['cast'] + movies_df['crew']
# print(movies_df['tags'][0])
# print()

movies_df['tags'] = movies_df['tags'].apply(lambda x:[i.replace(" ","") for i in x])
# print(movies_df['tags'][0])

new_df = movies_df[['movie_id','title','tags']]
# print(new_df)

# Again convert the list into string(tags col)
new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x)) # here ignore the warning 
# print(new_df)

new_df['tags'] = new_df['tags'].apply(lambda x:x.lower()) # ignore the warning
# print(new_df)

# Convert the tags col words into a vectorMatrix of 5000*5000 matrix
cv = CountVectorizer(max_features=5000, stop_words='english') 
# 5000 are words in matrix and stop_words remove english words which are used to create a sentence eg-> is a in the 

vectors = cv.fit_transform(new_df['tags']).toarray() # directly convert into a array by using toarray function
# print(vectors)

# By use PosterStemmer class converting the words in a correct verb eg -> [look, looked, looking] -> look 
ps = PorterStemmer()

def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))
    
    return " ".join(y) # convert into string and then return it

new_df['tags'] = new_df['tags'].apply(stem) # ignore the warning

# print(len(cv.get_feature_names_out(10)))

# Similarity 
similarity = cosine_similarity(vectors)
# print(similarity[0])

# Create a recommended function for recommending the movies name using (similarity)
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0] # Find the movie index from new_df
    distances = similarity[movie_index] # get all the similarity distance from that movie to each other movies
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    # enumerate -> This function is used to sorted the tuples based on the second val which is similarity_distance 
    # sorted it in descending order according to more nearest or closest movies distance and return 5 movies name from the new_df
    
    for i in movie_list:
        print(new_df.iloc[i[0]].title) 
        # Its get the title of the movies using there indexs


print(recommend('Spider-Man 3'))

