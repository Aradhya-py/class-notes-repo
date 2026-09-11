'''
First_name = input("Enter your First Name: ")
Last_Name = input("Enter your Last Name: ")
print(First_name)
print(First_name[2:8])
print(First_name[:2]) 
print(Last_Name[::2]) 
'''
output=input("> ")
part1=output[0:2]
part2=output[2:4]
part3=output[4:6]
print(part1)
print(part2)
print(part3)
print(part1[::-1])
print(part2[::-1])
print(part3[::-1])
print(f'result:{part1[::-1]+part2[::-1]+part3[::-1]}')
