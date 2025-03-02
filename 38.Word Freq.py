                                  #!Your Way(Inefficient way)
# word=input("Enter A Word:").lower()
# letters=list(word)
# letter_dict={}
# highest_frequency=0
# for letter in letters:
#     if letter in letter_dict:
#         letter_dict[letter]+=1
#     else:
#         letter_dict[letter]=1
# for count in letter_dict:
#     for count_next in letter_dict:
#         if letter_dict[count_next]>letter_dict[count]:
#             highest_frequency=letter_dict[count_next]
# value_to_find_key_for=highest_frequency
# for key,value in letter_dict.items():
#     if value==value_to_find_key_for:
#         print(f"Most common letter is: {key} and its frequency is: {highest_frequency}")        

                              #!Ghazarat's Way(More Efficient)
word = input("Enter your word: ")
letter_dict = {}
highest_letter = None
highest_freq = 0
for letter in word:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1
    if letter_dict[letter] > highest_freq:
        highest_freq = letter_dict[letter]
        highest_letter = letter

print(f"Highest frequency: {highest_freq}")
print(f"Highest frequency letter: {highest_letter}")            


        
        
         





