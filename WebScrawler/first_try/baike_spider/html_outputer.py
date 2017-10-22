# coding: utf-8
'''
Created on 2017年10月22日

@author: TangLi
'''  
    
class HtmlOutputer(object):
    
    #列表维护收集的数据，初始化
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        
        #参数校验
        if data is None:
            return 
        
        self.datas.append(data)

    
    def out_html(self):
        
        #文件对象
        fout = open('output.html', 'w')
        
        #输出html文件格式
        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write("<body>")
        #表格
        fout.write("<table>")
        
        # python 默认编码 ascii，输出中文编码  utf-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))           
            fout.write("</tr>")
            
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close() 
    
    
    
    



