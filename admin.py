import json
from tkinter import *
import functools

with open('questions_answers.json', 'r') as file:
    questions_answers_list = json.load(file)
root = Tk()
root.geometry('300x150')
root['bg'] = 'SteelBlue2'
root.title('Редактор вопросов')
questions_list = []

def destroy():
    '''Уничтожиение окна'''
    root.destroy()

def save_changes():
    with open('questions_answers.json', 'w') as file:
        json.dump(questions_answers_list, file)

def clear(event):
    '''Очистка окна'''
    for element in root.winfo_children():
        element.destroy()

def level_selection():
    root.geometry('300x150')
    root.title('Выбор уровня')
    clear(root)
    level = 0
    levels_list = []
    levels_listbox = Listbox(width=40, height=5, bg='light yellow', selectbackground='SkyBlue4')
    levels_listbox.place(x=28, y=10)
    while level < 9:
        levels_listbox.insert(4, questions_answers_list[level])
        levels_list.append(questions_answers_list[level])
        level += 2
    level_selection_button = Button(text='Далее', bg='light yellow', activebackground='light yellow', command=functools.partial(level_questions, levels_listbox, levels_list))
    level_selection_button.place(x=125, y=110)


def level_questions(levels_listbox, levels_list):
    root.title(levels_listbox.get(ACTIVE))
    root.geometry('1300x500')
    level_questions_list = questions_answers_list[levels_list.index(levels_listbox.get(ACTIVE)) * 2 + 1]
    clear(root)
    questions_listbox = Listbox(width=200, height=25)
    questions_listbox.place(x=50, y=20)
    for i in level_questions_list:
        questions_listbox.insert(len(level_questions_list), i[0])
        questions_list.append(i[0])
    create_button = Button(text='Создать вопрос', bg='light yellow', activebackground='light yellow', command=functools.partial(create_question, level_questions_list, questions_listbox))
    create_button.place(x=50, y=460)
    change_button = Button(text='Изменить вопрос', bg='light yellow', activebackground='light yellow', command=functools.partial(change_question, level_questions_list, questions_listbox))
    change_button.place(x=150, y=460)
    delete_button = Button(text='Удалить вопрос', bg='light yellow', activebackground='light yellow', command=functools.partial(delete_question, level_questions_list, questions_listbox))
    delete_button.place(x=261, y=460)
    back_button = Button(text='Назад', bg='light yellow', activebackground='light yellow', command=level_selection)
    back_button.place(x=1200, y=460)
    exit_button = Button(text='Выход', bg='light yellow', activebackground='light yellow', command=destroy)
    exit_button.place(x=1250, y=460)

def create_question(level_questions_list, questions_listbox):

    def save_create():
        new_question = [question_entry.get(), [option_1_entry.get(), option_2_entry.get(), option_3_entry.get(), option_4_entry.get()], (int(answer_entry.get())-1)]
        level_questions_list.append(new_question)
        questions_list.append(new_question[0])
        save_changes()
        questions_listbox.insert(len(questions_answers_list[0]), question_entry.get())
        root_create.destroy()

    root_create = Tk()
    root_create.title('Создать вопрос')
    root_create.geometry('800x300')
    root_create['bg'] = 'SteelBlue2'
    question = Label(root_create, text='Введите новый вопрос:', bg='SteelBlue2')
    question.pack()
    message = StringVar()
    question_entry = Entry(root_create, textvariable=message, width=125)
    question_entry.pack()
    option_1 = Label(root_create, text='Введите первый вариант ответа:', bg='SteelBlue2')
    option_1.pack()
    message_1 = StringVar()
    option_1_entry = Entry(root_create, textvariable=message_1, width=125)
    option_1_entry.pack()
    option_2 = Label(root_create, text='Введите второй вариант ответа:', bg='SteelBlue2')
    option_2.pack()
    message_2 = StringVar()
    option_2_entry = Entry(root_create, textvariable=message_2, width=125)
    option_2_entry.pack()
    option_3 = Label(root_create, text='Введите третий вариант ответа:', bg='SteelBlue2')
    option_3.pack()
    message_3 = StringVar()
    option_3_entry = Entry(root_create, textvariable=message_3, width=125)
    option_3_entry.pack()
    option_4 = Label(root_create, text='Введите четвертый вариант ответа:', bg='SteelBlue2')
    option_4.pack()
    message_4 = StringVar()
    option_4_entry = Entry(root_create, textvariable=message_4, width=125)
    option_4_entry.pack()
    answer = Label(root_create, text='Введите номер правильного ответа:', bg='SteelBlue2')
    answer.pack()
    message_5 = StringVar()
    answer_entry = Entry(root_create, textvariable=message_5, width=125)
    answer_entry.pack()
    save_button = Button(root_create, bg='light yellow', activebackground='light yellow', text='Сохранить', command=save_create)
    save_button.place(x=370, y=265)
    root_create.mainloop()

def delete_question(level_questions_list, questions_listbox):
    save_changes()
    index = questions_list.index(questions_listbox.get(ACTIVE))
    del level_questions_list[index]
    del questions_list[index]
    questions_listbox.delete(ACTIVE)

def change_question(level_questions_list, questions_listbox):

    def save_change():
        save_changes()
        index = questions_list.index(questions_listbox.get(ACTIVE))
        new_question = [question_entry.get(), [option_1_entry.get(), option_2_entry.get(), option_3_entry.get(), option_4_entry.get()], (int(answer_entry.get()) - 1)]
        del level_questions_list[index]
        del questions_list[index]
        level_questions_list.insert((index), new_question)
        questions_listbox.delete(ACTIVE)
        questions_listbox.insert(index, question_entry.get())
        questions_list.insert(index, new_question[0])
        root_change.destroy()

    root_change = Tk()
    root_change.title('Изменить вопрос')
    root_change.geometry('800x300')
    root_change['bg'] = 'SteelBlue2'
    question = Label(root_change, text='Измените вопрос:', bg='SteelBlue2')
    question.pack()
    message = StringVar()
    question_entry = Entry(root_change, textvariable=message, width=125)
    question_entry.insert(0, questions_listbox.get(ACTIVE))
    question_entry.pack()
    option_1 = Label(root_change, text='Измените первый вариант ответа:', bg='SteelBlue2')
    option_1.pack()
    message_1 = StringVar()
    option_1_entry = Entry(root_change, textvariable=message_1, width=125)
    option_1_entry.insert(0, level_questions_list[(questions_list.index(questions_listbox.get(ACTIVE)))][1][0])
    option_1_entry.pack()
    option_2 = Label(root_change, text='Введите второй вариант ответа:', bg='SteelBlue2')
    option_2.pack()
    message_2 = StringVar()
    option_2_entry = Entry(root_change, textvariable=message_2, width=125)
    option_2_entry.insert(0, level_questions_list[(questions_list.index(questions_listbox.get(ACTIVE)))][1][1])
    option_2_entry.pack()
    option_3 = Label(root_change, text='Введите третий вариант ответа:', bg='SteelBlue2')
    option_3.pack()
    message_3 = StringVar()
    option_3_entry = Entry(root_change, textvariable=message_3, width=125)
    option_3_entry.insert(0, level_questions_list[(questions_list.index(questions_listbox.get(ACTIVE)))][1][2])
    option_3_entry.pack()
    option_4 = Label(root_change, text='Введите четвертый вариант ответа:', bg='SteelBlue2')
    option_4.pack()
    message_4 = StringVar()
    option_4_entry = Entry(root_change, textvariable=message_4, width=125)
    option_4_entry.insert(0, level_questions_list[(questions_list.index(questions_listbox.get(ACTIVE)))][1][3])
    option_4_entry.pack()
    answer = Label(root_change, text='Введите номер правильного ответа:', bg='SteelBlue2')
    answer.pack()
    message_5 = IntVar()
    answer_entry = Entry(root_change, textvariable=message_5, width=125)
    answer_entry.insert(0, level_questions_list[(questions_list.index(questions_listbox.get(ACTIVE)))][2] + 1)
    answer_entry.pack()
    save_button = Button(root_change, text='Сохранить', bg='light yellow', activebackground='light yellow', command=save_change)
    save_button.place(x=370, y=265)
    root_change.mainloop()

hello_label = Label(text='Привет, здесь ты можешь изменить,\nдобавить и даже удалить любые вопросы', bg='SteelBlue2')
hello_label.place(x=35, y=45)
i_see_button=Button(text='Понятно', bg='light yellow', activebackground='light yellow', command=functools.partial(level_selection))
i_see_button.place(x=125, y=110)


root.mainloop()