import secrets
import string
import time

start = time.time()
target = 100
randdomstring = ''.join(secrets.choice(string.ascii_letters+string.digits)
                        for i in range(target))
print(randdomstring)

print(time.time() - start)
