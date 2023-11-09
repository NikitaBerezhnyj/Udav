import re
import tkinter as tk
from tkinter import *
from tkterm import Terminal
from tkinter import filedialog, messagebox, simpledialog

# Клас лексер для грамотної підсвітки коду
class SyntaxHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.keywords = ['func', 'print', 'input', 'if', 'else', 'elif', 'for', 'while', 'return']
        self.literal = ['\\+', '-', '\\*', '/', '\\+=', '-=', '\\*=', '\\+\\+', '--', '==', '!=', '<', '>', '<=', '>=']
        self.types = ['int', 'float', 'string', 'bool', 'char']
        self.patterns = [
            (r'\b(?:' + '|'.join(map(re.escape, self.keywords)) + r')\b', 'keywords', '#00A79D'),
            (r'\b(?:' + '|'.join(map(re.escape, self.literal)) + r')\b', 'literal', '#FF0000'),
            (r'\b(?:' + '|'.join(map(re.escape, self.types)) + r')\b', 'types', '#0080ff')
        ]

    def highlight(self):
        for pattern, tag, color in self.patterns:
            self.highlight_pattern(pattern, tag, color)

    def highlight_pattern(self, pattern, tag, color):
        start = '1.0'
        end = tk.END
        self.text_widget.tag_remove(tag, start, end)
        for match in re.finditer(pattern, self.text_widget.get(start, end)):
            start_index = f"{start}+{match.start()}c"
            end_index = f"{start}+{match.end()}c"
            self.text_widget.tag_add(tag, start_index, end_index)
            self.text_widget.tag_config(tag, foreground=color)

# Оголошення компонентів для програм
compiler = Tk()
compiler.title('NikLang IDE')

# Основні змінні
file_path = ''
is_visible_term = False
stackCursor = 0
on_text_change_index = 0

# Темна тема
def set_dark_theme():
    compiler.config(bg='#282C34')
    paned_window.config(bg='#282C34')
    textField.config(bg='#282C34', fg='#E6E6E6', insertbackground='#464E5E')
    menu_bar.config(bg='#282C34', fg='#E6E6E6')
    lineNumber.config(bg='#282C34', fg='#E6E6E6')

# Встановлення шрифту
def set_font(widget, font_size):
    font = f'{{TkDefaultFont}} {font_size}'
    widget.configure(font=font)

# Встановлення шляху до файлу
def set_file_path(path):
    global file_path
    file_path = path

# Відкрити файл
def open_file():
    global file_path

    if file_path and textField.get('1.0', END).strip() != open(file_path, 'r').read().strip():
        response = messagebox.askyesnocancel('Unsaved Changes', 'Do you want to save changes before opening a new file?')
        if response is not None:
            if response:
                save_file()

    file_types = [('NikLang Files', '*.nl'), ('Other Files', '*.*')]
    path = filedialog.askopenfilename(filetypes=file_types)

    if path:
        with open(path, 'r') as file:
            code = file.read()
            textField.delete('1.0', END)
            textField.insert('1.0', code)
            set_file_path(path)
            highlight_commands(None)
            update_line_number_autoscroll()

# Зміна файлу
def switch_file():
    global file_path
    if file_path and textField.get('1.0', END).strip() != open(file_path, 'r').read().strip():
        response = messagebox.askyesnocancel('Unsaved Changes', 'Do you want to save changes before switching to a new file?')
        if response is not None:
            if response:
                save_file()
    open_file()

# Зберегти як
def save_as():
    global file_path

    file_types = [('NikLang', '*.nl'), ('Other Files', '*.*')]
    path = filedialog.asksaveasfilename(filetypes=file_types)

    if path:
        with open(path, 'w') as file:
            code = textField.get('1.0', END)
            file.write(code)
            set_file_path(path)

# Зберегти файл
def save_file(event=None):
    global file_path

    if file_path:
        with open(file_path, 'w') as file:
            code = textField.get('1.0', END)
            file.write(code)
    else:
        save_as()

# Показувати термінал
def terminal_visible(event=None):
    global is_visible_term
    if is_visible_term:
        paned_window.forget(terminal)
        is_visible_term = False
    else:
        paned_window.add(terminal, stretch="always")
        is_visible_term = True

# Вихід
def check_exit():
    global file_path
    if file_path:
        current_code = textField.get('1.0', END).strip()
        
        # Перевірка існування файлу
        try:
            with open(file_path, 'r') as file:
                saved_code = file.read().strip()
        except FileNotFoundError:
            saved_code = None

        if current_code != saved_code:
            response = messagebox.askyesnocancel('Unsaved Changes', 'Do you want to save changes before exiting?')
            if response is not None:
                if response:
                    save_file()
                compiler.destroy()
        else:
            compiler.destroy()
    else:
        # Якщо file_path порожній, запитаємо користувача, чи хоче він зберегти файл як новий
        current_code = textField.get('1.0', END).strip()
        if current_code:
            response = messagebox.askyesnocancel('Unsaved Changes', 'Do you want to save changes before exiting?')
            if response is not None:
                if response:
                    save_as()
                compiler.destroy()
        else:
            compiler.destroy()

# Виділити все
def select_all(event):
    if isinstance(event, Event) and event.widget == textField:
        textField.tag_add(SEL, "1.0", END + "-1c")
        textField.mark_set(INSERT, END)
        textField.see(INSERT)
        return "break"

# Пошук
def find(event=None):
    global on_text_change_index
    on_text_change_index = 0
    # Очищаємо всі попередні теги 'found'
    textField.tag_remove('found', '1.0', END)

    search_term = simpledialog.askstring("Find", "Enter search term:")

    # Отримуємо введений користувачем текст
    s = s = search_term

    if s:
        # Індекс для початку пошуку
        idx = '1.0'
        while True:
            # Шукаємо слово
            idx = textField.search(s, idx, nocase=1, stopindex=END)
            if not idx:
                break

            # Кінцевий індекс слова
            lastidx = f"{idx}+{len(s)}c"

            # Додаємо тег 'found' для виділення слова
            textField.tag_add('found', idx, lastidx)
            idx = lastidx

            # Переміщуємо курсор до кінця знайденого слова
            textField.mark_set(INSERT, lastidx)
            textField.see(INSERT)

        # Конфігуруємо тег 'found' для встановлення кольору
        textField.tag_config('found', background='yellow', foreground='black')
    textField.focus()

# Відміна виділення знайденого тексту
def on_text_change(event):
    global on_text_change_index
    if event.keysym == "Return" and on_text_change_index < 1:
        on_text_change_index = 1
    else:
        # Очищаємо теги 'found' при зміні тексту
        textField.tag_remove('found', '1.0', END)
        highlight_commands(event)
        update_line_number_autoscroll(event)
        add_matching_bracket(event)
        highlight_comments()

# Відміна подій
def undo(event=None):
    global stackCursor  # Додаємо глобальну змінну
    if stackCursor != 0:
        clear()
        if stackCursor > 0:
            stackCursor -= 1
        T1.insert("0.0", stack[stackCursor])

# Отримання номерів строк
def get_line_number(text_widget):
    output = ""
    row, col = text_widget.index('end').split('.')
    for i in range(1, int(row)):
        output += str(i) + "\n"
    return output

# Оновлення номерів строк
def update_line_number(event=None):
    lineNumber_bar = get_line_number(textField)
    lineNumber.config(state="normal")
    lineNumber.delete(1.0, END)
    lineNumber.insert(1.0, lineNumber_bar)
    lineNumber.config(state="disabled")

# Прокрутка обох елементів
def on_scroll(*args):
    lineNumber.yview_moveto(args[0])
    textField.yview_moveto(args[0])

# Оновлення номерів строк + авто прокрутка
def update_line_number_autoscroll(event=None):
    update_line_number()
    text_height = int(textField.index("end-1c").split('.')[0])
    visible_height = int(textField.cget("height"))
    
    if text_height > visible_height:
        lineNumber.yview_moveto(textField.yview()[0])

# Зміна розміру шрифту
def change_font_size(event):
    current_size = int(textField.cget("font").split(" ")[-1])
    if event.keysym == "minus" and current_size > 1:
        textField.configure(font=("TkFixedFont", current_size - 1))
        lineNumber.configure(font=("TkFixedFont", current_size - 1))
    elif event.keysym == "equal":
        textField.configure(font=("TkFixedFont", current_size + 1))
        lineNumber.configure(font=("TkFixedFont", current_size + 1))

# Додавання дужок
def add_matching_bracket(event):  
    entered_char = event.keysym
    brackets = {
        'parenleft': ')',
        'braceleft': '}',
        'bracketleft': ']',
        'quotedbl': '"',
        'apostrophe': "'"
    }
    
    if entered_char in brackets:
        cursor_index = textField.index(INSERT)
        matching_bracket = brackets[entered_char]

        textField.insert(cursor_index, matching_bracket)
        
        # Визначаємо позицію курсора після вставлення закриваючого символу
        new_cursor_index = f"{cursor_index}+1c"
        
        # Додаємо мітку на відстань -1c від нової позиції курсора
        textField.tag_add("insert_marker", new_cursor_index, f"{new_cursor_index}-1c")
        
        # Встановлюємо позначений курсор
        textField.mark_set(INSERT, new_cursor_index)
    
        move_cursor()

# Рухати курсор
def move_cursor():
    current_index = textField.index(tk.INSERT)
    line, char = map(int, current_index.split('.'))
    new_index = f"{line}.{max(char - 1, 0)}"
    textField.mark_set(tk.INSERT, new_index)
    textField.see(tk.INSERT)

# Вимкнення стандартних функцій
def disable_default_binding(event=None):
    print("disable_default_binding")
    return 'break'

def remove_selection(event=None):
    # Зняти виділення
    textField.tag_remove(tk.SEL, "1.0", tk.END)

# Додавання коментарів на Ctrl+/
def add_comments(event=None):
    # Отримуємо поточну позицію курсора
    cursor_position = textField.index(INSERT)

    # Отримуємо номер активного рядка
    current_line = int(cursor_position.split('.')[0])

    # Отримуємо початок рядка та його кінець
    line_start = f"{current_line}.0"
    line_end = f"{current_line + 1}.0"

    # Отримуємо текст активного рядка
    line_text = textField.get(line_start, line_end).rstrip()

    # Перевірка чи вже є коментар
    if line_text.startswith("// "):
        # Видаляємо існуючий коментар
        textField.delete(line_start, f"{current_line}.{len('// ')}")
    else:
        # Додаємо коментарі тільки якщо рядок не порожній
        if line_text.strip():
            # Відміна стандартної обробки події виділення
            textField.bind('<Control-slash>', disable_default_binding)

            # Вставляємо "// " на початок рядка
            textField.insert(line_start, "// ")

            # Позначаємо виділену область (початок і кінець)
            sel_start = f"{current_line}.0"
            sel_end = f"{current_line}.{len('// ')}"

            # Встановлюємо виділення
            textField.tag_add(tk.SEL, sel_start, sel_end)

            # Відновлюємо стандартну обробку події виділення
            textField.bind('<Control-slash>', add_comments)

            # Знімаємо виділення після закінчення вставки коментарів
    textField.after(1, remove_selection)
    highlight_comments()

# Підсвітка коментарів
def highlight_comments():
    code = textField.get('1.0', END)
    textField.tag_remove('comments', '1.0', END)

    # Знайдемо всі коментарі та додамо їм тег comments
    pattern = re.compile(r'(?P<comments>//.*)')
    matches = pattern.finditer(code)

    for match in matches:
        start, end = match.span('comments')
        for i in range(start, end):
            textField.tag_add('comments', f'1.0+{i}c')

    # Конфігурація тегу comments
    textField.tag_config('comments', foreground='grey')

# Підсвітка коду
def highlight_commands(event):
    highlighter.highlight()

lineNumber = Text(compiler, width=4, padx=5, state="disabled", takefocus=0, background="grey", wrap="none", height=20, font=("TkFixedFont", 14))

# Створення вікна з панелями
paned_window = PanedWindow(compiler, orient=VERTICAL)

# Встановлення значень, щоб зміни були двосторонніми
paned_window.pack(expand=YES, fill="both")

# Створення меню бару
menu_bar = Menu(compiler)

# Команди для меню
menu_bar.add_command(label='Open', command=open_file)
menu_bar.add_command(label='Save', command=save_file)
menu_bar.add_command(label='Save as', command=save_as)
menu_bar.add_command(label='Terminal', command=terminal_visible)
menu_bar.add_command(label='Exit', command=check_exit)

# Створення editor_frame
editor_frame = Frame(paned_window)

# Створення покажчика номерів строк
lineNumber = Text(editor_frame, width=4, padx=5, state="disabled", takefocus=0, background="grey", wrap="none", height=20, font=("TkFixedFont", 14))
lineNumber.pack(side="left", fill="y")
lineNumber.config(font=("TkFixedFont", 14))  # Встановлення шрифту

# Створення редактору коду
textField = Text(editor_frame, height=20, wrap=WORD, font=("TkFixedFont", 14), undo=True)
textField.bind("<KeyRelease>", update_line_number)
textField.pack(expand=YES, fill="both")

# Додавання прокрутки через авто прокрутку
paned_window.add(editor_frame)
textField['yscrollcommand'] = on_scroll
textField.bind('<KeyRelease>', update_line_number_autoscroll)

# Створення віджету термінал
terminal = Terminal(compiler)

# Конфігурація меню бару
compiler.config(menu=menu_bar)

# Bind подій
textField.bind('<Control-z>', undo)
textField.bind('<Control-f>', find)
textField.bind('<Control-s>', save_file)
textField.bind('<Control-a>', select_all)
textField.bind('<Control-minus>', change_font_size)
textField.bind('<Control-equal>', change_font_size)
textField.bind('<Control-asciitilde>', terminal_visible)
textField.bind('<Control-slash>', lambda event: add_comments())
textField.bind('<KeyRelease>', add_matching_bracket, update_line_number_autoscroll)
textField.bind('<KeyRelease>', lambda event: [update_line_number_autoscroll(event), highlight_commands(event)])
textField.bind('<KeyRelease>', on_text_change)

compiler.protocol("WM_DELETE_WINDOW", check_exit)

# Увімкнення темної теми
set_dark_theme()

# Відображення номерів строк коли відкривається файл
update_line_number_autoscroll()

# Запуск підсвітки коду через клас лексер
highlighter = SyntaxHighlighter(textField)

# Запуск програми
compiler.mainloop()