# реализация бейс 32
from textwrap import wrap
from de_in_bi_8byte import de_bi
from de_in_bi_5byte import de_bi_5bit


def my_encode_base32(word: str):

    array_base32 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", \
                    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "2", "3", "4", "5", "6", "7"]


    # перевод аски в 10 систему и перевод в двоичную
    array_word = [de_bi(ord(i)) for i in word]
    # склеивание

    if len(array_word) % 5 == 4:
        array_word.append("xxxxxxxx")
    elif len(array_word) % 5 == 3:
        for i in range(2):
            array_word.append("xxxxxxxx")
    elif len(array_word) % 5 == 2:
        for i in range(3):
            array_word.append("xxxxxxxx")
    elif len(array_word) % 5 == 1:
        for i in range(4):
            array_word.append("xxxxxxxx")

    array_word = "".join(map(str, array_word))

    array_word = wrap(array_word, 5)

    for i in range(len(array_word)):
        if "x" in array_word[i]:
            if "1" in array_word[i] or "0" in array_word[i]:

                array_word[i] = list(array_word[i])
                for j in range(len(array_word[i])):
                    if array_word[i][j] == "x":
                        array_word[i][j] = "0"

                array_word[i] = "".join(map(str, array_word[i]))
            else:
                array_word[i] = "="

    #перевод двоичный в десятичную
    for i in range(len(array_word)):
        if array_word[i] != "=":
            array_word[i] = int(array_word[i], 2)
    print(array_word)
    # приравнение к буквам из таблицы бейс 64
    for i in range(len(array_word)):
        if array_word[i] != "=":
            array_word[i] = array_base32[int(array_word[i])]

    # финальное скреивание слова
    array_word = "".join(map(str, array_word))
    return array_word


def my_decode_base32(word: str):

    array_base32 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", \
                    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "2", "3", "4", "5", "6", "7"]

    array_word = list(word)

    for i in range(len(array_word)):
        if array_word[i] != "=":
            for j in range(len(array_base32)):
                if array_word[i] == array_base32[j]:
                    array_word[i] = j

    for i in range(len(array_word)):
        if array_word[i] != "=":
            array_word[i] = de_bi_5bit(str(array_word[i]))
        else:
            array_word[i] = "xxxxx"

    array_word = "".join(array_word)
    array_word = wrap(array_word, 8)

    for i in range(len(array_word)):
        if "x" not in array_word[i]:
            array_word[i] = chr(int(array_word[i], 2))

    array_word = [i for i in array_word if "x" not in i]

    array_word = "".join(array_word)
    return array_word


while True:
    a = input("введите слово для шифровки: ")
    print("зашифрованная строка: ", my_encode_base32(a))
    print("расшифрованная строка: ", my_decode_base32(my_encode_base32(a)))