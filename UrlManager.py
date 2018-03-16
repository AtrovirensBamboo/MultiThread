# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class UrlManager():
    
    def __init__(self):
        '''
        初始化各属性
        crawl_urls:未爬取链接列表
        reload_urls:需再次爬取链接列表
        crawled_urls:已爬取链接列表
        '''
        urls = []
        for i in range(1,24):
            url = 'http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(i)
            urls.append(url)
        self.crawl_urls = list(reversed(urls[:]))
        self.reload_urls = []
        self.crawled_urls = []
        
    def get_crawl_url(self):
        '''
        从未爬取链接列表取出一个链接
        '''
        url = self.crawl_urls.pop()
        return url
    
    def get_reload_url(self):
        '''
        从需再次爬取链接列表取出一个链接字典
        '''
        dic_url = self.reload_urls.pop()
        return dic_url
    
    def judge_craw_urls(self):
        '''
        判断未爬取链接列表是否为空
        '''
        if self.crawl_urls:
            return False
        else:
            return True
        
    def judge_reload_urls(self):
        '''
        判断需再次爬取链接列表是否为空
        '''
        if self.reload_urls:
            return False
        else:
            return True
        
    def add_reload_url(self,dic_url):
        '''
        将爬取失败的链接存入需再次爬取的链接列表
        '''
        self.reload_urls.append(dic_url)
        
    def add_crawled_url(self,url):
        '''
        将爬取成功的链接存入已爬取链接列表
        '''
        self.crawled_urls.append(url)
    
    
    
    
    
    
    

