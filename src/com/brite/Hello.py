def reverse_number(num):
    original_number = num
    reverse = 0
    for i in str(num):
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    print(f"Original Number: {original_number}")
    print(f"Reversed Number: {reverse}")


reverse_number(123456789)


def listcomp():
    myList = list(range(100))
    for item in myList:
        if item % 2 == 0:
            print(item, end=" ")
    print("\n")


listcomp()

myList1 = list(range(100))
filteredList = [item for item in myList1 if 10 < item < 50 and item % 3 == 0]
for item in filteredList:
    print(item, end=" ")

myString = 'My name is Muralidhar Veluru. I live in Boston'
print(myString.split('.'))
myString = myString.replace('.', '').lower()
print(myString)
