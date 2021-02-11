# Napište funkci, která zploští seznam seznamů do jednoho nového
# seznamu tak, že vnořené seznamy pospojuje za sebe.

def concat(lists):
    return sum(lists, [])


def main():
    assert concat([["1"], [2], [1, 2]]) == ["1", 2, 1, 2]
    assert concat([[0, 40, 1], [43, -1], [2]]) == [0, 40, 1, 43, -1, 2]
    assert concat([[1]]) == [1]
    assert concat([[], [1], []]) == [1]
    assert concat([[1, 1, 1], [1], [1, 1]]) == [1, 1, 1, 1, 1, 1]


if __name__ == "__main__":
    main()