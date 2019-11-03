#importing arguments variables from the system
from sys import argv

#assigning the value of arguments variables in the script and filename
script, filename = argv


#asking the user to enter the filename & delete options. 
print(f"We are going to erase {filename}.")
print("If you dont't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("? ")

#opening the  file in write mode.
print("Opening the file...")
target = open(filename, 'w')

#deleting the contents.
print("Truncating the file. Goodbye!")
target.truncate()
 
#asking user to enter 3 lines .
print("Now i am going to ask you for three lines.") 

line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

#writing the contents to the file.
print("I am going to write these to the file.")
print("line 1 is%s,line 2 is%s, line 3 is %s" %{line1}, %{line2}, %line{3}) 

#closing the program.
print("And finally, we close it.")
target.close()