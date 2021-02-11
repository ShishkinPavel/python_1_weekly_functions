# Napište funkci, která pro zadané číslo ‹number› najde nejbližší větší
# číslo, které je násobkem čísla ‹k›.

def next_multiple(number, k):
    number += 1
    while number % k != 0:
        number += 1
    return number


# Dále napište funkci, která pro zadané číslo ‹number› najde
# nejbližší větší prvočíslo.

def next_prime(number):
    np = []
    prime = []
    for i in range(number + 1, number + 200):
        np.append(i)
    for j in np:
        val_is_prime = True
        for x in range(2, j - 1):
            if j % x == 0:
                val_is_prime = False
                break
        if val_is_prime:
            prime.append(j)
    return min(prime)


def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13


if __name__ == "__main__":
    main()
