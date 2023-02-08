import string

# ceaser_cipher key value
k = 3
list_input = print("welcome to ceaser cipher technique")
alphas = list(string.ascii_lowercase )
print(alphas)
print("kindly do not use spaces in between words or letters ")
encrypt_word = input("enter word to encrypt:- ")
try:
    strlen = len(encrypt_word)
    for j in range(0,strlen):
        p = string.ascii_letters.index(encrypt_word[j])
        final = (p+k)%26
        print(f"{encrypt_word[j]} is encrypted as :- ",alphas[final])
except Exception :
    print("warning!")
    print("kindly do not use symbols,numbers and spaces in between words or letters")

print("lets do decryption of ceaser cipher!")
decrypt_word = input("enter word to decrypt:- ")
try:
    strlen = len(decrypt_word)
    for j in range(0,strlen):
        p = string.ascii_letters.index(decrypt_word[j])
        final = (p-k)%26
        print(f"{decrypt_word[j]} is decrypted as :- ",alphas[final])
except Exception :
    print("warning!")
    print("kindly do not use symbols,numbers and spaces in between words or letters")

print("*******Just for reference purpose******** ")
for i in range(0,23):
    alphas[i]=alphas[i+3]
alphas[23] = "a"
alphas[24] = "b"
alphas[25] = "c"
print(list(alphas))
