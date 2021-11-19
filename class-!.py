class human:
    x = "female"
    def __init__(self):

        self.y="Boy"
    def level(self):

        return self.y
    def __del__(self):
        return self.y



if "Male" in human.x:
    print("Boy or Man")

else:
    print("Girl or Women")
for i in human.x:
    print(i)

a=human()
print(a.level())

