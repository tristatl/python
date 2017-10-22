#coding: utf-8
'''
Created on 2017年10月22日

@author: TangLi
'''
import urllib2


class HtmlDownloader(object):
    
    
    def __init__(self):
        pass

    
    def download(self, url):
        if url is None:
            return None
        
        #请求url的内容，结果存在response中
        response = urllib2.urlopen(url)
        
        #返回请求码结果，不等于200则请求失败
        if response.getcode() != 200:
            return None
        
        #否则读取请求结果
        return response.read()
    
    
    
    



