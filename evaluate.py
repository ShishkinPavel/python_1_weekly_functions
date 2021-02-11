from typing import Optional, Dict, Any


# V tomto příkladu budeme opět pracovat se stromy, které
# reprezentují aritmetické výrazy. Tyto mají následující strukturu:
#
#  • konstantu reprezentuje strom, který má oba podstromy prázdné,
#  • složený výraz je reprezentován stromem, který má v kořenu
#    uložen operátor a jeho neprázdné podstromy reprezentují
#    operandy.
#
# Žádné jiné uzly ve stromě přítomny nebudou. Hodnoty konstant lze
# na celá čísla převést zabudovanou funkcí ‹int›.

class Tree:
    def __init__(self, value: str,
                 left: Optional['Tree'] = None,
                 right: Optional['Tree'] = None):
        self.value = value
        self.left = left
        self.right = right


# Napište čistou funkci, která na vstupu dostane instanci výše
# popsaného stromu a vrátí výsledek vyhodnocení výrazu, který
# tento strom reprezentuje.

def evaluate(tree: Tree) -> int:
    if tree.left is None or tree.right is None:
        return int(tree.value)

    #   I can do it like this:

    #   return int(eval(str(evaluate(tree.left)) +
    #                   tree.value +
    #                   str(evaluate(tree.right))))

    #   But i think this is better and safer way:

    operator: Dict[str, Any] = {'+': lambda x, y: x + y,
                                '-': lambda x, y: x - y,
                                '*': lambda x, y: x * y,
                                '/': lambda x, y: x / y,
                                '^': lambda x, y: x ^ y}

    return int(operator[tree.value](evaluate(tree.left),
                                    evaluate(tree.right)))


def main() -> None:
    t1 = Tree("5")
    t2 = Tree("+", Tree("2"), Tree("4"))
    t3 = Tree("*", t1, t2)
    t4 = Tree("*", Tree("0"), t3)

    assert evaluate(t1) == 5
    assert evaluate(t2) == 6
    assert evaluate(t3) == 30
    assert evaluate(t4) == 0


if __name__ == '__main__':
    main()
