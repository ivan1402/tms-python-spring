""" Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)[03-10.32]
"""
list_exp = ['ivavi', 'nana', 'opo']


def palindrom_(*args):
    for i in args:
        if i[::-1] == i:
            print(f"{i} - палиндром")
        else:
            print(f"{i} - не палиндром")


for j in list_exp:
    palindrom_(j)
