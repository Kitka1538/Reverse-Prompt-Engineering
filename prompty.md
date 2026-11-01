# **Prompty przebudowy programu RPG – wersja A do wersji B**



#### **Prompt 1 – Zmiana struktury danych**



**Cel:** Przebudowa danych wejściowych z listy słowników na tablice NumPy.



**Treść promptu:**



Przebuduj dane wejściowe programu. Zastąp listę słowników dwiema tablicami NumPy: tablicą nazw postaci oraz dwuwymiarową macierzą statystyk o wymiarach 8 × 4. Zachowaj wszystkie pierwotne wartości. Macierz statystyk ma mieć typ float. Dodaj wektor wag \[0.20, 0.40, 0.25, 0.15].



**Kryteria sprawdzenia:**

* 8 nazw postaci.
* Macierz 8 × 4.
* Typ float.
* Zachowanie pierwotnych danych.



#### **Prompt 2 – Normalizacja i obliczanie siły**



**Cel:** Zastąpienie dotychczasowego wzoru obliczeniami wektorowymi.



**Treść promptu:**



Dodaj funkcję normalizującą metodą min-max. Normalizuj każdą kolumnę osobno. Obsłuż kolumny stałe, zwracając w nich same zera. Wykorzystaj np.divide z parametrami out i where. Następnie oblicz siłę wszystkich postaci poprzez mnożenie znormalizowanej macierzy przez wektor wag.



**Kryteria sprawdzenia:**

* Normalizacja w przedziale 0–1.
* Brak dzielenia przez zero.
* Obliczanie siły za pomocą mnożenia macierzowego.



#### **Prompt 3 – Role i ranking**



**Cel:** Dodanie klasyfikacji postaci i pełnego rankingu.



**Treść promptu:**



Dodaj przypisywanie ról:

\-Szturmowiec: atak >= 35 i szybkość >= 12.

\-Obrońca: HP >= 120 i obrona >= 18.

\-Wszechstronny: pozostałe przypadki.



Szturmowiec ma pierwszeństwo, jeśli postać spełnia oba zestawy warunków. Utwórz pełny ranking malejący według siły, wykorzystując stabilne sortowanie. Wyświetl miejsce, nazwę, rolę i siłę z dokładnością do trzech miejsc.



**Kryteria sprawdzenia:**

* Każda postać ma jedną rolę.
* Ranking zawiera osiem postaci.
* Remisy zachowują pierwotną kolejność.



#### **Prompt 4 – Macierz pojedynków**



**Cel:** Dodanie matematycznego modelu symulowania pojedynków.



**Treść promptu:**



Dodaj wektorową funkcję obliczającą macierz pojedynków. Prawdopodobieństwo wygranej oblicz za pomocą wzoru logistycznego:



P(i,j) = 1 / (1 + exp(-8 \* (S(i) - S(j))))



Wykorzystaj rozszerzanie wymiarów tablic NumPy zamiast zagnieżdżonych pętli. Na przekątnej ustaw 0.5. Oblicz średnią szansę wygranej, wykluczając pojedynek z samym sobą.



**Kryteria sprawdzenia:**

* Macierz ma wymiar 8 × 8.
* Przekątna zawiera wartości 0.5.
* P + P.T = 1.
* Średnia nie uwzględnia pojedynku z samym sobą.



#### **Prompt 5 – Filtrowanie i statystyki**



**Cel:** Dodanie dodatkowych analiz zbioru postaci.



**Treść promptu:**



Dodaj filtrowanie z trzema jednoczesnymi warunkami:

\-HP >= 100.

\-Szybkość >= 10.

\-Siła >= 0.45.



Zastosuj jedną maskę logiczną NumPy. Dodaj statystyki grupy: minimum, średnia i maksimum dla każdej z czterech kolumn. Obsłuż pusty wynik filtrowania.



**Kryteria sprawdzenia:**

* Wszystkie trzy warunki są sprawdzane jednocześnie.
* Filtrowanie wykorzystuje maskę logiczną.
* Statystyki obejmują wszystkie cztery kolumny.
* Obsługiwany jest pusty wynik filtrowania.



#### **Prompt 6 – Walidacja danych**



**Cel:** Zwiększenie odporności programu na niepoprawne dane.



**Treść promptu:**



Dodaj funkcję walidującą dane przed rozpoczęciem obliczeń. Sprawdzaj:

\-Dwuwymiarowość macierzy.

\-Dokładnie cztery statystyki na postać.

\-Zgodność liczby postaci z liczbą nazw.

\-Co najmniej dwie postacie.

\-Unikatowość nazw.

\-Brak wartości ujemnych, NaN i nieskończoności.



Niepoprawne dane mają powodować ValueError z komunikatem wyjaśniającym przyczynę.



**Kryteria sprawdzenia:**

* Odrzucanie nieprawidłowych wymiarów.
* Odrzucanie duplikatów.
* Odrzucanie wartości ujemnych.
* Odrzucanie NaN i nieskończoności.
* Poprawne dane przechodzą walidację.



#### **Prompt 7 – Testy automatyczne**



**Cel:** Sprawdzenie poprawności algorytmów.



**Treść promptu:**



Dodaj funkcję testową wykorzystującą np.testing.assert\_allclose. Sprawdź normalizację macierzy, w której pierwsza i czwarta kolumna są stałe. Przetestuj macierz pojedynków dla trzech postaci. Zweryfikuj przekątną, symetrię względem dopełnienia do jedności i sposób obliczania średniej szansy wygranej.



**Kryteria sprawdzenia:**

* Test stałych kolumn.
* Test przekątnej macierzy.
* Test P + P.T = 1.
* Test średniej szansy wygranej.
* Niepoprawny wynik powoduje niepowodzenie testu.



#### **Prompt 8 – Eksport CSV i funkcja main**



**Cel:** Przygotowanie końcowego raportu i uporządkowanie programu.



**Treść promptu:**



Dodaj eksport do pliku raport\_postaci.csv przy użyciu biblioteki csv. Zastosuj separator średnikowy, kodowanie utf-8-sig i newline="". Plik powinien zawierać kolumny:

\-Miejsce

\-Postać

\-Rola

\-Siła

\-Średnia szansa wygranej



Siłę zapisuj z czterema miejscami po przecinku, a szansę jako procent z dwoma miejscami.



Uporządkuj wszystkie operacje w funkcji main. Kolejność:

1. Walidacja danych.
2. Uruchomienie testów.
3. Obliczenie siły.
4. Przypisanie ról.
5. Utworzenie rankingu.
6. Obliczenie macierzy pojedynków i średnich szans.
7. Wyświetlenie rankingu.
8. Filtrowanie postaci.
9. Wyświetlenie statystyk grupy.
10. Zapis raportu CSV.



Dodaj warunek if \_\_name\_\_ == "\_\_main\_\_". Nie usuwaj żadnej z wcześniej przygotowanych funkcjonalności.



**Kryteria sprawdzenia:**

* Program uruchamia się bez błędów.
* CSV zawiera pięć kolumn i osiem rekordów.
* Dane są zapisane według rankingu.
* Kodowanie umożliwia poprawne wyświetlanie polskich znaków.
* Wszystkie wcześniejsze funkcje działają.







# **Dwie korekty po testach**



#### **Korekta 1 – Obsługa stałych kolumn**



**Problem:** Zwykłe dzielenie przez rozpiętość może powodować dzielenie przez zero.



**Prompt naprawczy:**



Przetestuj normalizację na danych, w których pierwsza i czwarta kolumna są stałe. Zastosuj np.divide z parametrami out i where. Wszystkie wartości w stałych kolumnach muszą wynosić zero. Dodaj test sprawdzający ten warunek. Upewnij się, że wynik nie zawiera NaN ani nieskończoności.



**Oczekiwany rezultat:** Stałe kolumny są bezpiecznie normalizowane do zer.



#### **Korekta 2 – Średnia szansa wygranej**



**Problem:** Uwzględnienie pojedynku postaci z samą sobą powoduje błędne obliczenie średniej.



**Prompt naprawczy:**



Popraw obliczanie średniej szansy wygranej. Od sumy każdego wiersza macierzy pojedynków odejmij 0.5, a następnie podziel przez n-1. Dodaj test dla trzech postaci, który porównuje wynik z ręcznie wyliczoną średnią dwóch pojedynków. Nie zmieniaj pozostałych algorytmów.



**Oczekiwany rezultat:** Średnia obejmuje wyłącznie pojedynki z pozostałymi postaciami.







# **Końcowa lista wymagań**



1\. NumPy i obliczenia wektorowe.

2\. Tablice nazw i statystyk.

3\. Normalizacja min-max.

4\. Ważony wynik siły.

5\. Stabilny ranking.

6\. Przypisywanie ról.

7\. Macierz pojedynków.

8\. Średnie szanse wygranej.

9\. Filtrowanie postaci.

10\. Statystyki grupy.

11\. Walidacja danych.

12\. Testy automatyczne.

13\. Eksport CSV.

