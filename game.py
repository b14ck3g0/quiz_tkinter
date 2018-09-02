import random
import json
from tkinter import *
from itertools import zip_longest
import functools

percent = 0
level = 1
level_name = 0
glasses = 0
course_name = 0
correct_answer_list = ['Молодец!', 'Так держать!', 'Не сбавляй темп!', 'Умничка!', 'Круто!', 'Абсолютно верно!', 'Правильно!', 'Превосходно!', 'Верно!', 'Невероятно!']
wrong_answer_list = ['Неправильно!', 'Увы, но нет!', 'В следующий раз повезет!', 'Поднажми!', 'Неверно!', 'Готовься лучше!', 'Учить, учить и еще раз учить!', 'Не в этот раз!', 'Ошибка!', 'Не угадал!']
course_number_list = [' первого ', ' второго ', ' третьего ', ' четвертого ']
number_question_list = []
with open('questions_answers.json', 'r') as questions_answers_file:
    questions_answers = json.load(questions_answers_file)
with open('highscores.json', 'r') as scores_file:
    scores = json.load(scores_file)

root = Tk()
root['bg'] = 'light yellow'
root.title('Викторина ТИЭИ')
root.geometry('300x250')
root.title('Давайте познакомимся')

label_name = Label(text='Привет, напиши свое имя, чтобы \n мы знали как к тебе обращаться:', bg='light yellow')
label_name.place(x=50, y=75)
name = StringVar()
name_entry = Entry(textvariable = name, width=30)
name_entry.place(x=55, y=115)

def destroy():
    '''Уничтожиение окна'''
    root.destroy()

def clear(event):
    '''Очистка окна'''
    for element in root.winfo_children():
        element.destroy()

def menu():
    '''Меню'''
    clear(root)
    root.geometry('375x275')
    root.title('Главное меню')
    start_button = Button(text='Играть', width=20, height=6, bg='lime green', activebackground='lime green',  command=functools.partial(levels, percent, level, level_name, course_name))
    start_button.place(x=30, y=20)
    records_buttonn = Button(text='Рекорды', width=20, height=6, bg='medium orchid',activebackground='medium orchid', command=highscores)
    records_buttonn.place(x=200, y=19)
    rules_of_the_game_button = Button(text='Правила игры', width=20, height=6, bg='SteelBlue1',activebackground='SteelBlue1', command=rules)
    rules_of_the_game_button.place(x=30, y=150)
    exit_button = Button(text='Выход', width=20, height=6, bg='pale violet red',activebackground='pale violet red', command=destroy)
    exit_button.place(x=200, y=149)

def highscores():
    root.title('Рекорды')
    def delete_highscore():
        scores.clear()
        menu()
    clear(root)
    if len(scores) > 5:
        del scores[5:]
    if len(scores) > 0:
        score = 0
        while score != len(scores):
            score_label = Label(text=('\n' + str((score+1)) + '. '+  (scores[score][0]) + '   '+ str(scores[score][1])), bg='light yellow')
            score_label.pack()
            score += 1
        clear_highscore_button = Button(text='Очистить рекорды', bg='tomato', activebackground='tomato', padx=10, command=functools.partial(delete_highscore))
        clear_highscore_button.place(x=20, y=240)
    back_button = Button(text='Назад', bg='spring green', activebackground='spring green', padx=45, command=menu)
    back_button.place(x=220, y=240)

def rules():
    '''Правила игры'''
    clear(root)
    root.title('Правила игры')
    label_rules = Label(text=('\nПривет ' + name.get() + '.' +
    ''' 
    В этой игре тебе предстоит 
    пройти путь от абитуриента
    до бакалавра. Ты должен будешь
    выбирать правильный ответ на
    вопрос из четырех предложеннных.
    Если ты отвечаешь более чем на 50%
    вопросов на уровне правильно, 
    то ты переходишь на следующий уровень,
    если нет, то придется играть сначала.
    Так же за каждый правильный ответ ты
    получаешь очки. Ты всегда можешь можешь
    посмотреть кто набрал больше всех очков в 'Рекорды'. 
    Удачи.
    ''' ), bg='light yellow')
    label_rules.pack()

    i_see_button = Button(text='Понятно', width=10, height=1, bg='SteelBlue1', activebackground='SteelBlue1', command=menu)
    i_see_button.place(x=150, y=240)

def shuffle_question():
    '''Перемешивает номера вопросов'''
    i = 0
    while len(number_question_list) != len(questions_answers[level]):
       number_question_list.append(str(i))
       i += 1
    random.shuffle(number_question_list)

shuffle_question()
PERCENT_UP = 100 / len(number_question_list)

def levels(percent, level, level_name, course_name):
    '''Движок уровня. Переключение уровней'''
    root.title(questions_answers[level_name])
    root.geometry('575x325')
    global glasses
    clear(root)
    if len(number_question_list) == 0:
        clear(root)
        if percent > 50:
            if level == 9:
                win_label = Label(text=('Поздраляю, ты прошел все уровни. Ты набрал ' + str(glasses) + ' очков.'), bg='light yellow')
                win_label.pack()
                exit_button = Button(text='Выход', bg='lime green', activebackground='lime active', command=destroy)
                exit_button.pack()
                scores.append([name.get(), glasses])
                scores.sort(key=lambda x: x[1])
                scores.reverse()
            else:
                result_label = Label(text=('Поздравляю, ты набрал, ' + str(percent) + '%.\n Теперь ты студент ' + course_number_list[course_name] + ' курса'), bg='light yellow')
                result_label.place(x=180, y=130)
                level += 2
                level_name += 2
                percent = 0
                course_name += 1
                shuffle_question()
                level_up_button = Button(text='Перейти на следующий уровень', bg='SteelBlue1',activebackground='SteelBlue1', command = functools.partial(levels, percent, level, level_name, course_name))
                level_up_button.place(x=185, y=190)
        else:
            scores.append([name.get(), glasses])
            scores.sort(key=lambda x: x[1])
            scores.reverse()
            result_label = Label(text=('Увы, но ты набрал всего, ' + str(percent) + '%.\n В следующий раз будешь лучше готовиться.'), bg='light yellow')
            result_label.place(x=150, y=130)
            repeat_label = Label(text='Попробовать еще раз?', bg='light yellow')
            repeat_label.place(x=215, y=165)
            level_name = 0
            level = 1
            glasses = 0
            percent = 0
            course_name = 0
            shuffle_question()
            yes_button = Button(text='Да', width=10, bg='spring green', activebackground='spring green', command = functools.partial(levels, percent, level, level_name, course_name))
            yes_button.place(x=160, y=225)
            no_button = Button(text='Нет', width=10, bg='tomato', activebackground='tomato', command=destroy)
            no_button.place(x=300, y=224)
        return
    n = 75
    question = questions_answers[level][int(number_question_list[0])][0]
    def split_str(que, n):
        args = [iter(que)] * n
        for s in zip_longest(*args, fillvalue=''):
            yield ''.join(s)
    que_1 = ''
    for s in split_str(question, n):
        que_1 += s + '\n'
    question_label = Label(text=('\n' + que_1), bg='light yellow')
    question_label.pack()
    def yes_no(percent, level):
        global glasses
        if r_var.get() == true_answer:
            glasses += PERCENT_UP
            percent += PERCENT_UP
            correct_label = Label(text=random.choice(correct_answer_list), bg='spring green')
            correct_label.pack(expand=True, fill=BOTH)
        else:
            wrong_label = Label(text=random.choice(wrong_answer_list), bg='orange red')
            wrong_label.pack(expand=True, fill=BOTH)
        check_button.destroy()
        question_label.destroy()
        option_1.destroy()
        option_2.destroy()
        option_3.destroy()
        option_4.destroy()
        if len(number_question_list) == 0:
            result_button = Button(text='Узнать результат', bg='SteelBlue1', activebackground='SteelBlue1', command = functools.partial(levels, percent, level, level_name, course_name))
            result_button.place(x=235, y=290)
        else:
            next_button = Button(text='Следующий вопрос', bg='SteelBlue1', activebackground='SteelBlue1', command = functools.partial(levels, percent, level, level_name, course_name))
            next_button.place(x=220, y=290)
    reduction = questions_answers[level][int(number_question_list[0])][1]
    r_var = IntVar()
    option_1 = Radiobutton(text=reduction[0], variable=r_var, value=0, bg='light yellow')
    option_2 = Radiobutton(text=reduction[1], variable=r_var, value=1, bg='light yellow')
    option_3 = Radiobutton(text=reduction[2], variable=r_var, value=2, bg='light yellow')
    option_4 = Radiobutton(text=reduction[3], variable=r_var, value=3, bg='light yellow')
    option_1.place(x=100, y=150)
    option_2.place(x=100, y=175)
    option_3.place(x=100, y=200)
    option_4.place(x=100, y=225)
    true_answer = questions_answers[level][int(number_question_list[0])][2]
    number_question_list.pop(0)
    check_button = Button(text='Проверить', bg='SteelBlue1',activebackground='SteelBlue1', command = functools.partial(yes_no, percent, level))
    check_button.place(x=240, y=290)
    root.mainloop()

ok_button = Button(text='Ok', width=10, height=1, bg='SteelBlue1',activebackground='SteelBlue1', command = menu)
ok_button.place(x=110, y=210)
root.mainloop()
with open('highscores.json', 'w') as score_file:
    json.dump(scores, score_file)
