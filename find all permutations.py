from itertools import permutations

def get_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example usage
string = "xyz"
perms = get_permutations(string)
print(perms)