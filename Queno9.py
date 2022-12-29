# Write a recursive python function to print first N multiples of a given number.
def f1(a):
    if a==1:
        return 1
    s=a*f1(a-1)
    return s
b=int(input('Enter a Nummber: '))
print(f1(b))