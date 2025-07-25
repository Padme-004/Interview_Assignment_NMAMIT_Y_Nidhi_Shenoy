#Run this file to check if the solution in problem1.py passes the following test cases:
#nums=[[3, 2, 3, 9], [1, 2, 3, 4], [1, 2, 3, -1], [1, 2, -3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], [0, 0, 0, 1]]

from problem1 import containsDuplicate1, containsDuplicate2
#I will use containsDuplicate2 here

tests=[[3, 2, 3, 9], [1, 2, 3, 4], [1, 2, 3, -1], [1, 2, -3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], [0, 0, 0, 1]]
expected_ans=[[True],[False], [False], [False], [True], [True]]
for i in range(len(tests)):
    print("Test case: ", tests[i])
    print("Expected answer: ", expected_ans[i])
    print("Answer given by candidate's solution: ")
    print(containsDuplicate2(tests[i]), end="\n\n")
