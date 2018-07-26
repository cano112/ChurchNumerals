# Liczebniki Churcha
## Co to jest?
Liczebniki Churcha są jednym z możliwych sposobów reprezentacji liczb naturalnych.  
Weźmy dowolną funkcję f oraz dowolną liczbę naturalną n. Liczbie n przypisujemy funkcję wyższego rzędu c<sub>n</sub>:

**c<sub>n</sub> (f (x)) = f (x) &#8728; f (x) &#8728; ... &#8728; f (x) &#8728; f (x) = f<sup>n</sup> (x)**

Liczbę n interpretujemy jako ilość aplikacji funkcji f na argument x.

### Przykłady
  * c<sub>1</sub> = f (x) - reprezentacja liczby 1
  * c<sub>2</sub> = f (f (x)) - reprezentacja liczby 2
  * c<sub>6</sub> = f( f( f( f( f( f (x)))))) - reprezentacja liczby 6
  
## Rachunek lambda
### Definicja
Liczebniki Churcha możemy zdefiniować w rachunku lambda, w sposób przedstawiony w poniższej tabeli.

|Liczba naturalna|Wyrażenie lambda|
|:--------------:|------------------|
|0|&lambda;f.&lambda;x.x|
|1|&lambda;f.&lambda;x.f x|
|2|&lambda;f.&lambda;x.f (f x)|
|3|&lambda;f.&lambda;x.f (f (f x))|
|...|...|
|n|&lambda;f.&lambda;x.f<sup>n</sup> x

### Operacje arytmetyczne
Na zdefiniowanych w ten sposób liczbach możemy wykonywać normalne operacje arytmetyczne. 
W poniższej tabeli przedstawiono operacje, ich definicje w rachunku lambda oraz tożsamości użyte do ich zdefiniowania.

|Operacja|Algebraicznie|Tożsamość|Wyrażenie lambda|
|:------:|:-----------:|---------|----------------|
|następnik|n + 1|f<sup>n+1</sup> (x) = f (f<sup>n</sup> (x))|&lambda;n.&lambda;f.&lambda;x.f (n f x)|
|dodawanie|m + n|f<sup>m+n</sup> (x) = f<sup>m</sup> (f<sup>n</sup> (x))|&lambda;n.&lambda;f.&lambda;x.m f (n f x)|
|mnożenie|m * n|f<sup>m*n</sup> (x) = [f<sup>m</sup> (x)]<sup>n</sup>|&lambda;n.&lambda;f.&lambda;x.m (n f) x|
|potęgowanie|m<sup>n</sup>|n (m (f)) = m<sup>n</sup> (f)|&lambda;n.&lambda;f.&lambda;x.(n m) f x|

Tożsamość wykorzystaną do zdefiniowania potęgowania można wyprowadzić bezpośrednio z definicji liczebników Churcha.

## Implementacja
Liczebniki Churcha doskonale nadają się do implementacji w dowolnym funkcyjnym języku programowania.  
Przykładową implementację przeprowadziłem w języku Python, który obsługuje operacje na wyrażeniach lambda.
