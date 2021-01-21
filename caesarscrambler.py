# CAESAR SCRAMBLER by lowdon
# 17/01/21
# Use '-e' to encrypt and '-d' to decrypt
# IDEAS: PROGRAM WHICH SHIFTS LETTERS IN SENTENCE AND ADDS +1 WITH EVERY SPACE
# IF SHIFTCOUNT (which is an offseter) LOOPS BACK, ADD TWO IN ORDER TO SKIP SHIFT BY 26 OR BY 0

import sys

firstCharVal = 97
numOfLetters = 26
lCount = 0
ignoreChars = [".", ",", "/", ":", "!", "?", ";", "'", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]

print("\nCAESAR SCRAMBLER by lowdon\n-----------------\n\n")

start = input("input text: ").lower()
#"aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa" #
#

try:
    shiftCount = int(input("starting shift (zero defaults to one): "))
except ValueError:
    print("\nPlease fill in some number for me to work with!")
    exit(0)

result = ""

while (lCount < len(start)):

    shiftCount = shiftCount % numOfLetters
    if(shiftCount == 0):
        shiftCount += 1
    
    if(start[lCount] == " "):
        shiftCount = shiftCount + 1
        result += " "
    
    else:
        try:
            if(start[lCount] in ignoreChars):
            #if(start[lCount] == "." or start[lCount] == "," or start[lCount] == "/" or start[lCount] == ":" or start[lCount] == "!" or start[lCount] == "?" or start[lCount] == ";" or start[lCount] == "'"):
                result += start[lCount]
            elif(str(sys.argv[1]) == "-d"):
                result += chr( ( ( ord(start[lCount]) - firstCharVal - shiftCount ) % numOfLetters ) + firstCharVal )
            elif(str(sys.argv[1]) == "-e"):
                result += chr( ( ( ord(start[lCount]) - firstCharVal + shiftCount ) % numOfLetters ) + firstCharVal )
        except IndexError:
            print("Use '-e' to encrypt and '-d' to decrypt")
            exit(0)
        
    lCount = lCount + 1

print(result)