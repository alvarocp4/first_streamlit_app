#IMPORTS
import streamlit
import pandas
#TABLES
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#BODY
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breaksfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#LIST TO PICK
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#DISPLAY TABLE
streamlit.dataframe(my_fruit_list)
