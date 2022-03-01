from datetime import timedelta, date

def daterange(start, end):
  return [start + timedelta(n) for n in range(int((end - start).days))]


k=daterange(date(2020, 10, 1), date(2020, 10, 5))
print(*k)
