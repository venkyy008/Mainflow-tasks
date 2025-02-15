def is_substring(main_string, sub_string):
    return sub_string in main_string

# Example usage
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring: ")

if is_substring(main_str, sub_str):
    print("The substring exists in the main string.")
else:
    print("The substring does not exist in the main string.")