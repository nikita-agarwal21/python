numbers=[2,32,11,45,32,6]
number2=numbers.copy()
numbers.append(100)
numbers.insert(3,45)
#we can clear,pop,reverse,append,insert,count,find.sort,copy in list
number2.pop() #deletes last item
numbers.sort()
number2.sort()
print(number2)
number2.reverse()
print(number2)
print(numbers)
print(numbers.count(32))
print(20 in numbers)
print(numbers.index(32))