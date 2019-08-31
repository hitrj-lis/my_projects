from tkinter import Tk, Menu, Text, messagebox, END, filedialog


def context(event):
    context_menu.tk_popup(event.x_root, event.y_root)


def close():
    if messagebox.askyesno(exit_out_txt, asky_exit_txt):
        window.destroy()


def new_file():
    if messagebox.askyesno(new_file_txt, asky_new_txt):
        text_panel.delete(1.0, END)
        window.title(new_file_txt)


def open_file():
    try:
        if messagebox.askyesno(new_file_txt, asky_new_txt):
            file_name = filedialog.askopenfilename()
            with open(file_name, 'r', encoding='utf-8') as file:
                text_panel.delete(1.0, END)
                content = file.read()
            text_panel.insert(1.0, content)
            window.title(file_name)
        else:
            return
    except FileNotFoundError:
        pass


def save_file():
    file_name = filedialog.asksaveasfilename()
    with open(file_name + '.txt', 'w') as file:
        content = text_panel.get(1.0, END)
        file.write(content[:-1])


# окно
window = Tk()
window.geometry('800x600')
window.title('Новый файл')
window.resizable(False, False)

# текстовые данные
top_txt = 'Файл'
new_txt = 'Создать'
open_txt = 'Открыть'
save_txt = 'Сохранить'
copy_txt = 'Копировать'
paste_txt = 'Вставить'
cut_txt = 'Вырезать'
exit_out_txt = 'Выход'
asky_exit_txt = 'Все изменения будут утеряны!\n\t  Выйти?'
new_file_txt = 'Новый файл'
asky_new_txt = 'Все изменения будут утеряны!\n        Создать новый файл?'

# верхняя панель
top_panel = Menu()
window.config(menu=top_panel)

# менюшки в верхней панели
file_menu = Menu(top_panel, tearoff=0)
top_panel.add_cascade(label=top_txt, menu=file_menu)

# меню файл
file_menu.add_command(label=new_txt, accelerator='Ctr+N', command=new_file)
file_menu.add_command(label=open_txt, accelerator='Ctr+O', command=open_file)
file_menu.add_command(label=save_txt, accelerator='Ctr+S', command=save_file)

# текстовое поле
text_panel = Text(width=800, height=600)
text_panel.pack()

# контекстное меню
context_menu = Menu(text_panel, tearoff=0)
context_menu.add_command(label=copy_txt)
context_menu.add_command(label=paste_txt)
context_menu.add_command(label=cut_txt)

# сигнал от пользователя
text_panel.bind('<Button-3>', context)
window.protocol('WM_DELETE_WINDOW', close)

window.mainloop()
