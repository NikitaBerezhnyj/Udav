import os
import udav
import snake
import readline
import shell_commands as sc

is_worked = True
version = 0.1

while is_worked:
	text = input('УДАВ >> ')

	# Пропуск пустого рядка в інтерпретаторі
	if text == '':
		continue

	# Ініціалізація Удав
	if text == "ініціалізація":
		sc.init()
		continue

	# Деініціалізація Удав
	if text == "деініціалізація":
		sc.deinit()
		continue

	# Допомога з переліком синтаксису та командами
	if text == "допомога":
		sc.help()
		continue

	# Версія удав
	if text == "версія":
		sc.version_check(version)
		continue

	# Показати цю теку
	if text == "цт":
		sc.this_dir()
		continue

	# Показати вміст теки
	if text == "лф":
		sc.list_files()
		continue

	# Змінити теку
	words = text.split()
	if words[0] == "зт":
		directory = words[1]
		sc.change_dir(directory)
		continue

	# Створити файл
	words = text.split()
	if words[0] == "сф":
		filename = words[1]
		sc.create_file(filename)
		continue

	# Створити теку
	words = text.split()
	if words[0] == "ст":
		foldername = words[1]
		sc.create_dir(foldername)
		continue

	# Очистити термінал
	if text == "очистити":
		sc.clear()
		continue

	# Вихід з терміналу удав
	if text == "вихід": 
		is_worked = False
		break

	# Маленька велекодка
	if text == "УДАВ":
		snake.fill_terminal(version)
		continue

	if text.strip() == "": continue
	result, error = udav.run('Командний рядок Удав', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))