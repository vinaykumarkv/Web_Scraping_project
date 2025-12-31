import sqlite3
import emailer
import requests
import selectorlib
from sqlalchemy import create_engine
import pandas as pd
from io import StringIO

URL = "https://www.sensorsone.com/celsius-conversion-table-100-1000degc/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """
    Scrape the web page
    :param url:
    :return:
    """
    r = requests.get(URL, headers=HEADERS)

    data = r.text
    with open("html.txt", "w", encoding="utf-8") as file:
        file.write(data)
    return data



def extract(data):
    html_io = StringIO(data)
    dfs = pd.read_html(html_io, attrs={'class': 'four_column_conversion_table'})
    return dfs[0]

def send_email(content):
    emailer.send_email(content)

def store_extracted_data(data):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")

def read_extracted_data():
    with open("data.txt", "r", encoding="utf-8") as file:
        return file.read()

def update_in_db(df):
    engine = create_engine(f'sqlite:///data.db')
    df.to_sql('temperatures', con=engine, index=False, if_exists='replace')
    conn = sqlite3.connect('data.db')
    query = "SELECT count(*) FROM temperatures"
    result = pd.read_sql(query, conn)
    conn.close()
    return result

if __name__ == "__main__":
    data = scrape(URL)
    temperature_df = extract(data)
    print(temperature_df.shape[0])
    print(temperature_df)

    updated_counts = update_in_db(temperature_df)

    send_email(f"data is updated with {updated_counts}: \n {temperature_df}")

