from bs4 import BeautifulSoup
import pandas as pd
import requests

url_list_file = pd.read_excel("urls.xlsx", chunk_size=50)

for chunk_size in url_list_file:
    print (chunk_size)


def scrap_body(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    print(url)
    try:
        title = soup.select('.watch-title')
        title = title[0].getText()
        title = title.strip().replace('\n',' ')
    except:
        title = ''
    try:    
        views = soup.select('.watch-view-count')
        views = views[0].getText()
        views = views.strip().replace('views','')
    except: 
        views= ''
    try:
        watch_sentiment = soup.find_all(id = 'watch8-sentiment-actions')[0]
        soup.find_all(id = 'watch8-sentiment-actions')[0]
        button_class_like = watch_sentiment.find_all('button')[0]
        watch_sentiment.find_all('button')[0]
        like= button_class_like.find_all('span')[0].get_text()
    except: 
        like= ''
        
    try:
        watch_sentiment.find_all('button')[2]
        button_class_dislike = watch_sentiment.find_all('button')[2]
        dislike = button_class_dislike.find_all('span')[0].get_text()
    except: 
        dislike = ''
    datas = [url, title, views, dislike, like] 
    return datas


datas = url_list_file.apply(lambda row: scrap_body(row['Watch URL']), axis=1)
dataframe= datas.to_frame('data')
dataframe[['url', 'title', 'views','dislike', 'like' ]] = pd.DataFrame(dataframe.data.values.tolist())
dataframe = dataframe[['url', 'title', 'views','dislike', 'like']]
dataframe.to_excel("final_output.xlsx")

