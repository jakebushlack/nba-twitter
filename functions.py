# importing the module
from urllib.request import urlopen as uReq
import queries_list
import tweepy
import pandas as pd
from bs4 import BeautifulSoup as Soup
# import tweepy
from pandasql import sqldf
import StatsAppAccessKeys as Keys


def scrape(url):
    file_name = url[54:-5]
    table_name = file_name + "_stats"
    try:
        uClient = uReq(url)
    except:
        exit()  # NOT SURE IF THIS IS RIGHT
    html = uClient.read()  # STORE HTML DATA FROM WEBPAGE TO A VARIABLE
    uClient.close()
    page_soup = Soup(html, "html.parser")
    html_table = page_soup.find('table', {'id': table_name})

    with open(file_name, 'w', encoding="utf-8") as file_contents:
        for stat in html_table.thead.find_all('th', {"data-stat": True}):
            if stat.get('data-stat') == 'ranker' or '':
                pass
            else:
                file_contents.write(str(stat.get('data-stat') + ','))
        for row in page_soup.find_all('tr', {"class": "full_table"}):
            file_contents.write('\n')
            for stat in row.find_all('td', {"data-stat": True}):
                if stat.get('data-stat') == '':
                    pass
                else:
                    file_contents.write(str(stat.text) + ',')
    return file_name


# def write_file()


def write_df(file_name):
    df = pd.read_csv(file_name)
    return df


def merge_df(_left, _right):
    return pd.merge(_left, _right, 'player')


# query
def get_query(i):
    return queries_list[i]


def query_df(_df, _query):
    return None


def tweet(tweet_contents):
    try:
        auth = tweepy.OAuthHandler(Keys.consumer_key, Keys.consumer_secret)
        auth.set_access_token(Keys.access_token, Keys.access_token_secret)
        api = tweepy.API(auth)
        disclaimer = "Stats courtesy of Basketball-Reference.com"
        api.update_status(tweet_contents + '\n\n' + disclaimer)
    except Exception as e:
        print(len(tweet_contents) + len(disclaimer))
        print(e)
