from math import floor, log

def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start) / log(step)) + 1)]

res=geometric_progression(256, 3)
print(res)


#_____arithmetic_progression______
'''
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
arithmetic_progression(5, 25)
#_____________________________