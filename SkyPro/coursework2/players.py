class Player():
    '''класс игрока'''
    def __init__(self, name_user, words_used=[]):
        self.name_user = name_user # имя пользователя,
        self.words_used = words_used # использованные слова пользователя.

    def get_words_used(self):
        # получение количества использованных слов (возвращает int)
        return len(self.words_used)

    def add_words_used(self, user_input):
        # добавление слова в использованные слова (ничего не возвращает)
        self.words_used.append(user_input)

    def check_word_before(self, user_input):
        # - проверка использования данного слова до этого (возвращает bool).
        return user_input in self.words_used

    def __repr__(self):
        return f'Player {self.name_user, self.words_used}'