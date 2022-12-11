import difflib
import pickle
import pandas as pd
import streamlit as st
def main():
    st.title("Movie Recommendation Web App")
    df = pd.read_csv("movies.csv")
    filename = "movies.sav"
    load_set = pickle.load(open(filename, "rb"))
    movie = st.text_input("Enter your favorite movie: ")
    movie_list = list(df['title'])
    close = (difflib.get_close_matches(movie, movie_list))[0]
    y = df[df.title == close]['index'].values[0]
    z = list(enumerate(load_set[y]))
    sort = sorted(z, key=lambda x: x[1], reverse=True)
    i = 1
    if st.button("Suggest Movies"):
        for movie in sort:
            index = movie[0]
            movie_name = df[df.index == index]['title'].values[0]
            if (i <= 30):
                st.success(f"{i}-{movie_name}")
                i = i + 1


if __name__=="__main__":
    main()

