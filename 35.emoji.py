emojis={
    ":)":"😀",
    ":(":"🥺",
    "xD":"🤬"
}
words=input("How do you feel?:")
output=""
word_list=words.split()
for x in word_list:
    output+= emojis.get(x,x)+""
print(output)


