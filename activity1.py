class Myclass: 
    __privatevar = 27


    def privmeth(self):
        print("in am in class my class")
    
    def hello(self):
        print("private variable value: ",Myclass.__privatevar)

foo = Myclass()

foo.hello()

foo.__privmeth()
    

