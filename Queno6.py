# Write a recursive python function to print first N even natural numbers in reverse order.
def f1(a):
    if a<=0:
        return 2
    if a%2==0:
       print(a)
       f1(a-2)
    else:
        print("You Enter a odd number: ")
b=int(input('Enter a Even Number: '))
f1(b)