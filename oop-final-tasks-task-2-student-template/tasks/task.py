class Cipher:
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z'
    ]

    def __init__(self, keyword):
        self.keyword = keyword
        self.to_cipher_alphabet = {}
        self.to_plain_alphabet = {}
        self.make_cipher_alphabet()

    def make_cipher_alphabet(self):
        lst_letters = []
        for s in self.keyword:
            if s not in lst_letters:
                lst_letters.append(s.upper())

        for s in self.alphabet:
            if s not in lst_letters:
                lst_letters.append(s)

        self.to_cipher_alphabet = {k: v for k, v in zip(self.alphabet, lst_letters)}
        self.to_plain_alphabet = {k: v for k, v in zip(lst_letters, self.alphabet)}

    def encode(self, data):
        cipher_data = ""
        for s in data:
            if self.to_cipher_alphabet.get(s.upper()) is not None:
                cipher_data += self.to_cipher_alphabet.get(s.upper())
            else:
                cipher_data += s
        return cipher_data.capitalize()
    
    def decode(self, data):
        plain_data = ""
        for s in data:
            if self.to_plain_alphabet.get(s.upper()) is not None:
                plain_data += self.to_plain_alphabet.get(s.upper())
            else:
                plain_data += s
        return plain_data.capitalize()
