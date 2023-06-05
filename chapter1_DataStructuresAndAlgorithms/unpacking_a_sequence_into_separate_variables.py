# Problems:
## You have an N-element tuple or sequence that you would like to unpack into a collection
## of N variables

p = (4, 5)
x, y = p
print(x, y)

data = ['ACME', 50, 91.1, (2021, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

# discard certain values
_, shares, price, _, date = data