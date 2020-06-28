import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'

def get_info(link):
    response = requests.get(link, headers = header)
    selector = lxml.etree.HTML(response.text)
    movie_show_data = selector.xpath('//*[@id="info"]/span[10]/text()')
    movie_score = selector.xpath(
        '//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    return (movie_show_data[0], movie_score[0])

data = []
header = {'user-agent': user_agent}
# my_url = r'https://movie.douban.com/top250'
def read_movie_info(my_url):
    response = requests.get(my_url, headers = header)
    # print(response.text)
    print('return code :', response.status_code)

    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs = {'class':'hd'}):
        for atag in tags.find_all('a'):
            movie_link = atag.get('href')
            movie_name = atag.find('span').text
            movie_show_data, movie_score = get_info(movie_link)
            data.append([movie_name, movie_show_data, movie_score])
            print(movie_name, movie_show_data, movie_score)

# urls = ['https://movie.douban.com/top250?start={}&filter='.format(i) for i in range(0, 230, 25)]
for i in range(0, 230, 25):
    my_url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
    read_movie_info(my_url)

for i in urls:
    print(i)
print(data)
movie = pd.DataFrame(data = data)
movie.to_csv('movie.csv', encoding = 'utf-8', index = False, header = False)
