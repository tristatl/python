# coding:utf-8
'''
Created on 2017年10月22日

@author: TangLi
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    #解析出新的url列表和数据  
    
    #获取页面中新的url  
    def _get_new_urls(self, page_url, soup):
        
        #储存结果
        new_urls = set()
        
        # /item/123.htm
        #正则表达式匹配 得到所有的词条url
        links = soup.find_all('a', href=re.compile(r"/item/.*"))
        
        for link in links:
            new_url = link['href'] 
            #获得完整的url
            #将new_url按照page_url进阶为全新的完整的url
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
        
    
    def _get_new_data(self, page_url, soup):
        
        #结果储存在字典中
        res_data = {}

        #url
        res_data['url'] = page_url
        
                    
        #找到标题节点
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        #class_与python中自带的class模块以示区分
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data
        
        
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 
    
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    



