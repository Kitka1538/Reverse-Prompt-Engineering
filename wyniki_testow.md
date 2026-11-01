# **Raport testowania analizatora postaci RPG**

## **1. Kontrola funkcjonalności**

|Wymaganie|Oczekiwany rezultat|Dowód lub test|
|-|-|-|
|Dane wejściowe|8 postaci, 4 statystyki|Macierz NumPy 8 × 4|
|Normalizacja|Wyniki od 0 do 1|Funkcja normalizuj()|
|Stałe kolumny|Same zera|Test np.testing.assert\_allclose|
|Obliczanie siły|Mnożenie przez wektor wag|Funkcja oblicz\_sile()|
|Ranking|8 pozycji malejąco|np.argsort(kind="stable")|
|Role|3 możliwe role|Funkcja okresl\_role()|
|Pojedynki|Macierz 8 × 8|Funkcja macierz\_pojedynkow()|
|Średnie szanse|Bez walki z samym sobą|Funkcja oblicz\_srednie\_szanse()|
|Filtrowanie|Berserker|Maska logiczna NumPy|
|Statystyki|Min, średnia, max|Obliczenia dla 4 kolumn|
|Walidacja|Odrzucanie błędnych danych|Funkcja waliduj()|
|CSV|5 kolumn i 8 rekordów|Kontrola pliku wynikowego|

## **2. Wyniki rankingu**

|Miejsce|Postać|Rola|Siła|
|-:|-|-|-:|
|1|Berserker|Szturmowiec|0.535|
|2|Łotrzyk|Szturmowiec|0.511|
|3|Paladyn|Obrońca|0.489|
|4|Mag|Szturmowiec|0.475|
|5|Łucznik|Wszechstronny|0.459|
|6|Wojownik|Obrońca|0.454|
|7|Strażnik|Obrońca|0.450|
|8|Druid|Wszechstronny|0.395|

## **3. Statystyki grupy**

|Statystyka|Minimum|Średnia|Maksimum|
|-|-:|-:|-:|
|HP|75|110|155|
|Atak|18|32|44|
|Obrona|6|14|26|
|Szybkość|5|12.25|21|

## **4. Wynik filtrowania**

Zastosowane warunki:

* HP >= 100.
* Szybkość >= 10.
* Siła >= 0.45.

**Wynik: Berserker.**

## **5. Korekta pierwsza – obsługa stałych kolumn**

**Wykryty problem:** Dzielenie przez rozpiętość równą zero może powodować błędne wyniki normalizacji.

**Wprowadzona poprawka:** Zastosowanie np.divide z parametrami out i where.

**Test:** Przygotowano macierz zawierającą stałe kolumny i sprawdzenie wyników za pomocą np.testing.assert\_allclose.

**Oczekiwany wynik:** Wszystkie wartości w stałych kolumnach wynoszą zero.

## **6. Korekta druga – średnia szansa wygranej**

**Wykryty problem:** Uwzględnienie pojedynku postaci z samą sobą zniekształca średnią szansę wygranej.

**Wprowadzona poprawka:** Od sumy prawdopodobieństw w wierszu odejmowane jest 0.5, a następnie wynik dzielony jest przez n-1.

**Test:** Porównanie wyniku dla trzech postaci z ręcznie obliczoną średnią dwóch pojedynków.

**Oczekiwany wynik:** Średnia obejmuje wyłącznie pojedynki z pozostałymi postaciami.

## **7. Kontrola pliku CSV**

Wymagania eksportu:

* Kodowanie UTF-8 z BOM.
* Separator średnikowy.
* 5 kolumn.
* 8 rekordów postaci.
* Jeden wiersz nagłówka.
* Siła z czterema miejscami po przecinku.
* Średnia szansa jako procent z dwoma miejscami.
* Kolejność zgodna z rankingiem.

## **8. Weryfikacja końcowa**

Wartości rankingu, statystyk grupy, filtrowania i CSV zostały niezależnie przeliczone na podstawie danych wejściowych.

Kod zawiera testy automatyczne normalizacji, pojedynków i średnich szans wygranej.

**Do potwierdzenia po uruchomieniu programu:**

* Poprawne wykonanie wszystkich testów.
* Utworzenie pliku raport\_postaci.csv.
* Zgodność rzeczywistej zawartości CSV z oczekiwanymi wynikami.
* Poprawne kodowanie polskich znaków.

Nie należy oznaczać testów jako zaliczonych przed ich rzeczywistym wykonaniem.

