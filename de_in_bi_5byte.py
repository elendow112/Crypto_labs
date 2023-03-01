# перевод десятичной в двоичный (в ответе выдает 5 байт информации)
def de_bi_5bit(number: int or str):
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

    if len(binary) != 5:
        for i in range(5-len(binary)):
            binary = "0" + binary

    return binary


#print(de_bi_5bit('7'))