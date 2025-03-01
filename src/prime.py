number = int(input("Enter the number: "))
def prime():
  c = 0
  for i in range(1, number+1):
      if number % i == 0:
        c += 1
  if c == 2:
    print("Prime")
  else:
    print("Not Prime")

prime()