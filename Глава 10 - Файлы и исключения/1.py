class Name:

    def __init__(self, first, last):
        self.first_n = first
        self.last_n = last

    def first_name(self):
        name = self.first_n
        return name.title

    def last_name(self):
        print(f"{self.last_n}")

    def full_name(self):
        name = f"{self.first_n} {self.last_n}"
        print(name.title())



    def initials(self):
        name = f"{self.first_n[0]}.{self.last_n[0]}"
        print(name.title())


a1 = Name('john', 'SMITH')
print(a1.first_name())
a1.last_name()
a1.full_name()
a1.initials()

