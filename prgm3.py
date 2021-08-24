
#python program 3
n = int(input("enter the array size: "))
arr = map(int, input("enter the numbers: ").split())
arr = list(arr)
ar_length = len(arr)
arr = sorted(arr)
print(arr[ar_length-2])
