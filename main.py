def multiply(arg1=5, arg2=0):
  accumulator = 0
  for i in range(arg2):
	  accumulator = accumulator + arg1
  return accumulator

def exponent(arg1=5, arg2=7):
  accumulator = 1
  for i in range(arg2):
    accumulator = accumulator * arg1
  return accumulator  

def square(arg=0):
  return multiply(arg1=arg, arg2=arg)

result = multiply(arg1=5, arg2=7)
print(result)

result = exponent(arg1=2, arg2=1)
print(result)

result = square(arg=2)
print(result)