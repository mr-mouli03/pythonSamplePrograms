import os

file = os.listdir()
f1 = open('sample.txt', 'r')
f2 = open('sample.txt', 'r')
f3 = open('files.txt', 'w')

while True:
    line1 = f1.readline()
    line2 = f2.readline()
    
    if not line1 or not line2:
        break
    
    if line1:
        f3.write(line1)
    if line2:
        f3.write(line2)

f1.close()
f2.close()
f3.close()