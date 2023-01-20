from collections import Counter

# kurwa

def get_word_lengths(filename):
  word_lengths = []
  with open(filename, 'r') as f:
    for line in f:
      word = line.strip()
      length = len(word)
      word_lengths.append((word, length))
    return word_lengths

def merge_list(listname):
  return "".join(listname)

def user_most_common_check(most_common_letter_ranking): #this ranks and picks the first most common letter
  n = 0
  for string in most_common_letter_ranking:
    string = most_common_unique_char[n]
    string = string[0]
    user_response = input('Is "%s" in your word? (True/False)' % (string))
    if user_response == "False":
        n += 1
        continue
    elif user_response == "True":
        print("Thanks for the info! <3")
        n = 0
        return string
    else:
        print("Invalid input. Please enter True or False.")

word_and_wordlength = get_word_lengths('words.txt')

while True:
  try:
    user_wordlength = input('Enter the length of your word, which should be a number between 1 and 12: ')
    user_wordlength = int(user_wordlength)
    if 1 <= user_wordlength <= 12:
      break
    else:
      print('Invalid input: Word length must be between 1 and 12')
  except ValueError:
    print('Invalid input: Please enter a valid integer <3')
#gets userlength with exceptions and stores it as user_wordlength

filtered_wordlist_withtuples = [(x, y) for x, y in word_and_wordlength if y == user_wordlength]
filtered_wordlist = [tuple[0] for tuple in filtered_wordlist_withtuples]
#print(filtered_wordlist)
#makes a list with JUST the words

words_with_uniquechar = [(word, ''.join(set(word))) for word in filtered_wordlist]
#print(Words_with_uniquechar)
#Makes a new list with words and their unique characters (each item is a tuple)

unique_characters = [tuple_item[1] for tuple_item in words_with_uniquechar]
#print(unique_characters)
#makes separate list for the unique characters

merged_list = merge_list(unique_characters)
c = Counter(merged_list)
most_common_unique_char = c.most_common(26)
#print(most_common_unique_char)
#needed to rank the most common letters in merged list

most_common_letter = user_most_common_check(most_common_unique_char)
#print(most_common_letter)
#gets the most common letter and stores it, inteded to be used to filter the word list further based on position