from typing import Optional, List


# Naprogramujte třídu ‹RingBuffer› která se bude chovat jako fronta,
# ale bude mít shora omezenou velikost. Pro ukládání dat bude
# využívat jinou třídu SimpleList (tuto třídu nesmíte měnit, ani
# přistupovat k jejím atributům), která poskytuje toto rozhraní
# (‹sl› je instance ‹SimpleList›):
#
#  • ‹sl.append(x)› vloží na konec seznamu prvek ‹x›,
#  • ‹sl.get(i)› vrátí hodnotu na indexu ‹i›,
#  • ‹sl.size()› vrátí aktuální velikost seznamu,
#  • ‹sl.set(i, x)› nastaví index ‹i› na hodnotu ‹x›.

class RingBuffer:

    # Při inicializaci se nastaví velikost kruhové fronty na ‹size›.
    # Pro ukládání dat bude použita instance třídy ‹SimpleList›
    # předaná parametrem ‹storage›.

    def __init__(self, size: int, storage: 'SimpleList'):
        self.size = size
        self.storage = storage

    # Metoda ‹push› se pokusí přidat prvek na konec fronty. Je-li
    # fronta plná, metoda vrátí ‹False› a nic neudělá. V opačném
    # případě prvek vloží na konec fronty a vrátí ‹True›.

    def push(self, value: int) -> bool:
        # I'm sure it doesn't work the way it should, but
        # I couldn't remove the element from SimpleList,
        # so I had to come up with a "crutch".

        # I put -100 in a place that should be empty,
        # and if the function returns -100, then I replace it with None
        len_storage: int = SimpleList.size(self.storage)
        if len_storage < self.size:
            self.storage.append(value)
            return True
        elif len_storage == self.size and \
                SimpleList.get(self.storage, i=len_storage - 1) == -100:
            i: int = 0
            while i < len_storage:
                if SimpleList.get(self.storage, i=i) == -100:
                    SimpleList.set(self.storage, i=i, x=value)
                    return True
                i += 1
            return True
        else:
            return False

    # Metoda ‹pop› odstraní prvek ze začátku fronty a vrátí jej.
    # Je-li fronta prázdná, metoda nic neudělá a vrátí ‹None›.

    def pop(self) -> Optional[int]:
        if SimpleList.size(self.storage) == 0:
            check: int = 0
            while check < self.size:
                self.storage.append(-100)
                check += 1
            return None
        x: int = SimpleList.size(self.storage)
        y: int = SimpleList.get(self.storage, i=0)
        SimpleList.set(self.storage, i=0, x=-100)
        if SimpleList.get(self.storage, i=0) == -100:
            i: int = 0
            while i < x - 1:
                SimpleList.set(self.storage, i=i,
                               x=SimpleList.get(self.storage, i=i + 1))
                i += 1
            SimpleList.set(self.storage, i=x - 1, x=-100)
        if y == -100:
            return None
        else:
            return y


def main() -> None:
    sl = SimpleList()
    buf = RingBuffer(4, sl)
    for i in [1, 2, 7, 4]:
        assert buf.push(i)
    assert not buf.push(5)

    expected = [1, 2, 7, 4]
    for i in range(4):
        expected.remove(sl.get(i))

    check_result(buf.pop(), 1)
    check_result(buf.pop(), 2)
    assert buf.push(7)
    assert sl.size() <= 4
    check_result(buf.pop(), 7)
    check_result(buf.pop(), 4)
    check_result(buf.pop(), 7)
    assert buf.pop() is None
    for i in [11, 12, 13, 14]:
        buf.push(i)
    assert sl.size() <= 4
    assert not buf.push(0)
    check_result(buf.pop(), 11)
    assert sl.size() <= 4

    sl = SimpleList()
    buf = RingBuffer(3, sl)
    assert buf.pop() is None
    assert buf.push(0)
    check_result(buf.pop(), 0)
    assert buf.push(0)
    check_result(buf.pop(), 0)
    assert buf.pop() is None
    assert sl.size() <= 3

    sl = SimpleList()
    buf = RingBuffer(1, sl)
    assert buf.pop() is None
    assert buf.push(3)
    assert not buf.push(1)
    check_result(buf.pop(), 3)
    assert buf.push(3)


def check_result(result: Optional[int], expected: int) -> None:
    assert result is not None
    assert result == expected


class SimpleList:

    def __init__(self) -> None:
        self.__items: List[int] = []

    def append(self, x: int) -> None:
        self.__items.append(x)

    def get(self, i: int) -> int:
        return self.__items[i]

    def set(self, i: int, x: int) -> None:
        self.__items[i] = x

    def size(self) -> int:
        return len(self.__items)


if __name__ == "__main__":
    main()
