import csv
from functools import reduce

def count(predicate, itr):
  count_filter = filter(predicate, itr)  
  count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
  return count_reduce
  
with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')

  fields = next(reader)
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print(count_belgiums)
