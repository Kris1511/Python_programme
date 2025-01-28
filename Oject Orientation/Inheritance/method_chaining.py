# Method chaining is a mechanism to call one methods from another methods.

class GrandParent:
    def cook(self):
        print('GrandParent is cooking biryani')

class Parent(GrandParent):
    def cook(self):
        print('Parent is cooking pulav')

class Child(Parent):
    def cook(self):
        print('Child is cooking noodles')
        super().cook()
        super(Parent, self).cook()

c = Child()
c.cook()            # Child is cooking noodles
                    # Parent is cooking pulav
                    # GrandParent is cooking biryani