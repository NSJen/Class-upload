

def mean(nums=[1,2,3,4]):
    sum = 0
    for num in nums:
        sum = sum + num

    return sum / len(nums)

def createNumlist():
    numbers = []
    choice = input("Would you like to choose numbers? \n")
    if choice == 'yes':
        how_many = int(input("How many numbers would you like to choose? \n"))
        for _ in range(how_many):
            numbers.append(int(input("Please choose a number to add to the list. \n")))
        return numbers
    else:
        return False

def main():
    numbers = createNumlist()
    if numbers != False:    
        print(f"Mean: {mean(numbers)}")
    else:
        print(f"Mean: {mean()}")

main()
