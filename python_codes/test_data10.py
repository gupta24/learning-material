class Abc:
    stream = "cse"
    def __init__(self, std_name):
        self.name = std_name

    @classmethod
    def change_state(cls, val):
        cls.stream = val
        return cls.stream

    


a = Abc("rahul")
b = Abc("sumit")

Abc.change_state("new_ course")
print(a.name, b.name)
print(a.stream, b.stream)
a.stream = "abc"
print(a.stream, b.stream)
Abc.stream = "el"
print(a.stream, b.stream)
Abc.change_state("electric")
print(Abc.stream)
print(a.stream, b.stream)