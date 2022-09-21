from random_word import RandomWords
import sys, getopt

r = RandomWords()

key = r.get_random_word()

word = sys.argv[0]

try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["username=","password="])
except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
for opt, arg in opts:
    if opt in ("-u", "--username"):
        sender = arg
    elif opt in ("-p", "--password"):
        password = arg