# Write a recursive python function to print first N odd natural numbers in reverse order
def f1(a):
    if a<=0:
        return 1
    if a%2!=0:
      print(a)
      f1(a-2)
    else:
        print('You Enter a Even Number:')
b=int(input('Enter a Odd Number: '))
f1(b)