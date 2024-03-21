# Udav

Udav repository has [Ukrainian :ukraine:](#мова-програмування-удав-ukraine) and [English :uk:](#programming-language-udav-uk) localizations

# Мова програмування Удав :ukraine:

<p align='center'>
  <img src='./VS Code Extension/udav-extension/icon-udav.png' alt='Udav icon' style="width:50%">
</p>

***Мова програмування Удав*** - це жартівлива мова програмування, створена на основі Python. Ідея виникла, коли мій друг, не програміст, назвав Python "Удавом". З тих пір у нас в компанії ходив прикол про "Удава".

Коли я вирішив створити щось більш менш серйозне, я вирішив провести маленьку підготовку та випробування своїх знань, написавши мову програмування Удав. Я намагався не напружуватися і просто отримати задоволення від процесу створення, оскільки це все ще лишається жартом.

За основу я взяв синтаксис Python перекладений на українську. Це означає, що код на Удав можна відтворити багато разів, оскільки він автоматично перекладається на Python. Крім того, Удав підтримує усі python модулі.

***Як ви вже зрозуміли мова програмування називається Удав, тож логічно буде, якщо код цією мовою писався з застосуванням snake_case***

***Швидкий перехід між розділами:***

- [Udav](#udav)
- [Мова програмування Удав :ukraine:](#мова-програмування-удав-ukraine)
  - [Мова програмування Удав](#мова-програмування-удав)
    - [Інсталяція](#інсталяція)
      - [Компіляція](#компіляція)
      - [Ініціалізація](#ініціалізація)
      - [Деніціалізація](#деніціалізація)
    - [Синтаксис](#синтаксис)
  - [Власне IDE для Удав](#власне-ide-для-удав)
  - [Розширення для VS code](#розширення-для-vs-code)
- [Programming language Udav :uk:](#programming-language-udav-uk)
  - [Programming language Udav](#programming-language-udav)
    - [Installation](#installation)
      - [Compiling](#compiling)
      - [Initialization](#initialization)
      - [Denialization](#denialization)
    - [Syntax](#syntax)
  - [A custom IDE for Udav](#a-custom-ide-for-udav)
  - [Extensions for VS code](#extensions-for-vs-code)

___

## Мова програмування Удав

### Інсталяція

Цей розділ надасть вам інструкції, щодо встановлення, ініціалізації та деініціалізації компілятора Удав.

#### Компіляція

Щоб запустити компілятор Удава, вам необхідно буде виконати наступні дії:

1. Клонуйте репозиторій з GitHub:

``` bash
git clone https://github.com/NikitaBerezhnyj/Udav.git
```

2. Перейдіть в теку з проектом:

``` bash
cd Udav/'Programming Language'/src
```

3. Відкомпілюйте C++ файл:

``` bash
g++ compiler.cpp -o udav
```

Після завершення компіляції в теці з проектом буде створений виконуваний файл udav. Після ініціалізації цей файл можна буде використовувати для запуску програм мовою Удав з будь-якої теки.

#### Ініціалізація

Ініціалізація компілятора Удав необхідна для того, щоб можна було використовувати його з будь-якої теки на вашому комп'ютері. Для цього виконайте наступну команду:

``` bash
./udav -i
```

або

``` bash
./udav --init
```

Після ініціалізації компілятора файл udav буде скопійовано в теку з іншими утилітами, що дасть можливість використовувати його для запуску програм мовою Удав з будь-якої теки.

#### Деніціалізація

Деініціалізація компілятора Удав необхідна, якщо ви більше не плануєте використовувати його. Для цього виконайте наступну команду:

``` bash
./udav --u
```

або

``` bash
./udav --uninit
```

Це видалить Удав з теки з утилітами, але залишить його у теці з проєктом, тому ви зможете використовувати його і потім, якщо забажаєте

### Синтаксис

Синтаксис Удав є перекладом мови Python на українську, для більшої простоти навчання та програмування українських розробників, тому синтаксиси цих двох мов майже не відрізняються.

***Створення коментарів***

``` python
# Це коментар, його компілятор не бачить
```

***Вивід тексту на екран***

``` python
# Вивід звичайного тексту
друк("Привіт, Світ!")

# Вивід змінної
а = 10
друк(а)
```

***Оголошення змінних***

``` python
# Цілочисельна змінна
інт = 10

# Дійсна змінна
флоат = 10.5

# Рядкова змінна
стрінг = "Рядок"

# Булева змінна
бул = правда

```

***Ввід користувача***

``` python
# Записується рядок
рядок_вводу = ввід()

# Записується ціле число
число_вводу = число(ввід())

# Записується ціле число
дріб_вводу = дріб(ввід())
```

***Оголошення масивів***

``` python
# Оголошення масиву цілих чисел
цілий_масив = [0, 1]

# Оголошення масиву дійсних чисел
дробовий_масив = [0.5, 1.001]

# Оголошення масиву рядків
рядковий_масив = ["привіт", "світ"]

# Оголошення масиву булевих виразів
булевий_масив = [правда, правда, брехня]

```

***Умови if (якщо), else if (інакшеЯкщо) та else (інакше)***

``` python
# Умова якщо
якщо а < 5:
    друк("<5")

# Умова якщо-інакше
якщо а < 5:
    друк("<5") 
інакше:
    друк(">8")

# Умова якщо-інакшеЯкщо-інакше
якщо а < 5 : 
    друк("<5") 
інакшеЯкщо а > 5 і а < 8: 
    друк("<5 and >8") 
інакше :
    друк(">8")
```

***Оголошення циклу while (поки)***

``` python
# Приклад циклу while (поки)
лічильник = 0
поки лічильник < 10:
    лічильник += 1
    друк(лічильник)
```

***Оголошення циклу for (для)***

``` python
# Приклад циклу for (для)
для л в границях(10):
    друк("Привіт, Світ!")
```

***Оголошення функції***

``` python
# Приклад функції
функція Привіт_світ():
	рази = число(ввід("Введіть кількість повторів: "))
	друк(рази)
	для i в range(рази) :
		друк("Привіт, Світ!")
```

***Робота з сторонніми модулями***

``` python
# Приклад роботи з datetime
отримати datetime

поточна_година = datetime.datetime.now()
друк("Поточна дата та час: ", поточна_година)

# Приклад роботи з random
отримати random

число = random.randint(1, 100)
друк(число)
```

***Приклад коду з стандартних конструкцій***

``` python
отримати random

функція Гра(кількість_спроб, випадкове_число) :
    для спроба в границях(кількість_спроб) :
        друк("Введіть будь ласка число від 1 до 10:")
        користувацьке_число = число(ввід("Введіть число: "))
        якщо користувацьке_число < випадкове_число:
            друк("Переможне число більше")
        інакшеЯкщо користувацьке_число > випадкове_число:
            друк("Переможне число менше")
        інакшеЯкщо користувацьке_число == випадкове_число:
            друк("Ви виграли!")
            повернути 0
        інакше:
            продовжити
    друк("Ви програли")
    друк(f"Переможне число: {випадкове_число}")

випадкове_число = random.randrange(1, 10)
кількість_спроб = число(ввід("Скільки ви хочете спроб:"))
Гра(кількість_спроб, випадкове_число)
```

***Приклад коду в ООП парадигмі***
```python
клас Тварина:
    функція __init__(своє , прізвисько, вік):
        своє.прізвисько = прізвисько
        своє.вік = вік
        
    функція Голос(своє):
        підняти ПомилкаВіртуальногоМетоду("Метод реалізується у підкласах")

клас Собака(Тварина):
    функція Голос(своє):
        повернути "Гав!"

клас Кіт(Тварина):
    функція Голос(своє):
        повернути "Няв!"


пес = Собака("Лорд", 3)
кішка = Кіт("Плюша", 2)

друк(пес.прізвисько + " каже :" + пес.Голос())
друк(кішка.прізвисько + " каже " + кішка.Голос())
```

___

***[Дивитись код мови](./Programming%20Language/)***

## Власне IDE для Удав

***NUB IDE*** - це інтегроване середовище розробки для мов програмування [NikLang](https://github.com/NikitaBerezhnyj/NikLang), [Udav](https://github.com/NikitaBerezhnyj/Udav) та [Based](https://github.com/NikitaBerezhnyj/Based). Воно надає зручний і функціональний інтерфейс для написання коду цими мовами.

Особливості:

- Підсвічування синтаксису для мов NikLang, Udav та Based 
- Автоматичне доповнення коду
- Вбудований термінал з власними командами для керування IDE
- Інтуїтивний графічний інтерфейс на основі Tauri + React

***NUB IDE*** створено з метою максимально спростити та прискорити розробку на мовах NikLang, Udav та Based. Воно поєднує сучасний дизайн, зручність використання та всі необхідні для продуктивної роботи інструменти.

Завантажити та дізнатися більше про NUB IDE ви можете за посиланням нижче

___

***[Дивитись код IDE]([./Based%20IDE/](https://github.com/NikitaBerezhnyj/NUB_IDE))***

## Розширення для VS code

Розширення додає підтримку мови програмування Удав у VS Code.

***Функціональність***

- Підсвічування синтаксису для файлів .udav
- Автодоповнення ключових слів мови Удав

***Використання***

Після встановлення розширення, VS Code автоматично розпізнаватиме файли .udav і застосовуватиме до них підсвічування і автодоповнення.

***Установка***

На даний момент розширення не доступне в маркетплейсі VS Code, тож його можна встановити тільки клонувавши репозиторій та встановивши його локально. Для цього вам необхідно буде виконати наступні кроки:

1. Копіювати репозиторій на свій ПК через термінал
```bash
git clone https://github.com/NikitaBerezhnyj/Udav.git
```

2. Потім знайти теку VS code на вашому ПК
   
3. Скопіювати теку udav-extension до теки з іншими розширеннями

***Підтримувані мови:*** Udav (.udav)

***Залежності:*** Не має

***Версія:*** 1.0.0
___

***[Дивитись код розширення](./VS%20Code%20Extension/udav-extension/)***

___

# Programming language Udav :uk:

<p align='center'>
  <img src='./VS Code Extension/udav-extension/icon-udav.png' alt='Udav icon' style="width:50%">
</p>

***Programming language Udav*** is a comic programming language based on Python. The idea came about when a non-programmer friend of mine called Python "Boa". Since then, we've had a joke about Boa in our company.


When I decided to create something more or less serious, I decided to do a little training and test my knowledge by writing a programming language called Boa. I tried to take it easy and just have fun with the process of creating it, since it was still a joke.


I took the Python syntax translated into Ukrainian as a basis. This means that the code in Udav can be reproduced many times because it is automatically translated into Python. In addition, Udav supports all python modules.

***As you have already understood, the programming language is called Udav, so it would be logical if the code in this language was written using snake_case***

***Quick transition between sections:***

- [Udav](#udav)
- [Мова програмування Удав :ukraine:](#мова-програмування-удав-ukraine)
  - [Мова програмування Удав](#мова-програмування-удав)
    - [Інсталяція](#інсталяція)
      - [Компіляція](#компіляція)
      - [Ініціалізація](#ініціалізація)
      - [Деніціалізація](#деніціалізація)
    - [Синтаксис](#синтаксис)
  - [Власне IDE для Удав](#власне-ide-для-удав)
  - [Розширення для VS code](#розширення-для-vs-code)
- [Programming language Udav :uk:](#programming-language-udav-uk)
  - [Programming language Udav](#programming-language-udav)
    - [Installation](#installation)
      - [Compiling](#compiling)
      - [Initialization](#initialization)
      - [Denialization](#denialization)
    - [Syntax](#syntax)
  - [A custom IDE for Udav](#a-custom-ide-for-udav)
  - [Extensions for VS code](#extensions-for-vs-code)

___

## Programming language Udav

### Installation

This section will provide you with instructions on how to install, initialize, and uninitialize the Udav compiler.

#### Compiling

To run the Udav compiler, you will need to perform the following steps:

1. Clone the repository from GitHub:

```bash
git clone https://github.com/NikitaBerezhnyj/Udav.git
```

2. Change to the project folder:

```bash
cd Udav/'Programming Language'/src
```

3. Compile the C++ file:

```bash
g++ compiler.cpp -o udav
```

After the compilation is completed, the udav executable file will be created in the project folder. After initialization, this file can be used to run Udav programs from any folder.

#### Initialization

Initialization of the Udav compiler is necessary in order to use it from any folder on your computer. To do this, run the following command:

```bash
./udav -i
```

or

```bash
./udav --init
```

After the compiler is initialized, the udav file will be copied to the folder with other utilities, which will make it possible to use it to run programs in Udav from any folder.

#### Denialization

You need to deinitialize the Udav compiler if you no longer plan to use it. To do this, run the following command:

```bash
./udav --u
```

or

```bash
./udav --uninit
```

This will remove Udav from the utilities folder, but leave it in the project folder, so you can use it later if you want to.

### Syntax


Syntax Udav is a translation of Python into Ukrainian, for ease of learning and programming for Ukrainian developers, so the syntaxes of these two languages are almost identical.


***Creating comments***

``` python
# This is a comment, the compiler does not see it
```

***Display text on the screen***

``` python
# print simple text
друк ("Привіт, Світ!")

# print a variable
а = 10
друк (а)
```

***Declaration of variables***

``` python
# integer variable
інт = 10

# float variable
флоат = 10.5

# string variable
стрінг = "Рядок"

# boolean variable
бул = правда

```

***User input***

``` python
# the string is written
рядок_вводу = ввід ()

# an integer is written
число_вводу = число ( ввід () )

# A float is written
дріб_вводу = дріб ( ввід ()) )
```

***Declaration of arrays***

``` python
# Declaration of an array of integers
цілий_масив = [0, 1]

# Declaring an array of floats
дробовий_масив = [0.5, 1.001]

# Declaring an array of strings
рядковий_масив = ["привіт", "світ"]

# Declaring an array of booleans
булевий_масив = [ правда , правда , брехня ]

```

***If, else if, and else conditions***.

``` python
# Condition if
якщо а < 5 :
    друк ("<5")

# Condition if-else
якщо а < 5 :
    друк ("<5") 
інакше :
    друк(">8")

# Condition if-elif-else
якщо а < 5 : 
    друк ("<5") 
інакшеЯкщо а > 5 і а < 8 : 
    друк ("<5 and >8") 
інакше :
    друк (">8")
```

***Declaring a while loop***

``` python
# An example of a while loop
лічильник = 0
поки лічильник < 10 :
    лічильник += 1
    друк (лічильник)
```

***Declaring a for loop***

``` python
# An example of a for loop
для л в границях (10) :
    друк ("Привіт, Світ!")
```

***Function declaration***

``` python
# An example of a function
функція Привіт_світ() :
	рази = число ( ввід ("Введіть кількість повторів: ") )
	друк (рази)
	для i в range(рази) :
		друк ("Привіт, Світ!")
```

***Working with third-party modules***

``` python
# An example of working with datetime
отримати datetime

поточна_година = datetime.datetime.now()
друк ("Поточна дата та час:", поточна_година )

# An example of working with random
отримати random

число = random.randint(1, 100)
друк (число)
```

***Example code from standard constructions***

``` python
отримати random

функція Гра(кількість_спроб, випадкове_число) :
    для спроба в границях ( кількість_спроб ) :
        друк ("Введіть будь ласка число від 1 до 10:")
        користувацьке_число = число ( ввід ("Введіть число: ") )
        якщо користувацьке_число < випадкове_число :
            друк ("Переможне число більше")
        інакшеЯкщо користувацьке_число > випадкове_число :
            друк ("Переможне число менше")
        інакшеЯкщо користувацьке_число == випадкове_число :
            друк ("Ви виграли!")
            повернути 0
        інакше :
            продовжити
    друк ("Ви програли")
    друк (f"Переможне число: {випадкове_число}")

випадкове_число = random.randrange(1, 10)
кількість_спроб = число ( ввід ("Скільки ви хочете спроб:"))
Гра(кількість_спроб, випадкове_число)
```

***A sample code in the OOP paradigm***
```python
клас Тварина:
    функція __init__(своє , прізвисько, вік):
        своє.прізвисько = прізвисько
        своє.вік = вік
        
    функція Голос(своє):
        підняти ПомилкаВіртуальногоМетоду("Метод реалізується у підкласах")

клас Собака(Тварина):
    функція Голос(своє):
        повернути "Гав!"

клас Кіт(Тварина):
    функція Голос(своє):
        повернути "Няв!"


пес = Собака("Лорд", 3)
кішка = Кіт("Плюша", 2)

друк (пес.прізвисько + " каже :" + пес.Голос())
друк (кішка.прізвисько + " каже " + кішка.Голос())
```

___

***[View language code](./Programming%20Language/)***

## A custom IDE for Udav

Not ready yet

___

***[See the IDE code](./Udav%20IDE/)***

## Extensions for VS code

The extension adds support for the Udav programming language to VS Code.

***Features***

- Syntax highlighting for .udav files

- Auto-completion of Udav keywords

***Usage***

After installing the extension, VS Code will automatically recognize .udav files and apply syntax highlighting and auto-completion to them.

***Installation***

At the moment, the extension is not available in the VS Code marketplace, so you can install it only by cloning the repository and installing it locally. To do this, you will need to follow these steps:

1. Copy the repository to your PC using the terminal

```bash
git clone https://github.com/NikitaBerezhnyj/Udav.git
```

2. Then find the VS code folder on your PC

3. Copy the udav-extension folder to the folder with other extensions

***Supported languages:*** Udav (.udav)

***Dependencies:*** None

***Version:*** 1.0.0
___

***[View extension code](./VS%20Code%20Extension/udav-extension/)***