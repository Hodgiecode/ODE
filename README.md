### ODE solver

### Warning 

Параметр eps меньше 1e-6 может вызвать поломку программы

Перед использованием из исходников получить исполняемый файл и положить его в папку с gui_1.py или gui_2.py

gui_1.py: y'=f(x,y)

gui_2.py: y''+p(x)*y'+q(x)*y=f(x)

### Функции

- Load from file - заполняет верхнюю строку данными из выбранного файла

- Solution function - аналитическое решение (необязательно)

- F - ввод функции. f(x,y) для  y'=f(x,y) и p(x),q(x),f(x) для  y''+p(x)*y'+q(x)*y=f(x)

- Run запускает встроенный решатель. Метод Кунцмана-Бутчера (Butcher–Kuntzmann Runge–Kutta) для y'=f(x,y) и метод РК 4-го порядка + метод пристрелки (деления пополам) для y''+p(x)*y'+q(x)*y=f(x)

- Exe or txt - выбор исполняемого файла, решающего задачу или выбор текстового файла с имеющимся ответом. Необходимый формат 

x_i y_i 

x_(i+1) y_(i+1) ... 

Если выбирается exe файл, то имя для входного файла необходимо ввести в соседнее поле.

- Get solution - строит решение и график для него из имеющихся данных

### Тестовые программы: 

(11) Неявный метод Адамса для уравнения вида y'=f(x,y) и (22) РК по правилу (3/8)  + метод Ньютона для решения уравнения вида y''+p(x)*y'+q(x)*y=f(x)


![image](https://github.com/Hodgiecode/ODE/blob/main/img2.png)

![image](https://github.com/Hodgiecode/ODE/blob/main/img1.png)
