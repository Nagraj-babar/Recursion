# Write a recursive python function to print a number in reverse order.
def f1(a):
   if a<=0:
     return 1
   print(a)
   f1(a-1)
b=int(input('Enter a Number: '))
f1(b)