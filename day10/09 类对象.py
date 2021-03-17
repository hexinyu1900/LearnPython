class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃美食" % self.name)


print(Person)
print(id(Person))