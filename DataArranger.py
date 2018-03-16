# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:25:48 2018

@author: 89288
"""

import pymongo

class DataArranger():
    
    def __init__(self):
        '''
        链接数据库
        '''
        self.client = pymongo.MongoClient('localhost',27017)
        self.database = self.client.MultiThread
        
    def save_reload_url(self,dic_url):
        '''
        将需要再次爬取的链接存入数据库
        '''
        collection_reload_urls = self.database['reload_urls']
        collection_reload_urls.insert(dic_url)
        
    def save_crawled_url(self,url):
        '''
        将已爬取的链接存入数据库
        '''
        collection_crawled_urls = self.database['crawled_urls']
        collection_crawled_urls.insert({'url':url})
        
    def save_song_information(self,dic_song):
        '''
        将歌曲信息存入数据库
        '''
        collection_song_information = self.database['song_information']
        collection_song_information.insert(dic_song)
    
    def save_crawl_urls(self,list_urls):
        '''
        将需要爬取的链接存入数据库
        '''
        collection_crawl_urls = self.database['crawl_urls']
        collection_crawl_urls.insert({'urls':list_urls})
    
    def read_reload_urls(self):
        '''
        查询需要再次爬取的链接的数量
        '''
        collection_reload_urls = self.database['reload_urls']
        if collection_reload_urls:
            number = collection_reload_urls.find().count()
        else:
            number = 0
        return number
    
    
    
    
    