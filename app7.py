def greet_user(name,DOB):#function defined,define a function first
    print(f'hii {name}')
    print ("good morning")
    print(f'your age {DOB}')


greet_user(name=input("wht is ur name: "),DOB=input("ur date of birth: "))#function called
print(" ")
greet_user("nikita","5-9-2000")#positional argument
print("finish")
