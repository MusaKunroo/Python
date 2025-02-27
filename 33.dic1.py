phone_number=(input("Input your number:"))
dictionary={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for x in phone_number:
    output+=(dictionary.get(x,"invalid"))+""
print(output)
    