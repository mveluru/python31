phonesList = ['apple', 'samsung', 'oneplus', 'nokia']


phoneList_iter = iter(phonesList)
for item in phoneList_iter:
    print(item, end=' ')

print('\n***sorted***')
sortedlist = sorted(phonesList)
print(sortedlist)

print('\n***reverse order***')
print(sortedlist[::-1])

print('\n***specific position***')
print(sortedlist[0])
