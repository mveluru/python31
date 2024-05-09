Names = ["John", "Smith", "George", "paul", "Ringo"]
Ages = [20, 21, 21, 23, 25]

# Dictionary
nameage = {}
for key in Names:
    for value in Ages:
        nameage[key] = value
        break

print(nameage)
