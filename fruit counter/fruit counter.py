fruit = ["apple", "apple", "banana", "banana", "strawberry", "kiwi", "peach", "peach", "peach"]

d = {}

for f in fruit:
    if f in d:
        d[f] = d[f] + 1
    else:
        d[f] = 1
print(d)