# Run this file to check if the code in problem2.py passes the following test cases
# nums= [[0, 1, 0, 4, 21], [0, 1, 0, 3, 12], [1, 2, 3, 4], [0, 0, 0, 0]]

from problem2 import moveZeroes1, moveZeroes2
#I will use moveZeroes2 as it is more optimal

tests= [[0, 1, 0, 4, 21], [0, 1, 0, 3, 12], [1, 2, 3, 4], [0, 0, 0, 0]]
expected_ans= [[1, 4, 21, 0, 0], [1, 3, 12, 0, 0], [1, 2, 3, 4], [0, 0, 0, 0]]
for i in range(len(tests)):
    print("Test case: ", tests[i])
    print("Expected answer: ", expected_ans[i])
    moveZeroes2(tests[i])
    print("Test case array after in-place operation by candidate's solution: ")
    print(tests[i], end="\n\n")
