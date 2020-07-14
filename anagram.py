class A:
    b = 1
    def abc(self,c):
        print(self.b+c)
    @classmethod
    def xyz(cls,argument):
        cls.b=4
        print(cls.b+argument)
    @staticmethod
    def shakir():
        print("Hello World")




if __name__ == '__main__':
    a=A()
    a.b=5
    a.abc(2)
    a1=A()
    a1.abc(2)
#class method
    a.xyz(2)
    A.xyz(5)
    a2=A()
    a2.b=3
    a2.abc(5)
    a3=A()
    a3.abc(3)
a=filter(lambda a:a%2==0,[2,4,5,6])
a=list(a)
print(a)
