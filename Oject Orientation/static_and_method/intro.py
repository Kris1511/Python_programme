class Student:
    def learn(self):
        print(self.name , 'Inside learn method')

    def play():
        print('Inside play method')

s1 = Student()              
# s1.play()                           # TypeError: play() takes 0 positional arguments but 1 was given
s1.name = 'John'
print(s1.name)                      # John

s1.learn()                          # Inside learn method method is after the object creation
