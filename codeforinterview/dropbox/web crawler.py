"""
Implement a webpage Crawler to crawl webpages of
http://www.wikipedia.org/. To simplify the question,
let's use url instead of the the webpage content.

Your crawler should:

Call HtmlHelper.parseUrls(url) to get all urls from a webpage of given url.
Only crawl the webpage of wikipedia.
Do not crawl the same webpage twice.
Start from the homepage of wikipedia: http://www.wikipedia.org/
"""
from threading import Thread
from Queue import Queue
from urlparse import urlparse

queue = []
results = set()
class soluction:
    def crawler(self,url):
        queue.put(url)
        while True:
            url=queue.pop()
            if url not in results and urlparse(url).hostname.endswith('target.org'):
                results[url]=True
                urls=HtmlHelper.parseUrls(url)
                for url in urls:
                    queue.append(url)
        return results

queue = Queue()
results = set()
class CrawlerThread(Thread):
    def run(self):
        global queue, results
        while True:
            url = queue.get()
            if url not in results \
                    and urlparse(url).hostname.endswith("target.org"):
                results[url] = True
                urls = HtmlHelper.parseUrls(url)
                for url in urls:
                    queue.put(url)
            queue.task_done()

# class HtmlHelper:
#    @classmethod
#    def parseUrls(cls, url)
#       # Get all urls from a webpage of given url.
class Solution:
    # @param {string} url a url of root page
    # @return {string[]} all urls
    def crawler(self, url):
        # Write your code here
        global queue, results
        thread_pools = []
        for i in xrange(10):
            thread_pools.append(CrawlerThread())
            thread_pools[i].setDaemon(True)
            thread_pools[i].start()

        queue.put(url)

        queue.join()

        return results