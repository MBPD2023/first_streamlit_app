import streamlit
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") #read csv

streamlit.title("My Mom's New Healthy Diner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free_Range Egg")
streamlit.text("🥑🍞 Avocado Teast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#picklist for fruits
stremlit.multiselector("Pick some fruits:", list(myfruits_list.index))

#display table
streamlit.dataframe(my_fruit_list)
