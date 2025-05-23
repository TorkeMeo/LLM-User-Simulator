class UrlManager():
    """
    url manager
    """
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()

    def add_new_url(self,url):
        if url is None or len(url)==0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        if self.has_new_url():
            url=self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0

if __name__ == "__main__":
    urlManager = UrlManager()

    urlManager.add_new_url("url1")
    urlManager.add_new_urls(["url1","url2","url3"])
    print(urlManager.new_urls,urlManager.old_urls)

    print("*"*30)
    new_url = urlManager.get_url()
    print(urlManager.new_urls, urlManager.old_urls)

    print("*" * 30)
    new_url = urlManager.get_url()
    print(urlManager.new_urls, urlManager.old_urls)

    print("*" * 30)
    new_url = urlManager.get_url()
    print(urlManager.new_urls, urlManager.old_urls)

    print("*" * 30)
    new_url = urlManager.get_url()
    print(urlManager.new_urls, urlManager.old_urls)

    print("*" * 30)
    print(urlManager.has_new_url())
















