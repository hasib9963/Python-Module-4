def split_balanced_string(S):
    counter = 0
    balanced_strings = []
    current_string = ""

    for char in S:
        if char == 'L':
            counter += 1
        elif char == 'R':
            counter -= 1
        current_string += char
        if counter == 0:
            balanced_strings.append(current_string)
            current_string = ""
    return len(balanced_strings), balanced_strings
S = input()
max_num_strings, balanced_strings = split_balanced_string(S)
print(max_num_strings)
for string in balanced_strings:
    print(string)
