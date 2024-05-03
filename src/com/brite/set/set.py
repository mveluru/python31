#  python Set examples
#  Doesn't guarantee the order

mySet = {'a', 'b', 'c', 'd'}
print(mySet)
print('***set doesn''t guarantee the order')

for item in mySet:
    print(item, end=' ')

while len(mySet):
    mySet.pop()

intset = set()

print("\n")
for item in range(1, 200):
    if item % 5 == 0:
        intset.add(item)
print(intset)

# Remove an element
intset.discard(50)
print(sorted(intset))
