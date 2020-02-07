class Analysis():
    # ініціалізуємо змінну шляху
    def __init__(self, file):
        self.file = file
    # зчитужмо файл і повертаємо строку з його вмістом
    def read_file(self):
        with open(self.file, encoding="utf-8") as my_new_file:
            return my_new_file.read()
    # ентропія нерівноймовірного алфавіту
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
    # обраховує частоти (імовірності) появи символів в тексті
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

    # визначає кількість інформаці
    def calculate_chars(self):
        import re
        count = 0
        for item in self.read_file():
            if item in '([а-яА-Я])':
                count += 1
        return count * self.entropy(self.read_file())

    def base_64_Encode(self):
        import re

        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7",
                    "8", "9", "+", "/"]
        bit_str = ""
        base64_str = ""
        text = self.read_file()

        # Проведіть через усі символи об'єднавши їх у бінарний рядок
        for char in text:
            bin_char = bin(ord(char)).lstrip("0b")
            bin_char = (8 - len(bin_char)) * "0" + bin_char
            bit_str += bin_char

        # Додайте нуль, поки довжина тексту не ділиться на 3
        while (((len(text)) % 3) != 0):
            bit_str += "00000000"
            text += "0"

        # Розділіть bit_str на 6-бітні дужки
        brackets = re.findall('(\d{6})', bit_str)

        # Кодує дужки
        for bracket in brackets:
            if (bracket == "000000"):
                base64_str += "="
            else:
                base64_str += alphabet[int(bracket, 2)]
        return base64_str



file1 = "G:\Projects\Labs_Computer_Systems\Lab1_CS\TextFiles\Whenidie.txt"
file2 = "G:\Projects\Labs_Computer_Systems\Lab1_CS\TextFiles\Tigrolovi.txt"
file3 = "G:\Projects\Labs_Computer_Systems\Lab1_CS\TextFiles\Aforyzmy.txt"

analysis = Analysis(file1)
print('Entrophy:', analysis.entropy(analysis.read_file()))
print('Char frequency:', analysis.char_frequency())
print('Calculate chars', analysis.calculate_chars())
print(analysis.base_64_Encode())
