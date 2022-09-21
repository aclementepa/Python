from random_word import RandomWords


r = RandomWords()
key = r.get_random_word()
word = "Hello there"

length = len(word)

# for i in range(length):
# word = (word[:i] + chr(ord(word[i]) ^ ))