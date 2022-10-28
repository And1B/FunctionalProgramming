import csv
from functools import reduce

def average(itr):  
  iterable = iter(itr)
  return avg_helper(0, iterable, 0)

def avg_helper(curr_count, itr, curr_sum):
  next_num = next(itr, 'null')
  if next_num == 'null':
    return curr_sum / curr_count
  curr_count += 1
  curr_sum += next_num
  return avg_helper(curr_count, itr, curr_sum)


with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')

  fields = next(reader)
  csvfile.seek(0)
  avg_portugal = average(map(lambda x: float(x[13]),filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)
