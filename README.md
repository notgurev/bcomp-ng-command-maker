# bcomp-ng-command-maker

Скрипт, составляющий hex-микрокоманды для БЭВМ-NG из мнемоник и удобных чисел.

ВНИМАНИЕ! Скрипт не проверяет почти никакие ошибки. 
Возможные опечатки: несуществующая мнемоника, отсутствие пробела/ключевого слова/неправильный формат введенного числа.
Скрипт может либо крашнуться, либо вообще не дать знать об ошибке.
Сори, у меня не было времени всё предусмотреть (можете кидать PR с фиксами).

### Синтаксис микрокоманд (мнемоники вводятся через пробел):
Операционная: `oper [мнемоники]`

Управляющая:  `control {значение COMP 1/0} {hex адрес перехода} 
{decimal поле выбора проверяемого бита (8бит) из коммутатора} [мнемоники]`

Скрипт к регистру не чувствителен.

Вопросы: vk.com/notgurev
