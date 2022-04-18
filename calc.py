# Simple calculator. Test example
# Author: @Vsevolod Demidov (fondad@gmail.com)

a = 5
b = 10

def calc(x,y,sign):
    # Add two numbers
    if sign == '+':
        return x + y
    if sign == '-':
        return x - y
    else:
        return "Unknown sign"

z = calc(a,b,'+')

print ('Result = {}'.format(z))
