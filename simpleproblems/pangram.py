''' 
Pangram function
'''
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def IsPangram(input_str):
    missing_char = ''
    input_str = input_str.lower()
    print(input_str)
    for char in ALPHABET:
       
        if char not in input_str:
             missing_char += char
    print(f'missing char {missing_char}')
    if len(missing_char) > 0:
        return False
        #return missing_char
    else:
        return True

if __name__ == "__main__":
    print(IsPangram("The quick brown fox jumps over the lazy dog"))