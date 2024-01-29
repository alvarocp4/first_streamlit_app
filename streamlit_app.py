#IMPORTS
import snowflake.connector
from urllib.error import URLError
import streamlit
import pandas
import requests
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

#create a function
def get_fruityvice_data (this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


#New section 
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
  else:
        back_from_function = get_fruityvice_data (fruit_choice)
        streamlit.dataframe(back_from_function)

#Hellow from snowflake/CONNECTOR
streamlit.header("The fruit load list contais:")
#Snowflake functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
#Add a button
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

streamlit.stop()
#New box
add_my_fruit= streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
#Add new excute insert into
my_cur.execute("insert into fruit_load_list values('from streamlit')")
