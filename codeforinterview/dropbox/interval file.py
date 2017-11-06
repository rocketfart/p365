chunks=[[0,1],[2,3],[3,4]]
size=4

def merge(chunks,size):
    res=[]
    for i in chunks:
        if not res:
            res.append(i)
        elif res[-1][1]>=i[0]:
            res[-1][1]=max(res[-1][1],i[1])
        else:
            res.append(i)

    return len(res)==1 & (res[0][1]-res[0][0]==size)

#print merge(chunks,size)
import bintrees

tree=bintrees.AVLTree()
treeb=bintrees.BinaryTree()
getSeccessor
getpredecessor

def insert(one):
    if not tree:
        tree.insert(one[0],one)
    else:
        start=one[0]
        tree.insert(start,one)

        pre=tree[start].getSeccessor()
        post=tree[start].getpredecessor()

        # key=start
        #can combine pre and post
        if pre and post and tree[pre][1]==tree[start][0] and tree[post][0]==tree[start][1]:
            tree[pre][1]=tree[start][1]
            tree[pre][1]=tree[post][1]
            tree.remove(start)
            tree.remove(post)
        #can combine only pre
        elif pre and tree[pre][1] == tree[start][0]:
            tree[pre][1] = tree[start][1]
            tree.remove(tree[start])
        #can combine only post
        elif pre and tree[post][0]==tree[start][1]:
            tree[start][1] = tree[post][1]
            tree.remove(tree[post])

def isfull(tree):
    #size==1 and substract between them are the size of full
    return tree.len()==1 and tree[0][1]-tree[0][0]==size

