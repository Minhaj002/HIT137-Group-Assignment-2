
#Encryption function
def encrypt(shift1, shift2):
    
    raw_file = open("raw_text.txt", 'r') #open raw file 
    encrypted_file = open('encrypted_text.txt', 'w') #open file for encryption
    
    text = raw_file.read() #read content 
    new_ch = "" #init string

#loop to read file content
    for ch in text:
        if ch.isalpha(): #check if alphabet
        
         # lowercase a-m conditions
            if ch.islower() and 'a' <= ch <= 'm':
                #base and index to keep within limits
                base = ord('a') 
                index = ord(ch) - base 
                key = shift1 * shift2 #shift rule for lowercase first half
                new_index = (index + key) % 13 #module 13 to ensure rule applies to alphabet-half
                new_ch += chr(new_index + base) #encrypted text

        # lowercase n-z conditions
            elif ch.islower() and 'n' <= ch <= 'z':
                base = ord('n')
                index = ord(ch) - base
                key = shift1 + shift2 #shift rule for lowercase second half
                new_index = (index - key) % 13
                new_ch += chr(new_index + base)

        # uppercase A-M conditions
            elif ch.isupper() and 'A' <= ch <= 'M':
                base = ord('A')
                index = ord(ch) - base
                key = shift1 #shift rule for uppercase first half