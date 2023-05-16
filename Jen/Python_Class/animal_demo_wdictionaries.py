'''pacman = {
    'isAlive': True, 
    'points': 380, 
    'lives': 7,
    }

test1 = pacman.get('isAlive')
print(f"Test 1 {test1}")
test2 = pacman.get('isGodmode')
print(test2)
test3 = type(pacman.get('ghost'))
print(test3)
test4 = pacman['isGodmode']
print(test4)


user_choice = int(input("Pick a number "))

while user_choice == 1 or user_choice == 2:
    if user_choice == 1:
        print("something")
    
    elif user_choice == 2:
        print("something else")
        
    user_choice = int(input("that is not a valid choice, please choose 1 or 2"))
print("You will eat next time.1")
        
'''
'''
while True:
    user_choice = input("Enter your choice! ")
    if user_choice == "1" or user_choice == "2":
        print("This is number " + user_choice)
        break
    else:
        break
print("Thank you for making a choice!")
'''

'''
    

def function_name():
    It's good practice to identify what this function does.
    Parameters can be given a default value by assigning a value.
    The code can reurn one or more values.
    Variables within this function will be local. They will not affect 
    variables outside this funciton unless they are returned. 
    #This information can be in a docstring or comments. 
    return "Returns this string" 

print(function_name())

'''
def plural(word):
    if word[-1] == 'y':
        word = word[0:-1:]+"ies"
    elif word[-1] == 's':
        word = word
    elif word [-1] == 'x':
        word = word+'es'
    else:
        word = word+'s'
    return word
def printAnimal(dictionary):
    print("------------------------------\n")
    for key,value in dictionary.items():

        if key == 'Colors':
            print(f"I like these {key}:")
            for value in dictionary.values():
                for item in value:
                    print(item)

        elif key == 'Nope':
            print(f"I don't like:") 
            for value in dictionary.values():
                for item in value:
                    item = plural(item)
                    print(item)
        else:
            print(f'I like these {key}:')
            for value in dictionary.values():
                for item in value:
                    item = plural(item)
                    print(item)
  
name = input('What is your name? \n')
        

animals = {'Animals':["giraffe", "whale", "otter", "frog", "cat", "echidna"]}    
rabbits = {'Rabbits':["Rex", "Blanc de Hotot", "Angora", "Czech Frosty", "French Lop"]}
dogs = {'Dogs':["German Shepherd", "Rotweilers", "Chihuahua", "Aierdale", "Doberman Pinser", "Golden Retriever"]}
nope = {'Nope':["vegetables", "avalanche", "meany", "slimy things"]}
colors = {'Colors':[]}
color1= input(f"Welcome, {name}, Please enter a color. ")
color2= input("Please enter another color. ")
colors['Colors'].append(color1)
colors['Colors'].append(color2)
all_likes = [animals, rabbits, dogs, nope, colors]

#Throw a while loop in for the inputs. Have them add colors as long as they would like. 

#Create dictionaries instead of lists with the key being the topic and the value being the list. Place the topic (key)
#at the beginning of each list. 

#Could write it more as a narrative.

print(f"\nMy name is {name}")
for dictionary in all_likes: 
    
    printAnimal(dictionary)
    



