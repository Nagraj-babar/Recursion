# Write a recursive python function to print first N natural numbers.
def f1(a):
    if a==0:
        return 1
    f1(a-1)
    print(a)
b=int(input('Enter a number: '))
f1(b)