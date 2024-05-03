#  python Set examples
#  Doesn't guarantee the order

mySet = {'a', 'b', 'c', 'd'}
for item in mySet:
    print(item, end=' ')

while len(mySet):
    mySet.pop()

print("\n")
for item in range(100):
    if item % 5 == 0:
        mySet.add(item)
print(mySet)

# Remove an element
mySet.discard(50)
print(mySet)
