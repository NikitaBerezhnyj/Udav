import os
import shutil
import platform

# Ініціалізація Удав
def init():
    # Windows
    if platform.system() == 'Windows':
        
        if os.path.exists(f"C:\\Program Files\\udav\\udav.exe"):
            print("Удав вже ініціалізований")
        else:
            shutil.copy("udav.exe", "C:\\Program Files\\udav\\")
            print("Удав ініціалізовано")
    # Linux
    elif platform.system() == 'Linux':
        if os.path.exists("/usr/bin/udav"):
            print("Удав вже ініціалізований")
        else:
            os.system("sudo cp udav /usr/bin")
            print("Удав ініціалізовано")
    # MacOS
    else:
        if os.path.exists("/usr/local/bin/udav"):
            print("Удав вже ініціалізований")
        else:
            shutil.copy("udav", "/usr/local/bin/")
            print("Удав ініціалізовано")


# Деініціалізація Удав
def deinit():
    # Windows
    if platform.system() == 'Windows':
        if os.path.exists(f"C:\\Program Files\\udav\\udav.exe"):
            os.remove(f"C:\\Program Files\\udav\\udav.exe")
            print("Деініціалізація пройшла успішно")
        else:
            print("Удав не ініціалізовано, тож вам не потрібно використовувати деініціалізація")
    # Linux
    elif platform.system() == 'Linux':
        if os.path.exists("/usr/bin/udav"):
            os.system("sudo rm /usr/bin/udav")
            print("Деініціалізація пройшла успішно")
        else:
            print("Удав не ініціалізовано, тож вам не потрібно використовувати деініціалізація")
    # MacOS
    else:
        if os.path.exists("/usr/local/bin/udav"):
            os.remove("/usr/local/bin/udav")
            print("Деініціалізація пройшла успішно")
        else:
            print("Удав не ініціалізовано, тож вам не потрібно використовувати деініціалізація")

# Допомога з переліком синтаксису та командами
def help():
    print("\033[1mМОВА ПРОГРАМУВАННЯ УДАВ\033[0m")
    print("")
    print("\033[1mСинтаксис:\033[0m")
    print("")
    print("  Вивід тексту на екран")
    print("  \033[1mдрук(\"Привіт, Світ!\")\033[0m")
    print("")
    print("  Оголошення змінних")
    print("  \033[1mзмінна а = 10\033[0m")
    print("")
    print("  Ввід користувача")
    print("  \033[1mзмінна а = ввід()\033[0m")
    print("")
    print("  Оголошення масивів")
    print("  \033[1mзмінна а = [0, 1]\033[0m")
    print("")
    print("  Умови if (якщо), else if (інакше_якщо) та else (інакше)")
    print('  \033[1mякщо а < 5 тоді; друк("<5") інакше_якщо а > 5 і а < 8 тоді; друк("<5 and >8") інакше друк(">8")\033[0m')
    print("")
    print("  Оголошення циклу while (поки)")
    print("  \033[1mпоки л < 10 тоді змінна л = л + 1; друк(л)\033[0m")
    print("")
    print("  Оголошення циклу for (для_кожного)")
    print("  \033[1mдля_кожного л = 0 до 10 тоді друк(л)\033[0m")
    print("")
    print("  Оголошення функцій")
    print("  \033[1mфункція Привіт_світ() -> друк(\"Привіт, світ!\")\033[0m")
    print("")
    print("\033[1mКоманди:\033[0m")
    print("")
    print("  \033[1mдопомога\033[0m     показує всі доступні команди для терміналу інтерпретатора та базовий синтаксис для записів коду у ньому")
    print("  \033[1mзапуск\033[0m       запускає файл .udav. (Приклад використання: \033[1mзапуск(\"приклад.udav\")\033[0m)")
    print("  \033[1mцт\033[0m           ця тека. Показує шлях до поточної теки")
    print("  \033[1mлф\033[0m           лист файлів. Показує вміст поточної теки")
    print("  \033[1mзт\033[0m           змінити теку. Змінює поточну теку")
    print("  \033[1mсф\033[0m           створити файл. Створює файли")
    print("  \033[1mст\033[0m           створити теку. Створює теку в поточній")
    print("  \033[1mочистити\033[0m     очищує термінал інтерпретатора")
    print("  \033[1mвихід\033[0m        закриває інтерпретатор")
    print("  \033[1mдопомога\033[0m     показує версію Удав")
    print("  \033[1mУДАВ\033[0m         виводить основну інформацію про стан Удава")
    print("")
    print("\033[1mІніціалізація\033[0m")
    print("")
    print("  Щоб використовувати Удав у будь-якій теці, вам слід ініціалізувати його.")
    print("  Це можна зробити за допомогою команди: \033[1mініціалізація\033[0m")
    print("")
    print("\033[1mДеініціалізація\033[0m")
    print("")
    print("  Якщо ви більше не плануєте використовувати Удав, вам слід скасувати ініціалізацію")
    print("  його, що можна зробити за допомогою наступної команди: \033[1mдеініціалізація\033[0m")
    print("")
    print("\033[1mДІЗНАТИСЬ БІЛЬШЕ МОЖНА ЗА ПОСИЛАННЯМ НА GITHUB:\033[0m")
    print("https://github.com/NikitaBerezhnyj/Udav")

# Версія удав
def version_check(version):
    print(f"Удав {version}")

# Очистити термінал
def clear():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

# Показати цю теку
def this_dir():
    current_dir = os.getcwd()
    new_dir = os.path.realpath(current_dir)
    print(new_dir)

# Змінити теку
def change_dir(directory):
    current_dir = os.getcwd()
    if directory == "..":
        os.system("cd ../")
        print("Теку було знято на одну")
    else:
        if os.path.exists(directory):
            os.chdir(directory)
            print("Теку змінено на", directory)
        else:
            print("Каталог", directory, "не існує")

    print("Поточна тека:", os.getcwd())
    
# Показати вміст теки
def list_files():
    os.system("ls")

# Створити файл
def create_file(filename):
    current_directory = os.getcwd()
    if "." in filename:
        full_filename = os.path.join(current_directory, filename)
    else:
        full_filename = os.path.join(current_directory, filename + ".udav")
    with open(full_filename, "w") as f:
        f.write("")
        f.close()
    print("Файл створено")

# Створити теку
def create_dir(foldername):
    os.mkdir(foldername)
    print("Теку створено")