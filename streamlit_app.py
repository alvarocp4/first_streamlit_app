#IMPORTS
import snowflake.connector
import streamlit
import pandas
#TABLES
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#BODY
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breaksfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#LIST TO PICK
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruit_selected]
#DISPLAY TABLE
streamlit.dataframe(fruits_to_show)
#New section display: f.fruitvyce
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# normalize
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output
streamlit.dataframe(fruityvice_normalized)

#Hellow from snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contais:")
streamlit.text(my_data_row)
