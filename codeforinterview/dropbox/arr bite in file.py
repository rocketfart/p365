import hashlib

file = open('arrfile', 'r+')
arr='2.7'

def run():
    m=len(arr)
    h=hashlib.md5()
    h.update(arr)
    code=h.hexdigest()

    file.seek(0, 2)
    size = file.tell()

    for i in range(size):
        file.seek(i)
        r=file.read(m)

        while r and len(r)==m:
            x = hashlib.md5()
            x.update(r)
            newcode = x.hexdigest()
            if newcode==(code):
                return True
            r=file.read(m)
    return  False

print run()




