#Decryption function
def decrypt(shift1, shift2):

    encrypted_file = open("encrypted_text.txt", 'r') #open encrypted file
    decrypted_file = open("decrypted_text.txt", 'w') #open file for decrypted content

    new_text = encrypted_file.read() #read encrypted content
    old_ch = "" #init string

    #loop to read content
    for ch in new_text:
        if ch.isalpha(): #condition for alphabet characters
            
            # lowercase a-m  
            if ch.islower() and 'a' <= ch <= 'm': #retaining encryption rule
                #see encryption.py
                base = ord('a')  
                index = ord(ch) - base 
                key = shift1 * shift2 #shift rule for lowercase first half
                old_index = (index - key) % 13 #inverse of encryption see encryption.py 
                old_ch += chr(old_index + base) #decrypted text
            # uppercase A-M
            elif ch.isupper() and 'A' <= ch <= 'M':
                base = ord('A')
                index = ord(ch) - base
                key = shift1 #shift condition for uppercase first half
                old_index = (index + key) % 13
                old_ch += chr(old_index + base)
