class UrlManager(object):
    def __init__(self):
        self.img_urls = []

    def add_urls(self, urls):
        if urls is None:
            return
        else:
            self.img_urls.extend(urls)
