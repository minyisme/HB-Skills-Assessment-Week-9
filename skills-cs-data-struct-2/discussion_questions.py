# Recursion:
# 1. Recursion is something that calls itself.
# 2. It's necessary to have a base case so that recursion doesn't go on forever.

# Graphs:
# 1. A graph 
# 2. A tree is acyclical (has a heirarchy) while graphs can be cyclical.
# 3. Facebook friends.

# Runtime of Data Structures:
# Data Structure                  Index   Search  Add-R   Add-L   Pop-L   Pop-R
# Python List (Array)             O(1)    O(n)    O(1)    O(n)    O(n)    O(1)
# Linked List                     O(n)    O(n)    O(n)    O(1)    O(1)    O(1)     
# Doubly-Linked List              O(n)    O(n)    O(1)    O(1)    O(1)    O(1)         
# Queue (as Array)                X       X       O(1)    X       O(n)    X
# Queue (as LL or DLL)            X       X       O(1)    X       O(1)    X
# Stack (as Array, LL, or DLL)    X       X       O(1)    X       O(1)    X    
# Deque (as DLL)                  X       X       O(1)    O(1)    O(1)    O(1)        

# Runtime of More Data Structures:
# Data Structure          Get         Add     Delete  Iterate     Memory
# Dictionary (Hash Map)   O(1)        O(1)    O(1)    O(n)        medium
# Set (Hash Map)          O(1)        O(1)    O(1)    O(n)        medium         
# Binary Search Tree      O(log(2)n)  O(n)    O(n)    O(1)        small          
# Tree                    O(n)        O(1)    O(1)    O(1)        small 

# Sorting:
# 1. Bubble Sort algorithm iterates over a list by pairs and sorts the small to the left and big to the rights. In each iteration over the list, the biggest number gets sorted to the right most. So it needs to iteratre over the entire list (minus the last element) a len(list) times.
# 2. Merge Sort first recursively divides a list into lists of a single number (which is always sorted). Then it (in each level of recursion) merges each pair of sorted lists by always popping the smallest of the two lists' zero-th item and appending to the merged list.
# 3. In quick sort, a random item is chosen, and all other items are compared to it, with putitng larger items to the right and smaller items to the left. then that random item is sorted. Then this process is repeated in each still unsorted half recursively.

# Git Branching:
# 1. When multiple people are working together on a project and they're each doing a smaller piece.
# 2. A pull request is when you request an owner of a repository to pull up your changes to their github branch and to merge them into their repository.