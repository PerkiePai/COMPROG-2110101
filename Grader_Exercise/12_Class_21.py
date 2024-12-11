class Complex :
    def __init__(self,a,b):
        self.real=a
        self.ima=b
    def __str__(self):
        out=''
        if self.ima==0:
            return str(self.real)
        elif self.real==0:
            return str(self.ima)+'i'
        elif self.ima>0:
            return str(self.real)+'+'+str(self.ima)+'i'
        else:
            return str(self.real)+'-'+str(self.ima)+'i'
        
    def __add__(self, rhs):
        return Complex(self.real+rhs.real,self.ima+rhs.ima)
    def __mul__(self, rhs):
        return Complex(self.real*rhs.real-self.ima*rhs.ima,self.real*rhs.ima+rhs.real*self.ima)
    def __truediv__(self, rhs):
        return 
    
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)
