# Napište predikát ‹is_visa›, který je pravdivý, reprezentuje-li
# číslo ‹number› validní číslo platební karty VISA, tj. začíná
# cifrou 4, má 13, 16, nebo 19 cifer a zároveň je validním číslem
# platební karty (viz příklad ‹credit›).

def is_valid_card(number):
    cifry = list(map(int, str(number)))
    sum1 = sum(cifry[-1::-2])
    sum2 = sum([sum(divmod(2 * k, 10)) for k in cifry[-2::-2]])
    return (sum1 + sum2) % 10 == 0


def is_visa(number):
    bo = bool(is_valid_card(number))
    x = str(number)  # перевод в строку
    a = x.find("4")  # поиск позиции четверки
    c = len(x)  # длина строки
    if (a == 0) and (
            c == 16 or c == 19 or c == 13) and bo is True:
        return True


# Dále napište predikát ‹is_mastercard›, který je pravdivý,
# reprezentuje-li číslo ‹number› validní číslo platební karty
# MasterCard, tj. začíná prefixem 50–55, nebo 22100–27209, má 16
# cifer a zároveň je validním číslem platební karty.

def is_mastercard(number):
    bo = bool(is_valid_card(number))
    x = str(number)  # перевод в строку
    is5x = x[0:2]  # первые 2 символа строки х
    is2xxxx = x[0:5]  # первые 5 символов строки х
    l1 = list(range(50, 56))  # лист валидности 50-55
    l2 = list(range(22100, 27210))  # лист валидности 22100-27209
    c = len(x)  # длина строки
    if c == 16 and bo is True and (int(is5x) in l1 or int(is2xxxx) in l2):
        return True


def main():
    assert is_visa(4111111111111111)
    assert is_visa(4012888888881881)
    assert is_visa(4988438843884305)
    assert is_visa(4646464646464644)
    assert is_visa(4199350000000002)
    assert is_visa(4222222222222)
    assert is_visa(4111111111111111110)

    assert not is_visa(411111111111116)
    assert not is_visa(5500000000000004)
    assert not is_visa(4929300836739328)

    assert is_mastercard(5500000000000004)
    assert is_mastercard(5555555555554444)
    assert is_mastercard(5105105105105100)
    assert is_mastercard(5424000000000015)
    assert is_mastercard(2223520443560010)
    assert is_mastercard(5101180000000007)
    assert is_mastercard(2222400070000005)

    assert not is_mastercard(4012888888881881)
    assert not is_mastercard(22004000700000003)
    assert not is_mastercard(5624000000000013)
    assert not is_mastercard(2721000030000016)
    assert not is_mastercard(5101180000000000003)


if __name__ == "__main__":
    main()
