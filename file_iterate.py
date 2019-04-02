import os

directory_1 = 'images/not_santa'
hello = []

for filename in os.listdir(directory_1):
    hello.append(filename)

print(hello)