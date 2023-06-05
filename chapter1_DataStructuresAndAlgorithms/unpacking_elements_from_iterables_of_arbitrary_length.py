# Problems:
## You need to unpack N elements from an iterable, but the iterable may be longer than N
## elements, causing a "too many values to unpack" exception.

user_record = ('Dave', 'dave@example.com', '7773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name, email, phone_numbers)

# The starred variable can also be the first one in the list
*trailing_qtrs, current_qtrs = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing_qtrs, current_qtrs)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)
    
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print(uname, fields, homedir, sh)


record = ('ACME', 50, 123.45, (12, 18, 2012))

name, *_, (*_, year) = record
print(name, year)