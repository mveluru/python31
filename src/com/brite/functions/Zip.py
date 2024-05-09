##zip together first value to first value age

Names = ["John", "Smith", "George", "paul", "Ringo"]
Ages = [20, 21, 21, 23, 25]
for name, age in zip(Names, Ages):
    print(f"{name}: {age}")

# OR

for name, age in zip(Names, Ages):
    namevalue = name
    agevalue = age
    print(namevalue, ':', agevalue)
