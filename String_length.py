def string_length(string):
  count = 0
  for char in string:
    count += 1
  return count
my_string = "Hello, World!"
length = string_length(my_string)
print("Length of the string:", length)