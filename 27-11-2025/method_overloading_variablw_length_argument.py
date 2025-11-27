class Mathops:
    def add(self, *args):
        return sum(args)

m=Mathops()
print(m.add(1))
print(m.add(2,3))
print(m.add(2,3, 4))