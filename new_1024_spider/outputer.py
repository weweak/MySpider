# coding=utf-8
import string

from new_1024_spider import html_downloader


class OutPuter(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()

    def save_img(self, img_urls):
        count = 1
        for url in img_urls:
            img_name = string.zfill(count, 5) + '.jpg'
            img_path = r'C:\Users\49475\Documents\spider\1024_img\\' + img_name
            try:
                img = self.downloader.download(url)
            except Exception:
                print u'第' + str(count) + u'张图片下载失败'
                print u'第' + str(count) + u'张图片url是', url
                count += 1
            else:
                f = open(img_path, 'wb')
                print u'正在下载第' + str(count) + u'张照片，并将其储存为' + img_name + '......'
                print u'第' + str(count) + u'张图片url是', url
                f.write(img)
                f.close()
                count += 1
