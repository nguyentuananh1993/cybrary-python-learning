import urllib2  

proxy_support = urllib2.ProxyHandler({"http":"http://218.97.194.202:80"})  
opener = urllib2.build_opener(proxy_support)  
url='http://mazii.net/api/mazii/%E5%85%AC/10'  
page = opener.open(url)  
contents=page.read()  
print contents  