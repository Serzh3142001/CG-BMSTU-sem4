from tkinter import Tk, Button, Label, Entry, END, Listbox, Canvas, Radiobutton, LEFT, RIGHT, IntVar, PhotoImage, \
    Spinbox, ttk
from tkinter import messagebox
from math import sqrt, acos, degrees, pi, sin, cos, radians, floor, fabs
import copy
from tkinter.constants import Y
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange

from time import time, sleep

# import colorutils as cu

WIN_WIDTH = 1500
WIN_HEIGHT = 900
WIN_COLOR = "#bf80ff"

CV_WIDE = 900
CV_HEIGHT = 900
CV_COLOR = "#ffffff"  # f3e6ff" #"#cce6ff"
MAIN_TEXT_COLOR = "#b566ff"  # "lightblue" a94dff
TEXT_COLOR = "#ce99ff"

TEMP_SIDE_COLOR_CHECK = (255, 0, 255)  # purple
TEMP_SIDE_COLOR = "#ff00ff"

BOX_COLOR = "#dab3ff"

COLOR_LINE = "#000002"  # (0, 0, 0) # black
COLOR_LINE_CHECK = (0, 0, 2)

FILL_COLOR = "#ff6e41"
story = []

# Define

X_DOT = 0
Y_DOT = 1
Z_DOT = 2

FROM = 0
TO = 1
STEP = 2

FROM_SPIN_BOX = -1000.0
TO_SPIN_BOX = 1000.0
STEP_SPIN_BOX = 0.1

DEFAULT_SCALE = 45
DEFAULT_ANGLE = 20

# For spins
trans_matrix = []


def back():
    global LINEFLAG, CUTTERFLAG, redrawCommands
    if not len(story):
        return


    command = story[-1]
    commands = []
    if ';' in command:
        commands = command.split(';')
    else:
        commands.append(command)

    for com in commands:
        if not com:
            continue
        print(com)
        eval(com)

    del story[-1]

def set_trans_matrix():
    global trans_matrix

    trans_matrix.clear()

    for i in range(4):
        tmp_arr = []

        for j in range(4):
            tmp_arr.append(int(i == j))

        trans_matrix.append(tmp_arr)


def check_option(option):
    messagebox.showinfo("Выбран", "Выбрана опция %d" % (option))


def clear_canvas():
    canvas_win.delete("all")


def get_fill_check_color(collor_fill):
    return (int(collor_fill[1:3], 16), int(collor_fill[3:5], 16), int(collor_fill[5:7], 16))


def reboot_prog():
    canvas_win.delete("all")
    canvas_win.create_line([3, 3], [902, 3], [902, 902], [3, 902], [3, 3], fill='black',
                           width=1, dash=(5, 9))


def parse_color(num_color):
    color = "orange"

    if (num_color == 1):
        color = "#ff6e41"  # "orange"
    elif (num_color == 2):
        color = "#ff0000"  # "red"
    elif (num_color == 3):
        color = "#0055ff"  # "blue"
    elif (num_color == 4):
        color = "#008000"  # "green"

    return color


def parse_funcs(func_num):
    func = lambda x, z: sin(x) * cos(z)

    if (func_num == 1):
        return eval(f'lambda x, z: {entt.get()}')
        # func = lambda x, z: sin(x) * sin(z)
    elif (func_num == 2):
        func = lambda x, z: sin(x) * sin(z)
    elif (func_num == 3):
        func = lambda x, z: cos(x) * z / 3
    elif (func_num == 4):
        func = lambda x, z: cos(x) * cos(sin(z))

    return func


def read_limits():
    try:
        x_from = float(x_from_entry.get())
        x_to = float(x_to_entry.get())
        x_step = float(x_step_entry.get())

        x_limits = [x_from, x_to, x_step]

        z_from = float(z_from_entry.get())
        z_to = float(z_to_entry.get())
        z_step = float(z_step_entry.get())

        z_limits = [z_from, z_to, z_step]

        return x_limits, z_limits
    except:
        return -1, -1


def rotate_matrix(matrix):
    global trans_matrix

    res_matrix = [[0 for i in range(4)] for j in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                res_matrix[i][j] += trans_matrix[i][k] * matrix[k][j]

    trans_matrix = res_matrix


def spin_x(angle=None):
    if not angle:
        try:
            angle = -float(x_spin_entry.get()) / 180 * pi
        except:
            messagebox.showerror("Ошибка", "Угол - число")
            return

        story.append(f'spin_x({-angle})')
    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    # story.append()
    rotating_matrix = [[1, 0, 0, 0],
                       [0, cos(angle), sin(angle), 0],
                       [0, -sin(angle), cos(angle), 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    # build_graph()
    scale_graph()


def spin_y(angle=None):
    if not angle:
        try:
            angle = float(y_spin_entry.get()) / 180 * pi
        except:
            messagebox.showerror("Ошибка", "Угол - число")
            return
        story.append(f'spin_y({-angle})')
    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    rotating_matrix = [[cos(angle), 0, -sin(angle), 0],
                       [0, 1, 0, 0],
                       [sin(angle), 0, cos(angle), 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    # build_graph()
    scale_graph()

def spin_z(angle=None):
    if not angle:
        try:
            angle = float(z_spin_entry.get()) / 180 * pi
        except:
            messagebox.showerror("Ошибка", "Угол - число")
            return
        story.append(f'spin_z({-angle})')
    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    rotating_matrix = [[cos(angle), sin(angle), 0, 0],
                       [-sin(angle), cos(angle), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    # build_graph()
    scale_graph()

PREVSC = 0
def scale_graph(scale_param=None):
    global PREVSC
    if not scale_param:
        try:
            if float(scale_entry.get()) < 1:
                scale_param = 45*(float(scale_entry.get()))
            else:
                scale_param = 45*(float(scale_entry.get()))
        except:
            messagebox.showerror("Ошибка", "Коэффициент масштабирования должен быть числом")
            return
        # story.append(f'scale_graph({PREVSC})')
    # else:
        PREVSC = scale_param

    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    build_graph(scale_param=scale_param)


def trans_dot(dot, scale_param):
    dot.append(1)

    # print(dot)

    res_dot = [0, 0, 0, 0]

    for i in range(4):
        for j in range(4):
            res_dot[i] += dot[j] * trans_matrix[j][i]

    # print(res_dot)

    for i in range(3):
        res_dot[i] *= scale_param

    res_dot[0] += CV_WIDE // 2
    res_dot[1] += CV_HEIGHT // 2

    return res_dot[:3]


def is_visible(dot):
    return (0 <= dot[X_DOT] <= CV_WIDE) and \
           (0 <= dot[Y_DOT] <= CV_HEIGHT)


def draw_pixel(x, y):
    color = parse_color(colors[set10.get()])

    canvas_win.create_line(x, y, x + 1, y + 1, fill=color)


def draw_dot(x, y, high_horizon, low_horizon):
    if not is_visible([x, y]):
        return False

    # print(x, y)

    if y > high_horizon[int(x)]:
        high_horizon[int(x)] = y
        draw_pixel(x, y)
        return 5
    elif y < low_horizon[int(x)]:
        low_horizon[int(x)] = y
        draw_pixel(x, y)
        return 5
    # else:
    #     return False

    return True


def draw_horizon_part(dot1, dot2, high_horizon, low_horizon):
    if (dot1[X_DOT] > dot2[X_DOT]):
        dot1, dot2 = dot2, dot1

    # print(dot1, dot2)

    dx = dot2[X_DOT] - dot1[X_DOT]
    dy = dot2[Y_DOT] - dot1[Y_DOT]

    if (dx > dy):
        l = dx*3
    else:
        l = dy*3

    dx /= l
    dy /= l

    x = dot1[X_DOT]
    y = dot1[Y_DOT]

    for _ in range(int(l) + 1):
        if not draw_dot(round(x), y, high_horizon, low_horizon):
            return

        x += dx
        y += dy


def draw_horizon(function, high_horizon, low_horizon, limits, z, scale_param):
    f = lambda x: function(x, z)

    prev = None

    for x in arange(limits[FROM], limits[TO] + limits[STEP], limits[STEP]):
        cur = trans_dot([x, f(x), z], scale_param)

        if (prev):
            draw_horizon_part(prev, cur, high_horizon, low_horizon)

        prev = cur


def draw_horizon_limits(f, x_limits, z_limits, scale_param, hi, lo):
    color = parse_color(colors[set10.get()])

    for z in arange(z_limits[FROM], z_limits[TO] + z_limits[STEP], z_limits[STEP]):
        dot1 = trans_dot([x_limits[FROM], f(x_limits[FROM], z), z], scale_param)
        dot2 = trans_dot([x_limits[FROM], f(x_limits[FROM], z + x_limits[STEP]), z + x_limits[STEP]], scale_param)
        # if draw_dot(dot1[X_DOT], dot1[Y_DOT], hi, lo) == 1:
        canvas_win.create_line(dot1[X_DOT], dot1[Y_DOT], dot2[X_DOT], dot2[Y_DOT], fill=color)

        dot1 = trans_dot([x_limits[TO], f(x_limits[TO], z), z], scale_param)
        dot2 = trans_dot([x_limits[TO], f(x_limits[TO], z + x_limits[STEP]), z + x_limits[STEP]], scale_param)
        # if draw_dot(dot1[X_DOT], dot1[Y_DOT], hi, lo) == 1:
        canvas_win.create_line(dot1[X_DOT], dot1[Y_DOT], dot2[X_DOT], dot2[Y_DOT], fill=color)

    canvas_win.create_line([3, 3], [902, 3], [902, 902], [3, 902], [3, 3], fill='black',
                           width=1, dash=(5, 9))


def build_graph(new_graph=False, scale_param=DEFAULT_SCALE):
    global PREVSC

    reboot_prog()
    try:
        if float(scale_entry.get()) < 1:
            sc = 45 * (float(scale_entry.get()))
        else:
            sc = 45 * (float(scale_entry.get()))
    except:
        messagebox.showerror("Ошибка", "Коэффициент масштабирования должен быть числом")
        return
    PREVSC = sc


    if (new_graph):
        set_trans_matrix()

    f = parse_funcs(option_function.get())

    x_limits, z_limits = read_limits()

    print(x_limits, z_limits)

    high_horizon = [0 for i in range(CV_WIDE + 1)]
    low_horizon = [CV_HEIGHT for i in range(CV_WIDE + 1)]

    #  Горизонт
    for z in arange(z_limits[FROM], z_limits[TO] + z_limits[STEP], z_limits[STEP]):
        draw_horizon(f, high_horizon, low_horizon, x_limits, z, scale_param)

    # Границы горизонта
    draw_horizon_limits(f, x_limits, z_limits, scale_param, high_horizon, low_horizon)


if __name__ == "__main__":
    '''
        Основной графический модуль
    '''

    win = Tk()
    # win['bg'] = WIN_COLOR
    win.geometry("%dx%d" % (960, 1130))
    win.title("figure")
    win.resizable(False, False)

    canvas_win = Canvas(win, width=CV_WIDE, height=CV_HEIGHT, bg=CV_COLOR)
    # canvas_win2 = Canvas(win, width=CV_WIDE + 8, height=CV_HEIGHT + 8, bg=CV_COLOR)
    # canvas_win2.place(x=26, y=196)
    canvas_win.place(x=30, y=200)
    # canvas_win.create_line([3, 3], [900, 3], [899, 899], [3, 899], [3, 3], fill='black',
    #               width=1, dash=(5, 9))
    canvas_win.create_line([3, 3], [902, 3], [902, 902], [3, 902], [3, 3], fill='black',
                           width=1, dash=(5, 9))

    # Set function

    # back_box = Label(text="", font="-family {Consolas} -size 16", width=43, height=8, bg=BOX_COLOR)
    # back_box.place(x=CV_WIDE + 20, y=10)

    add_dot_text = Label(win, text="Функция", width=10, font="-family {Consolas} -size 16", fg='blue')
    add_dot_text.place(x=30, y=10)

    option_function = IntVar()
    option_function.set(2)

    entt = Entry(font="-family {Consolas} -size 14", width = 15)
    entt.delete(0, END)
    entt.insert(0, "x**2 + z")
    # entt.place(x=20, y=40)

    graph1_option = Radiobutton(variable=option_function, value=1)
    graph1_option.place(x=20, y=40)
    entt.place(x=48, y=38)

    graph2_option = Radiobutton(text="sin(x) * sin(z)", font="-family {Consolas} -size 14",
                                variable=option_function, value=2)
    graph2_option.place(x=20, y=70)

    graph3_option = Radiobutton(text="cos(x) * z / 3", font="-family {Consolas} -size 14", variable=option_function,
                                value=3)
    graph3_option.place(x=20, y=100)

    graph4_option = Radiobutton(text="cos(x) * cos(sin(z))", font="-family {Consolas} -size 14",
                                variable=option_function, value=4)
    graph4_option.place(x=20, y=130)

    # Set limits for function

    # back_box = Label(text="", font="-family {Consolas} -size 16", width=10, height=5)
    # back_box.place(x=CV_WIDE + 20, y=225)

    dx1 = -10
    figure_add_dot_text = Label(win, text="Пределы", width=10, font="-family {Consolas} -size 16", fg='blue')
    figure_add_dot_text.place(x=255, y=10)

    # Axis OX

    x_limit_text = Label(text="Ось X:", font="-family {Consolas} -size 14")
    x_limit_text.place(x=245+dx1, y=63)

    x_from_text = Label(text="от: ", font="-family {Consolas} -size 14")
    x_from_text.place(x=300+dx1, y=40)
    # x_from_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                        increment=STEP_SPIN_BOX, width=6)
    x_from_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    x_from_entry.place(x=300+dx1, y=60)

    x_to_text = Label(text="до: ", font="-family {Consolas} -size 14")
    x_to_text.place(x=350+dx1, y=40)
    # x_to_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                      increment=STEP_SPIN_BOX, width=6)
    x_to_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    x_to_entry.place(x=350+dx1, y=60)

    x_step_text = Label(text="шаг: ", font="-family {Consolas} -size 14")
    x_step_text.place(x=400+dx1, y=40)
    # x_step_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                        increment=STEP_SPIN_BOX, width=6)
    x_step_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    x_step_entry.place(x=400+dx1, y=60)

    # Insert
    x_from_entry.delete(0, END)
    x_from_entry.insert(0, "-10")
    x_to_entry.delete(0, END)
    x_to_entry.insert(0, "10")
    x_step_entry.delete(0, END)
    x_step_entry.insert(0, "0.4")

    # Axis OZ
    z_limit_text = Label(text="Ось Z:", font="-family {Consolas} -size 14")
    z_limit_text.place(x=245+dx1, y=93)

    # z_from_text = Label(text="от: ", font="-family {Consolas} -size 14")
    # z_from_text.place(x=CV_WIDE + 150, y=315)
    # z_from_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                        increment=STEP_SPIN_BOX, width=6)
    z_from_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    z_from_entry.place(x=300+dx1, y=90)

    # z_to_text = Label(text="до: ", font="-family {Consolas} -size 14")
    # z_to_text.place(x=CV_WIDE + 295, y=315)
    # z_to_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                      increment=STEP_SPIN_BOX, width=6)
    z_to_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    z_to_entry.place(x=350+dx1, y=90)

    # z_step_text = Label(text="шаг: ", font="-family {Consolas} -size 14")
    # z_step_text.place(x=CV_WIDE + 430, y=315)
    # z_step_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                        increment=STEP_SPIN_BOX, width=6)
    z_step_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    z_step_entry.place(x=400+dx1, y=90)

    # Insert
    z_from_entry.delete(0, END)
    z_from_entry.insert(0, "-10")
    z_to_entry.delete(0, END)
    z_to_entry.insert(0, "10")
    z_step_entry.delete(0, END)
    z_step_entry.insert(0, "0.4")

    # Set spin

    # back_box = Label(text="", font="-family {Consolas} -size 16", width=10, height=7, bg=BOX_COLOR)
    # back_box.place(x=CV_WIDE + 20, y=380)

    dx1 = 65
    figure_add_dot_text = Label(win, text="Вращение", width=10, font="-family {Consolas} -size 16", fg='blue')
    figure_add_dot_text.place(x=450+dx1, y=10)

    # Spin OX
    dy1 = -20
    x_spin_text = Label(text="OX: ", font="-family {Consolas} -size 14")
    x_spin_text.place(x=440+dx1, y=63+dy1)

    # x_spin_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                        increment=STEP_SPIN_BOX, width=6)
    x_spin_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    x_spin_entry.place(x=480+dx1, y=60+dy1)

    x_spin_btn = Button(win, text='↻', fg='green', width=2, height=1, font="-family {Consolas} -size 14",
                        command=lambda: spin_x())
    x_spin_btn.place(x=535+dx1, y=65+dy1)

    # Insert
    x_spin_entry.delete(0, END)
    x_spin_entry.insert(0, str(DEFAULT_ANGLE))

    # Spin OY

    y_spin_text = Label(text="OY: ", font="-family {Consolas} -size 14")
    y_spin_text.place(x=440+dx1, y=93+dy1)

    # y_spin_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                        increment=STEP_SPIN_BOX, width=6)
    y_spin_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    y_spin_entry.place(x=480+dx1, y=90+dy1)

    y_spin_btn = Button(win, text='↻', fg='green', width=2, height=1, font="-family {Consolas} -size 14",
                        command=lambda: spin_y())
    y_spin_btn.place(x=535+dx1, y=96+dy1)

    # Insert
    y_spin_entry.delete(0, END)
    y_spin_entry.insert(0, str(DEFAULT_ANGLE-10))

    # Spin OZ

    z_spin_text = Label(text="OZ: ", font="-family {Consolas} -size 14")
    z_spin_text.place(x=440+dx1, y=123+dy1)

    # z_spin_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                        increment=STEP_SPIN_BOX, width=6)
    z_spin_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    z_spin_entry.place(x=480+dx1, y=120+dy1)

    z_spin_btn = Button(win, text='↻', fg='green', width=2, height=1, font="-family {Consolas} -size 14",
                        command=lambda: spin_z())
    z_spin_btn.place(x=535+dx1, y=126+dy1)

    # Insert
    z_spin_entry.delete(0, END)
    z_spin_entry.insert(0, str(DEFAULT_ANGLE-10))
    win.bind("<Command-z>", lambda event: back())
    # Set scale

    # back_box = Label(text="", font="-family {Consolas} -size 16", width=43, height=5)
    # back_box.place(x=CV_WIDE + 20, y=570)

    figure_add_dot_text = Label(win, text="Масштабирование", width=15, font="-family {Consolas} -size 16", fg='blue')
    figure_add_dot_text.place(x=750, y=10)

    # Scale k

    scale_text = Label(text="Коэффициент k: ", font="-family {Consolas} -size 14")
    scale_text.place(x=730, y=43)

    # scale_entry = Spinbox(font="-family {Consolas} -size 14", from_=FROM_SPIN_BOX, to=TO_SPIN_BOX,
    #                       increment=STEP_SPIN_BOX, width=7)
    scale_entry = Entry(font="-family {Consolas} -size 14", width = 4)
    scale_entry.place(x=870, y=40)

    scale_btn = Button(win, text="Масштабировать", width=14, font="-family {Consolas} -size 14",
                       command=lambda: scale_graph(), fg='blue')
    scale_btn.place(x=750, y=80)

    # Insert
    scale_entry.delete(0, END)
    scale_entry.insert(0, 1.00)



    # back_box_filling = Label(text="", font="-family {Consolas} -size 16", width=43, height=4, bg=BOX_COLOR)
    # back_box_filling.place(x=CV_WIDE + 20, y=710)

    color_text = Label(win, text="Цвет: ", font="-family {Consolas} -size 16", fg='blue')
    color_text.place(x=20, y=160)
    # color_coords1 = (125, 844), (125, 862), (175, 862), (175, 844)
    colors = {"Оранжевый":1, "Красный":2, "Синий":3, "Зеленый":4}
    set10 = ttk.Combobox(win, state='readonly', values=["Оранжевый", "Красный", "Синий", "Зеленый"], width=10)
    set10.current(2)
    set10.place(x=75, y=160)
    # canvas_win.create_polygon(color_coords, width=2, fill='black', tag='color')

    # option_color_graph = IntVar()
    # option_color_graph.set(3)
    #
    # color_graph_orange = Radiobutton(text="Оранжевый", font="-family {Consolas} -size 14", variable=option_color_graph,
    #                                  value=1, bg=BOX_COLOR, activebackground=BOX_COLOR, highlightbackground=BOX_COLOR)
    # color_graph_orange.place(x=CV_WIDE + 25, y=750)
    #
    # color_graph_red = Radiobutton(text="Красный", font="-family {Consolas} -size 14", variable=option_color_graph,
    #                               value=2, bg=BOX_COLOR, activebackground=BOX_COLOR, highlightbackground=BOX_COLOR)
    # color_graph_red.place(x=CV_WIDE + 400, y=750)
    #
    # color_graph_blue = Radiobutton(text="Синий", font="-family {Consolas} -size 14", variable=option_color_graph,
    #                                value=3, bg=BOX_COLOR, activebackground=BOX_COLOR, highlightbackground=BOX_COLOR)
    # color_graph_blue.place(x=CV_WIDE + 25, y=780)
    #
    # color_graph_green = Radiobutton(text="Зеленый", font="-family {Consolas} -size 14", variable=option_color_graph,
    #                                 value=4, bg=BOX_COLOR, activebackground=BOX_COLOR, highlightbackground=BOX_COLOR)
    # color_graph_green.place(x=CV_WIDE + 400, y=780)

    cut_btn = Button(win, text="🎨Нарисовать", font="-family {Consolas} -size 14",
                     command=lambda: build_graph(new_graph=True), fg='red')
    cut_btn.place(x=250, y=160)

    clear_btn = Button(win, text="🗑заново", font="-family {Consolas} -size 14",
                       command=lambda: reboot_prog(), fg='orange')
    btn_back = Button(win, text='назад', fg='purple', command=lambda: back())
    btn_back.place(x=420, y=160)
    clear_btn.place(x=500, y=160)

    win.mainloop()
