# ......calculator ....
# ..implementing use of ;
# ..print statements
# ..while loop
# ..for loop
# ..if statement
# ..arithmetic operators
# ..multiline strings
# ..string manipulation
# ..exception handling

import numpy as np

print("Welcome to ***musiitwa's calc***"" Do you want to do some calculations?")
print('use the following algebraic forms;\n  +,*,-,/,sin,cos,tan,log . ')

while True:
  

  expr = input('enter the expression to be calculated:')

  oper = ['+','-','*','/','sin','cos','tan','log']
  for op in oper :
    if op in expr:
      val = expr.split(f'{op}')

      try:
        print(val)
        if op =='+':
          result = float(val[0])+float(val[1])
        elif op =='-':
          result = float(val[0])-float(val[1])
        elif op =='*':
          result = float(val[0])*float(val[1])
        elif op =='/':
          result = float(val[0])/float(val[1])

        elif op =='sin':
          result = np.sin(np.radians(float(val[1])))
        elif op == 'cos':
          result = np.cos(np.radians(float(val[1])))
        elif op == 'tan':
          result = np.tan(np.radians(float(val[1])))
        elif op == 'log':
          result = np.log10(np.radians(float(val[1])))

        else:
          print('check your expression and try again!!!')

        print(f'{expr} = {result}')

      except ZeroDivisionError:
        print('YOU HAVE DIVIDED BY ZERO!!! \n TRY AGAIN')
      
  if expr =='0':
   break