# Your code here!!
def sing():
    lib = "let it be"
    letra = ""
    for i in range(1,5):
        letra+= lib+",\n"             
    letra += "whisper words of wisdom, let it be, let it be,\n"
    for i in range(1,4):
        letra+= lib+",\n"
    letra += "there will be an answer, let it be"
    return letra

print(sing())