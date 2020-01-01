import sort
import random

print("Making lists...")
aList = []
lengthA = 1e4
for _ in range(int(lengthA)):
    aList.append(random.randint(0, 1000))

bList = []
lengthB = 1e4
for i in range(int(lengthB)):
    bList.append(random.randint(0 if i-50 < 0 else i-50, i))

print("Running sort...")
selRes, selTime = sort.sort(aList.copy(), "selection", True)
insRes, insTime = sort.sort(aList.copy(), "insertion", True)
shlRes, shlTime = sort.sort(aList.copy(), "shell", True)
selResB, selTimeB = sort.sort(bList.copy(), "selection", True)
insResB, insTimeB = sort.sort(bList.copy(), "insertion", True)
shlResB, shlTimeB = sort.sort(bList.copy(), "shell", True)

print("Verifying...")
verified = selRes == insRes == shlRes
verifiedB = selResB == insResB == shlResB

print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Sorting Result Comparison
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Task 1: fake-random
------------------------------------
Run result is {0}.
Task length: {1} fake-random values.

----------------------------
Sort Type         | Time
----------------------------
Selection Sorting | {4:.5f}s
Insertion Sorting | {6:.5f}s
Shell Sorting     | {8:.5f}s
----------------------------

Task 2: semi-sort
------------------------------------
Run result is {2}.
Task length: {3} semi-sorted values.

----------------------------
Sort Type         | Time
----------------------------
Selection Sorting | {5:.5f}s
Insertion Sorting | {7:.5f}s
Shell Sorting     | {9:.5f}s
----------------------------
""".format("verified" if verified else "unverified", len(aList), "verified" if verifiedB else "unverified", len(bList), selTime, selTimeB, insTime, insTimeB, shlTime, shlTimeB))
