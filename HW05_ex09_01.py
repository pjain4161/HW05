#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body

def read_file():
    fin = open('words.txt')
    #for every line in file, split the line to get individual words 
    #and count the number of letters in that word. 
    #If number of letters in word is greater than 20, then print that word. 
    for line in fin:
        word = line.strip()
        if  len(word) > 20 :
            print word
        
    

##############################################################################
def main():
    read_file()

if __name__ == '__main__':
    main()
