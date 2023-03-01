# перевод десятичной в двоичный (в ответе выдает 6 байт информации)
def de_bi_6bit(number: int or str):
    binary = []
    while True:

        if int(number) % 2 == 0:
            number = int(number) / 2
            binary.append("0")
        elif int(number) % 2 == 1:
            number = int(int(number) / 2)
            binary.append("1")
        if number == 0:
            break
    binary.reverse()
    binary = "".join(map(str, binary))

    if len(binary) != 6:
        for i in range(6-len(binary)):
            binary = "0" + binary

    return binary


#print(de_bi_6bit('10'))