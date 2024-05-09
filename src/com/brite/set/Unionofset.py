class Union:

    def __init__(self):
        self.unionofset = set()

    def unionset(self, listset):
        for i in listset:
            self.unionofset = self.unionofset.union(i)
        return self.unionofset


myunion = Union()


listset = [{1, 2, 3, 4}, {4, 5, 6, 7}, {4, 5, 6, 7}, {1, 2, 3, 4}, {4, 5, 6, 7}, {4, 5, 6, 7}]
newset = myunion.unionset(listset)

print(str(newset))
