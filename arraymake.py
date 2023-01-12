from collections import Counter

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
n = 0
def user_most_common_check(most_common_letter_ranking):
  for string in most_common_letter_ranking:
    string = most_common_in_merged_list[n]
    string = string[0]
    user_response = input('Is %s in your word? (True/False)' % (string))
    if user_response == "False":
        n ++ 1
        continue
    elif user_response == "True":
        print("Thanks for the info! <3")
        n = 0
        break
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
#Reaching this point is required for each time the program is used

merged_list = merge_list(filtered_wordlist)
c = Counter(merged_list)
most_common_in_merged_list = c.most_common(26) #needed to rank the most common letters in merged list

#print(most_common_in_merged_list)

user_most_common_check(most_common_in_merged_list)
