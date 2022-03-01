def pluck(lst, key):
  return [x.get(key) for x in lst]


simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name': 'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]

res=pluck(simpsons, 'age')

print(res)