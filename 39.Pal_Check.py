                              #!My Way(Not Very Efficient)
sentence=input("Enter A Sentence:").lower()
letter_list=list(sentence)
listt=[]
rev_list=[]
for reverse_index_of_letters in range(len(letter_list)-1,-1,-1):
    if letter_list[reverse_index_of_letters] !=" ":
         rev_list.append(letter_list[reverse_index_of_letters])
for index_of_letter in range(0,len(letter_list),1):
         if letter_list[index_of_letter] !=" ":
            listt.append(letter_list[index_of_letter])
if rev_list==listt:
      print(f"{sentence} is a palindrome")
else:
     print(f"{sentence}is not a palindrome")   
                  
                    #!Ghazarat's Way(Little More Efficient)

# Take user input and convert it to lowercase to make the check case-insensitive
sentence = input("Enter your sentence: ").lower()

# Initialize two empty lists to store characters in original and reverse order (ignoring spaces)
letter_list = []
rev_letter_list = []

# Loop through each character in the sentence
for i in range(0, len(sentence)):
    # Calculate the corresponding index from the end of the sentence
    j = len(sentence) - 1 - i
    
    # Get characters at positions i and j
    i_char, j_char = sentence[i], sentence[j]
    
    # If the character at position i is not a space, add it to letter_list
    if i_char != " ":
        letter_list.append(i_char)
    
    # If the character at position j is not a space, add it to rev_letter_list
    if j_char != " ":
        rev_letter_list.append(j_char)

# Compare the two lists to check if the sentence is a palindrome
if rev_letter_list == letter_list:
    print("Is a palindrome")
else:
    print("Is not a palindrome")








     

