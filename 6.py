
class Alphabet:
    def __init__(self):
        self.letters = 'abcdefg'

    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration
harf = Alphabet()
for letter in harf:
    print(letter)
