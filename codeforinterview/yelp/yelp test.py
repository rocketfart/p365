class Business():
    def __init__(self,id,rating):
        self.id=id
        self.rating=rating




list1=[Business(101,1),Business(102,5),Business(103,5)]

'''list=[{'id': 101, rating: 5},
{'id': 102, rating: 2},
{'id': 103, rating: 3},
{'id': 104, rating: 5},
{'id': 105, rating: 5}]'''


list1=sorted(list1,key=lambda x: x.rating,reverse=True)

print [i.id for i in list1]