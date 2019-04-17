class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        A.__init__(self)
        print('B')# this self cannot be omitted
        pass


class B2(A):
    def __init__(self):
        A.__init__(self)
        print('B2')# this self cannot be omitted
        pass


class C(B, B2):
    def __init__(self):
        B.__init__(self)
        B2.__init__(self)
        print('C')


c = C()

print("_______________________________________________")


class B1_super(A):
    def __init__(self):
        super().__init__()
        print("B1")


class B2_super(A):
    def __init__(self):
        super().__init__()
        print("B2")


class C_super(B1_super, B2_super):
    def __init__(self):
        super().__init__()  # super does not need to pass "self"
        print("C")


c_super = C_super()
print(C_super.__mro__)

# calling sequence of init method is the reverse of the MRO list
# with super() we don't need to bother with every init method of base classes, just one super() is enough
# with super() the we also avoid to repeatedly call the same base class's init method
print("_______________________________________________")

