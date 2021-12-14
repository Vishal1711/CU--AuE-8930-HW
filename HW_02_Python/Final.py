numbers = []
for n in range(2000, 3201):
    if (n%7==0) and (n%5!=0):
        numbers.append(str(n))

print(','.join(numbers))

number = input('Enter Number: ')
n = int(number)
factor = 1

for i in range(1,n+1):
    factor = factor * i

print(factor)

num = input('Enter a number:')
n = int(num)
numberdi = dict()


for i in range(1,n+1):
    numberdi[i] = i*i

print(numberdi)

number = input('Enter a number: ')

list = number.split(",")

tuple = tuple(list)

print(list)
print(tuple)


class MyClass():
    def __init__(self):
        self.str1 = ""
    def getString(self):
        self.str1 = input("Enter String: ")
    def printString(self):
        print(self.str1.upper())

str1 = MyClass()
str1.getString()
str1.printString()

import math
number = input('Enter a number: ')
C = 50
H = 30
list = number.split(",")
value = []
for D in list:
    value.append(str(int(round(math.sqrt(2*C*float(D)/H)))))

print(','.join(value))

input_str = input('Enter: ')
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)


word = input('Enter a Word: ')

word = sorted(word.split(","))
print(",".join(word))


lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print (sentence)


word = input()
word = word.split()

for i in word:
    if word.count(i) > 1:
        word.remove(i)

word.sort()
print(" ".join(word))


class sampleclass:
    count = 0

    def increase(self):
        sampleclass.count += 1


s1 = sampleclass()
s1.increase()
print(s1.count)


s2 = sampleclass()
s2.increase()
print(s2.count)

print(sampleclass.count)

d=dict()

for i in range(1,21):
    d[i]=i**2

for k,v in d.items():
    print(v)

d=dict()

for i in range(1,21):
    d[i]=i**2

for k,v in d.items():
    print(k)


d=dict()

for i in range(1,21):
    d[i]=i**2

print(d)

tupl = (1,2,3,4,5,6,7,8,9,10)
lst = list()
for i in tupl:
    if i%2==0:
        lst.append(i)

tupl1 = tuple(lst)
print(tupl1)


class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(14,10)
print(aRectangle.area())


class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length


Asqr = Square(10)
print(Asqr.area())
print(Square().area())

def divide():
    return 5/0

try:
    divide()
    print(divide())

except:
    print('divisionbyzeroerro')


lst=[12,24,35,24,88,120,155,88,120,155]

def duplicateremove(lst):
    newlst=[]
    group = set()
    for item in lst:
        if item not in group:
            group.add( item )
            newlst.append(item)
    return newlst



print(duplicateremove(lst))
