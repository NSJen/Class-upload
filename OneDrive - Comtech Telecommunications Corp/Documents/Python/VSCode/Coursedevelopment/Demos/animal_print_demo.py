# This is a comment. It can be used for only one line at a time. 
# To do multiple lines, you need multiple #s.

'''
This is a doc string
It's true purpose is to be a string with multiple lines. 
However, if you never assign it to a variable, it has no 
action and is used to create multi-line comments. 



def function_name():
    It's good practice to identify what this function does.
    Parameters can be given a default value by assigning a value.
    The code can reurn one or more values.
    Variables within this function will be local. They will not affect 
    variables outside this funciton unless they are returned. 
    #This information can be in a docstring or comments. 
    a = 1
    b = 2
    output = a + b
    print(output)




def plural(word):
    [print("Made it to 'plural' function")]
    #This function will take any word and make it the plural version. 
    if word[-1] == 'y': # I had to get tricky with some words. This slice is referring to the last letter of the string. 
                        # If the last letter is 'y' then it will go to the next statement. 
        if word == 'Jay': #Jay is an exception so I gave it its own line. 
            word = 'Jays'
        else:
            word = word[0:-1:]+"ies" #Otherwise, if a word ends in y, the y will be dropped using the slice and we'll add "ies"
    elif word[-1] == 's':
        word = word
    elif word [-1] == 'x':
        word = word+'es'
    else:
        word = word+'s'
    return word # Notice the return statment here. Whatever is in the return statement at the end of the function
                # will be what is there when the function is called. Not all functions have return statements. 

def printAnimal(dictionary):
    #This function prints each list.  
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

        #This function doesn't have a return statement. It just has actions. 

def makelist(thing):
    print("I made it to makelist")
    #This function makes the lists that become the value in each dictionary. 
    if thing == 'color':
        counter = int(input(f"How many colors would you like to add? "))
    elif thing == 'nope': 
        counter = int(input(f"How many things would you like to add that you don't like? "))
    else:
        counter = int(input(f"How many types of {thing} would you like to add? "))
        print(type(counter))
    list = []
    while counter > 0:
        if thing == 'color':
            eachthing = input(f"Name a color that you like. ")
        elif thing == 'nope':
            eachthing = input(f"What is a thing that you don't like? ")
        else:
            eachthing = input(f"Name a type of {thing} that you like. ")
        list.append(eachthing)
        counter -= 1
    return(list) # Once again, we have a return statement. 
    
name = input('What is your name? \n')
        
animals = {'Animals':makelist('animal')}    # This is a dictionary with "Animals" as the key. The value is a list
                                            # that is created by the makelist function using the arguement 'animal'. 
                                            # 'animal' then becomes the parameter for makelist. 
birds = {'Birds':makelist('bird')}
dogs = {'Dogs':makelist('Dog')}
nope = {'Nope':makelist('nope')}
colors = {'Colors':makelist('color')}
all_likes = [animals, birds, dogs, colors, nope] # This list combines all of the dictionaries into one list. 
 

# Could write it more as a narrative.

print(f"\nMy name is {name}") # The \n here puts it on a new line, to leave a space between the questions and the response. 
for dictionary in all_likes: 
    
    printAnimal(dictionary) # This prints everything in the list of dictionaries one at a time. 
                            # Everything up to this point was setting up to give us this information. 
    



'''

def countdown(n):
    print(n)
    if n == 0:
        return             # Terminate recursion
    else:
        countdown(n - 1)   # Recursive call


countdown(5)
print("done")