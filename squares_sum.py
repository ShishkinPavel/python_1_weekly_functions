from typing import List
from math import sqrt


# Napište predikát, který rozhodne, zda lze dané nezáporné číslo
# ‹num› napsat jako součet ⟦∑ᵢ₌₁ⁿaᵢ²⟧, kde ⟦n⟧ je zadáno parametrem
# ‹count› a ⟦aᵢ⟧ jsou po dvou různá nezáporná čísla. Jinými slovy,
# lze ‹num› zapsat jako součet ‹count› druhých mocnin různých
# nezáporných čísel?

# -----------------------------------------
# -----------------------------------------
# I started making Python after Haskell
# and I got something strange, but it works

# I made 1 complex example and 2 simple ones,
# but still don't understand anything

def combinations(a: List[int]) -> List[List[int]]:
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combinations(a[1:]):
        cs += [c, c + [a[0]]]
    return cs


def square(number: int) -> int:
    return number ** 2


def is_sum_of_squares(num: int, count: int) -> bool:
    # I take the square root of a number,
    # because it is the largest number
    # to satisfy the condition.
    x = round(sqrt(num))
    list_x = []

    check_num = 0
    check_count = 0

    # Must be check_count > count to satisfy the condition
    for i in range(1, x):
        check_num += i ** 2
        list_x.append(i)
        check_count += 1
        if check_num > num:
            break

    if check_count <= count:
        return False

    # I take all possible combinations of numbers
    elements = combinations(list_x)

    for elem in elements:
        if len(elem) == count and \
                sum(map(square, elem)) == num:
            return True
    return False


def main() -> None:
    assert is_sum_of_squares(42, 3)
    assert not is_sum_of_squares(42, 2)
    assert not is_sum_of_squares(18, 2)
    assert not is_sum_of_squares(100, 3)
    assert is_sum_of_squares(100, 5)
    assert not is_sum_of_squares(1000, 13)


if __name__ == '__main__':
    main()
