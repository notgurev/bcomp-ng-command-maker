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
