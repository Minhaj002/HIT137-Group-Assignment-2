#Encryption function
def encrypt(shift1, shift2):
    
    raw_file = open("raw_text.txt", 'r') #open raw file 
    encrypted_file = open('encrypted_text.txt', 'w') #open file for encryption
    
    text = raw_file.read() #read content 
    new_ch = "" #init string

#loop to read file content
    for ch in text:
        if ch.isalpha(): #check if alphabet
