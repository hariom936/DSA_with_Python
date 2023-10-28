'''
Set is a collection which is unordered, unchangeable*, and unindexed.
No duplicate members.
'''

thisset1 = {"apple", "banana", "cherry"}
print(thisset1)

#Duplicate values will be ignored:

thisset2 = {"apple", "banana", "cherry", "apple"}
print(thisset2)

#True and 1 is considered the same value:
thisset3 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset3)
print(len(thisset3))
print(type(thisset3))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1,set2, set3)