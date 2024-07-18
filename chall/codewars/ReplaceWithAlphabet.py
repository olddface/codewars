def alphabet_position(text):
    text00 = ""
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        for j in range(len(Alphabet)):
            if text[i].lower() == Alphabet[j]:
                text00 += "{} ".format(str(j+1))
    return text00[0:-1]
print(alphabet_position("sad asa"))