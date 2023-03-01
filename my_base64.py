# реализация бейс 64
from textwrap import wrap
from de_in_bi_8byte import de_bi
from de_in_bi_6byte import de_bi_6bit


def my_encode_base64(word: str):
    # таблица бейс 64
    array_base64 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",\
                    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h",\
                    "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",\
                    "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]


    array_word = []
    # перевод аски в 10 систему и перевод в двоичную
    array_word = [de_bi(ord(i)) for i in word]
    # склеивание
    array_word = "".join(map(str, array_word))
    flag = int
    # проверка на кратность 6(нужно для постановки =)
    if len(array_word) % 6 == 4:
        array_word += "00"
        flag = 1
    elif len(array_word) % 6 == 2:
        array_word += "0000"
        flag = 2
    # разрез строки
    array_word = wrap(array_word, 6)
    # перевод двоичный в десятичную
    array_word = [int(i, 2)for i in array_word]
    # приравнение к буквам из таблицы бейс 64
    for i in range(len(array_word)):
        array_word[i] = array_base64[array_word[i]]
    # постановка = по флагу
    if flag == 1:
        array_word.append("=")
    if flag == 2:
        array_word.append("==")
    # финальное скреивание слова
    array_word = "".join(map(str, array_word))
    return array_word


def my_decode_base64(word: str):
    array_base64 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", \
                    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", \
                    "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", \
                    "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
    array_word = list(word)
    flag = str

    if array_word[-2] == "=" and array_word[-1] == "=":
        flag = 2
        del array_word[-1]
        array_word.remove("=")
    elif array_word[-1] == "=":
        flag = 1
        del array_word[-1]

    for i in range(len(array_word)):
        for j in range(len(array_base64)):
            if array_word[i] == array_base64[j]:
                array_word[i] = de_bi_6bit(j)

    if flag == 1:
        array_word[-1] = array_word[-1][:-2]
    elif flag == 2:
        array_word[-1] = array_word[-1][:-4]

    array_word = "".join(map(str, array_word))
    array_word = wrap(array_word, 8)
    array_word = [chr(int(i, 2))for i in array_word]
    array_word = "".join(map(str, array_word))

    return array_word


while True:
    a = input("введите слово для шифровки: ")
    print("зашифрованная строка: ", my_encode_base64(a))
    print("расшифрованная строка: ", my_decode_base64(my_encode_base64(a)))

#
#
#