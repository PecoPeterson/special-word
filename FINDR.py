from collections import Counter
import collections

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

def flatten_and_set(original_list):
    result = [set(x[0]) for x in original_list]
    return "".join([str(elem) for sublist in result for elem in sublist])
#makes a variable with the unique characters of the first items in a list of tuples

def char_frequency(string):
    counter = collections.Counter(string)
    char_freq = counter.most_common()
    char_list = [char for char, freq in char_freq]
    return char_list
#takes in a string and returns a list of all the characters based on frequency

def search_list(my_list):
    found_letter = ""
    positions = []
    while my_list:
        item = my_list[0]
        while True:
            try:
                response = input("Is " + item + " your letter? (yes/no) \n").lower()
                if response == "yes" or response == "no":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid response (yes or no) \n")
        if response == "yes":
            found_letter = item
            while True:
                try:
                    position = input("What are the positions of this letter? (comma separated) \n")
                    position = position.split(',')
                    position = [int(x.strip()) - 1 for x in position]
                    positions.extend(position)
                    break
                except ValueError:
                    print("Please enter valid positions (comma separated) \n")
            break
        else:
            my_list.pop(0)
    return (found_letter, positions)

raw_characters = flatten_and_set(filtered_list)
char_ranking = char_frequency(raw_characters)

print("this is the character ranking",char_ranking,"\n\n")

char_positions = search_list(char_ranking)
print(char_positions)



#print("this is the character ranking",char_ranking,"\n\n")
#print("confirmed used character: ", char_positions[0], "\n")
#print("positions of character: ", char_positions[1], "\n")