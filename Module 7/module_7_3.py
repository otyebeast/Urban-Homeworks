class WordsFinder:
    def __init__(self, *file_txt):
        self.file_names = file_txt

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                file = file.read().lower()
                for j in  [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(j, '')
                words = file.split()
                all_words[i] = words
        return all_words


    def find(self, word):
        result1 = {}
        for i, word_ in self.get_all_words().items():
            for j, wd in enumerate(word_, 1):
                if wd == word.lower():
                    result1[i] = j
                    break
        return result1


    def count(self, word):
        result2 = {}
        for i, word_ in self.get_all_words().items():
            result2[i] = word_.count(word.lower())
        return result2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего