# Word Replacement Program

def replace_word():

    frase =  "Hello how are you, are you ok?"
    word_to_replace = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")

    print(frase.replace(word_to_replace, new_word))

replace_word()