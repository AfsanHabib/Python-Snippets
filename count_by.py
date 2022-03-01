from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  print(dict(count))


from math import floor

count_by([6.1, 4.2, 6.3,8], floor) 
count_by(['one', 'two', 'three'], len) 


#--Groups the elements of a list based on the given function and returns the count of elements in each group.

#--Use collections.defaultdict to initialize a dictionary.

#--Use map() to map the values of the given list using the given function.

#--Iterate over the map and increase the element count each time it occurs.