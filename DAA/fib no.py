print("enter the total no for fibo:")
n = int(input())
def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recursive_fibonacci(n):
    first=0
    second=1
    print(first)
    print(second)
    while n-2>0:
        third = first + second
        first=second
        second=third
        print(third)
        n-=1
print("Recursive:")
for i in range(n):
	print(recursive_fibonacci(i))
print("Non_recursive:")
non_recursive_fibonacci(n)