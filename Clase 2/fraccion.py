
def mcd(n1,n2):
    """algoritmo de euclides 
    si a > b > 0   a = b * q + r  ==>> mcd(a.b)=mcd(b,r)"""
    if n1>n2:pass
    else:
        aux = n2
        n2 , n1 = n1 , aux
    while n1 % n2 !=0:
        n1 ,n2  = n2 , n1 % n2
    return n2

class Fraccion:
    def __init__(self,num,den=1):
        self.num = int(num)
        self.den = int(den)

    def __str__(self):
        a = mcd(self.num,self.den)
        self.num /= a
        self.den /= a
        if self.den < 0 and self.num > 0: self.num *=-1 ; self.den *=-1
        entero = self.num // self.den
        if entero > 0:
            resto=self.num % self.den
            if resto > 0:
                return "{0} {1}/{2}".format(int(entero),int(resto),int(self.den))
            else:
                return "{0}/1".format(entero)
        else:
            return "{0}/{1}".format(int(self.num),int(self.den))

    def numero(self):
        return self.num / self.den

    def __add__(self, other):
        s = Fraccion(0,0)
        s.num = (self.num * other.den) + (other.num * self.den)
        s.den = self.den * other.den
        return s

    def __sub__(self, other):
        if self == other:return 0
        s = Fraccion(0,0)
        s.den = self.den * other.den
        s1 = int(s.den / self.den)
        s2 = int(s.den / other.den)
        s.num = (self.num * s1) - (other.num * s2)
        return s

    def __mul__(self,other):
        r = Fraccion(0,0)
        r.num = self.num * other.num
        r.den = self.den * other.den
        return r

    def __truediv__(self, other):
        s = Fraccion(0,0)
        s.num = self.num * other.den
        s.den = self.den * other.num
        return s

    def __gt__(self, otro):
        if self.numero()>otro.numero():return True
        return False

    def __it__(self,otro):
        if self.numero()<otro.numero():return True
        return False

    def __le__(self,otro):
        if self.numero()<=otro.numero():return True
        return False

    def __eq__(self,otro):
        if self.numero() == otro.numero():return True
        return False

    def __ge__(self,otro):
        if self.numero()>=otro.numero():return True
        return False

    def __ne__(self,otro):
        if self.numero() != otro.numero():return True
        return False

if __name__ == "__main__":
    f=input("Ingresa la primera fraccion [a/b]: ")
    try:
        g = f.split("/")
        f1 = Fraccion(int(g[0]),int(g[1]))
    except :
        f1 = Fraccion(int(f))
    f=input("Ingresa la segunda fraccion [c/d]: ")
    try:
        g = f.split("/")
        f2 = Fraccion(int(g[0]),int(g[1]))
    except :
        f2 = Fraccion(int(f))
    print("La suma es ",f1+f2)
    print("La resta es ",f1-f2)
    print("La multiplicación es ",f1*f2)
    print("La división es ",f1/f2)
    print(f1," Es  :", f1.numero())
    print(f2," Es  :", f2.numero())
    print(f1==f2,"igauldad")
    print(f1!=f2,"desigauldad")
    print(f1<f2,"menor")
    print(f1<=f2,"menor igual")
    print(f1>f2,"mayor")
    print(f1>=f2,"mayor igual")



