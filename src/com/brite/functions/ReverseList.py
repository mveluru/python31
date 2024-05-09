Names = ["John", "Smith", "George", "paul", "Ringo"]
print('\nGiven Order')
print(Names)

print('\nReversed Order')
print(Names[::-1])

print('\nReversed Order using for loop reversed(Names)')
for name in reversed(Names):
    print(name, ',', end="")

print('\n Natural Sort order')
print(sorted(Names))

# enumerate to know the index of each element
print('\n')
for i, name in enumerate(Names):
    print(f"{i} {name}")
