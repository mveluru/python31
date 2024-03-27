class Union:
    info = "Dog has four legs and its Barks"

    def __init__(self, name, age):
        self.unionofset = set()
        self.name = name
        self.age = age

    def unionset(self, s):
        for i in s:
            self.unionofset = self.unionofset.union(i)
        return self.unionofset


listset = [{1, 2, 3, 4}, {4, 5, 6, 7}, {4, 5, 6, 7}, {1, 2, 3, 4}, {4, 5, 6, 7}, {4, 5, 6, 7}]
myunion = Union("puppy", 1)
newset = set()
newset = myunion.unionset(listset)
print(str(newset))
