class Translator:

    def __init__(self, dictionary):
        self.__dictionary = dictionary


    @property
    def dictionary(self):
        return self.__dictionary


    @dictionary.setter
    def dictionary(self, value):
        if isinstance(value, dict):
            self.__dictionary = value
        else:
            print("Словарь должен быть типа <dict>")


    def translate_word(self, key):
        if key in self.__dictionary:
            print(key, " -> ", self.__dictionary[key])
        else:
            print("Для слова " + key + " перевода нет")

