# Type Function 
'''
Type	 What it means	                                   example
Numeric	 Stores numbers	                                   x = 10
bool	 Stores True or False	                           is_student = True
None	 Means no value / empty value	                   x = None
str	     Stores text	                                   name = "John"
bytes 	 Stores binary data	                               data = b"Hello"
tuple	 Ordered collection that cannot be changed	       x = (1, 2, 3)
list	 Ordered collection that can be changed	           x = [1, 2, 3]
range	 Generates a sequence of numbers	               x = range(5)
set	     Collection of unique values	                   x = {1, 2, 3}
dict	 Stores key-value pairs	                           x = {"name": "John"}

'''
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
y=bytes(x)
print(y[0])
for a in y:
    print(a)

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