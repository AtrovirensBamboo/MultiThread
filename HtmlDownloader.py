# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:45:19 2018

@author: 89288
"""

import requests
import chardet


class HtmlDownloader():
    
    def download(self,url):
        '''
        将爬取到的网页存储下来
        return:成功返回以网页内容及编码方式的字字典，失败返回None
        '''
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/\
        1.53.4882.400 QQBrowser/9.7.13059.400'
        refer = 'http://www.kugou.com/yy/html/rank.html'
        headers = {'User-Agent':user_agent,'Refer':refer}
        
        response = requests.get(url,headers=headers)
        encoding_type = chardet.detect(response.content)['encoding']
        response.encoding = encoding_type
        
        if response.status_code == 200 or (response.status_code == 304):
            html = {'response':response.text,'encoding':encoding_type}
            return html
        else:
            return None



