class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count = self.count + 1
            return self.count
        else:
            raise StopIteration

cd = Counter(5)
print(cd.__next__())        # or print(next(cd))        output: 1\

print(cd.__next__())        # 2
print(cd.__next__())        # 3
print(cd.__next__())        # 4
print(cd.__next__())        # 5
print(cd.__next__())        # StopIteration