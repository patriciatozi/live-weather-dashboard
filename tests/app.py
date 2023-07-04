from bs4 import BeautifulSoup
import requests
import streamlit as st
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0'
}

def find_weather(city_name):
    city_name = city_name.replace(" ", "+")
 
    try:
        res = requests.get(
            f'https://www.google.com/search?q={city_name}+clima&sxsrf=AB5stBhLApXHcmwKWeuoSFlPN2CFgpAbpQ%3A1688438813095&ei=HYijZKe7BdnC5OUPlbmB8AQ&ved=0ahUKEwjnvbfdhPT_AhVZIbkGHZVcAE4Q4dUDCA4&uact=5&oq=londres+clima&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIQCAAQgAQQsQMQgwEQRhCAAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgcIABCABBAKOgoIABBHENYEELADOgoIABCKBRCwAxBDOgsIABCABBCxAxCDAToFCC4QgAQ6CwguEIAEEMcBEK8BSgQIQRgAUI8IWPwMYIoSaAJwAXgAgAGTAYgB2QSSAQMwLjWYAQCgAQHAAQHIAQo&sclient=gws-wiz-serp', headers=headers)
        
        print("Loading...")

        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('.BBwThe')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        temperature = soup.select('#wob_tm')[0].getText().strip()

        print(location)
        print(time)
        print(info)
        print(temperature)

        df = pd.DataFrame(data = {'Location': [location], 'Time': [time], 'Info': [info], 'Temperature': [temperature]}, columns = ['Location', 'Time', 'Info', 'Temperature'])

        return df
       #print("Location: " + location)
       #print("Temperature: " + temperature + "&deg;C")
       #print("Time: " + time)
       #print("Weather Description: " + info)
    except:
       print("Please enter a valid city name")


user_input = st.text_input("City")

df = find_weather(user_input)

st.dataframe(df)