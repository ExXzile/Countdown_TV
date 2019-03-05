
# Countdown Letters Round, free open source, python beginner practice
# by Ray Ziemelis, 2019
# Python programming language #Closed Facebook Group

import tkinter
import random
import pickle
from num2words import num2words


root = tkinter.Tk()
root.title('Countdown, letters round')
root.geometry('+500+100')

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=0)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=0)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)


def random_go():

# official weights to letters by countdown
# source http://www.thecountdownpage.com/letters.htm
    
    vowels = ['A'] * 15 \
           + ['E'] * 21 \
           + ['I'] * 13 \
           + ['O'] * 13 \
           + ['U'] * 5

    constn = ['B'] * 2 \
           + ['C'] * 3 \
           + ['D'] * 6 \
           + ['F'] * 2 \
           + ['G'] * 3 \
           + ['H'] * 2 \
           + ['J'] \
           + ['K'] \
           + ['L'] * 5 \
           + ['M'] * 4 \
           + ['N'] * 8 \
           + ['P'] * 4 \
           + ['Q'] \
           + ['R'] * 9 \
           + ['S'] * 9 \
           + ['T'] * 9 \
           + ['V'] \
           + ['W'] \
           + ['X'] \
           + ['Y'] \
           + ['Z']

    weight_alphabet = vowels + constn

    if random_value.get() == 0:
        select_letters = random.choices(weight_alphabet, k=9)
    else:
        select_letters = random.choices(vowels, k=int(vowels_spinbox.get())) \
                                        + random.choices(constn, k=(9 - int(vowels_spinbox.get())))
        random.shuffle(select_letters)

    show_letters(select_letters)


def manual_go():

    tru_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    manual_letters = manual_entry_box.get().upper()
    select_letters = []

    for letter in manual_letters:
        if letter not in tru_alphabet:
            continue
        if len(select_letters) == 9:
                break
        else:
            select_letters.append(letter)

    show_letters(select_letters)


def show_letters(select_letters):

    letters_box_Canvas.delete('canvas_letters')

    x_coor = 32
    for letter in select_letters:
        x_coor += 32
        letters_box_Canvas.create_text(x_coor, 18, text=letter, fill='white',
                                       font=('ariel', 18), tags='canvas_letters')

    text_box.delete(1.0, tkinter.END)

    if timer_state.get() == 1:
        user_entry(select_letters)
    else:
        output(select_letters)


def user_entry(select_letters):

    def user_word_button():
        user_word = []
        for letter in user_entry_box.get():
            user_word.append(letter.upper())
        user_word_result(user_word)

    user_entry_pop = tkinter.Tk()
    user_entry_pop.title('Entry')
    user_entry_pop.geometry('+1050+500')

    timer_canvas = tkinter.Canvas(user_entry_pop, width=150, height=150)
    timer_canvas.grid(row=1, column=0, sticky='news')

    timer_canvas.create_oval(10, 10, 142, 142, width=4, outline='white')

    for seconds in range(int(timer_spinbox.get()), -1, -1):
        timer_canvas.create_text(76, 76, text=(str(seconds)), font=('ariel', 72), fill='blue', tags='timer')
        timer_canvas.after(1000, timer_canvas.update(), timer_canvas.delete('timer'))

    timer_canvas.destroy()

    user_entry_pop_frame = tkinter.LabelFrame(user_entry_pop, text=' Entry ')
    user_entry_pop_frame.grid(row=0, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

    user_entry_box = tkinter.Entry(user_entry_pop_frame, width=12)
    user_entry_box.grid(row=0, column=0, sticky='ews', padx=10, pady=5)

    user_entry_button = tkinter.Button(user_entry_pop_frame, text='Enter', width=7, command=user_word_button)
    user_entry_button.grid(row=0, column=1, sticky='e', padx=10, pady=5)

    def user_word_result(user_word):

        invalid_word = True

        if not all([letter in select_letters for letter in user_word]):
            tkinter.Label(user_entry_pop, text=' Invalid Entry!\n not in letters')\
                   .grid(row=1, column=0, columnspan=2, pady=5, sticky='news')
            pass
        else:
            letters_checklist = list(select_letters)
            for letter in user_word:
                if letter in letters_checklist:
                    letters_checklist.remove(letter)
                else:
                    tkinter.Label(user_entry_pop, text=' Invalid Entry!\n not in letters')\
                           .grid(row=1, column=0, columnspan=2, pady=5, sticky='news')
                    invalid_word = False
                    break

            if not invalid_word:
                pass
            else:
                with open('alpha_words_upper.dat', 'rb') as word_tuple:
                    words = pickle.load(word_tuple)

                    if str(''.join(user_word)) in words:
                        score = len(user_word)
                        tkinter.Label(user_entry_pop, text=f' Dictionary Match!\n {score} points')\
                               .grid(row=1, column=0, columnspan=2, pady=5, sticky='news')
                    else:
                        tkinter.Label(user_entry_pop, text=f' No Dictionary Match!\n 0 points ')\
                               .grid(row=1, column=0, columnspan=2, pady=5, sticky='news')

        stop_button = tkinter.Button(user_entry_pop, width=9, text='Stop', command=user_entry_pop.destroy)
        stop_button.grid(row=2, column=0, padx=5, pady=5)

        show_button = tkinter.Button(user_entry_pop, width=9, text='Show', command=lambda: output(select_letters))
        show_button.grid(row=2, column=1, padx=5, pady=5)


def output(select_letters):

    with open('alpha_words_upper.dat', 'rb') as words_tuple, open('text_box.dat', 'w') as text_out:
        words = pickle.load(words_tuple)

        match_words_dic = {3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

        for word in words:

            if not all([letter in select_letters for letter in word]):
                continue

            duplicate_check = True
            letters_pool = list(select_letters)

            for letter in word:
                if letter in letters_pool:
                    letters_pool.remove(letter)
                else:
                    duplicate_check = False
                    break

            if duplicate_check:
                match_words_dic[len(word)].append(word)

        print('', file=text_out)
        print(*select_letters, sep='  ', file=text_out)
        print('', file=text_out)

        for letter_count in range(3, 10):
            if match_words_dic[letter_count]:

                if len(match_words_dic[letter_count]) == 1:
                    print(f'there is [1] {num2words(letter_count)}-letter-word:', file=text_out)
                    print('-' * 34, file=text_out)
                else:
                    print(f'there are [{len(match_words_dic[letter_count])}]'
                          f' {num2words(letter_count)}-letter-words:', file=text_out)
                    print('-' * 34, file=text_out)

                for letter_count_print in range(0, len(match_words_dic[letter_count]), 6):
                    print(*match_words_dic[letter_count][letter_count_print: letter_count_print + 6],
                          sep='  ', file=text_out)

                print('\n', file=text_out)

    with open('text_box.dat', 'r') as text_out:

        text_box.insert(tkinter.INSERT, text_out.read())


# Tkinter Grid GUI --------------------------------------------------------------------

# logo
top_logo_frame = tkinter.LabelFrame(root, text='Countdown')
top_logo_frame.grid(row=0, column=0, sticky='news', padx=5, pady=5)

top_logo = tkinter.PhotoImage(file='Countdown_logo.gif')

top_label = tkinter.Label(top_logo_frame, image=top_logo, width=321, height=176)
top_label.grid(row=0, column=0)

# options frame
options_frame = tkinter.LabelFrame(root, text=' Options ')
options_frame.grid(row=0, column=1, sticky='news', padx=5, pady=5)

# timer frame in options frame
timer_state = tkinter.IntVar()
timer_state.set(1)
timer_spinbox_value = tkinter.StringVar()
timer_spinbox_value.set('30')

options_frame_timer_frame = tkinter.LabelFrame(options_frame, text=' Delay & Input ')
options_frame_timer_frame.grid(row=0, column=0, padx=15, pady=10, sticky='w')

timer_radio_button_on = tkinter.Radiobutton(options_frame_timer_frame, variable=timer_state, value=1)
timer_radio_button_on.grid(row=0, column=0, sticky='w')

timer_spinbox = tkinter.Spinbox(options_frame_timer_frame, width=3, from_=1, to=60,
                                state='readonly', textvariable=timer_spinbox_value)
timer_spinbox.grid(row=0, column=1, sticky='w')

tkinter.Label(options_frame_timer_frame, text=' Sec ').grid(row=0, column=2, sticky='w')

timer_radio_button_off = tkinter.Radiobutton(options_frame_timer_frame, text='  Off',
                                             variable=timer_state, value=0)
timer_radio_button_off.grid(row=1, column=0, columnspan=2, sticky='w')

# manual entry in options frame
options_frame_manual_entry_frame = tkinter.LabelFrame(options_frame, text=' Manual Entry ')
options_frame_manual_entry_frame.grid(row=0, column=1, columnspan=2, sticky='news', padx=10, pady=10)

tkinter.Label(options_frame_manual_entry_frame, text='9 Letters or Less').grid(row=0, column=0, sticky='w', padx=9)

manual_entry_box = tkinter.Entry(options_frame_manual_entry_frame, width=14)
manual_entry_box.grid(row=1, column=0, sticky='w', padx=10)

manual_entry_button = tkinter.Button(options_frame_manual_entry_frame, text='Go!', width=4, command=manual_go)
manual_entry_button.grid(row=0, column=1, rowspan=2, sticky='es', padx=10)

# random frame in options frame
random_value = tkinter.IntVar()
random_value.set(0)

options_frame_random_frame = tkinter.LabelFrame(options_frame, text=' Random ')
options_frame_random_frame.grid(row=1, column=0, columnspan=2, padx=15, sticky='news')

random_on_option = tkinter.Radiobutton(options_frame_random_frame, text='All Random',
                                       variable=random_value, value=0)
random_on_option.grid(row=0, column=0, columnspan=2, padx=5, sticky='w')

random_force_vowels = tkinter.Radiobutton(options_frame_random_frame, text='Force',
                                          variable=random_value, value=1)
random_force_vowels.grid(row=1, column=0, padx=5, sticky='w')

vowels_spinbox = tkinter.Spinbox(options_frame_random_frame, width=2, from_=0, to=9, state='readonly')
vowels_spinbox.grid(row=1, column=1, sticky='w')

tkinter.Label(options_frame_random_frame, text='Vowels').grid(row=1, column=2, padx=3, sticky='w')

random_button = tkinter.Button(options_frame_random_frame, text='Go!', width=4, command=random_go)
random_button.grid(row=0, column=3, rowspan=2, sticky='e', padx=10, pady=5)

# quit button in options frame
quit_button = tkinter.Button(options_frame, text='Quit', width=5, command=root.destroy)
quit_button.grid(row=1, column=2, sticky='ws', padx=8, pady=10)

# selected letters frame
letters_box_Frame = tkinter.LabelFrame(root, text=' Selected Letters ', padx=10, pady=10)
letters_box_Frame.grid(row=3, column=0, columnspan=2)

letters_box_Canvas = tkinter.Canvas(letters_box_Frame, background='blue', height=30)
letters_box_Canvas.grid(row=0, column=0, sticky='news')

# output box
main_box = tkinter.Frame(root, relief='raised', borderwidth=2)
main_box.grid(row=5, column=0, columnspan=2, sticky='news', pady=5)

text_box = tkinter.Text(main_box, relief='sunken', borderwidth=2)
text_box.grid(row=0, column=0, sticky='news')

scrollbar = tkinter.Scrollbar(main_box, orient=tkinter.VERTICAL, command=text_box.yview)
scrollbar.grid(row=0, column=1, sticky='news')
text_box['yscrollcommand'] = scrollbar.set

main_box.grid_columnconfigure(0, weight=1)
main_box.grid_columnconfigure(1, weight=0)
main_box.grid_rowconfigure(0, weight=1)


tkinter.Label(root, text='Countdown Letters | v0.6pre-a | 2019').grid(row=6, column=0, columnspan=2, sticky='s')

root.mainloop()
