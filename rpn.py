stack = list()

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y    
}

def calculate(operator):
    # calculate using the last two numbers in the stack
    y,x = stack.pop(),stack.pop()
    return operations[operator](x, y)

def evaluate(input_str, startover):
    try:
        if startover == True:
            stack.clear()
        for token in input_str.split():
            if token in operations:
                if len(stack) < 2:
                    return "Stack too small to apply operation. So ignoring the last operator."
                else:        
                    stack.append(calculate(token))
            else:
                # Upon valid number: Add it to the stack
                stack.append(float(token))
        if len(stack) >= 1:
            return stack[-1]           
    except ZeroDivisionError:
        return 'ZeroDivisionError'           
    except:                  
        return 'Please type in valid number or supported operator (' + str(list(operations.keys())) + ')'                  

if __name__ == '__main__':
  print("CLI RPN Calculator - Supported operators: " + str(list(operations.keys()))) 
  while True:
    try:
      print(evaluate(input('> '), False))     
    except EOFError:  break