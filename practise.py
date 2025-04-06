def reverse_string(s):
    reverse = ''
    for i in s:
        reverse = i + reverse
    return reverse

word = input('Enter a word:\n')
reversed_string = reverse_string(word)
print(reversed_string)

