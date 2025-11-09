from random import randint
from graphic_arts.start_game_banner import run_screensaver

DEFAULT_DAMAGE = 5
DEFAULT_DEFENSE = 10
DEFAULT_STAMINA = 80


class Character:
    DAMAGE_RANGE = (1, 3)
    DEFENSE_RANGE = (1, 5)
    DEFAULT_SPECIAL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name

    def attack(self):
        """Возвращает нанесённый персонажем урон."""
        damage = DEFAULT_DAMAGE + randint(*self.DAMAGE_RANGE)
        return (f'{self.name} нанёс урон противнику равный '
                f'{damage}')

    def defense(self):
        """Возвращает блокированный персонажем урон."""
        block = DEFAULT_DEFENSE + randint(*self.DEFENSE_RANGE)
        return (f'{self.name} нанёс урон противнику равный '
                f'{block}')

    def special(self):
        """Возвращает примененное персонажем
        специальное умение."""
        return (f'{self.name} применил специальное умение '
                f'«{self.DEFAULT_SPECIAL} {self.SPECIAL_BUFF}»')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    DAMAGE_RANGE = (3, 5)
    DEFENSE_RANGE = (5, 10)
    DEFAULT_SPECIAL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = ('дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')


class Mage(Character):
    DAMAGE_RANGE = (5, 10)
    DEFENSE_RANGE = (-2, 2)
    DEFAULT_SPECIAL = 'Атака'
    SPECIAL_BUFF = DEFAULT_DAMAGE + 40
    BRIEF_DESC_CHAR_CLASS = ('находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом.')


class Healer(Character):
    DAMAGE_RANGE = (-3, -1)
    DEFENSE_RANGE = (2, 5)
    DEFAULT_SPECIAL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENSE + 30
    BRIEF_DESC_CHAR_CLASS = ('могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов.')


def choice_char_class(char_name: str) -> Character:
    """Возвращает выбранный персонажем класс."""
    classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = ''
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: '
                               'Воитель — warrior, Маг — mage, '
                               'Лекарь — healer: ').lower()
        if selected_class in classes:
            char_class: Character = classes[selected_class](char_name)
            print(char_class)
            approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                                   'или любую другую кнопку, '
                                   'чтобы выбрать другого персонажа ').lower()
        else:
            print('Неверно введено название класса. Повторите попытку.')
            continue
    return char_class


def start_training(char: Character) -> str:
    """Имитирует тренировку персонажа."""
    # Передать значениями саму ФУНКЦИЮ, а не её значение,
    # чтобы затем в момент print-а её вызвать и каждый раз
    # получать заново посчитанное рандомное значение.
    commands = {
        'attack': char.attack,
        'defense': char.defense,
        'special': char.special
        }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd not in commands:
            print('Повторите ввод команды (attack, defense, special): ')
            continue
        print(commands[cmd]())

    return 'Тренировка окончена.'


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    character: Character = choice_char_class(char_name)
    print(start_training(character))
