# Given a text as input, find and output the longest word.

# Sample Input
# this is an awesome text

# Sample Output
# awesome
# Recall the split(' ') method, which returns a list of words of the string.

txt = input()



longest = max(txt.split(), key=len)


# Displaying longest word
print(longest)

