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
'''
def cvad(x):
    return x*x
list = [1, 2, 3, 5, 8, 15, 23, 38]
list_par = [(i,cvad(i)) for i in list if i%2==0]
print(list_par)
'''
'''
def f(x):
    return x**2
print(f(5))
print(type(f))
g=f
print(f(6))
print(g(6))
print(type(g))
'''
'''
def f1(x):
    return x**2

def f2(x):
    return x+20

def f3(x):
    return x-30

def f4(x):
    return x**3

def math(f, x):
    print(f(x))
math(f1, 50)
math(f2, 50)
math(f3, 50)
math(f4, 50)
'''
# list comrehension
'''
list = []
for i in range(1,21):
    if i%2==0:
        list.append(i)
#print(list)
list = [i for i in range(1,21) if i%2==0]
print(list)
print([i for i in range(1,21) if i%2==0])
print([(i, i, i**2) for i in range(1,21)])

def f(x):
    return x**3
print([(i, i**2, f(i)) for i in range(1,11) if i%2!=0])
'''
# В файле храняться числа,нужно выбрать из них четные и составить список пар(числоб квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38 -> [(2,4), (8, 64), (38, 1444)]
'''
#variant1
f = open('file1.txt', 'r')

data=f.read()
print(data)
print(type(data))
res=data.split()
print(res)
res1=[]
for x in res:
    if int(x)%2==0:
        res1.append((int(x),(int(x))**2))
print(res1)
'''
'''
#variant2
fun = open('file1.txt', 'r').read()
data = fun.split()
print(data)
def func1(f, col):
    return [f(x) for x in col]
res=func1(int, data)

def func2(f2, col):
    return [x for x in col if f2(x)]
res=func2(lambda x: x%2==0, res)
print(res)
res=func1(lambda x: (x, x**2), res)
print(res)
'''
'''
list1 = [x for x in range(1,21)]
print(list1)
list2 = list(map(lambda x: x**2, list1))
print(list2)
'''
'''
list = list(map(int,input().split()))
print(type(list))
print(list)
'''
'''
#variant3
data = open('file1.txt', 'r')
text = data.read()
list_st=text.split()
print(list_st)
list1 = list(map(int, list_st))
print(list1)
list1 = list(filter(lambda x: x%2==0, list1))
print(list1)
list1=list(map(lambda x: (x, x**2), list1))
print(list1)
'''
# zip- , enumerate-
'''
list1 = ['som', 'don', 'ert', 'jok']
list2 = [12, 23, 34, 45, 56, 67]
list3 = [111, 222, 333, 444, 555, 666, 777, 888]
list = list(zip(list1, list2, list3))
print(list)
'''
'''
list1 = ['som', 'don', 'ert', 'jok']
list = list(enumerate(list1))
print(list)
'''
list1 = ['som', 'don', 'ert', 'jok']
list2 = [0, 1, 2, 3]
list = list(zip(list2, list1))
print(list)