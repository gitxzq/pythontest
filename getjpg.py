#coding=utf-8
import urllib

def getHtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

html=getHtml('http://tieba.baidu.com/f?kw=%C4%DA%BA%AD%CD%BC&fr=index')
print html