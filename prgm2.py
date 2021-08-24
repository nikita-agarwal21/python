#python program 2
string=input("enter the string: ")
player1=0;
player2=0;
str_len=len(string)
for i in range(str_len):
        if string[i] in "AEIOUaeiou":
            player1 +=(str_len)-i
        else:
            player2 +=(str_len)-i
if player1 > player2:
          print('kevin',player1)
elif player1 < player2:
           print('stuart',player2)
else:
        print('draw')


