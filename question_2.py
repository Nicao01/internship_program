# 2) 
def fibonacci_sequence(number):
    a, b = 0, 1

    if number == 0 or number == 1:
        return True
    

    while True:
        c = a + b
        if c == number:
            return True
        elif c > number:
            return False
        a, b = b, c

# for previously selected number, code below
previously_selected_number = 50;

if fibonacci_sequence(previously_selected_number):
    print(f'The number {previously_selected_number} belongs to the fibonacci sequence')
else:
    print(f'The number {previously_selected_number} dont belong to the fibonacci sequence')

# for input number, code below
prompt_number = int(input("Inform a number: "))

if fibonacci_sequence(prompt_number):
    print(f'The number {prompt_number} belongs to the fibonacci sequence')
else:
    print(f'The number {prompt_number} dont belong to the fibonacci sequence')