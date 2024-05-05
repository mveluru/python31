name = 'JOHNSMITH'
print(name)

print('***reverse string***')

rerversestring = name[::-1]
print(rerversestring)


def reverseString(string):
    rev = ''
    if len(string) > 1:
        rev = string[::-1]

    print(rev.strip(''))


reverseString('02221')


def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


print(reverse("JOHNSMITH"))
