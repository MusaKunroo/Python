# sentence=input("Enter A sentence:").lower()
# words=sentence.split()
# word_list={}
# for word in words:
#     if word in word_list:
#         word_list[word]+=1
#     else:
#         word_list[word]=1
# for rat,values in word_list.items():
#     print(f"{rat}->{values}")         


                                                    #! Another Way To This

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")

    
    