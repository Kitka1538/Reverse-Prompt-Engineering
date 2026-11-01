import numpy as np
from analizator import waliduj, normalizuj

nazwy = np.array(["Postać A", "Postać B"])

dane = np.array([
    [100, 20, 10, 5],
    [120, 30, 15, 10]
], dtype=float)

waliduj(nazwy, dane)

przypadki = [
    (
        "Duplikaty",
        np.array(["A", "A"]),
        dane
    ),
    (
        "Nieprawidłowy wymiar",
        nazwy,
        np.array([[1, 2, 3], [4, 5, 6]])
    ),
    (
        "Wartości ujemne",
        nazwy,
        np.array([[1, 2, 3, 4], [-1, 2, 3, 4]])
    ),
    (
        "NaN",
        nazwy,
        np.array([[1, 2, 3, 4], [np.nan, 2, 3, 4]])
    ),
    (
        "Nieskończoność",
        nazwy,
        np.array([[1, 2, 3, 4], [np.inf, 2, 3, 4]])
    ),
    (
        "Za mało postaci",
        np.array(["A"]),
        np.array([[1, 2, 3, 4]])
    ),
]

for opis, test_nazwy, test_dane in przypadki:
    try:
        waliduj(test_nazwy, test_dane)
        raise AssertionError(f"Nie wykryto błędu: {opis}")
    except ValueError:
        print(f"OK: {opis}")

wynik = normalizuj(np.array([
    [5, 10, 20, 7],
    [5, 20, 20, 7]
], dtype=float))

np.testing.assert_allclose(wynik[:, 0], [0, 0])
np.testing.assert_allclose(wynik[:, 1], [0, 1])
np.testing.assert_allclose(wynik[:, 2], [0, 0])
np.testing.assert_allclose(wynik[:, 3], [0, 0])

print("OK: kolumny stałe")
print("Wszystkie testy dodatkowe zakończone powodzeniem.")