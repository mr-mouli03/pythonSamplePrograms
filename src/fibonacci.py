firstNumber = 0
secondNumber = 1
  
def fibonacci():
  global firstNumber, secondNumber
  n = int(input("Enter the number: "))
  while firstNumber <= n:
    print(firstNumber)
    temp = firstNumber
    firstNumber = secondNumber
    secondNumber = firstNumber + temp
  
fibonacci()