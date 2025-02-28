import random
import string
def passwordGenerator():
  words = string.ascii_letters + string.digits
  generatedPassword = ''.join(random.choices(words, k=4))
  return generatedPassword
print(passwordGenerator())