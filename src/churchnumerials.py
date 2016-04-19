# -*- coding: utf-8 -*-

zero = lambda f:lambda x:x

succ = lambda n: lambda f: lambda x:f ((n)(f)(x))
add = lambda m: lambda n: lambda f: lambda x:m (f)((n)(f)(x))
multi = lambda m: lambda n: lambda f: lambda x:m ((n)(f))(x)
exp = lambda m: lambda n: lambda f: lambda x:((n)(m)) (f) (x)

#Funkcja zamienia liczebnik Churcha na liczbe calkowita, wykorzystujac funkcje f(x) = x+1.
#Przyklad: 3 = f (f (f (x)))) = f (f (f (0)))) = ((x + 1) + 1) + 1) = ((0 + 1) + 1) + 1) = 3
def church_to_int(churchNum):
    return churchNum(lambda x:x+1)(0)

#Funkcja zwraca liczbe x w postaci liczebnika Churcha, np. 3 = f (f (f (x)))) = f^3 (x)
def int_to_church(x):
    if x==0:
        return zero
    else:
        return succ(int_to_church(x-1))

#Przyklady
a = 4
b = 5

print church_to_int(zero), " <- powinno wypisac 0"
print church_to_int(succ(int_to_church(a))), " <- powinno wypisac %d" % (a+1)
print church_to_int(add(int_to_church(a))(int_to_church(b))), " <- powinno wypisac %d" % (a+b)
print church_to_int(multi(int_to_church(a))(int_to_church(b))), " <- powinno wypisac %d" % (a*b)
print church_to_int(exp(int_to_church(a))(int_to_church(b))), " <- powinno wypisac %d" % (pow(a,b))