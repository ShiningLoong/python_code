class A:
    def __init__(self):
        print(A)


class B(A):
    def __init__(self):
        A.__init__(self)   # this self cannot be omitted
        pass


b = B()

