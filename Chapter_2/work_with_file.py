file = open('text.txt', 'w')
file_symbols = file.write(('spam' * 2) + '\n')

print(file_symbols)

file = open('text.txt')
text = file.read()
print(text)