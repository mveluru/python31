a = "abc"
alist = list(a)
b = "abcd"
blist = list(b)

for e in blist:
    if e in alist:
        alist.remove(e)
print(alist)
