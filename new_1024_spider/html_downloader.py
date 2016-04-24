import urllib2


class HtmlDownloader(object):
    def download(self, url):
        opener = urllib2.build_opener(urllib2.ProxyHandler(dict(http='http://127.0.0.1:8787')))
        urllib2.install_opener(opener)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/45.0.2454.101 Safari/537.36'}
        req = urllib2.Request(
            url=url,
            headers=headers
        )
        return urllib2.urlopen(req).read()
