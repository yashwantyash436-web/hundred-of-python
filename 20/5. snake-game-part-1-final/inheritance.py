class animal():
    
    def eyes(self):
        self.no_of_eyes=2
        
    def breadth(self):
        print("inhale andc exhale")
    
    
class fish(animal):
    def __init__(self):
        super().__init__()
        
    def swim(self):
        print("i know to swim")
        
nemo=fish()
nemo.swim()
nemo.breadth()
nemo.eyes()
print(nemo.no_of_eyes)
        