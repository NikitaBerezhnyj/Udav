import re
import tkinter as tk
from tkinter import *
from tkterm import Terminal
from tkinter import filedialog, messagebox, simpledialog

# Клас лексер для грамотної підсвітки коду
class SyntaxHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.keywords = ['func', 'print', 'input', 'if', 'else', 'elif', 'for', 'while', 'return', 'add']
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

class Autocomplete:
    def __init__(self, text_widget, suggestions):
        self.text_widget = text_widget
        self.suggestions = suggestions
        self.last_word = ''

        try:
            self.popup_menu.destroy()
        except AttributeError:
            pass

        self.popup_menu = tk.Listbox(self.text_widget, selectmode=tk.SINGLE)
        self.popup_menu.bind('<Return>', self.insert_selection)
        self.popup_menu.place_forget()

        self.text_widget.bind('<KeyRelease>', self.handle_key_release)
        self.text_widget.bind('<Down>', self.handle_down)
        self.text_widget.bind('<Up>', self.handle_up)
        self.text_widget.bind('<FocusIn>', self.handle_focus_in)
        self.text_widget.bind('<FocusOut>', self.handle_focus_out)

    def show_popup_menu(self, suggestions):
        if suggestions:
            self.popup_menu.delete(0, tk.END)
            for suggestion in suggestions:
                self.popup_menu.insert(tk.END, suggestion)

            x, y, _, _ = self.text_widget.bbox(tk.INSERT)
            self.popup_menu.place(x=x, y=y + 20, anchor='nw', height=len(suggestions) * 20)

    def insert_selection(self, event):
        selected_item = self.popup_menu.get(tk.ACTIVE)
        if selected_item:
            current_line = self.text_widget.get('insert linestart', 'insert lineend')
            current_line_words = current_line.split()
            current_word_index = len(current_line_words) - 1

            if current_word_index >= 0:
                current_word_start = self.text_widget.search(current_line_words[current_word_index], 'insert', backwards=True, regexp=True)
                current_word_end = f"{current_word_start}+{len(current_line_words[current_word_index])}c"
                self.text_widget.delete(current_word_start, current_word_end)

            self.text_widget.insert(tk.INSERT, selected_item)
            self.text_widget.focus_set()
            self.popup_menu.place_forget()

    def handle_key_release(self, event):
        current_line = self.text_widget.get('insert linestart', 'insert lineend')
        words = current_line.split()
        current_word = words[-1] if words else ''

        if current_word and current_word != self.last_word:
            suggestions = [word for word in self.suggestions if word.startswith(current_word) and word != current_word]
            self.show_popup_menu(suggestions)
            self.last_word = current_word
        else:
            self.popup_menu.place_forget()

    def handle_down(self, event):
        if self.popup_menu.winfo_ismapped():
            self.popup_menu.focus_set()
            self.popup_menu.selection_set(0)

    def handle_up(self, event):
        if self.popup_menu.winfo_ismapped():
            self.popup_menu.focus_set()
            self.popup_menu.selection_set(tk.END)

    def handle_focus_in(self, event):
        self.text_widget.tag_remove(tk.SEL, '1.0', tk.END)

    def handle_focus_out(self, event):
        self.popup_menu.place_forget()
        self.text_widget.after(10, self.check_focus)

    def check_focus(self):
        try:
            if self.text_widget.winfo_exists() and self.text_widget == self.text_widget.focus_get():
                self.handle_key_release(None)
            else:
                self.text_widget.after(10, self.check_focus)
        except tk.TclError:
            # Обробка випадку, коли відбувається видалення віджета під час закриття програми
            pass

