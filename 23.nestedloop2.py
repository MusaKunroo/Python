numbers=[2,2,2,2,7]
for x_count in numbers:
    output=''
    for count in range(x_count): #count is redundant variable that is only there to keep the sytax of loops correct our main objective is to just run to nested loop as many time as the numbers inside the numbers vairable using the range function adn when is nested loop runs the output variable runs as many times as the numbers is the number variable after printing the first time loops runs again till all number of the loop enter the loop
        output+='x'
    print(output)
    
    