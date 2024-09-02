# Anagram binarny

Każdy wiersz pliku tekstowego, którego ścieżka przekazana jest jako argument funkcji, zawiera liczbę binarną, składającą się z maksymalnie 14 cyfr. Każda liczba zaczyna się jedynką i żadna z nich się nie powtarza.

## Podzadanie 1
Liczbę binarną nazywamy *zrównoważoną*, gdy zawiera tyle samo zer i jedynek, natomiast *prawie zrównoważoną*, gdy liczba jedynek różni się od liczby zer o 1.

**Przykład:**  
Liczba 101010 jest liczbą *zrównoważoną*  
Liczba 1011010 jest liczbą *prawie zrównoważoną*

Podaj, ile liczb zrównoważonych, a ile prawie zrównoważonych, zapisanych jest w podanym pliku tekstowym (patrz: wskazówka dotyczącą zwracania wielu wartości z funkcji w pythonie).

## Podzadanie 2
*Anagramy cyfrowe* to liczby utworzone z tego samego zestawu cyfr ustawionych w różnych kolejnościach. Przy tym pierwsza cyfra liczby nie może być równa zero.

**Przykład:**    
Z liczby 209 zapisanej dziesiętnie można utworzyć 4 anagramy: 209, 902, 290, 920.  
Z liczby binarnej 11100 można utworzyć 6 różnych anagramów: 10011, 10101, 10110, 11001, 11010, 11100.

Znajdź wszystkie takie liczby binarne 8-cyfrowe w pliku, z których można utworzyć największą liczbę anagramów. Zwróć je w postaci listy, zawierającej je w takiej kolejności, w jakiej występują one w podanym pliku tekstowym.

## Podzadanie 3
Podaj największą wartość bezwzględną różnicy między sąsiednimi liczbami (to jest liczbami zapisanymi w sąsiednich wierszach np. 1 i 2 wierszu, 2 i 3 wierszu itd.) w podanym pliku tekstowym. Podaj tę wartość w zapisie binarnym.

## Podzadanie 4
Zamień wszystkie liczby binarne z podanego pliku tekstowego na ich odpowiedniki w systemie dziesiętnym. Następnie spośród otrzymanych liczb dziesiętnych:
1. podaj, ile jest takich, w zapisie których nie występuje cyfra zero
2. podaj liczbę, która ma największą sumę różnych cyfr (jeśli liczb, które mają tę samą, największą sumę różnych cyfr, jest więcej niż jedna – podaj tę, która występuje jako pierwsza w pliku z danymi)

**Przykład:**    
Dla liczby 20462 suma jej różnych cyfr to 12 (2+0+4+6)   
Dla liczby 344 suma różnych cyfr to 7.

Patrz: wskazówka dotyczącą zwracania wielu wartości z funkcji w pythonie

# Zwracanie wielu wartości z funkcji w pythonie
Żeby zwrócić kilka wartości z funkcji w pythonie można zastosować krotkę (tuple), na przykład:
```python
def func():
    var1 = 5
    var2 = 10

    return var1, var2
```
