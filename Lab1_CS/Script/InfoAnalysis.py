class Analysis():

    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(self.file, encoding="utf-8") as my_new_file:
            return my_new_file.read()

    def entropy(self, text=''):
        self.text = text
        from math import log
        log2 = lambda x: log(x) / log(2)
        total = len(self.text)
        counts = {}
        for item in self.text:
            counts.setdefault(item, 0)
            counts[item] += 1
        ent = 0
        for i in counts:
            p = float(counts[i]) / total
            ent -= p * log2(p)
        return ent

    def char_frequency(self):
        chars = list(set(self.read_file()))
        collection_chars = {}
        for item in chars:
            collection_chars[item] = 0
        for item in self.read_file():
            collection_chars[item] += 1
        for item in chars:
            collection_chars[item] /= len(self.read_file())
        return collection_chars

    def calculate_chars(self):
        import re
        count = 0
        for item in self.read_file():
            if item in '([а-яА-Я])':
                count += 1
        return count * self.entropy(self.read_file())



file1 = "G:\Projects\Labs_Computer_Systems\Lab1_CS\TextFiles\Whenidie.txt"
file2 = "G:\Projects\Labs_Computer_Systems\Lab1_CS\TextFiles\Tigrolovi.txt"
file3 = "G:\Projects\Labs_Computer_Systems\Lab1_CS\TextFiles\Aforyzmy.txt"

analysis = Analysis(file1)
print('Entrophy:', analysis.entropy(analysis.read_file()))
print('Char frequency:', analysis.char_frequency())
print('Calculate chars', analysis.calculate_chars())
