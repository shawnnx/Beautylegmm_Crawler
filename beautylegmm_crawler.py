#_*_coding:utf-8
#页面url解析模块功能，入口参数为page_url，返回next_page_url，和model_pic_folder_url。分别放入两个列表
#页面下载模块。入口参数为model_pic_folder_url，解析该链接的图片url，下载存储

from html_parser import HtmlParser
from time import clock

start =clock()

root_url = "http://www.beautylegmm.com/"
#初始化存储所有model写真集的集合
#集合中存储每个model的写真集的名称和url
modelfolder_urls = set()
MM_parser = HtmlParser()

#生成待爬取的页面列表
page_num = 73
for num in range(page_num):
	showpage_url = root_url + "index-" + str(num+1) + ".html"
	MM_parser.get_modelfolder_url(showpage_url,modelfolder_urls)

end = clock()
print('程序运行历时:%f'%(end-start))






