fruitandveg = {'a': 'Apple', 'b': 'blueBerries', 'c': 'carrot', }
print(fruitandveg)

# print specific element
print(fruitandveg['a'])

for key, value in fruitandveg.items():
    print(f"{key} : {value}")

# converting list of tuples to dictionary
fruitandveg = [('a', 'Apple'), ('b', 'blueBerries'), ('c', 'carrot')]
print({key: value for key, value in fruitandveg})

# Delete specific element

myDict = {'firstname': 'Muralidhar', 'middlename': 'Reddy', 'lastName': 'Veluru'}
for key, value in myDict.items():
    if key.__eq__('firstname'):
        print(value)
