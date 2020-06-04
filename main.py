bits = {
    # Чтение регистров
    'RDDR': 0,
    'RDCR': 1,
    'RDIP': 2,
    'RDSP': 3,
    'RDAC': 4,
    'RDBR': 5,
    'RDPS': 6,
    'RDIR': 7,
    # АЛУ
    'COMR': 8,
    'COML': 9,
    'PLS1': 10,
    'SORA': 11,
    # Управление коммутатором
    'LTOL': 12,
    'LTOH': 13,
    'HTOL': 14,
    'HTOH': 15,
    'SEXT': 16,
    'SHLT': 17,
    'SHL0': 18,
    'SHRT': 19,
    'SHRF': 20,
    'SETC': 21,
    'SETV': 22,
    'STNZ': 23,
    # Чтение регистров
    'WRDR': 24,
    'WRCR': 25,
    'WRIP': 26,
    'WRSP': 27,
    'WRAC': 28,
    'WRBR': 29,
    'WRPS': 30,
    'WRAR': 31,
    # Работа с памятью
    'LOAD': 32,
    'STOR': 33,
    # Организация ввода-вывода
    'IO': 34,
    'IRQS': 35,
    # Резервные сигналы
    'no idea what to write there': 36,
    'should not be possible to write this anyway': 37,
    # Останов БЭВМ
    'HALT': 38,
    # Работа с памятью
    'TYPE': 39
}


def mnemonics_to_bits(mnemonics_list):
    this_lines_bits = sorted(list(map(bits.get, mnemonics_list)), reverse=True)
    command_binary = ''
    for bit in range(39, -1, -1):
        command_binary = command_binary + ('1' if bit in this_lines_bits else '0')
    return command_binary


def bits_to_hex(bit_line):
    # костыль потому что у меня нет времени разбираться как нормально сделать
    return str(hex(int(bit_line, 2)))[2:]


def operational(line_split):
    line_split.pop(0)  # удаляем oper
    return bits_to_hex(mnemonics_to_bits(line_split)).zfill(10)


b = {  # у меня мозг не работает, потом нормально сделаю
    '0': '00',
    '1': '02',
    '2': '04',
    '3': '08',
    '4': '10',
    '5': '20',
    '6': '40',
    '7': '80'
}


def control(line_split):
    line_split.pop(0)  # удаляем control
    command_hex = '8' + line_split.pop(0)  # код операции + резерв + однобитовое поле сравнения (COMP)
    command_hex = command_hex + line_split.pop(0)  # hex адрес перехода
    # поле выбора проверяемого бита (8 бит) из коммутатора, от 0 до 7
    command_hex = command_hex + b.get(line_split.pop(0))
    command_hex = command_hex + bits_to_hex(mnemonics_to_bits(line_split))  # мнемоники
    return command_hex


print("""
ВНИМАНИЕ! Скрипт не проверяет почти никакие ошибки. 
Возможные опечатки: несуществующая мнемоника, отсутствие пробела/ключевого слова/неправильный формат введенного числа.
Скрипт может либо крашнуться, либо вообще не дать знать об ошибке.
Сори, у меня не было времени всё предусмотреть.

Синтаксис микрокоманд (мнемоники вводятся через пробел):
Операционная: oper [мнемоники]
Управляющая:  control {значение COMP 1/0} {hex адрес перехода} {decimal поле выбора проверяемого бита (8бит) из коммутатора} [мнемоники]
""")

with open('input.txt', 'r', encoding='utf-8') as lines:
    for line in lines:
        line_split = line.upper().strip().split(' ')
        try:
            if line_split[0] == 'OPER':
                print(operational(line_split))
            elif line_split[0] == 'CONTROL':
                print(control(line_split))
            else:
                print('Неправильное ключевое слово в строке: ' + line)
        except:
            print('Где-то тут ошибка:' + line)
