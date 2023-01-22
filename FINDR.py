from collections import Counter

def string_lengths(file_path): #reads the file and makes a list containing the words and their length
    with open(file_path, "r") as file:
        content = file.read()
        lines = content.split("\n")
        string_lengths = []
        for line in lines:
            line = line.strip()
            string_lengths.append((line, len(line)))
    return string_lengths
word_lengths = string_lengths("words.txt")

def get_user_length():
    while True:
        try:
            user_input = int(input("Please enter a number between 1 and 12: "))
            if 1 <= user_input <= 12:
                return user_input
            else:
                print("Invalid input. Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12.")
#needs following line
input_value = get_user_length()

def filter_tuples(tuple_list, length):
    filtered_list = []
    for tuple_ in tuple_list:
        if tuple_[1] == length:
            filtered_list.append(tuple_)
    return filtered_list
filtered_list = filter_tuples(word_lengths, input_value)
#print(filtered_list)

def get_unique_string(original_list):
    return ''.join(''.join(set(string)) for string, value in original_list)
unique_char_string = get_unique_string(filtered_list)

def get_sorted_list(original_list):
    new_string = get_unique_string(original_list)
    char_count = Counter(new_string)
    return sorted(new_string, key=lambda x: char_count[x], reverse=True)
unique_char_string_ranking = get_sorted_list(unique_char_string)
print(unique_char_string_ranking) 