from typing import List


# Napište (čistou) funkci, která na vstupu dostane průřez krajiny a
# spočte, kolik vody se v dané krajině udrží, bude–li na ni
# neomezeně pršet. Krajina je reprezentována sekvencí celých
# nezáporných čísel, kde každé reprezentuje výšku jednoho úseku.
# Všechny úseky jsou stejně široké a mimo popsaný úsek krajiny je
# všude výška 0.
#
# Například krajina ‹[3, 1, 2, 3, 2]› dokáže udržet 3 jednotky vody
# (mezi prvním a čtvrtým segmentem):
#
#   ┌───┐       ┌───┐
#   │   │       │   │
#   │   │   ┌───┤   ├───┐
#   │   │   │   │   │   │
#   │   ├───┤   │   │   │
#   │   │   │   │   │   │
#   └───┴───┴───┴───┴───┘
#     3   1   2   3   2

def lakes(land: List[int]) -> int:
    result: int = 0
    # I reduce the maximum height to the second maximum height every step.
    # After that, I have two identical heights, and then calculate
    # the amount of water between them.
    # After that I reduce the heights
    # I was working with and enter a new cycle
    # When all the heights are equal I return the result
    while True:
        max_land: int = max(land)
        actual_max: int = 0
        if land.count(max_land) == 1:
            if max_land > 0:
                actual_max = max_land - 1
            while actual_max not in land and actual_max > 0:
                actual_max -= 1
            if max_land > 0:
                while max_land in land:
                    index_max: int = land.index(max_land)
                    land[index_max] = actual_max
        else:
            actual_max = max_land
        max_indexes: List[int] = [i for i in range(len(land))
                                  if land[i] == actual_max]
        if len(max_indexes) == len(land):
            return result
        max_indexes.reverse()
        len_max_indexes: int = len(max_indexes)
        for i in max_indexes:
            next_num: int = max_indexes.index(i) + 1
            if next_num < len_max_indexes:
                result = result + (i - max_indexes[next_num] - 1)
        while actual_max in land:
            land[land.index(actual_max)] = actual_max - 1
    return result


def main() -> None:
    assert lakes([0, 0, 0]) == 0
    assert lakes([20, 0, 1]) == 1
    assert lakes([1, 2, 3, 2, 1]) == 0
    assert lakes([3, 1, 2, 3, 2]) == 3
    assert lakes([2, 0, 1, 3, 2]) == 3
    assert lakes([4, 3, 2, 1, 0, 4]) == 10
    assert lakes([5, 6, 0, 3, 2, 5, 4, 1, 4, 2, 1, 3]) == 16
    assert lakes([4, 3, 2, 3, 1, 4, 5, 5, 3, 2, 1, 3]) == 10


if __name__ == '__main__':
    main()
