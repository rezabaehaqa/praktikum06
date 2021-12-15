import math
print ('latihan 6')
print('============')
#1. asli
print('\n number 1 :')
def a(x):
    return x**2

print(a(6))

#lambda
a=lambda x: (x**2)

print(a(6))

#2. asli 
print('\nnumber 2 :')
def b(x,y):
    return math.sqrt(x**2 + y**2)

print(b(2,3))

#lambda
b=lambda x,y: math.sqrt(x**2 + y**2)
print(b(2,3))

#3. asli
print('\nnumber 3 :')
def c(*args):
    return sum(args)/len(args)
print(c(8))
#lambda
c=lambda *args:sum(args)/len(args)
print(c(8))

#4. asli
print('\nnumber 4 :')
def d(s):
    return "".join(set(s))
print(d("Reza Baehaqa"))
#lambda
d=lambda s: "".join(set(s))
print(d("Reza Baehaqa"))