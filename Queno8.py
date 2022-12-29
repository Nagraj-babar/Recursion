# Write a recursive python function to print cubes of first N natural numbers
def f1(a):
    if a<=0:
        return 1
    f1(a-1)
    print(a**3)
b=int(input('Enter a Number: '))
f1(b)