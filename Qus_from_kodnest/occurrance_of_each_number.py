li = list(map(int, input().split()))
d = {}

for i in li:
    if i in d:
        d[i] = d[i] + 1
    else: 
        d[i] = 1

for num, count in d.items():
    print(f"{num} occurs {count} times(s)")

# 10 occurs 2 times(s)
# 30 occurs 3 times(s)
# 40 occurs 5 times(s)
# 20 occurs 8 times(s)