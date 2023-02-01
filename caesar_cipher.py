def caesar(text, shift, alphabets: list, code):
    shift %= 26
    shifted_alphabets = tuple(map(lambda alphabet: alphabet[shift:] + alphabet[:shift], alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabets = ''.join(shifted_alphabets)
    if code == 0: # Encrypt
        table = str.maketrans(final_alphabet, final_shifted_alphabets)
    if code == 1: # Decrypt (reverse)
        table = str.maketrans(final_shifted_alphabets, final_alphabet)

    return text.translate(table)

    
