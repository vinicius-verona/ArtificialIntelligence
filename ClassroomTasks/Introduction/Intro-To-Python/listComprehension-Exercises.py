nums = [i for i in range(1, 1001)]
sentence = "Practice Problems to Drill List Comprehension in your Head"

"""
 Exercício A
"""
print("Números de 1 a 1000 divisíveis por 8: " +
      str([i for i in nums if (i % 8) == 0]) + "\n")


def hasDigit(num, digit):
    pos = str(num).find(digit)
    if (pos == -1):
        return False
    return True


"""
 Exercício B
"""
print("Números de 1 a 1000 que possuem o dígito 6: " +
      str([i for i in nums if (hasDigit(i, "6"))]) + "\n")


"""
 Exercício C
"""
print("Números de espaços na string 'sentence': " +
      str(sum([1 for i in sentence if (i == ' ')])) + "\n")


def isVowel(i):
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        return True
    else:
        return False


"""
 Exercício D
"""
copySentece = list(sentence)

# Remove vowels
idxList = [i for i in range(len(sentence))
           if (isVowel(sentence[i]))]
for i in idxList:
    copySentece[i] = ''

copySentece = ''.join(copySentece)
print("String 'sentence' sem as vogais: " + copySentece + "\n")


"""
 Exercício E
"""
print("Palavras com menos de 5 letras: ", [
      i for i in sentence.split() if (len(i) < 5)])
