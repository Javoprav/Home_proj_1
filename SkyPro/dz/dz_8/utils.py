'''импорты'''

import json, os

'''Определение класса с вопросами'''


class Question():

    def __init__(self, question_text, difficulty, correct_answer, is_asked=False, user_answer='', points=0):
        self.question_text = question_text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.is_asked = is_asked
        self.user_answer = user_answer
        self.points = points

    def get_points(self):
        return int(self.points * self.difficulty)

    def is_correct(self):
        return self.correct_answer == self.user_answer

    def build_question(self):
        return self.question_text

    def build_positive_feedback(self):
        return f'Ответ верный, получено {self.points} баллов'

    def build_negative_feedback(self):
        return f'Ответ неверный, верный ответ {self.correct_answer}'

    def __repr__(self):
        return f'Question {self.question_text, self.difficulty, self.correct_answer, self.is_asked, self.user_answer, self.points}'


'''загрузка списка вопросов'''


def dict_by():
    dict_by = os.path.join('SkyPro', 'dz', 'dz_8', 'question_answer.json')
    with open(dict_by, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    return data1


'''функция статистики'''


def print_stat(q, b):
    return f'Вот и всё! \nОтвечено {q} вопросов из {q} \nНабрано баллов: {b}'