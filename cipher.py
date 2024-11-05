# add your code here
def replace_letters(sentence, letter_dict):
    # Create a new string 
    replaced_sentence = ''.join([letter_dict.get(char.lower(), char) if char.isalpha() else char for char in sentence])
    
    return replaced_sentence

# Dictionary
letter_dict = {
    'a': 'f',
    'b': 'g',
    'c': 'h',
    'd': 'i',
    'e': 'j',
    'f': 'k',
    'g': 'l',
    'h': 'm',
    'i': 'n',
    'j': 'o',
    'k': 'p',
    'l': 'q',
    'm': 'r',
    'n': 's',
    'o': 't',
    'p': 'u',
    'q': 'v',
    'r': 'w',
    's': 'x',
    't': 'y',
    'u': 'z',
    'v': 'a',
    'w': 'b',
    'x': 'c',
    'y': 'd',
    'z': 'e'
}

sentence = input("Enter a sentence: ")
replaced_sentence = replace_letters(sentence, letter_dict)

print("Original sentence: ", sentence)
print("Replaced sentence: ", replaced_sentence)
