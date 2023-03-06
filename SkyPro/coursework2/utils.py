'''импорты и переменные(константы)'''

import requests, json, random
from basic_word import BasicWord

URL_WORDS = "https://www.jsonkeeper.com/b/F632"


def load_words():
    #загрузка слов из url
    req = requests.get(URL_WORDS)
    data = req.json()
    return data  
    

def load_random_word():
    #функция получит список слов с внешнего ресурса,- выберет случайное слово,- создаст экземпляр класса `BasicWord`,- вернет этот экземпляр.
    list_words = []
    for i in load_words():
        orig_word = i['word']
        orig_subswords = i['subwords']
        orig_word_app = BasicWord(orig_word, orig_subswords)
        list_words.append(orig_word_app)
    return random.choice(list_words)