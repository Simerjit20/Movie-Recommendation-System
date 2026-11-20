
import streamlit as st
import pandas as pd
from recommender import recommend_movies

# Page settings
st.set_page_config(
    page_title="CineMatch | Movie Recommendations",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #10101c, #1c1230, #10101c);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    color: #ffcc70;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #c5bdd8;
    font-size: 18px;
    margin-bottom: 35px;
}

.section-title {
    color: #ffcc70;
    font-size: 27px;
    font-weight: bold;
    margin-top: 25px;
}

.movie-card {
    background: linear-gradient(145deg, #29203d, #191526);
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #49365f;
    margin-bottom: 15px;
    text-align: center;
}

.movie-name {
    color: white;
    font-size: 17px;
    font-weight: 600;
}

.stButton > button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 28px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    color: white;
    border: 1px solid #ffcc70;
}

</style>
""", unsafe_allow_html=True)


# Load dataset
movies = pd.read_csv("dataset/movies.csv")

# Header
st.markdown(
    '<div class="main-title">🎬 CineMatch</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Discover your next favourite movie ✨</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# Introduction
st.markdown("### 🍿 Find Movies You'll Love")
st.write(
    "Choose a movie you enjoy and CineMatch will discover "
    "five similar movies based on their genres."
)

# Movie selection
movie_list = movies["title"].sort_values().tolist()

selected_movie = st.selectbox(
    "🎥 Select your favourite movie",
    movie_list
)

# Recommendation button
if st.button("✨ Discover Movies"):

    recommendations = recommend_movies(selected_movie)

    if recommendations:

        st.markdown(
            '<div class="section-title">🍿 Your Recommendations</div>',
            unsafe_allow_html=True
        )

        columns = st.columns(5)

        for i, movie in enumerate(recommendations):

            with columns[i]:
                st.markdown(f"""
                <div class="movie-card">
                    <div style="font-size:35px;">🎞️</div>
                    <div class="movie-name">{movie}</div>
                    <div style="color:#ffcc70; margin-top:12px;">
                        ★ Recommended
                    </div>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.error("Movie not found!")

# Footer
st.markdown("---")

st.markdown(
    "<center style='color:#aaa;'>"
    "Made with ❤️ using Python, Pandas, Scikit-learn & Streamlit"
    "</center>",
    unsafe_allow_html=True
)
