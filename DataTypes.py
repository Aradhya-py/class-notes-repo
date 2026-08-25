# Type Function 

value = 10 
print(value)
print(type(value))
value = 10.5 
print(value)
print(type(value))

# packing 
a,b,c = 1,2,3 # Gives error when a,b,c = 1,2 ValueError: not enough values to unpack
print(a,b,c)

# Assigning same value to multiple varianble
a=b=c=10
print(a)
print(a,b,c)

#Data Type
emp_id = 11
name = 'Josh'
salary = 100000

print("My employee id is :" , emp_id)
print("My name is :" , name)
print("My salary is:" , salary)

print(12E1) # E1 = 10 , E2 = 100 , E3 = 1000 , E4 .... 

# Boolean Value
a= True
b= 'not empty'
print(a * 2) 
print(a * b) 
print(bool(a))

# None Type
a = None 
print(a)
print(type(a))

#Byte
print(bytes(10)) # Changes value in binary form 
x=[10 , 20 , 30]
y=bytes(x) # You cannot store negative value and no. shouldn't be greater than 256 also you cannot modify byte information
print(y[0])
for a in y:
    print(a)
'''
#To check byte data type is immutable
x= [10 , 20 , 30 ]
y = bytes(x)
y[0] = 30  # shows error dbecause byte cannot be modified 
'''
# Range function
a= range(10,5)
for x in a: 
    print(x)

  
# Float Type

salary1 = 50.5
print(salary1)
print(type(salary1))


#Complex Type

a= 3 + 5j
b= 2-5.5j

print(a+b)  

#String 

s1 = '1'
s2 = "2"
s3 = '''
1
2
3
'''
s4 = """"
1
2
3
"""

print(s1 , s2 , s3 , s4)

# String Convertion 

val = "abcd" + str(34)
print(val)
val1 = 12 + int("56")
print(val1)

#int variable 
a = 5 

# typecast to float 
n = float(a)
print(n)
print(type(n))

# float variable 
a = 5.9

# typecast to int 
n = int(a)
print(n)
print(type(n))

#int variable 
a = 5

# typecast to str 
n = str(a)
print(n)
print(type(__name__))