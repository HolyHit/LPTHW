from sys import argv

#Set arguments for the user to fill in before starting the program
script, filename = argv
#open the text file with the name given by the argument
txt = open(filename)

#print the text and the name of the file
print "Here's your file %r:" % filename
#print the innards of the file
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()