import unicodedata
import re


class Helpers():
    @staticmethod
    def normalize_string(string):
        formatting1 = ''.join(c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn')
        formatting2 = formatting1.lower()
        return re.sub(r'[^a-z0-9]+', '', formatting2)

