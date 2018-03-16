# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:04:21 2018

@author: 89288
"""

import DataArranger 
import HtmlDownloader 
import HtmlParser 
import UrlManager 
import time
import threading


class MultipThread(threading.Thread):
    
    def __init__(self,class_crawl,name):
        
        threading.Thread.__init__(self)
        self.name = name
        self.class_crawl = class_crawl
        
        
    def run(self):
        #类的start方法将运行改函数，所以重写父类threading.Thread的run方法 
        while self.class_crawl.UM.crawl_urls:
            print (self.name+' start.')
            #得到爬取链接
            my_lock.acquire()
            url = self.class_crawl.UM.get_crawl_url()
            my_lock.release()
            #访问链接并下载存储网页内容
            response = self.class_crawl.HD.download(url)
            if response:
                iters_p = self.class_crawl.HP.parse(response['response'])
                #存储网页中歌曲信息
                for iter_p in iters_p:
                    
                    my_lock.acquire()
                    self.class_crawl.DA.save_song_information(iter_p)
                    my_lock.release()
                #存储爬取成功的链接
                my_lock.acquire()
                self.class_crawl.DA.save_crawled_url(url)
                my_lock.release()
                #线程休眠6s
                time.sleep(6)
            else:
                #爬取失败则将链接存入另一集合
                my_lock.acquire()
                self.class_crawl.DA.save_reload_url({'url':url,
                                                     'reload_times':1})
                my_lock.release()          
            print (self.name+' end.')
        else:
            print ('爬取完毕')
        



#为了保证各线程的操作对象都是同一类
class WebCrawler():
    
    def __init__(self):
        '''
        初始化各模块
        '''
        self.DA = DataArranger.DataArranger()
        self.HD = HtmlDownloader.HtmlDownloader()
        self.HP = HtmlParser.HtmlParser()
        self.UM = UrlManager.UrlManager()

my_lock = threading.RLock()
if __name__ == '__main__':
    #创建爬虫类
    web_crawler = WebCrawler()
    web_crawler.DA.save_crawl_urls(web_crawler.UM.crawl_urls)
    #创建多线程并开始运行
    threads = []
    pre_thread_name = 'Thread_'
    for i in range(0,4):
        thread_name = pre_thread_name + str(i)
        thread = MultipThread(class_crawl=web_crawler,name=thread_name)
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
        
    '''
    #单线程测试
    thread = MultipThread(class_crawl=web_crawler,name='thread_1')
    thread.start()
    thread.join()
    '''

