# Napište a otypujte funkci ‹parse_gps›, která přečte GPS souřadnice
# ze vstupního řetězce ‹raw›. Očekávaný vstup je ve formátu
# ‹lat=X;lon=Y› kde ‹X› a ‹Y› jsou čísla. Není-li vstup není v tomto
# formátu, funkce vrací ‹None›, jinak vrátí dvojici s číselnými
# hodnotami zeměpisné šířky (latitude) a délky (longitude).
# Nespadají-li hodnoty do platného rozsahu souřadnic, funkce vrací
# ‹None›: zeměpisná šířka je v rozmezí -90 až 90 a délka v rozmezí
# -180 až 180.
from typing import Tuple, Optional, List


def parse_gps(raw: str) -> Optional[Tuple[float, ...]]:
    if ';' not in raw or '.' not in raw:
        return None
    a: List[str] = raw.split(';')
    if 'lat' not in a[0] or 'lon' not in a[1]:
        return None
    lat: float = float(a[0].split('=')[1])
    lon: float = float(a[1].split('=')[1])

    if (-90.0 < lat < 90.0) and (-180.0 < lon < 180.0):
        s: Tuple[float, ...] = (lat, lon)
        return s
    else:
        return None


# Dále napište a otypujte funkci ‹parse_gps_stream›, která přečte
# seznam GPS souřadnic a vrátí seznam dvojic s číselnými hodnotami
# souřadnic. Souřadnice na vstupu jsou každá na vlastním řádku.
# Nekóduje-li kterýkoliv řádek GPS souřadnici, funkce vrátí ‹None›.

def parse_gps_stream(raw: str) -> Optional[List[Tuple[float, ...]]]:
    if raw == "":
        return []
    if ';' not in raw or '.' not in raw:
        return None
    a1: List[str] = raw.split()
    lea: int = len(a1)
    i: int = 0
    result: List[Tuple[float, ...]] = []
    while lea > 0:
        a: List[str] = a1[i].split(';')
        if 'lat' not in a[0] or 'lon' not in a[1]:
            return None
        lat: float = float(a[0].split('=')[1])
        lon: float = float(a[1].split('=')[1])
        if (-90.0 > lat or lat > 90.0) or (-180.0 > lon or lon > 180.0):
            return None
        c: Tuple[float, ...] = (lat, lon)
        result.append(c)
        i += 1
        lea -= 1
    return result


def main() -> None:
    res = parse_gps("lat=49.2099839;lon=16.5989169")
    assert res and res == (49.2099839, 16.5989169)
    res = parse_gps("lat=49.2099839;lon=-16.5989169")
    assert res and res == (49.2099839, -16.5989169)
    res = parse_gps("lat=-49.2099839;lon=16.5989169")
    assert res and res == (-49.2099839, 16.5989169)

    assert parse_gps("lat=99.2099839;lon=16.5989169") is None, \
        "latitude out or range"
    assert parse_gps("lat=-99.2099839;lon=16.5989169") is None, \
        "latitude out or range"
    assert parse_gps("lat=49.2099839;lon=-196.5989169") is None, \
        "longitude out or range"
    assert parse_gps("lat=49.2099839;lon=196.5989169") is None, \
        "longitude out or range"
    assert parse_gps("text") is None, "invalid format"
    assert parse_gps("49.2099839;16.5989169") is None, "invalid format"
    assert parse_gps("lat=49.2099839 lon=16.5989169") is None, "invalid format"
    assert parse_gps("lon=16.5989169;lat=49.2099839") is None, "invalid format"
    assert parse_gps("lat=49;lon=16") is None, "invalid format"
    assert parse_gps("lat=49;2099839;lon=16;5989169") is None, "invalid format"

    sres = parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=17.1093064
lat=50.0835494;lon=14.4341414""")

    assert sres == [(49.2099839, 16.5989169),
                    (48.1516986, 17.1093064),
                    (50.0835494, 14.4341414)]

    sres = parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=-17.1093064
lat=-50.0835494;lon=14.4341414""")

    assert sres == [(49.2099839, 16.5989169),
                    (48.1516986, -17.1093064),
                    (-50.0835494, 14.4341414)]

    sres = parse_gps_stream("")
    assert sres is not None and sres == []

    assert parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=-189.1093064
lat=-50.0835494;lon=14.4341414""") \
           is None
    assert parse_gps_stream("""lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=17.1093064
invalid entry""") \
           is None


if __name__ == "__main__":
    main()