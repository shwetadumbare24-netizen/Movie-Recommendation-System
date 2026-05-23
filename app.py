
import streamlit as st
import pickle
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# Load Data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values

# Custom CSS
st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    color: white;
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 40px;
}

.recommendation {
    background-color: #1F2937;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    color: white;
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

# Dropdown
selected_movie = st.selectbox(
    "Select Movie",
    movie_list
)

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies

# Button
if st.button("🎥 Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.markdown(
            f'<div class="recommendation">{movie}</div>',
            unsafe_allow_html=True
        )
