from random import choice

students = ['Reyes', 'Bachman', 'Brown', 'Campbell', 'Aquino', 'Anguiano', 'Castillo', 'Chaffin', 'Christian', 'Dervishi', 'Henriquez',
            'Gilbert', 'Griffin', 'Harris', 'Myles', 'Belanger', 'Maldonado', 'Malewski', 'McDonald', 'Mills', 'Milyadis', 
            'Minter', 'Romesser', 'Russel']

for number in range (1,25):
    student = choice(students)
    print(number, student)
    students.remove(student)


