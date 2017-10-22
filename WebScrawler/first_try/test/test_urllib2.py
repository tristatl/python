# coding: utf-8
import urllib2
import cookielib

url = "http://www.baidu.com"

print '第一种方法'
response1 = urllib2.urlopen(url)
#打印返回的状态码
print response1.getcode()
#打印网页字符长度
print len(response1.read())


print '第二种方法'
request = urllib2.Request(url)
#模拟浏览器登陆
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())


print '第三种方法'
#cookie容器
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()
