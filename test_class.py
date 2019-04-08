class animal():
    def eat():
        print("eating")
    def run(self):
        print("running")	

class mamalMixIn(animal):
	def eat(self):
	    print("%s is drinking milk"% self.name)
	

class beastMixIn(mamalMixIn):
    def hunt(self):
	    print("hunt for meat")
	
    def run(self):
        print("running with four legs")

class JumpableMixIn():
    def jump(self):
	    print("jump high")
		
class Tiger(beastMixIn,JumpableMixIn):
    def __init__(self,name):
	    self.name = name
    __slots__ = ('color','sex')
	
    @property
    def origin(self):
	    return self._origin
    
    @origin.setter
    def origin(self,value):
        self._origin = self.value
	

tiger1 = Tiger('tom')
#tiger1.jump()
tiger1.eat()
tiger1.color = "red"
tiger1.ss = 123
animal.eat()
