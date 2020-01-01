import sort
import random

print("Making list...")
aList = []
length = 1e4
for _ in range(int(length)):
    aList.append(random.randint(0, 1000))

print("Running sort...")
selRes, selTime = sort.sort(aList.copy(), "selection", True)
insRes, insTime = sort.sort(aList.copy(), "insertion", True)
shlRes, shlTime = sort.sort(aList.copy(), "shell", True)
breakpoint()

print("Verifying...")
verified = selRes == insRes

print("""
-=-=-=-=-=-=-=-=-=-=-=-=-=
Sorting Result Comparison
-=-=-=-=-=-=-=-=-=-=-=-=-=
Run result is {0}.
Task length: {1} values.

----------------------------
Sort Type         | Time
----------------------------
Selection Sorting | {2:.5f}s
Insertion Sorting | {3:.5f}s
----------------------------
""".format("verified" if verified else "unverified", length, selTime, insTime))
