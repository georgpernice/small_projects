pwd =  "cef7e8i>"
#pwd = "1111111111"
pwdDecrypted = ""
encryptedAlphabet = "abcdefghijklmnopqrstuvwxyz123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ";
j=0
for letter in pwd:
    position = str.find( encryptedAlphabet, letter);
    pwdDecrypted += encryptedAlphabet[position-j]
    j+=1


print (pwdDecrypted)