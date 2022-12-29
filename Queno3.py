# Write a recursive python function to print first N odd natural numbers
def f1(a):
    if a<=0:
        return a
    if a%2!=0:
       f1(a-2)
       print(a)
    else:
        print('You Enter a even number')
b=int(input('Enter a odd number'))        
f1(b)