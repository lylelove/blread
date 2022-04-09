import json
import re
import html2text
import requests
import sys

blreadid = sys.argv[1]


def bl_update(read):
    read_list = []
    date_list = []
    url = "https://api.bilibili.com/x/article/list/web/articles?id=" + str(read) + "&jsonp=jsonp"
    hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/99.0.4844.82 Safari/537.36'}
    response = requests.get(url, headers=hd)
    print(response.json())
    articles = response.json()
    articleslist = articles['data']['articles']
    for i in range(len(articleslist)):
        response = requests.get("https://www.bilibili.com/read/cv" + str(articleslist[i]['id']), headers=hd)
        info = response.text
        pat_read = r'<div id="article-content" class="article-content">(.*?)<div class="article-footer-box">'
        pat_date = r'<span class="publish-text" .*?>(.*?)</span>'
        dates = re.compile(pat_date, re.S).findall(info)
        date_list.append(dates)
        read = re.compile(pat_read, re.S).findall(info)
        read_list.append(html2text.html2text(read[0]))
        with open('source/_posts/' + str(articleslist[i]['id']) + '.md', 'w', encoding='UTF-8') as fp:
            fp.write('---')
            fp.write('\n')
            fp.write('title: ' + articleslist[i]['title'])
            fp.write('\n')
            fp.write('date: ' + str(date_list[i][0]) + ':00')
            fp.write('\n')
            fp.write('tags: ' + articleslist[i]['category']['name'])
            fp.write('\n')
            fp.write('---')
            fp.write('\n')
            fp.write(read_list[i])


blreadid(blreadid)
