# Write a recursive python function to print first N natural numbers in reverse order
def f1(a):
    if a<=0:
        return a
    print(a)    
    f1(a-1)
b=int(input('Enter a number: '))
f1(b)