def decrypt(shift1, shift2):

    encrypted_file = open("encrypted_text.txt", 'r') #open encrypted file
    decrypted_file = open("decrypted_text.txt", 'w') #open file for decrypted content

    new_text = encrypted_file.read() #read encrypted content
    old_ch = "" #init string

    #loop to read content
    for ch in new_text:
        if ch.isalpha(): #condition for alphabet characters
