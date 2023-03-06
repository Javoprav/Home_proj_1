'''### Основной цикл
**Задача 1**
У вас есть класс Player.
Создайте три экземпляра класса , положите в список players
Alex, 700
Mary, 950
Ann, 890
Напишите  функцию `total_score`, которая  и возвращает сумму всех игроков по очкам
Напишите функцию `avg_score`, которая получает список players возвращает среднее значени по очкам'''

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_score(self):
        return self.score