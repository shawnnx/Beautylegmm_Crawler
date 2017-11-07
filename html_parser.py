#_*_coding:utf-8
from urllib import request
from bs4 import BeautifulSoup
import re
from time import sleep
from os import mkdir,path
import traceback

class HtmlParser(object):

	def get_single_model_all_pages(self,modelfolder_url,single_model_all_pages):
		# 伪装成浏览器访问
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
		try:
			req = request.Request(modelfolder_url, headers=headers)
			res = request.urlopen(req, timeout=10)
			modelfolder_url_soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
			content = modelfolder_url_soup.find_all('a',href=re.compile(modelfolder_url))
			for pageurl in content:
				single_model_all_pages.add(pageurl['href'])
		except:
			print("Error in get_single_model_all_pages !")
			f = open("log.txt", 'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
		sleep(2)

	def get_modelfolder_url(self,showpage_url,modelfolder_urls):
		# 伪装成浏览器访问
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
		try:
			req = request.Request(showpage_url, headers=headers)
			res = request.urlopen(req, timeout=10)
			showpage_url_soup = BeautifulSoup(res,'html.parser',from_encoding='utf-8')

			#从展示页获取当前展示页中model写真集的url及写真集的名称,url和名称存入集合
			contents = showpage_url_soup.find_all('div', {'class': 'post_weidaopic'})
			for content in contents:
				modelfolder_name = content.get_text().strip('\n')
				print('正在解析%s' % modelfolder_name)

				#创建图片存储文件夹
				download_path = "H:\\Study\\PythonCode\\beautylegmm-图片爬虫\\download\\"
				modelfolder_path = download_path +modelfolder_name + "\\"
				if path.exists(modelfolder_path):
					print('%s,文件夹已存在!'%modelfolder_name)
				else:
					print('创建文件夹:%s'%modelfolder_name)
					mkdir(modelfolder_path)

				links = re.findall('http://www.beautylegmm.com/[^\s]*[\d+].html', str(content))

				#名称、url以tuple的形式存入集合
				modelfolder_urls.add((modelfolder_name,links[0]))
				single_model_all_pages =set()
				self.get_single_model_all_pages(links[0],single_model_all_pages)
				for single_model_one_page in single_model_all_pages:
					print("\t\t%s，开始下载网页上的图片："%single_model_one_page)
					self.down_img(single_model_one_page,modelfolder_path)
				print('\t\t%s解析完成！\n' % modelfolder_name)
				sleep(1)
		except:
			print("Error in get_modelfolder_url !")
			f = open("log.txt", 'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
		sleep(1)

	def down_img(self,single_model_one_page,modelfolder_name_path):
		# 伪装成浏览器访问
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
		try:
			req = request.Request(single_model_one_page, headers=headers)
			res = request.urlopen(req, timeout=10)
			single_model_one_page_soup = BeautifulSoup(res, 'html.parser', from_encoding='utf-8')
			img_urls = single_model_one_page_soup.find_all('a',href = re.compile('/photo/beautyleg/[^\s]*.jpg'))
			for img_url in img_urls:
				model_img_url = "http://www.beautylegmm.com" + img_url['href']
				img_path = modelfolder_name_path +img_url['title'] + ".jpg"
				if path.exists(img_path):
					print('\t\t\t\t\t%s,文件已存在！'%img_url['title'])
					continue
				else:
					print('\t\t\t\t\t正在下载%s'%model_img_url)
					request.urlretrieve(model_img_url,img_path)
					print('\t\t\t\t\t下载完成')
		except:
			print("Error in down_img !")
			f = open("log.txt", 'a')
			traceback.print_exc(file=f)
			f.flush()
			f.close()
		sleep(2)





