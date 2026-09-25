# each letter in the plaintext is replaced by a letter some fixed number of positions along the alphabet. 
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on
# the Caesar cipher is easily broken and in modern practice offers essentially no communications security.

from random import randrange
global shift
global alphabet_length
alphabet_length = 26
shift = randrange(alphabet_length)

def cypher(user_message):
    global shift
    global alphabet_length
    translated_message = ""
    for letter in user_message:
        #ord => char to int; chr => int to char
        numbered_letter = int((ord(letter) + shift) % alphabet_length)
        translated_message += chr(numbered_letter + ord('a'))
    return translated_message

def decypher(user_message):
    global shift
    global alphabet_length
    translated_message = ""
    for letter in user_message:
        numbered_letter = int((ord(letter) - shift) % alphabet_length)
        translated_message += chr(numbered_letter + ord('a'))
    return translated_message

action = input("Do you want to cypher or decypher a message?\n")
while(action not in ["cypher", "decypher"]):
    print("Please write \"cypher\" or \"decypher\"")
    action = input("Do you want to cypher or decypher a message?\n")

user_message = input("Enter a message\n")
translated_message = ""
if(action == "cypher"):
    translated_message = cypher(user_message)
else:
    translated_message = decypher(user_message)

print(translated_message)