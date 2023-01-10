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
print(filtered_wordlist)
#Reaching this point is required for each time the program is used

merged_list = merge_list(filtered_wordlist)
c = Counter(merged_list)
most_common_in_merged_list = c.most_common(26) #needed to rank the most common letters in merged list

user_most_common_check = False
while user_most_common_check == False:
  try:
    most_common_in_merged_list = most_common_in_merged_list[0]
    most_common_in_merged_list = most_common_in_merged_list[0] #this part is kinda messy (LEONEL MESSI!!! WOOO) I feel, but it works
    user_most_common_check = input('Is %s in your word?' % (most_common_in_merged_list))
    user_most_common_check = bool(user_most_common_check)
    if True:
      break
    else: #has to take the next most common letter in most_common_in_merged_list
      most_common_in_merged_list
  except ValueError:
    print('Invalid input: Please enter a valid boolean :>')
