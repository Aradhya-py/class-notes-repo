#Finding smallest number
a = 10 
b = -3 
c = 90 
d = -9
s =((a if a<d else d) if a<c else (c if c<d else d))
print(s)

# And Operator 
x=( 12 and 5)+4
print(x)

x = (9 and 6)+9
print(x)

x=('Amit' and 5)
print(x)

# OR OPerator

x= (12 or 5)
print(x)

x = (9 or 6)+9
print(x)

x=('Amit' or 5)
print(x)

# Not Operator

is_good = True
criminal = False
if is_good and not criminal: 
    print('Eligible')
else :
    print('Not Eligible')


x = 5
if x == 5 :
    x += 4 

print(x)

A = 10
B = 10
print(id(a)) #Even tho the value is same but the actual no. store diffrently 
print(id(b))

# Taking Input from user and Giving back Output
name = input("Enter your name : ")
print(f'You entered name as : {name}')
'''
a=float(input("Enter Num 1: "))
b=float(input("Enter Num 2: "))
c=(a) + (b)
print(int(c))


''' 
'''
from sys import argv
a= eval(argv(1))
b= eval(argv(2))
c = a + b 
print(c)
print (type(c))
'''

a = 10 
print(a)
print(-a)

l1 = [ " ruby " , "python", "Java" ,"c++"]
l2 = [ 1 , 2 , 3 ,4]
str1 = "python is a programming language and its is very easy to learn"
print("yes" if "python" in l1 else "no")
print("yes" if 3 in l2 else "no")
print("yes" if "Java" in l1 else "no")
    