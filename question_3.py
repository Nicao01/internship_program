# 3)
#first sequence

def complete_element_a(last_element):
    return last_element + 2

#second sequence
def complete_element_b(last_element):
    return last_element * 2

#third sequence
def complete_element_c(last_element):
    index = len(c_sequence)
    return index ** 2

#fourth sequence
def complete_element_d(last_element):
    index = len(d_sequence)
    return (index + 1) ** 2 * 4

#fifth sequence
def complete_element_e(last_element):
    index = len(e_sequence)
    return e_sequence[-1] + e_sequence[-2]

#sixth sequence
def complete_element_f(last_element):
    return last_element + 1

#initial prompt
a_sequence = [1, 3, 5, 7]
b_sequence = [2, 4, 8, 16, 32, 64]
c_sequence = [0, 1, 4, 9, 16, 25, 36]
d_sequence = [4, 16, 36, 64]
e_sequence = [1, 1, 2, 3, 5, 8]
f_sequence = [2, 10, 12, 16, 17, 18, 19]

print("Next element in a sequence a: ", complete_element_a(a_sequence[-1]))
print("Next element in a sequence b: ", complete_element_b(b_sequence[-1]))
print("Next element in a sequence c: ", complete_element_c(c_sequence[-1]))
print("Next element in a sequence d: ", complete_element_d(d_sequence[-1]))
print("Next element in a sequence e: ", complete_element_e(e_sequence[-1]))
print("Next element in a sequence f: ", complete_element_f(f_sequence[-1]))
