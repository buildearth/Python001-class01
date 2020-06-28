import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import time

'''
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
'''
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
headers = {
    'user-agent': user_agent,
    'Cookie':'__mta=209043117.1592966246630.1592975153153.1593325423044.14; uuid_n_v=v1; uuid=9BF004F0B5C311EAAD7CEBC74F78E0F95C3D56CAB3FE445F99D6EBA7900DD526; _lxsdk_cuid=172e42fbd2ac8-0e05f5e49d02d9-3f770c5a-100200-172e42fbd2ac8; _lxsdk=9BF004F0B5C311EAAD7CEBC74F78E0F95C3D56CAB3FE445F99D6EBA7900DD526; mojo-uuid=3541ca2920d824e62e5b2726f16d272f; _csrf=c34c908cefb54a819623eeccf8c573846c6eecd21914095e0988da7922407730; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-session-id={"id":"f13271cd89581a5453e1955afefc51be","time":1593325259374}; lt=iFP_tk4hEvWpLqe68TP_T3HUCYYAAAAA5woAAABR9yGapJYwO0XpVTCbTvsxiT8_GUcNj3-LxOwUhCMS_T0WruD7dQgLEsNacGiYhA; lt.sig=e7tPy7wQo2Um5GlrqY5ORYe5dbo; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592966244,1593325259,1593325402,1593325417; __mta=209043117.1592966246630.1593325403441.1593325417078.6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593325422; mojo-trace-id=10; _lxsdk_s=172f9960a5f-b50-465-74e%7C%7C17'}

url = r'https://maoyan.com/?channel=touch_group'
response = requests.get(url, headers = headers)
print(response.status_code)

bs_info = bs(response.text, 'html.parser')
top = bs_info.find('div', {'class': 'top100-wrapper'})
top10_link = []
for movie_info in top.find_all('a', attrs = {'data-act': 'TOP100-movie-click'}):
    link = movie_info.get('href')
    top10_link.append('https://maoyan.com{}'.format(link))
    time.sleep(2)

# print(top10_link)
movies = [('movie name', 'type', 'release time')]  # 电影详细信息
for url in top10_link:
    print('='*10,url)
    response = requests.get(url, headers = headers)
    bs_info = bs(response.text, 'html.parser')
    name = bs_info.find('h1', attrs = {'class': 'name'}).text
    bs_types_info = bs_info.find_all('a', {'class':'text-link'})
    types = []
    for movie in bs_types_info:
        types.append(movie.text)
    time.sleep(3)
    show_time = bs_info.find_all('li', {'class': 'ellipsis'})[-1].text

    movies.append((name, ','.join(types), show_time))

pd_movie = pd.DataFrame(data = movies)
pd_movie.to_csv('maoyan_top10.csv', mode = 'wt', encoding = 'utf-8',
    index = False, header = False)
# ranking-top-moive-name
