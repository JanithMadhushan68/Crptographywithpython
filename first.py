resultE   =""
message  =""
resultD  =""


message = input ("\n Enter the message to Encrypt :")
for i in range(0, len(message)):
    resultE = resultE + chr(ord(message[i])+3)
print("Encrypted Message:" , resultE)

for j in range (0, len(resultE)):
    resultD = resultD + chr(ord(resultE[j])-3)
print("Decrypted Message: ", resultD)    