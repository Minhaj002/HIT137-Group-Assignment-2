
"""
Group Name: DAN/EXT 03
Group Members:
MINHAJ ABDUL KHALEQ - 396076
NIMETH DULSITH KODAGODA DISSANAYAKE LIYANAGE - 397445
PRASHANNA RATNA BAJRACHARYA - 398024
SUGAM KAFLE - 398343
"""

#import functions 
from encryption import *
from decryption import *

def main():

    #take input for shift values from user
    shift1 = int(input("Enter shift1 value : "))
    shift2 = int(input("Enter shift2 value : "))

    #call encrypt & decrypt function
    encrypt(shift1, shift2)
    decrypt(shift1, shift2)

    #open files and read
    raw_file = open("raw_text.txt", "r")
    decrypted_file = open("decrypted_text.txt", "r")

    raw_text = raw_file.read()
    decrypted_text = decrypted_file.read()
    
    #check content for successful decryption
    if raw_text == decrypted_text:
        print("Decryption was successful!")
    else:
        print("Decryption failed!")

#run main
if __name__ == "__main__":
    main()

