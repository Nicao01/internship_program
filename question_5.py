def reverse_string(string):
    reversed_string = ""

    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

#for hardcoded string, code below
example_string = "Internship"
print("Original string: ", example_string)
print("Reversed string: ", reverse_string(example_string))

#for input string, code below
input_string = input("Type anything: ")
print("Original string: ", input_string)
print("Reversed string: ", reverse_string(input_string))