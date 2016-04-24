# -*- coding: utf-8 -*-
from new_1024_spider import html_downloader
from new_1024_spider import html_parser
from new_1024_spider import outputer
from new_1024_spider import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.out_put = outputer.OutPuter()

    def craw(self, url):
        list_page_cont = self.downloader.download(url)
        list_urls = self.parser.list_page_parser(list_page_cont)
        i = 0
        for page_url in list_urls:
            try:
                page_cont = self.downloader.download(page_url)
                i += 1
                img_urls = self.parser.post_parser(page_cont)
                self.urls.add_urls(img_urls)
                print "Get page %d Succeeded" % i
            except Exception:
                i += 1
                print "Get page %d failed" % i
            if i == 30:
                break

        self.out_put.save_img(self.urls.img_urls)


if __name__ == "__main__":
    Domain_1024 = "http://t66y.com/thread0806.php?fid=16&search=&page=1"
    spider_1024 = SpiderMain()
    spider_1024.craw(Domain_1024)
