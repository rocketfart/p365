import threading
import time
class solution:
    """ A lock object that allows many simultaneous "read locks", but
    only one "write lock." """

    def __init__(self):
        self.mutex = threading.RLock()
        self._read_ready = threading.Condition(self.mutex)
        self.reader = 0

    def acquire_read(self,x):
        """ Acquire a read lock. Blocks only if a thread has
        acquired the write lock. """

        while True:
            with self.mutex:
                self.reader += 1

            print('now read begin', x)
            time.sleep(0.001)
            print('now read end', x)

            with self.mutex:
                self.reader -= 1
                if not self.reader:
                    self._read_ready.notifyAll()

    def acquire_write(self,x):
        """ Acquire a write lock. Blocks until there are no
        acquired read or write locks. """
        while True:
            with self.mutex:
                while self.reader > 0:
                    self._read_ready.wait()

                print('now is writing', x)
                time.sleep(0.001)
                print('now writing ending', x)

    def test(self):

        t1=threading.Thread(target=self.acquire_read,args=[1])

        t2=threading.Thread(target=self.acquire_read,args=[2])

        t3=threading.Thread(target=self.acquire_write,args=[3])

        t4=threading.Thread(target=self.acquire_write,args=[4])
        t3.start()
        t1.start()
        t2.start()
        t4.start()

class solution4:

    """ A lock object that allows many simultaneous "read locks", but
    only one "write lock." """

    def __init__(self):
        self.mutex=threading.RLock()
        self.read = threading.Condition(self.mutex)
        self.write = threading.Condition(self.mutex)
        self.rw = 0
        self.wlist = 0

    def acquire_read(self, x):
        """ Acquire a read lock. Blocks only if a thread has
        acquired the write lock. """
        while True:
            with self.mutex:
                if self.rw<0 or self.wlist:
                    self.read.wait()
                self.rw+=1

            print('now read begin', x)
            time.sleep(1)
            print('now read end', x)



    def acquire_write(self, x):
        """ Acquire a write lock. Blocks until there are no
        acquired read or write locks. """
        while True:
            with self.mutex:
                if self.rw:
                    self.wlist+=1
                    self.write.wait()
                    self.wlist-=1
                self.rw-=1


            print('now is writing', x)
            time.sleep(1)
            print('now writing ending', x)


    def release(self):
        with self.mutex:
            if self.rw < 0:
                self.rw = 0
            else:
                self.rw -= 1

            wake_writer = self.wlist and self.rw == 0
            wake_reader = self.wlist == 0

        if wake_writer:
            with self.write:
                self.write.notify_all()
        if wake_reader:
            with self.read:
                self.read.notify_all()


    def test(self):

        t1 = threading.Thread(target=self.acquire_read, args=[1])

        t2 = threading.Thread(target=self.acquire_read, args=[2])

        t3 = threading.Thread(target=self.acquire_write, args=[3])

        t4 = threading.Thread(target=self.acquire_write, args=[4])

        t1.start()
        t2.start()
        t3.start()
        t4.start()


#type 2
class solution1:
    """ A lock object that allows many simultaneous "read locks", but
    only one "write lock." """

    def __init__(self):
        self.mutex = threading.RLock()
        self.can_read = threading.Condition(self.mutex)
        self.end_read = threading.Condition(self.mutex)
        self.can_write = threading.Condition(self.mutex)
        self.end_write = threading.Condition(self.mutex)
        self.reader=0
        self.writer=0
        self.writerlist=0





    def acquire_write(self,x):
        """ If no threads are reading or writing. """
        while True:
            with self.can_write:
                cur=threading.current_thread()
                self.writer+=1
                while self.grandwrite(cur):
                    self.can_write.wait()
                    self.writer-=1
                self.writerlist=cur

            print('now is writing', x)
            time.sleep(1)
            print('now writing ending', x)

            with self.end_write:
                self.writer-=1
                if self.writer==0:
                    self.writerlist=None
                self.end_write.notify_all()

    def grandwrite(self,cur):
        if len(self.readerlist)==1 and self.readerlist[cur]:
            return False
        if len(self.readerlist)>0: return True
        if self.writerlist==None: return False
        if self.writerlist!=cur:return True
        return False

    def test(self):

        t1=threading.Thread(target=self.acquire_read,args=[1])

        t2=threading.Thread(target=self.acquire_read,args=[2])

        t3=threading.Thread(target=self.acquire_write,args=[3])

        t4=threading.Thread(target=self.acquire_write,args=[4])
        t1.start()
        t3.start()
        t2.start()
        t4.start()

class solution2():
    def __init__(self):
        self.mutex = threading.RLock()
        self.can_read = threading.Semaphore(0)
        self.can_write = threading.Semaphore(0)
        self.active_readers = 0
        self.active_writers = 0
        self.waiting_readers = 0
        self.waiting_writers = 0

    def read(self,x):
        while True:
            with self.mutex:
                if self.active_writers == 0 and self.waiting_writers == 0:
                    self.active_readers += 1
                    self.can_read.release()
                else:
                    self.waiting_readers += 1
            self.can_read.acquire()

            print('now reading begin',x)
            time.sleep(1)
            print ('now reading end',x)

            with self.mutex:
                self.active_readers -= 1
                if self.active_readers == 0 and self.waiting_writers != 0:
                    self.active_writers += 1
                    self.waiting_writers -= 1
                    self.can_write.release()


    def write(self,x):
        while True:
            with self.mutex:
                if self.active_writers == 0 and self.waiting_writers == 0 and self.active_readers == 0:
                    self.active_writers += 1
                    self.can_write.release()
                else:
                    self.waiting_writers += 1
            self.can_write.acquire()

            print('now is writing',x)
            time.sleep(10)
            print('now is ending', x)

            with self.mutex:
                self.active_writers -= 1
                if self.waiting_writers != 0:
                    self.active_writers += 1
                    self.waiting_writers -= 1
                    self.can_write.release()
                elif self.waiting_readers != 0:
                    t = self.waiting_readers
                    self.waiting_readers = 0
                    self.active_readers += t
                    while t > 0:
                        self.can_read.release()
                        t -= 1
    def test(self):
        t1=threading.Thread(target=self.read,args=[1])

        t3 = threading.Thread(target=self.write, args=[3])

        t2=threading.Thread(target=self.read,args=[2])

        t4=threading.Thread(target=self.write,args=[4])

        t1.start()
        t2.start()
        time.sleep(10)
        t3.start()

class solution5:
    def __init__(self):

        self.mutex=threading.RLock()
        self.readlock=threading.Condition(self.mutex)
        self.writelock = threading.Condition(self.mutex)

        self.writer=0
        self.reader=0

    def read(self,x):
        while True:
            with self.mutex:
                if self.writer:
                    self.readlock.wait()
                self.reader += 1

            print('now reading begin', x)
            time.sleep(0.001)
            print('now reading end', x)

            with self.mutex:
                self.reader-=1
                if not self.reader:
                    self.writelock.notify_all()

    def write(self,x):
        while True:
            with self.mutex:
                if self.reader or self.writer:
                    self.writer+=1
                    self.writelock.wait()

                print('now is writing', x)
                time.sleep(0.001)
                print('now is ending', x)

                self.writer-= 1
                if self.writer:
                    self.writelock.notify_all()
                elif not self.writer:
                    with self.readlock:
                        self.readlock.notify_all()

    def test(self):

        t1 = threading.Thread(target=self.read, args=[1])

        t2 = threading.Thread(target=self.read, args=[2])

        t3 = threading.Thread(target=self.write, args=[3])

        t4 = threading.Thread(target=self.write, args=[4])

        t2.start()
        t3.start()
        time.sleep(2)
        t4.start()



case=solution5()
case.test()


