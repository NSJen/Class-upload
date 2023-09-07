'''import time

for n in range(5):
    print(n)

print('\n' + '*' * 10)

time.sleep(5)
'''
animals = ['cat', 'dog', 'frog', 'hog', 'bird']

'''
for n in range(len(animals)):
    print(f"{n+1}: {animals[n]}") 

print('\n' + '*' * 10)

time.sleep(5)

animals.append('tiger')

for n in range(len(animals)):
    print(f"{n+1}: {animals[n]}")

print('\n' + '*' * 10)

for animal in animals: 
    print(animal)

for animal in animals:
    if animal[0] == "c":
        print('\n' + '*' * 10)
        print(animal)
'''
for index, animal in enumerate(animals):
    print(f"{index}")
    