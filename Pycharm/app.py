import streamlit as st
import pickle
import pandas as pd
import requests as req
import pytest as pt


def fetch_poster(movie_id):
    repsonse = req.get('https://api.themoviedb.org/3/movie/{}?api_key=8a8b8b01e6a94dbbd892973ace314992'.format(movie_id))
    data = repsonse.json()
    return "https://image.tmdb.org/t/p/w1280/" + data['poster_path']
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movies_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies, recommended_movies_posters


movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_df = movies_list
movies_list = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Which movie Do you have currently in Mind!!', movies_list)
if st.button('Recommend'):
    name, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0], use_column_width=True)
    with col2:
        st.text(name[1])
        st.image(poster[1], use_column_width=True)
    with col3:
        st.text(name[2])
        st.image(poster[2], use_column_width=True)
    with col4:
        st.text(name[3])
        st.image(poster[3], use_column_width=True)
    with col5:
        st.text(name[4])
        st.image(poster[4], use_column_width=True)





