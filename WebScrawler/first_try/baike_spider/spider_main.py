# coding: utf-8
'''
Created on 2017年10月22日

@author: TangLi
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer

#爬虫总调度程序
class SpiderMain(object):
    #构造函数是初始化url管理器，下载器，，解析器，输出
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
            
    def craw(self, root_url):
        
        count = 1
        
        #将主页面存入url管理器
        self.urls.add_new_url(root_url)
        
        #当url管理器里有url时循环
        while self.urls.has_new_url():
            
            #异常处理
            try:
                # 是否有新的url
                new_url = self.urls.get_new_url()
                
                #输出爬取到第几个页面了
                print 'craw %d : %s' % (count, new_url)
                
                # 将新的url内容用下载器下载到html_cont页面中
                html_cont = self.downloader.download(new_url)
                
                # 对下载的页面进行解析
                new_urls, new_data = self.parser.parse(new_url, html_cont)
               
                # 将的url加入url管理器
                self.urls.add_new_urls(new_urls)
                
                # 进行数据的收集
                self.outputer.collect_data(new_data)
                
                #爬取200个页面后停止
                if count == 200:
                    break;
                
                count += 1
            except:
                print 'craw failed'
            
        self.outputer.out_html()
            


if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain() #爬虫总调度程序
    obj_spider.craw(root_url) #craw(url)启动爬虫
    
    
 
