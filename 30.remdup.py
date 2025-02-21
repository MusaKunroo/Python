numbers=[1,1,2,2,3,3,7,8,8,9,9]
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)        
                                              #!My Way
# numbers = [2,2, 2, 4, 6, 3, 4, 6, 1]                                             
# i = 0  
# while i < len(numbers): 
#     j = i + 1 
#     while j < len(numbers):  
#         if numbers[i] == numbers[j]:  
#             del numbers[j]  
#         else:
#             j += 1  
#     i += 1  

# print(numbers)              
    
