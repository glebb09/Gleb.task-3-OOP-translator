from Translator import Translator


eng_to_rus_dictionary = dict({
    "Hello": "Привет",
    "Morning": "Утро",
    "Car": "Автомобиль",
    "Truck": "Грузовик",
})



rus_to_eng_dictionary = dict({
    "Автомобиль": "Car",
    "Вечер": "Evening",
    "Грузовик": "Truck",
    "Платье": "Dress",
})



rus_to_blr_dictionary = dict({
    "Грузовик": "Грузавік",
    "Утро": "Раніца"

})

eng_to_rus_translator = Translator(eng_to_rus_dictionary)
rus_to_eng_translator = Translator(rus_to_eng_dictionary)
rus_to_blr_translator = Translator(rus_to_blr_dictionary)

print(eng_to_rus_translator.dictionary)
print(rus_to_eng_translator.dictionary)
print(rus_to_blr_translator.dictionary)

new_rus_to_blr_dictionary = dict({
    "Утро": "Раніца"

})


rus_to_blr_translator.dictionary = new_rus_to_blr_dictionary
print(rus_to_blr_translator.dictionary)

rus_to_blr_translator.dictionary = "MyDictionary"
print(rus_to_blr_translator.dictionary)

eng_to_rus_translator.translate_word("Hello")
eng_to_rus_translator.translate_word("Truck")
rus_to_blr_translator.translate_word("Грузовик")
rus_to_blr_translator.translate_word("Утро")
rus_to_eng_translator.translate_word("Вечер")
rus_to_eng_translator.translate_word("Платье")
