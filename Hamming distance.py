def hamming_distance(a, b):
  return bin(a ^ b).count('1')

ans=hamming_distance(20, 100)
print(ans)