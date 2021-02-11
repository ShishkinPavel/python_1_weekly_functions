# Napište a otypujte funkci ‹parse_datetime›, která z řetězce ve
# formátu ‹den/měsíc/rok hodiny:minuty› přečte datum a čas.
# Návratovou hodnotou funkce bude dvojice ‹(datum, čas)›, kde
# ‹datum› je trojice ve tvaru ‹(den, měsíc, rok)› a ‹čas› je dvojice
# ‹(hodiny, minuty)›. Všech pět položek je typu ‹int›. Není-li
# vstupní řetězec v zadaném formátu, nebo neobsahuje platné datum a
# čas, funkce vrátí ‹None›.
from typing import Tuple, Optional, List


def parse_datetime(input_string: str) -> Optional[Tuple[Tuple
                                                        [int, ...],
                                                        Tuple[int, ...]]]:
    # Dělám seznam z input_string a sdílím v místě mezery
    a1: List[str] = input_string.split()
    # Poznávám délku seznamu
    le: int = len(a1)
    # Zkontroloval jsem, zda jsou v seznamu dvě položky (čas a datum)
    # a správná syntaxe dělení.
    if le == 2 and '/' in a1[0] and ':' in a1[1]:
        # Rozděluji na den, měsíc a rok
        aa: List[str] = a1[0].split('/')
        # Rozděluji na hodinu a minutu
        bb: List[str] = a1[1].split(':')
        # Kontroluji počet položek
        if len(aa) == 3 and len(bb) == 2:
            # Přeložím str ze seznamu na int
            dd: int = int(aa[0])
            mm: int = int(aa[1])
            yyyy: int = int(aa[2])
            hour: int = int(bb[0])
            minute: int = int(bb[1])
            # Vytvářím tuple pro return
            result: Tuple[Tuple[int, ...], Tuple[int, ...]] = \
                (tuple([dd, mm, yyyy]), tuple([hour, minute]))
        else:
            return None
        # Kontrola měsíců s 31 dny
        # Zde a níže, pokud je True, pak xi = 1
        # False, pak xi = 0
        if (mm != 4 and mm != 6 and mm != 9 and mm != 11) and dd <= 31:
            x1: int = 1
        else:
            x1 = 0
        # Kontrola měsíců s 30 dny
        if (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd <= 30:
            x2: int = 1
        else:
            x2 = 0
        # Kontrola běžného února a přestupného února
        if (yyyy % 4 == 0 and mm == 2 and dd != 29) \
                or yyyy % 4 != 0 and (mm == 2 and dd != 28):
            x3: int = 1
        else:
            x3 = 0
        # Kontrola dnů, hodin a minut na správnost
        if 0 < dd < 32 and 0 < mm < 13 and 0 <= hour < 24 and 0 <= minute < 60:
            # Kontrola normality dnů v měsíci
            if (x1 == 1 or x2 == 1) and x3 != 1:
                return result



def main() -> None:
    assert parse_datetime("19/05/2020 17:00") == ((19, 5, 2020), (17, 0))
    assert parse_datetime("31/03/1998 6:07") == ((31, 3, 1998), (6, 7))
    assert parse_datetime("30/04/2007 7:45") == ((30, 4, 2007), (7, 45))
    assert parse_datetime("30/12/2010 13:30") == ((30, 12, 2010), (13, 30))
    assert parse_datetime("31/08/1998 21:20") == ((31, 8, 1998), (21, 20))
    assert parse_datetime("29/02/2020 23:51") == ((29, 2, 2020), (23, 51)), \
        "not accepting leap year additional day"

    # invalid days
    assert parse_datetime("00/01/2018 10:00") is None, \
        "accepting invalid day"
    assert parse_datetime("31/04/2018 15:12") is None, \
        "accepting invalid day"
    assert parse_datetime("29/02/2019 16:00") is None, \
        "accepting invalid day"
    assert parse_datetime("33/05/2015 15:12") is None, \
        "accepting invalid day"

    # invalid month
    assert parse_datetime("10/00/2018 15:12") is None, \
        "accepting invalid month"
    assert parse_datetime("10/14/2000 15:00") is None, \
        "accepting invalid month"

    # invalid time
    assert parse_datetime("19/05/2020 0:67") is None, \
        "accepting invalid minutes"
    assert parse_datetime("19/05/2020 10:60") is None, \
        "accepting invalid minutes"
    assert parse_datetime("19/05/2020 0:67:00") is None, \
        "accepting invalid time"
    assert parse_datetime("19/05/2020 24:00") is None, \
        "accepting invalid hours"
    assert parse_datetime("19/05/2020 35:00") is None, \
        "accepting invalid hours"

    # invalid format
    assert parse_datetime("10:14:2000 15:00") is None, \
        "accepting invalid format"
    assert parse_datetime("10:14:2000:15:00") is None, \
        "accepting invalid format"
    assert parse_datetime("10/14/2000") is None, \
        "accepting invalid format"
    assert parse_datetime("15:00 10/14/2000") is None, \
        "accepting invalid format"
    assert parse_datetime("invalid text") is None, \
        "accepting invalid format"
    assert parse_datetime("1/1/2020 time") is None, \
        "accepting invalid format"
    assert parse_datetime("date 20:15") is None, \
        "accepting invalid format"


if __name__ == "__main__":
    main()
