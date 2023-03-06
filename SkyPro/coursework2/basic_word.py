class BasicWord():
    '''Класс слов'''
    def __init__(self, original_word, subswords):
        self.original_word = original_word # исходное слово,
        self.subswords = subswords # набор допустимых подслов.

    def checking_entered_word(self, user_input):
        # проверка введенного слова в списке допустимых подслов (вернет bool)
        return user_input in self.subswords

    def len_subwords(self):
        # подсчет количества подслов (вернет int).
        return len(self.subswords)

    def __repr__(self):
        return f'BasicWord {self.original_word, self.subswords}'