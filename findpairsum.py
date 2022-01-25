# Given a square matrix of positive integers a, your task is to sort the numbers in each of its diagonals parallel to the secondary diagonal. Each diagonal should contain the same set of numbers as before, but sorted in ascending order from the bottom-left to top-right.
# For

# a = [[1, 3, 9, 4],
#      [9, 5, 7, 7],
#      [3, 6, 9, 7],
#      [1, 2, 2, 2]]
# the output should be

# diagonalsSort(a) = [[1, 9, 9, 7],
#                     [3, 5, 6, 9],
#                     [3, 4, 7, 7],
#                     [1, 2, 2, 2]]


# 4
# Given an array of integers a, your task is to find how many of its contiguous subarrays of length m contain a pair of integers with a sum equal to k.

# More formally, given the array a, your task is to count the number of indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains at least one pair (a[s], a[t]), where:

# s ≠ t
# a[s] + a[t] = k
# Example

# For a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output should be findPairsSummingToK(a, m, k) = 5.

# Let's consider all subarrays of length m = 4 and see which fit the description conditions:

# Subarray a[0..3] = [2, 4, 7, 5] doesn't contain any pair of integers with a sum of k = 10. Note that although the pair (a[3], a[3]) has the sum 5 + 5 = 10, it doesn't fit the requirement s ≠ t.
# Subarray a[1..4] = [4, 7, 5, 3] contains the pair (a[2], a[4]), where a[2] + a[4] = 7 + 3 = 10.
# Subarray a[2..5] = [7, 5, 3, 5] contains two pairs (a[2], a[4]) and (a[3], a[5]), both with a sum of k = 10.
# Subarray a[3..6] = [5, 3, 5, 8] contains the pair (a[3], a[5]), where a[3] + a[5] = 5 + 5 = 10.
# Subarray a[4..7] = [3, 5, 8, 5] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[5..8] = [5, 8, 5, 1] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[6..9] = [8, 5, 1, 7] doesn't contain any pair with a sum of k = 10.
# So the answer is 5, because there are 5 contiguous subarrays that contain a pair with a sum of k = 10.

def findPairsSummingToK(a, m, k):
  counter = 0
  have = {}

  for i, n in enumerate(a):
    if i > m - 1:
      if have.get(a[i - m], 0) <= 1:
        have.pop(a[i - m], None)
      else:
        have[a[i - m]] -= 1
    
    if k - n in have:
      counter += 1 # may want to track the index
    
    have[n] = have.get(n, 0) + 1
  
  return counter

example = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
findPairsSummingToK(example, 4, 10)

# From Jonathan Mary:
from collections import deque
def findPairs(a, m, k):
  count = 0
  # store will store combinations that make k
  store = []
  dq = deque(a[0:4])
  # populate the deque withy first 4 values.
  for i in range(4):
    if (k - a[i]) in a[i + 1:4]:
      store.append(a[i])
      store.append(a[k - a[i]])
  if store != []:
    count += 1
  # update deque and store at each value
  for x in a[4:]:
    dq.append(x)
    pp = dq.popleft()
    if k - x in dq:
      store.append(x)
      store.append(k - x)
    if k - pp in dq:
      store.remove(pp)
      store.remove(k - pp)
    if store != []:
      count += 1
    print('dq:', dq, 'store:', store, count)
  return count
findPairs([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10)