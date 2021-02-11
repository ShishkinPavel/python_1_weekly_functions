from typing import Tuple


# Naprogramujte třídu ‹TimeInterval›, která bude reprezentovat
# časový interval.

class TimeInterval:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Metoda zkrátí interval o čas reprezentovaný parametrem
    # ‹interval›.

    def shorten(self, interval: 'TimeInterval') -> None:
        self.hours = self.hours - interval.hours
        self.minutes = self.minutes - interval.minutes
        self.seconds = self.seconds - interval.seconds
        while self.seconds < 0:
            self.seconds += 60
            self.minutes -= 1
        while self.minutes < 0:
            self.minutes += 60
            self.hours -= 1
        if self.hours < 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    # Metoda prodlouží interval o čas reprezentovaný parametrem
    # ‹interval›.

    def extend(self, interval: 'TimeInterval') -> None:
        self.hours = interval.hours + self.hours
        self.minutes = interval.minutes + self.minutes
        self.seconds = interval.seconds + self.seconds
        while self.seconds // 60:
            self.minutes += 1
            self.seconds -= 60
        while self.minutes // 60:
            self.hours += 1
            self.minutes -= 60
        if self.hours > 23:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    # Metoda vrátí reprezentovaný interval jako n-tici ve formátu
    # (hodiny, minuty, sekundy), kde minuty a sekundy nabývají
    # hodnoty z uzavřeného intervalu [0, 59].

    def format(self) -> Tuple[int, int, int]:
        return self.hours, self.minutes, self.seconds


def main() -> None:
    for i in [(12, 3, 59), (14, 59, 59), (0, 0, 0), (0, 0, 1), (0, 12, 12)]:
        assert TimeInterval(i[0], i[1], i[2]).format() == i

    duration = TimeInterval(0, 0, 0)
    duration.extend(TimeInterval(0, 5, 30))
    assert duration.format() == (0, 5, 30)
    duration.extend(TimeInterval(0, 5, 30))
    assert duration.format() == (0, 11, 0)
    duration.extend(TimeInterval(0, 49, 0))
    assert duration.format() == (1, 0, 0)

    duration.shorten(TimeInterval(0, 32, 41))
    assert duration.format() == (0, 27, 19)
    duration.shorten(TimeInterval(123, 12, 43))
    assert duration.format() == (0, 0, 0)

    duration.extend(TimeInterval(1, 32, 56))
    duration.extend(duration)
    assert duration.format() == (3, 5, 52)
    duration.extend(duration)
    assert duration.format() == (6, 11, 44)
    duration.shorten(duration)
    assert duration.format() == (0, 0, 0)


if __name__ == "__main__":
    main()
