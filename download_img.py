#_*_coding:utf-8
#输入图片url和存储目录，下载图片，并保存图片到指定文件夹

from time import sleep
from urllib import request
from bs4 import BeautifulSoup
import re
class Download_Img(object):
	def down_img(self,single_model_one_page,modelfolder_name_path):
		# 伪装成浏览器访问
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
		req = request.Request(single_model_one_page, headers=headers)
		res = request.urlopen(req, timeout=10)
		single_model_one_page_soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
		img_urls = single_model_one_page_soup.find_all('a',href = re.compile('/photo/beautyleg/[^\s]*.jpg'))
		for img_url in img_urls:
			model_img_url = "http://www.beautylegmm.com" + img_url['href']
			request.urlretrieve(model_img_url,modelfolder_name_path)

