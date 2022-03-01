def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}

ans=sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print(ans)
ans2=sort_dict_by_value(d, True)
print(ans2)