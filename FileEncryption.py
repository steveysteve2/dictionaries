# Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. 
# For example:

# codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .} Using this example, 
# the letter A would be assigned the symbol %, the letter a would be assigned the number 9, 
# the letter B would be assigned the symbol @, and so forth. 

# The program should open this file -  info_security.txt
# Download info_security.txt, read its contents, then use the dictionary to 
# write an encrypted version of the file’s contents to a second file (name it 'encrypted.txt'). 
# Each character in the second file should contain the code for the corresponding character in 
# the first file.

infile = open("info_security.txt", "r")

outfile = open("encrypted.txt", "w")

infilestr = infile.read()

infilelist = infilestr.split()

codes = {"A" : "$", "a" : "^", "B" : "@", "b" : "!", "C" : ")", "c" : "(",
            "D" : "v", "d" : "*", "E" : "[", "e" : "]", "F" : "0", "f" : "|",
            "G" : ",", "g" : "?", "H" : ":", "h" : ";", "I" : "{", "i" : "}",
            "J" : "`", "j" : "~", "K" : "-", "k" : "_", "L" : "2", "l" : "3",
            "M" : "4", "m" : "1", "N" : "5", "n" : "6", "O" : "7", "o" : "8",
            "P" : "9", "p" : "+", "Q" : "=", "q" : "%", "R" : "a", "r" : "b",
            "S" : "c", "s" : "d", "T" : "e", "t" : "f", "U" : "g", "u" : "h",
            "V" : "i", "v" : "j", "W" : "k", "w" : "l", "X" : "m", "x" : "n",
            "Y" : "o", "y" : "p", "Z" : "q", "z" : "r"}

for word in infilelist:
    for char in word:
        if char in codes:                    #checks if char exists in codes database
            outfile.write(codes[char])
        else:                               #punctuation stays punctuation
            outfile.write(char)
    outfile.write(' ')                  #adds spaces where they belong

infile.close()

outfile.close()
