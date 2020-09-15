# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Гусь-на-гору-заберусь 🦆 решил забраться на гору. '
        'Взять ему зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Гусь-за-ногу-кусь стащил зонтик у мимо проходящей бабушки 👵. '
        'Найти чего-нибудь перекусить в дорогу? '
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_burger()
    return step3_no_burger()


def step2_no_umbrella():
    print(
        'Гусь-за-хвост-кусь испугал прогуливающегося кота. '
        'Найти чего-нибудь перекусить в дорогу? '
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_burger()
    return step3_no_burger()


def step3_burger():
    print(
        'Гусь-съем-и-съе.... спёр бутерброд у инвалида. '
        'Ну чо, гора?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_mountain()
    return step4_no_mountain()


def step3_no_burger():
    print(
        'Гусь-рокер-с-марса зацепил шланг бочки с бензином '
        'и взорвал бензоколонку. '
        'Начать заново?'
    )
    option = ''
    options = {'да': True}
    while option not in options:
        print('Выберите: {}'.format(*options))
        option = input()

    if options[option]:
        return step1()


def step4_mountain():
    print(
        'Гусь-наверх-крадусь взошёл на гору. Йей. '
        'Начать заново?'
    )
    option = ''
    options = {'да': True}
    while option not in options:
        print('Выберите: {}'.format(*options))
        option = input()

    if options[option]:
        return step1()


def step4_no_mountain():
    print(
        'Гусь-наверх-крадусь пошёл пакостничать дальше, его отловили и съели. '
        'Начать заново?'
    )
    option = ''
    options = {'да': True}
    while option not in options:
        print('Выберите: {}'.format(*options))
        option = input()

    if options[option]:
        return step1()


if __name__ == '__main__':
    step1()
