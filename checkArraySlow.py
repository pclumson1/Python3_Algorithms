
# Given two arrays, a and b, calculate how many times the following is true:
# i <= j
# a[i] - b[j] = a[j] - b[i]

# This works on O(n^2) time
def checkArraysSlow(a, b):
  counter = 0
  for i in range(len(a)):
    for j in range(i, len(a)):
      if a[i] - b[j] == a[j] - b[i]:
        counter += 1
  
  return counter

# This doesn't work and it's as far as I got to on the GCA
def checkArraysNR(a, b):
  counter = 0
  dict = {}

  for i in range(len(a)):
    dict[a[i] + b[i]] = i
  
  for j in range(len(a)):
    if a[j] + b[j] in dict and dict[a[j] + b[j]] <= j:
      counter += 1
  
  return counter

# This works on O(n) time
def checkArrays(a, b):
  counter = len(a)
  dict = {}

  for i in range(len(a)):
    if a[i] + b[i] in dict:
      counter += dict[a[i] + b[i]]
      dict[a[i] + b[i]] += 1
    else:
      dict[a[i] + b[i]] = 1
  
  return counter

a = [2,1,5,3,6,3,0,7,-1,9,4,1]
b = [-1,1,1,3,9,7,7,0,-1,8,3,0]
print(checkArraysSlow(a, b))
print(checkArraysNR(a, b))
print(checkArrays(a, b))