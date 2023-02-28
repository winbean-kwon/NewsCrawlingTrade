import csv 

duplicate_check = set()

with open('check_list.csv', 'r') as to_read:
  reader = csv.reader(to_read)
  for row in reader:
    print(row)
    duplicate_check.add(row[0])

print(duplicate_check)

print("duplicate_check:", duplicate_check)

# with open('test.csv', 'a', newline='') as to_write:
#   writer = csv.writer(to_write)
#   writer.writerow([])



a = tuple(['Proposal for election of new member for the Board of Directors'])
b = tuple(['Proposal for election of new member for the Board of Directors'])

print(a == b)
s = set()
s.add(a)
s.add(b)
print(s)
