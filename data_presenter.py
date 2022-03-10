#2.
open_file = open("CupcakeInvoices.csv");

#3.
for row in open_file:
    print(row);

#4.
for row in open_file:
    values = row.split(',')
    print(values[2]);

#5.
for row in open_file:
  values = row.split(',')
  total = int(values[3]) * float(values[4]);
  
  print(total);

#6.
total_all = 0;

for row in open_file:
    values = row.split(',')
    total = total + (int(values[3]) * (values[4]));

print(total_all);

open_file.close();