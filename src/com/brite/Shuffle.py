import random
from typing import List


def shuffleelements():
    listitems = ['Z', 'B', 'A', 'D', 'C', 'K', 'L', 'Z', 'B', 'A', 'D', 'C', 'K', 'L']
    random.shuffle(listitems)
    print(listitems)


shuffleelements()

items = list(range(100))
print(items)
print(items[::-1])
