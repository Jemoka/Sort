import sort
import random

print("Making list...")
aList = []
for _ in range(int(3e4)):
    aList.append(random.randint(0, 1000))

print("Running sort...")
print(sort.sort(aList, "selection", True)[1])
print(sort.sort(aList, "insertion", True)[1])

