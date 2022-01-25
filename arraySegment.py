# You are given an array of integers arr. Your task is to count the number of contiguous subarrays, such that each element of the subarray appears at least twice.

# Example

# For arr = [0, 0, 0], the output should be duplicatesOnSegment(arr) = 3.

# There are 3 subarrays that satisfy the criteria of containing only duplicate elements:

# arr[0..1] = [0, 0]
# arr[1..2] = [0, 0]
# arr[0..2] = [0, 0, 0]
# For arr = [1, 2, 1, 2, 3], the output should be duplicatesOnSegment(arr) = 1.

# There is only 1 applicable subarray: arr[0..3] = [1, 2, 1, 2].
def duplicatesOnSegment(a):
  if not a or len(a) == 0:
    return 0

  counter = 0
  for s in range(len(a) - 1): # O(n)
    for e in range(s + 1, len(a)): # O(n)
      sub = a[s:e + 1] # O(n)
      unique = 0
      dict = {}
      for v in sub: # O(n)
        if v in dict:
          dict[v] += 1
          unique -= 1
        else:
          dict[v] = 1
          unique += 1
      if unique <= 0:
        counter += 1
  
  return counter
    
  
# Time Complexity: # O(n^3)