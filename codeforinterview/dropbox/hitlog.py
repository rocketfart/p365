def __init__(self):
    """
    Initialize your data structure here.
    """
    self.deque = collections.deque()
    self.count = 0

    self.lock=threading.Rlock()



def hit(self, timestamp):
    """
    Record a hit.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: void
    """
    with self.lock:
        if not self.deque or self.deque[-1] != timestamp:
            self.deque.append([timestamp, 1])
        else:
            self.deque[-1][1] += 1
        self.count += 1


def getHits(self, timestamp):
    """
    Return the number of hits in the past 5 minutes.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: int
    """
    with self.lock:
        while self.deque and timestamp - self.deque[0][0] >= 300:
            self.count -= self.deque.popleft()[1]
        return self.count

# improve

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(-1)
        self.dummy = self.head
        self.count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.dummy.next = ListNode(timestamp)
        self.dummy = self.dummy.next
        self.count += 1
        self.clean(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.clean(timestamp)
        return self.count

    def clean(self, timestamp):
        diff = timestamp - 300
        while self.head.next and self.head.next.val <= diff:
            self.head = self.head.next
            self.count -= 1


class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 300
        self.count = [0] * 300
        self.lastposition = 0
        self.lastime = 0
        self.sum = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.move(timestamp)
        self.count[self.lastposition] += 1
        self.sum += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.move(timestamp)
        return self.sum

    def move(self, timestamp):
        gap = min(timestamp - self.lastime, self.n)
        for i in range(gap):
            self.lastposition = (self.lastposition + 1) % self.n
            self.sum -= self.count[self.lastposition]
            self.count[self.lastposition] = 0

        self.lastime = timestamp
        math.ceiling(1.5)
        # Your HitCounter object will be instantiated and called as such:
        # obj = HitCounter()
        # obj.hit(timestamp)
        # param_2 = obj.getHits(timestamp)