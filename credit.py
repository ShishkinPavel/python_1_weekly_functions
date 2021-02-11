# Napište predikát, který ověří, zda je číslo korektní číslo
# platební karty.  Číslo platební karty ověříte podle Luhnova
# algoritmu:
#
#  1. zdvojnásobte hodnotu každé druhé cifry zprava; je-li výsledek
#     větší než 9, odečtěte od něj hodnotu 9,
#  2. sečtěte všechna takto získaná čísla a cifry na lichých
#     pozicích (kromě první cifry zprava, která slouží jako
#     kontrolní součet),
#  3. je-li potřeba přičíst přesně hodnotu kontrolní cifry, aby
#     byl součet dělitelný 10, je číslo platné.
#
# Například pro číslo 28316 je kontrolní cifra 6 a součet je: ⟦2 +
# (2⋅8 - 9) + 3 + 2⋅1 = 2 + 7 + 3 + 2 = 14⟧. K výsledku je potřeba
# přičíst 6, aby byl násobkem 10, což je přesně hodnota kontrolní
# cifry. Číslo karty je tedy platné.

def is_valid_card(number):
    cifry = list(map(int, str(number)))
    sum1 = sum(cifry[-1::-2])
    sum2 = sum([sum(divmod(2 * k, 10)) for k in cifry[-2::-2]])
    return (sum1 + sum2) % 10 == 0


def main():
    assert is_valid_card(28316)
    assert is_valid_card(4556737586899855)
    assert is_valid_card(4929599116478604)
    assert is_valid_card(4929300836739668)
    assert not is_valid_card(4929300835539668)
    assert not is_valid_card(4929300836739328)
    assert not is_valid_card(5101180000000000007)

    assert is_valid_card(5294967072531977)
    assert is_valid_card(5354598557505686)
    assert is_valid_card(2720993849498580)


if __name__ == "__main__":
    main()
