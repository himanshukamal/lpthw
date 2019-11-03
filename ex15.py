# import argv from system
from sys import argv 

# puts data in script and filename from arguments variables
script, filename = argv

# opens the given file i.e ex15_sample.txt
txt = open(filename)


file_again = input("> ")

# open the given file to show its contents.
txt_again = open(file_again)
print(txt_again.read())