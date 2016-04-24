# coding=utf-8
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def list_page_parser(self, list_page_cont):
        soup = BeautifulSoup(list_page_cont, "html.parser", from_encoding="gbk")
        tag_a = soup.find_all('a')
        new_list = []
        for tag in tag_a:
            if tag.get_text():
                if tag.get_text()[-1] == u"】" or tag.get_text()[-1] == u"]":
                    new_list.append(tag)
        url_list = []
        for tag in new_list:
            page_url = tag.get("href")
            new_url = urlparse.urljoin("http://t66y.com/thread0806.php?fid=16&search=&page=1", page_url)
            url_list.append(new_url)
        return url_list

    def post_parser(self, page_cont):
        soup = BeautifulSoup(page_cont, "html.parser", from_encoding="gbk")
        urls = soup.find_all("img")
        url2 = soup.find_all('input', type='image')
        urls.extend(url2)
        img_list = []
        for x in urls:
            img_list.append(x.get("src"))
        return img_list
