import bitarray
class solution:
    def __init__(self,max):
        self.bitarray=bitarray(max)
        self.bitarray.setall(False)
        self.max=max

    def get(self):
        self.bitarray.