#This script encrypts plain text and also can be used to further encrypted
#text

#Example 1

Plain_Text = "Hello world"
Encrypted_Text = ""

for i in Plain_Text:
    j = ord(i)
    j = j + 1 # You can use any number less 110 to update,e.g j = j + 59
    k = chr(j)
    Encrypted_Text = Encrypted + k

print "Encrypted_Text: ", Encrypted_Text


#==============================================================================#
#This is the Decryption script for Example 1

#Example 2

Encrypted_Text = "Ifmmp!xpsme"
Plain_Text = ""

for i in  Encrypted_Text:
    j = ord(i)
    j = j - 1 # If you used 59 to update above you have to use j = j - 59
    k = chr(j)
    Plain_Text = Plain_Text + k

print "Plain_Text: ",Plain_Text 
