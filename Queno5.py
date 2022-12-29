# Write a recursive python function to print first N even natural numbers.
def f1(a):
    if a<=1:
        return 2
    if a%2==0:
      f1(a-2)
      print(a)
    else:
        print('You Enter a odd Number')
b=int(input('Enter a even number: '))
f1(b)