# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:58:36 2018

@author: 89288
"""

from lxml import etree
import re

class HtmlParser():
    
    def parse(self,response):
        '''
        解析网页
        yield:以生成器的方式返回歌曲信息组成的字典
        '''
        html = etree.HTML(response)
        elements_li = html.xpath('//li[@class=" "]')
        for element_li in elements_li:
            '''
            目标网页对歌曲排行的排版不一样，因此需要两种提取信息的方式
            '''
            try:
                rank = element_li.xpath(
                        './span[@class="pc_temp_num"]/strong/text()')[0]
            except IndexError:
                element_rank = element_li.xpath(
                        './span[@class="pc_temp_num"]/text()')[0]
                pattern_rank = re.compile('\d+')
                answer_rank = re.search(pattern_rank,element_rank)
                rank = answer_rank.group()
            
            string = element_li.xpath('a/text()')[0]
            list_string = string.split('-')
            #提取歌手名
            singer = list_string[0].rstrip()
            #提取歌名
            song_name = list_string[1].lstrip()
            #提取歌曲时长，
            compile_string = element_li.xpath(
                    './/span[@class="pc_temp_time"]/text()')[0] 
            pattern = re.compile('\d.+\d')
            answer = re.search(pattern,compile_string)
            time_length = answer.group()
            
            dic_song = {'rank':rank,'singer':singer,'song_name':song_name,
                        'time_length':time_length}
            yield dic_song
        


