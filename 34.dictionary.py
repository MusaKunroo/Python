customer={
    "Name":"Rampo",
    "Age":28,
    "is_verified":True

}
print(customer["Name"])#if we try to print for a the doesnt exist in the dictionary the code will yell an error
#if we try to print for a the doesnt exist in the dictionary the code will not yell an error instead will print none
print(customer.get("birthdate","19 September 1865"))#but this way you can not only avoid an error shout but also set a default value for a key  out side the dictionary though we can set the default value inside the dictionary we might need this method for  
                                                        #You don't control the dictionary's structure – If data is coming from an API, database, or user input, some keys might be missing. .get() prevents errors when accessing them.
                                                        # You want different fallbacks for different cases – If multiple parts of your code request "birthdate", they can provide different defaults based on context.
                                                        # You don't want to modify the dictionary – Using .get() avoids adding unnecessary default values to every dictionary you access.
                                                        # It's mostly about flexibility and error prevention when dealing with unpredictable or dynamic data
print(customer.get("Name"))                                                        