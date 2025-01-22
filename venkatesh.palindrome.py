my_str=str(input("Enter a String:"))
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
     print("The String is Palindrome")
else:
    print("The String is Not Palindrome")
