# импорты
from utils import load_words, load_random_word
from basic_word import BasicWord
from players import Player

# функция основного цикла
def main():
    user_name = input('Ввведите имя игрока: ')
    player = Player(user_name)
    print(f'Привет, {user_name}!')
    
    basic_word = load_random_word()
    
    print(f'Составьте {basic_word.len_subwords()} слов из слова {basic_word.original_word}')
    print(f'Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?: ')
    count = 0
    while count < basic_word.len_subwords():
        user_input = input('Ввод: ')
        if str(user_input) == "stop".lower() or str(user_input) == 'стоп'.lower():
            print(f'Игра завершена, вы угадали {player.get_words_used()}!')
            quit('программа завершена')
        elif len(user_input) < 3:
            print('слишком короткое слово')
        elif user_input not in basic_word.subswords:
            print('неверно')
        elif player.check_word_before(user_input):
            print('уже использовано')
        else:
            if user_input in basic_word.subswords:
                player.add_words_used(user_input)
                print('верно')
        count += 1
    print(f'Игра завершена, вы угадали {player.get_words_used()}!')
print(main())