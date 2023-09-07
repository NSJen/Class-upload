from time import sleep

animals = ['cat', 'dog', 'elephant', 'hog', 'bird']

for a in animals:
    #if a[0] == 'e' or a[0] == 'c':
        #print(a)
    
    print(f"\nI have a {a}")
  
    
    #print(a + animals[0])
    for letter in a:
        print(letter)
    sleep(10)
'''

animal_dict = {"cats" : 2, "dogs" : 2, "rabbits" : 67, "snake" : 1, "ducks" : 32, "chickens" : 10}
for animal, numbers in animal_dict.items():
    print (f"I have {numbers} {animal}")
    print(animal * numbers)



#for animal in animals:
   # print(animal)
'''