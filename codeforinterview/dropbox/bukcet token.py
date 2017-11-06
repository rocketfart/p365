from time import time


class TokenBucket3:
    from time import sleep, time

    def __init__(self, rate, maxnum=None):
        'Rate in tokens per second, maxnum in number of tokens'

        self.rate = float(rate)
        #if maxnum is None:
            #maxnum = self.rate
        self.rate = 1 / self.rate
        self.burst = float(maxnum) * self.rate
        self.toks = self.burst
        self.last = time()


    def rate_limit(self, tokens=1.0):
        tokens = float(tokens)

        if self.rate <= 0:
            return

        h = time()
        diff = h - self.last
        self.toks += diff*self.rate
        self.last = h

        if self.toks > self.burst:
            self.toks = self.burst

        if self.toks >= self.rate:
            self.toks -= self.rate

        if self.toks < self.rate:
            print(sleep for %f' % (self.rate - self.toks))
            self.sleep((self.rate - self.toks))


if __name__ == '__main__':
    tbf = TokenBucket3(2.0, 5.0)
    while True:
        tbf.rate_limit()
        print ('.')



import threading
from time import sleep, time

class TokenBucket:
    """
    An implementation of the token bucket algorithm.
    """
    def __init__(self,rate,maxnum):
        self.rate = rate
        self.max=maxnum

        self.tokens = maxnum
        self.last = time()
        self.lock = threading.RLock()

    def consume(self, n):
        with self.lock:
            #if not self.rate:
            #   return 0
            now = time()
            lapse = now - self.last
            self.last = now
            self.tokens += lapse * self.rate

            self.tokens = min(self.max, self.tokens)

            self.tokens -= n

            if self.tokens >= 0:
                return True
            else:
                sleep(-self.tokens / self.rate)
                return True

    def put(self,num):
        with self.lock:
            self.tokens+=num
            self.tokens=min(self.max,self.tokens)

if __name__ == '__main__':
    import sys

# start=time()
# for i in range(1):
#     bucket = TokenBucket(1.0,100.0)
#     print bucket.consume(90.0)
#     print bucket.tokens
# bucket.put(50.0)
# print bucket.tokens
# print bucket.consume(10.0)
# sys.exit(0)
