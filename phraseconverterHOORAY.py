print ("Type in a sentence, and it'll get converted to Pig-Latin!")
print ("Please don't use punctuation or numbers.")
print ("Also, we can't handle uppercase/lowercase yet, so lowers only please!")
text = input("Input a phrase: " )

def pig_latin(aword):
    vowels = "aeiou"
    for i in range(len(aword)):
        if aword[0] in vowels: # still checking first character; that doesn't change
            return aword+"yay"#returns awordyay
        if aword[i] not in vowels:
            continue
        else:
            consonant_clust = aword[:i] #defines what a consonant cluster is
            rest = aword[i:] #defines the rest of the word starting from [i]
            return rest + consonant_clust + "ay"

def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""
    for word in list_of_words:
        new_sentence = new_sentence + pig_latin(word)
        new_sentence = new_sentence + " "
    return new_sentence

print (convert_sentence(text))