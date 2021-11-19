class Human:

    mylist=["Olivia","Emma","Ava","Mia","Luna","Ella","Sofia"]


    def __init__(self,name,gender):
        self.n=name
        self.g=gender

    def deep_valid(self):
        if self.n in self.mylist:
            return "already exist"
    def valid(self):
       self.a=self.n
       self.b=self.g

       if self.a and self.b != None:
           if self.b==1:
               return "Male"
           else:
               return "Female"
           return "verified"
       else:

           return "Not verified"



x=input("enter name:")
y=int(input("enter Gender 1 for Male and 0 for Female:"))
obj=Human(x,y)
print(obj.deep_valid())
print(obj.valid())

