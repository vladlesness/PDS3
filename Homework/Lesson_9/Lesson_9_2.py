class TextProcessor:
    PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    def get_clean_string(self, text):
        clean_text = ''
        for char in text:
            if self.__is_punctuational(char):
                continue
            clean_text += char
        return clean_text

    def __is_punctuational(self, char):
        return char in self.PUNCTUATION


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print(f'Cleaned string is {self.__clean_string}')
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, text_list):
        clean_text_list = []
        for text in text_list:
            self._text_loader.set_clean_string(text)
            clean_text_list.append(self._text_loader.clean_string)
        return clean_text_list
