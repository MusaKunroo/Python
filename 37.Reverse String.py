# words=input("Enter A  Word:")
# words=words.lower()
# letters=list(words)
# rev_word=""
# for i in range(len(letters)-1,-1,-1):
#     rev_word+=words[i]
# print(rev_word)    
     
                                                        #!Better Way
string = input("Enter a string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string  # Prepend each character

print("Reversed string:", reversed_string)



