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
    # Останов БЭВМ
    'HALT': 38,
}


def mnemonics_to_bits(mnemonics_list):
    this_lines_bits = sorted(list(map(bits.get, mnemonics_list)), reverse=True)
    command_binary = ''
    for bit in range(39, -1, -1):
        command_binary = command_binary + ('1' if bit in this_lines_bits else '0')
    return command_binary


def bits_to_hex(bit_line):
    # костыль потому что у меня нет времени разбираться как нормально сделать
    return str(hex(int(bit_line, 2)))[2:].upper()


def operational(line_split):
    line_split.pop(0)  # удаляем oper
    return bits_to_hex(mnemonics_to_bits(line_split)).zfill(10)


def control(line_split):
    line_split.pop(0)  # удаляем control
    command_hex = '8' + line_split.pop(0)  # код операции + резерв + однобитовое поле сравнения (COMP)
    command_hex = command_hex + line_split.pop(0)  # hex адрес перехода
    # поле выбора проверяемого бита (8 бит) из коммутатора, от 0 до 7
    checked_bits_decimal = line_split.pop(0).split(',')  # проверяемые биты (несколько)
    checked_bits_binary = ''
    for bit in range(7, -1, -1):
        checked_bits_binary = checked_bits_binary + ('1' if str(bit) in checked_bits_decimal else '0')
    command_hex = command_hex + bits_to_hex(checked_bits_binary)
    command_hex = command_hex + bits_to_hex(mnemonics_to_bits(line_split))  # мнемоники
    return command_hex


def unconditional(address):
    return '80' + address + '101040'


print("""
ВНИМАНИЕ! Скрипт не проверяет почти никакие ошибки. 
Возможные опечатки: несуществующая мнемоника, отсутствие пробела/ключевого слова/неправильный формат введенного числа.
Скрипт может либо крашнуться, либо вообще не дать знать об ошибке.
Сори, у меня не было времени всё предусмотреть.

Синтаксис микрокоманд (мнемоники вводятся через пробел):
Операционная: oper [мнемоники]
Управляющая:  control/ctrl {значение COMP 1/0} {hex адрес перехода} {decimal выбранные проверяемые биты (0-7) из коммутатора} [мнемоники]

Дополнительные примочки:
Безусловный переход: jump {hex адрес перехода} (эквивалент ctrl 0 ADDR 4 RDPS LTOL)
""")

with open('input.txt', 'r', encoding='utf-8') as lines:
    for line in lines:
        line_split = line.upper().strip().split(' ')
        keyword = line_split[0]
        try:
            if keyword == 'OPER':
                print(operational(line_split))
            elif keyword == 'CONTROL' or keyword == 'CTRL':
                print(control(line_split))
            elif keyword == 'JUMP':
                print(unconditional(line_split[1]))
            else:
                print('Неправильное ключевое слово в строке: ' + line)
        except:
            print('Где-то тут ошибка:' + line)
