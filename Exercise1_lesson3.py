#Анонимные, Lambda function

'''
def f(x):
    x**3
g = f
print(type(f(2)))
print(type(g(2)))

def f(x):
    return x**2
print(f(3))

def f(x):
    return x+22
print(f(3))

def f1(x):
    return x*20
print(f1(3))

def calc(x):
    return operation

def math(op,x):
    return op(x)
print(math(f1,3))
'''
'''
def sum(x,y):
    return x+y
f = sum
f = lambda x,y:x+y
sum = lambda x, y: x+y

def mult(x,y):
    return x*y
mult = lambda x, y: x*y
def calc(op, a, b):
    print(op(a,b))

calc(sum, 10, 12)
calc(lambda x, y: x+y, 10,12)

calc(mult, 10, 12)
calc(lambda x, y: x*y,10,12)
'''
#List Comprehension
'''
list=[]
for i in range(1,101):
    if i%2==0:
        list.append(i)
print(list)
print()

list = [i for i in range(1,31) if i%2==0]
print(list)
print()
list = [(i,i,i**2,) for i in range(1,31) if i%2==0]
print(list)

def f(x):
    return x**2
list = [(i,f(i),i**3) for i in range(1,21) if i%2==0]
print(list)
'''
'''
Ex1: В файле храняться числа. Нужно выбрать из них четные и составить список пар(число, квадрат числа)
Например:
[1 2 3 5 8 15 23 38]
->
[(2,4) (8,64) (38,1444)]
'''
def cvad(x):
    return x*x
list = [1, 2, 3, 5, 8, 15, 23, 38]
list_par = [(i,cvad(i)) for i in list if i%2==0]
print(list_par)
