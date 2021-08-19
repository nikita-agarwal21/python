first=input('first name: ')
last=input("last name: ")
message= first +" " + last  +"  is a coder"
msg=f'{first}  {last} is a coder '
new_msg=msg[:]
print(message)
print(new_msg)
print(type(message))
print(type(new_msg))