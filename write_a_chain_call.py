class Chain():
    def __init__(self, name):
        self.name = name

    def __getattr__(self, new_attr):
        if new_attr == "user":
            return Chain(self.name)
        return Chain(self.name + '/' + new_attr)

    def __str__(self):
        return self.name

    def __call__(self, para):
        return Chain(self.name + '/' + para)


root = Chain("home")
print(root.get.whatIneed.sell.done)
print(root.user('Tommy').get.whatIneed.sell.done)