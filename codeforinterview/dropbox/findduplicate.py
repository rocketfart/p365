#path=list of string
#File class method: boolean isDirectory(), boolean isFile(), String[] list(), long length(), read(buffer, offset, size)
import collections
import hashlib
from mimify import File

import io


def findpaths(path):
#1  filelist=[]
    while path:
        cur=path.pop()
        curfile=File(cur)
        if curfile.isFile():
#1          filelist.append(curfile)

#2          size=curfile.lenth()
#2          hmap[size].append(curfile)
        else:
            if curfile.isDirectory():
                sub=file.list()
                for s in sub:
                    newpath=Paths.get(cur,s)
                    path.append(newpath)
#2  return [v for v in hmap if len(v)>1]
#1  return filelist

def findduplicate(path):

    if not path: return []
    filelist=findpaths(path)
    hmap=collections.defaultdict(list)
#1
    for f in filelist:
        hashing=hashlib.md5(f)
        hmap[hashing].append(f)

    return {m for m in hmap.values if len(m)>1}
#2
    for fs in filelist:
        for f in fs:
            hashing=hashlib.md5(f)
            hmap[hashing].append(f)
    return {m for m in hmap.values if len(m) > 1}

# findpths, we only get the one which has same size in paths
def findpaths2(path):

    hmap=collections.defaultdict(list)
    while path:
        cur=path.pop()
        curfile=File(cur)

        if curfile.isFile():
            size=curfile.lenth()
            hmap[size].append(curfile)
        else:
            if file.isDirectory():
                sub=file.list()
                for s in sub:
                    newpath=Paths.get(cur, s)
                    path.append(newpath)

    return [v for v in hmap if len(v)>1]

# devide file into 1kb,每次hash 那一kb
curfile=File(cur)
read=io.open(curfile,'rb',1024)
hash=hash(read)
