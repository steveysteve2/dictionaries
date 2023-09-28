# The program should create a dictionary in which the keys are the individual 
# words found in the file and the values are the number of times each word appears. 
# For example, if the word “the” appears 128 times, the dictionary would contain 
# an element with 'the' as the key and 128 as the value. The program should display 
# the frequency of each word.

infile = open("sometext.txt", "r")

newdict = {}
infilestr = infile.read()

infilestr = infilestr.replace(",", "")
infilestr = infilestr.replace(".", "")
infilestr = infilestr.replace(";", "")
infilestr = infilestr.lower()

infilelist = infilestr.split()

for word in infilelist:
    if word in newdict:
        newdict[word] += 1
    else:
        newdict[word] = 1
    
print(newdict)

infile.close()