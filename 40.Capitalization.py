sentence=input("Enter a sentence:").lower()
list_of_words=[]
capitalized_sentence=""
words=sentence.split()
for list_of_words in words:
    for i in range(0,len(list_of_words),1):
        if i==0:
            # list_of_words[i].upper()
            capitalized_sentence += list_of_words[i].upper() + list_of_words[i+1:]+" "
            print(capitalized_sentence)

    
    