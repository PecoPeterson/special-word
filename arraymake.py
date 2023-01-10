def get_word_lengths(filename):
  word_lengths = []
  with open(filename, 'r') as f:
    for line in f:
      word = line.strip()
      length = len(word)
      word_lengths.append((word, length))
    return word_lengths

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
    print('Invalid input: Please enter a valid integer (cunt)')
#gets userlength with exceptions and stores it as user_wordlength

filtered_wordlist_withtuples = [(x, y) for x, y in word_and_wordlength if y == user_wordlength]
filtered_wordlist = [tuple[0] for tuple in filtered_wordlist_withtuples]
print(filtered_wordlist)