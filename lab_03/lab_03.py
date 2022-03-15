from math import *
from tkinter import *
import tkinter.messagebox as box
from tkinter import messagebox
from tkinter import colorchooser
import matplotlib.pyplot as plt
# import seaborn as sns
from colorsys import *


# class Fox:
#     def __init__(self, coords):
#         self.coords = coords
#
#     def upd_coords(self, d1, d2):
#         for i in range(len(self.coords)):
#             self.coords[i] = [self.coords[i][0] + d1, self.coords[i][1] + d2]
#
#     def draw(self):
#         for elem in c.find_withtag('fox'):
#             c.delete(elem)
#         c.create_line(self.coords[:-7], width=2, activefill='lightgreen', tag='fox')
#         c.create_polygon(self.coords[-4:], width=2, activefill='lightgreen', tag='fox', fill='black')
#         c.create_polygon(self.coords[-7:-4], width=2, activefill='lightgreen', tag='fox', fill='black')
#
#     def rotate(self, alpha, center, st=1):
#         try:
#             alpha = radians(float(alpha))
#         except:
#             box.showinfo('Error', 'Некорректное значение угла поворота!')
#             return
#
#         try:
#             x, y = float(ent5.get()), float(ent7.get())
#         except:
#             box.showinfo('Error', 'Некорректные координаты!')
#             return
#
#         global rotate_point
#
#         reprint_dot([x, y], 2)
#         if st and [x, y] != rotate_point:
#             rot_coords.append([x, y] + [2])
#             if len(rot_coords) > 1:
#                 story.append(f'reprint_dot({rot_coords[-2][:-1]}, {rot_coords[-2][-1]});rot_coords.pop()')
#             else:
#                 story.append(f'del_with_tag("rot")' + ';rot_coords.pop()' if len(rot_coords) else '')
#
#         rotate_point = [x, y]
#
#         rotated_dots = []
#         for dot in self.coords:
#             rotated_dots.append(rotate(dot, alpha, net_to_canv(center)))
#
#         foxx = c.find_withtag('fox')
#         for elem in foxx:
#             c.delete(elem)
#
#         self.coords = rotated_dots
#         self.analyze_and_redraw()
#
#         if st:
#             story.append(f'fox.rotate({-degrees(alpha)}, {[ent5.get(), ent7.get()]}, 0)')
#
#         self.draw()
#
#     def resize(self, sign, k, k1, center, st=1):
#         try:
#             if sign == 1:
#                 k = float(k)
#                 k1 = float(k1)
#                 if abs(k * k1) < 1e-8:
#                     raise
#             else:
#                 k = 1 / float(k)
#                 k1 = 1 / float(k1)
#         except:
#             box.showinfo('Error', 'Некорректное значение процента масштабирования!')
#             return
#
#         try:
#             x, y = float(ent3.get()), float(ent6.get())
#         except:
#             box.showinfo('Error', 'Некорректные координаты!')
#             return
#
#         global resize_point, sz
#
#         reprint_dot([x, y], 1)
#         if st and [x, y] != resize_point:
#             res_coords.append([x, y] + [1])
#             if len(res_coords) > 1:
#                 story.append(f'reprint_dot({res_coords[-2][:-1]}, {res_coords[-2][-1]});res_coords.pop()')
#             else:
#                 story.append(f'del_with_tag("sz")' + ';res_coords.pop()' if len(res_coords) else '')
#
#         resize_point = [x, y]
#
#         resized_dots = []
#         for dot in self.coords:
#             resized_dots.append(resize(dot, [k, k1], net_to_canv(center)))
#
#         foxx = c.find_withtag('fox')
#         for elem in foxx:
#             c.delete(elem)
#
#         self.coords = resized_dots
#         self.analyze_and_redraw()
#
#         if st:
#             story.append(
#                 f'fox.resize({sign * (-1 if sign == -1 else 1)}, {1 / k}, {1 / k1}, '
#                 f'{[ent3.get(), ent6.get()]}, 0)')
#
#         self.draw()
#
#     def move(self, delta, dir, st=1):
#         global sz
#         try:
#             if type(delta) == list:
#                 delta[0] = float(delta[0]) / sz
#                 delta[1] = float(delta[1]) / sz
#             else:
#                 delta = float(delta) / sz
#         except:
#             box.showinfo('Error', 'Некорректное значение процента масштабирования!')
#             return
#
#         if st:
#             if type(delta) == list:
#                 story.append(f'fox.move({[-delta[0] * sz, -delta[1] * sz]}, "{dir}", 0)')
#             else:
#                 story.append(f'fox.move({-delta * sz}, "{dir}", 0)')
#
#         moved_dots = []
#         for dot in self.coords:
#             if dir == 'up':
#                 moved_dots.append([dot[0], dot[1] - delta])
#             elif dir == 'down':
#                 moved_dots.append([dot[0], dot[1] + delta])
#             elif dir == 'left':
#                 moved_dots.append([dot[0] - delta, dot[1]])
#             elif dir == 'right':
#                 moved_dots.append([dot[0] + delta, dot[1]])
#             elif dir == 'w':
#                 moved_dots.append([dot[0] + delta[0], dot[1] - delta[1]])
#
#         foxx = c.find_withtag('fox')
#         for elem in foxx:
#             c.delete(elem)
#
#         self.coords = moved_dots
#         self.analyze_and_redraw()
#         self.draw()
#
#     def analyze_and_redraw(self):
#         global sz
#         max_coord_x = 0
#         max_coord_y = 0
#
#         for dot in self.coords:
#             dot = canv_to_net(dot[0], dot[1])
#             if abs(dot[0]) > max_coord_x:
#                 max_coord_x = abs(dot[0])
#             if abs(dot[1]) > max_coord_y:
#                 max_coord_y = abs(dot[1])
#
#         try:
#             max_coord_x = max(max_coord_x, abs(float(ent3.get())), abs(float(ent5.get())))
#             max_coord_y = max(max_coord_y, abs(float(ent6.get())), abs(float(ent7.get())))
#         except:
#             box.showinfo('Error', 'Некорректные координаты!')
#
#         if (150 + dx) * sz <= max_coord_x <= (300 + dx) * sz and (150 + dy) * sz <= max_coord_y <= (300 + dy) * sz:
#             return
#
#         old = sz
#         scale(max_coord_x, max_coord_y)
#         new = sz
#         self.resize_dots(old / new, net_to_canv(0, 0))
#         reprint_dot([float(ent3.get()), float(ent6.get())], 1)
#         reprint_dot([float(ent5.get()), float(ent7.get())], 2)
#
#     def resize_dots(self, k, center):
#         resized_dots = []
#         for dot in self.coords:
#             resized_dots.append(resize(dot, [k, k], center))
#
#         self.coords = resized_dots

# class Dot:
#     def __init__(self, net=None, canv=None):
#         self.canv = canv
#         self.net = net
#         if not net and not canv:
#             raise
#         if not self.canv:
#             self.canv = self.net_to_canv(self.net)
#         if not self.net:
#             self.net = self.canv_to_net(self.canv)
#
#     def net_to_canv(self, x, y=None):
#         if y == None:
#             t = x[0]
#             y = x[1]
#             x = t
#         try:
#             x, y = float(x), float(y)
#         except:
#             box.showinfo('Error', 'Некорректные координаты!')
#
#         global sz, center
#
#         return [round(x / sz + center[0]), round(center[1] - y / sz)]
#
#     def canv_to_net(self, x, y=None):
#         if y == None:
#             t = x[0]
#             y = x[1]
#             x = t
#         try:
#             x, y = float(x), float(y)
#         except:
#             box.showinfo('Error', 'Некорректные координаты!')
#
#         global sz, center
#
#         return [(x - center[0]) * sz, (center[1] - y) * sz]


def my_round(x):
    if x > 0:
        return round(x)
    else:
        if fpart(x) >= 0.5:
            x += 0.5
            return round(x)
        else:
            x -= 0.5
            return round(x)

def net_to_canv(x, y=None, func=round):
    if y == None:
        t = x[0]
        y = x[1]
        x = t
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz, center

    return [func(x / sz + center[0]), func(center[1] - y / sz)]


def canv_to_net(x, y=None):
    if y == None:
        t = x[0]
        y = x[1]
        x = t
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz, center

    return [(x - center[0]) * sz, (center[1] - y) * sz]


window = Tk()

var = IntVar()
method = IntVar()
story = []
win_size = [700, 900]
c = Canvas(window, width=3840, height=2160, bg='white')

ent1 = Entry(width=3)
ent2 = Entry(width=3)
ent3 = Entry(width=3)
ent4 = Entry(width=3)
ent5 = Entry(width=3)
ent6 = Entry(width=3)
# ent7 = Entry(width=8)
ent8 = Entry(width=3)
ent9 = Entry(width=3)
# ent10 = Entry(width=2)
ent1.place(x=70, y=40)
ent2.place(x=70, y=70)
# ent3.place(x=320, y=80)
# ent4.place(x=570, y=40)
# ent5.place(x=570, y=80)
# ent6.place(x=320, y=110)
# ent7.place(x=570, y=110)
ent8.place(x=115, y=70)
ent9.place(x=115, y=40)
# ent10.place(x=104, y=97)
ent1.insert(0, 0)
ent2.insert(0, 200)
# ent3.insert(0, 0)
# ent4.insert(0, 5)
# ent5.insert(0, 0)
# ent6.insert(0, 0)
# ent7.insert(0, 0)
ent8.insert(0, 200)
ent9.insert(0, 0)
# ent10.insert(0, 15)

label1 = Label(text='Координаты отрезка:', font='Arial 15')
label1.place(x=60, y=5)
label2 = Label(text='Пучок отрезков:', font='Arial 15')
# label2.place(x=280, y=5)
label3 = Label(text='Центр:', font='Arial 15')
# label3.place(x=535, y=5)

label4 = Label(text='Начало:', font='Arial 15')
label5 = Label(text='Конец:', font='Arial 15')
label6 = Label(text='Цвет:', font='Arial 15')
label7 = Label(text='Радиус, шаг:', font='Arial 13')
# label8 = Label(text='X:', font='Arial 15')
# label9 = Label(text='Y:', font='Arial 15')
# label10 = Label(text='Относ.\nточки:', font='Arial 13')
label11 = Label(text='Способ:', font='Arial 15')
# label12 = Label(text='Относ.\nточки:', font='Arial 13')
# label13 = Label(text='раз', font='Arial 15')
label14 = Label(text='°', font='Arial 17')
# label15 = Label(text='◀ ▶ ▲ ▼', font='Arial 13', fg='orange')
# label16 = Label(text='⌘ ▲ ▼', font='Arial 13', fg='orange')
# label17 = Label(text='⌘[⇧]R', font='Arial 13', fg='orange')
label18 = Label(text='⌘Z', font='Arial 11', fg='orange')
label19 = Label(text='x:', font='Arial 11', fg='grey')
label20 = Label(text='y:', font='Arial 11', fg='grey')
label21 = Label(text='x:', font='Arial 11', fg='grey')
label22 = Label(text='y:', font='Arial 11', fg='grey')
label23 = Label(text='Цвет фона:', font='Arial 15')

label1.place(x=5, y=5)
# label2.place(x=280, y=5)
# label3.place(x=535, y=5)
label4.place(x=5, y=43)
label5.place(x=15, y=73)
label6.place(x=22, y=103)
# label7.place(x=295, y=112)
# label8.place(x=545, y=82)
# label9.place(x=545, y=112)
# label10.place(x=491, y=90)
label11.place(x=535, y=43)
# label12.place(x=241, y=90)
# label13.place(x=403, y=42)
# label14.place(x=653, y=42)
# label15.place(x=150, y=7)
# label16.place(x=425, y=7)
# label17.place(x=613, y=7)
label18.place(x=20, y=120)
label19.place(x=70, y=25)
label20.place(x=115, y=25)
label23.place(x=20, y=830)
# label21.place(x=70, y=50)
# label22.place(x=115, y=50)


btn_col_line = Button(window, text='v', fg='green', command=lambda: line_col_choose())
btn_col_bg = Button(window, text='v', fg='green', command=lambda: bg_col_choose())
btn_hist = Button(window, text='📊Гистограммы', fg='green', command=lambda: count_steps())
# btn_res_r = Button(window, text='▲', fg='green', command=lambda: fox.resize(1, ent2.get(), ent8.get(), [ent3.get(), ent6.get()]))
# btn_res_l = Button(window, text='▼', fg='green', command=lambda: fox.resize(-1, ent2.get(), ent8.get(), [ent3.get(), ent6.get()]))
# btn_mv = Button(window, text='move', fg='green', command=lambda: fox.move([ent1.get(), ent9.get()], 'w'))
# btn_mv_r = Button(window, text='▶', fg='green', command=lambda: fox.move(ent10.get(), 'right'))
# btn_mv_l = Button(window, text='◀', fg='green', command=lambda: fox.move(ent10.get(), 'left'))
# btn_mv_u = Button(window, text='▲', fg='green', command=lambda: fox.move(ent10.get(), 'up'))
# btn_mv_d = Button(window, text='▼', fg='green', command=lambda: fox.move(ent10.get(), 'down'))
btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
btn_draw = Button(window, text='Нарисовать отрез.', fg='blue', command=lambda: draw_line())
btn_draw_bunch = Button(window, text='Нарисовать пучок', fg='blue', command=lambda: draw_bunch())
btn_exit = Button(window, text=' выход ', fg='red', command=exit)

set0 = Radiobutton(text="➚", fg='black', variable=var, value=0)
set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)

set2 = Radiobutton(text="default", fg='black', variable=method, value=0)
set3 = Radiobutton(text="ЦДА", fg='black', variable=method, value=1)
set4 = Radiobutton(text="Брезенхейм (float)", fg='black', variable=method, value=2)
set5 = Radiobutton(text="Брезенхейм (int)", fg='black', variable=method, value=3)
set6 = Radiobutton(text="Брезенхейм (устр. ступен.)", fg='black', variable=method, value=4)
set7 = Radiobutton(text="ВУ", fg='black', variable=method, value=5)
set8 = Radiobutton(text="➚", fg='black', variable=var, value=2)

var.set(1)
method.set(0)
set0.place(x=157, y=42)
set1.place(x=157, y=72)

set2.place(x=220, y=42)
set3.place(x=220, y=65)
set4.place(x=220, y=88)
set5.place(x=220, y=111)
set6.place(x=220, y=134)
set7.place(x=220, y=157)

ents = '''ent1.place(x=70, y=40)
ent2.place(x=70, y=70)
ent3.place(x=525, y=40)
ent4.place(x=570, y=40)
ent5.place(x=525, y=70)
ent6.place(x=570, y=70)
ent8.place(x=115, y=70)
ent9.place(x=115, y=40)'''

lbls = '''label1.place(x=5, y=5)
label2.place(x=435, y=5)
label3.place(x=465, y=43)
label4.place(x=5, y=43)
label5.place(x=15, y=73)
label6.place(x=22, y=103)
label7.place(x=437, y=75)
label11.place(x=220, y=5)
label14.place(x=608, y=70)
label18.place(x=80, y=143)
label19.place(x=70, y=25)
label20.place(x=115, y=25)
label21.place(x=525, y=25)
label22.place(x=570, y=25)'''

# btns = '''btn_res_l.place(x=330, y=150)
# btn_res_r.place(x=360, y=150)
# btn_mv_r.place(x=128, y=100)
# btn_mv_l.place(x=85, y=100)
# btn_mv_u.place(x=106, y=75)
# btn_mv_d.place(x=106, y=125)
# btn_mv.place(x=165, y=43)
# btn_cl_all.place(x=25, y=170)
# btn_rot_r.place(x=620, y=150)
# btn_rot_l.place(x=590, y=150)
# btn_back.place(x=25, y=140)
# btn_exit.place(x=630, y=840)'''

btns = '''btn_col_line.place(x=135, y=103)
btn_back.place(x=25, y=140)
btn_hist.place(x=437, y=140)
btn_exit.place(x=630, y=840)
btn_draw.place(x=220, y=175)
btn_draw_bunch.place(x=437, y=105)'''

rbtns = '''set0.place(x=157, y=42)
set1.place(x=157, y=72)
set2.place(x=220, y=32)
set3.place(x=220, y=55)
set4.place(x=220, y=78)
set5.place(x=220, y=101)
set6.place(x=220, y=124)
set7.place(x=220, y=147)
set8.place(x=610, y=42)'''

TASK = '''
Реализовать различные алгоритмы построения одиночных отрезков. Отрезок задается координатой начала, координатой конца и цветом.

Сравнить визуальные характеристики отрезков, построенных разными алгоритмами, с помощью построения пучка отрезков, с заданным шагом.

Сравнение со стандартным алгоритмом. Задаются начальные и конечные координаты; рисуется отрезок разными методами. Отрисовка отрезка другим цветом и методом поверх первого, для проверки совпадения. Предоставить пользователю возможность выбора двух цветов – цвета фона и цвета рисования. Алгоритмы выбирать из выпадающего списка.

- ЦДА
- Брезенхем действительные числа
- Брезенхем целые числа
- Брезенхем с устранением ступенчатости
- ВУ

Построение гистограмм по количеству ступенек в зависимости от угла наклона.
'''
AUTHOR = '\n\nНиколаев Сергей ИУ7-44Б'
sz = 1
# resize_point = [0, 0]
# rotate_point = [0, 0]
# res_coords = []
# rot_coords = []
center = [365, 510]
dx = 0
dy = 0
color_coords = (87, 105), (87, 123), (137, 123), (137, 105)
resized_coords = [[87, 105], [87, 123], [137, 123], [137, 105]]
color = [(0.0, 0.0, 0.0), '#000000']

color_coords1 = (125, 844), (125, 862), (175, 862), (175, 844)
resized_coords1 = [[125, 844], [125, 862], [175, 862], [175, 844]]
color1 = [(254.9921875, 255.99609375, 255.99609375), '#feffff']

c.create_polygon(color_coords, width=2, fill='black', tag='color')
lines = []
bunches = []
old_dot = [0, 0]
old_angl = 0
cnt = -1


def rgb_to_hex(rgb):
    rgb = tuple(map(int, rgb))
    return '#%02x%02x%02x' % rgb


def draw_dot(x, y, colorr, tag, count_fl=False):
    global old_dot, old_angl, cnt

    if not count_fl:
        d = 1
        c.create_polygon([x, y], [x, y + d], [x + d, y + d], [x + d, y], fill=colorr, tag=tag)
    else:
        if x - old_dot[0]:
            new_angl = abs(y - old_dot[1])/abs(x - old_dot[0])
        else:
            new_angl = abs(x - old_dot[0]) / abs(y - old_dot[1])

        if new_angl != old_angl:
            cnt += 1

        old_angl = new_angl
        old_dot = [x, y]


def count_steps():
    global cnt, old_dot, old_angl
    # histt = []
    hist1 = []
    hist2 = []
    hist3 = []
    hist4 = []
    hist5 = []

    try:
        center = [float(ent3.get()), float(ent4.get())]
        radius = float(ent5.get())
        step = int(ent6.get())
    except:
        box.showinfo('Error', 'Некорректные координаты!')
        return

    colorr = color
    for met in range(1, 6):
        for alpha in range(0, 91, step):
            start = center
            stop = [start[0] + radius * sin(radians(alpha)), start[1] + radius * cos(radians(alpha))]
            draw_line(start, stop, colorr, met, True)
            for i in range(cnt//2):
                eval(f'hist{met}.append(alpha)')
            cnt = -1
            old_dot = [0, 0]
            old_angl = 0

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 3, 1)
    plt.hist(hist1, 90)
    # f'Угол, R={radius}, шаг={step}'
    plt.ylabel('Кол-во ступенек')
    plt.title('ЦДА')
    plt.subplot(2, 3, 2)
    plt.hist(hist2, 90)
    plt.title('Брезенхейм (float)')
    plt.subplot(2, 3, 3)
    plt.hist(hist3, 90)
    plt.title('Брезенхейм (int)')
    plt.subplot(2, 3, 4)
    plt.hist(hist4, 90)
    plt.xlabel('Угол')
    plt.title('Брезенхейм (устр. ступ)')
    plt.subplot(2, 3, 5)
    plt.hist(hist5, 90)
    plt.title('ВУ')

    plt.show()


def redraw_elems():
    del_with_tag('line')
    for line in lines:
        draw_line(line[0], line[1], line[2], line[3])
    for bunch in bunches:
        draw_bunch(bunch[0], bunch[1], bunch[2], bunch[3], bunch[4])


def draw_line(start=None, stop=None, colorr=None, met=None, count_fl=False):
    if not start:
        start, stop = [ent1.get(), ent9.get()], [ent2.get(), ent8.get()]
        met = method.get()
        colorr = color
        lines.append([start, stop, color, met])

    if max(abs(int(start[0])), abs(int(stop[0]))) > 300 + dx/2 or max(abs(int(start[1])), abs(int(stop[1]))) > 300 + dy/2:
        box.showinfo('Error', f'Выход за границы:\nx: ({-(300 + dx//2)}...{300 + dx//2})\ny: ({-(300 + dy//2)}...{300 + dy//2})')
        lines.pop()
        return

    if met == 0:
        standart_draw(start, stop, colorr[1])
    elif met == 1:
        dda_draw(start, stop, colorr[1], count_fl)
    elif met == 2:
        br_float_draw(start, stop, colorr[1], count_fl)
    elif met == 3:
        br_int_draw(start, stop, colorr[1], count_fl)
    elif met == 4:
        br_smooth_draw(start, stop, colorr, count_fl)
    elif met == 5:
        vu_draw(start, stop, colorr, count_fl)


def draw_bunch(center=None, colorr=None, met=None, radius=None, step=None):
    if not center:
        try:
            center = [float(ent3.get()), float(ent4.get())]
            radius = float(ent5.get())
            step = int(ent6.get())
        except:
            box.showinfo('Error', 'Некорректные координаты!')
            return

        met = method.get()
        colorr = color
        bunches.append([center, colorr, met, radius, step])

    max_stop = max(list(map(abs, center))) + radius
    if max(abs(int(center[0])), abs(int(max_stop))) > 300 + dx/2 or max(abs(int(center[1])), abs(int(max_stop))) > 300 + dy/2:
        box.showinfo('Error', f'Выход за границы:\nx: ({-(300 + dx//2)}...{300 + dx//2})\ny: ({-(300 + dy//2)}...{300 + dy//2})')
        bunches.pop()
        return

    for alpha in range(0, 360, step):
        start = center
        stop = [start[0] + radius * sin(radians(alpha)), start[1] + radius * cos(radians(alpha))]
        if met == 0:
            standart_draw(start, stop, colorr[1])
        elif met == 1:
            dda_draw(start, stop, colorr[1])
        elif met == 2:
            br_float_draw(start, stop, colorr[1])
        elif met == 3:
            br_int_draw(start, stop, colorr[1])
        elif met == 4:
            br_smooth_draw(start, stop, colorr)
        elif met == 5:
            vu_draw(start, stop, colorr)


def standart_draw(start, stop, colorr):
    c.create_line([net_to_canv(start), net_to_canv(stop)], width=1, fill=colorr, tag='line')


def dda_draw(start, stop, colorr, count_fl=False):
    x1, y1 = net_to_canv(start)
    x2, y2 = net_to_canv(stop)
    x = [0] * 1000
    y = [0] * 1000
    xstart = round(x1)
    ystart = round(y1)
    xend = round(x2)
    yend = round(y2)
    L = max(abs(xend - xstart), abs(yend - ystart))
    dX = (x2 - x1) / L
    dY = (y2 - y1) / L
    i = 0
    x[i] = x1
    y[i] = y1
    i += 1
    while i < L:
        x[i] = x[i - 1] + dX
        y[i] = y[i - 1] + dY
        i += 1
    x[i] = x2
    y[i] = y2

    i = 0
    while i <= L:
        draw_dot(round(x[i]), round(y[i]), colorr, 'line', count_fl)
        i += 1


# def br_float_draw(start, stop, colorr):
#     x0, y0 = list(map(int, net_to_canv(start)))
#     x1, y1 = list(map(int, net_to_canv(stop)))
#     deltax = abs(x1 - x0)
#     deltay = abs(y1 - y0)
#     error = 0
#     deltaerr = (deltay + 1) / (deltax + 1)
#     y = y0
#     x = x0
#     diry = y1 - y0
#     if diry > 0:
#         diry = 1
#     if diry < 0:
#         diry = -1
#
#     dirx = x1 - x0
#     if dirx > 0:
#         dirx = 1
#     if dirx < 0:
#         dirx = -1
#
#     if deltaerr <= 1:
#         for x in range(x0, x1):
#             draw_dot(round(x), round(y), colorr, 'line')
#             error += deltaerr
#             if error >= 1.0:
#                 y += diry
#                 error -= 1.0
#     else:
#         for y in range(y0, y1):
#             draw_dot(round(x), round(y), colorr, 'line')
#             error += deltaerr
#             if error >= 1.0:
#                 x += dirx
#                 error -= 1.0

def br_float_draw(start, stop, colorr, count_fl=False):
    # x1, y1 = list(map(int, start))
    # x2, y2 = list(map(int, stop))
    # dx = x2 - x1  # проекция на ось икс
    # dy = y2 - y1  # проекция на ось игрек
    #
    # sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    # # Определяем, в какую сторону нужно будет сдвигаться. Если dx < 0, т.е. отрезок идёт
    # # справа налево по иксу, то sign_x будет равен -1.
    # # Это будет использоваться в цикле постороения.
    #
    # sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    # # Аналогично. Если рисуем отрезок снизу вверх -
    # # это будет отрицательный сдвиг для y (иначе - положительный).
    #
    # # далее мы будем сравнивать: "if (dx < dy)"
    # # поэтому необходимо сделать dx = |dx|; dy = |dy|
    # dx = abs(dx)
    # dy = abs(dy)
    #
    # if dx > dy:  # определяем наклон отрезка:
    #     # Если dx > dy, то значит отрезок "вытянут" вдоль оси икс, т.е. он скорее длинный, чем высокий.
    #     # Значит в цикле нужно будет идти по икс (строчка el = dx), значит "протягивать" прямую по иксу
    #     # надо в соответствии с тем, слева направо или справа налево она идёт (pdx = sign_x), при этом
    #     # по y сдвиг такой отсутствует.
    #     pdx, pdy = sign_x, 0
    #     es, el = dy, dx
    # else:  # случай, когда прямая скорее "высокая", чем длинная, т.е. вытянута по оси y
    #     pdx, pdy = 0, sign_y
    #     es, el = dx, dy  # тогда в цикле будем двигаться по y
    #
    # x, y = x1, y1
    #
    # error, t = 0.0, 0
    # deltaerr = es/el
    #
    # draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line')  # ставим первую точку
    # # все последующие точки возможно надо сдвигать, поэтому первую ставим вне цикла
    #
    # while t < el:  # идём по всем точкам, начиная со второй и до последней
    #     error += deltaerr
    #     if error >= 1.0:
    #         error = 0.0
    #         x += sign_x  # сдвинуть прямую (сместить вверх или вниз, если цикл проходит по иксам)
    #         y += sign_y  # или сместить влево-вправо, если цикл проходит по y
    #     else:
    #         x += pdx  # продолжить тянуть прямую дальше, т.е. сдвинуть влево или вправо, если
    #         y += pdy  # цикл идёт по иксу; сдвинуть вверх или вниз, если по y
    #     t += 1
    #     draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line')

    x0, y0 = list(map(int, start))
    x1, y1 = list(map(int, stop))
    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    # tg = deltay/deltax
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = 0
    deltaerr = (dy + 1) / (dx + 1)
    y = y0
    x = x0
    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    if deltaerr <= 1:
        # if x1 < x0:
        #     x1, x0 = x0, x1
        #     diry *= -1
        for x in range(x0, x1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line', count_fl)
            error += deltaerr
            if error >= 1.0:
                y += diry
                error -= 1.0
    else:
        deltaerr = 1/deltaerr
        for y in range(y0, y1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line', count_fl)
            error += deltaerr
            if error >= 1.0:
                x += dirx
                error -= 1.0


# def br_int_draw(start, stop, colorr):
#     x1, y1 = list(map(int, start))
#     x2, y2 = list(map(int, stop))
#     dx = x2 - x1  # проекция на ось икс
#     dy = y2 - y1  # проекция на ось игрек
#
#     sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
#     # Определяем, в какую сторону нужно будет сдвигаться. Если dx < 0, т.е. отрезок идёт
#     # справа налево по иксу, то sign_x будет равен -1.
#     # Это будет использоваться в цикле постороения.
#
#     sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
#     # Аналогично. Если рисуем отрезок снизу вверх -
#     # это будет отрицательный сдвиг для y (иначе - положительный).
#
#     # далее мы будем сравнивать: "if (dx < dy)"
#     # поэтому необходимо сделать dx = |dx|; dy = |dy|
#     dx = abs(dx)
#     dy = abs(dy)
#
#     if dx > dy:  # определяем наклон отрезка:
#         # Если dx > dy, то значит отрезок "вытянут" вдоль оси икс, т.е. он скорее длинный, чем высокий.
#         # Значит в цикле нужно будет идти по икс (строчка el = dx), значит "протягивать" прямую по иксу
#         # надо в соответствии с тем, слева направо или справа налево она идёт (pdx = sign_x), при этом
#         # по y сдвиг такой отсутствует.
#         pdx, pdy = sign_x, 0
#         es, el = dy, dx
#     else:  # случай, когда прямая скорее "высокая", чем длинная, т.е. вытянута по оси y
#         pdx, pdy = 0, sign_y
#         es, el = dx, dy  # тогда в цикле будем двигаться по y
#
#     x, y = x1, y1
#
#     error, t = el/2, 0
#
#     draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line')  # ставим первую точку
#     # все последующие точки возможно надо сдвигать, поэтому первую ставим вне цикла
#
#     while t < el:  # идём по всем точкам, начиная со второй и до последней
#         error -= es
#         if error < 0:
#             error += el
#             x += sign_x  # сдвинуть прямую (сместить вверх или вниз, если цикл проходит по иксам)
#             y += sign_y  # или сместить влево-вправо, если цикл проходит по y
#         else:
#             x += pdx  # продолжить тянуть прямую дальше, т.е. сдвинуть влево или вправо, если
#             y += pdy  # цикл идёт по иксу; сдвинуть вверх или вниз, если по y
#         t += 1
#         draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line')

def br_int_draw(start, stop, colorr, count_fl=False):
    x0, y0 = list(map(int, start))
    x1, y1 = list(map(int, stop))
    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = 0
    deltaerr = (dy + 1)
    deltaerr1 = (dx + 1)
    y = y0
    x = x0
    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    if dx >= dy:
        for x in range(x0, x1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line', count_fl)
            error += deltaerr
            if error >= dx + 1:
                y += diry
                error -= (dx + 1)
    else:
        for y in range(y0, y1):
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), colorr, 'line', count_fl)
            error += deltaerr1
            if error >= dy + 1:
                x += dirx
                error -= (dy + 1)


def change_brightness(col, k):
    col = col[0]
    # print(col)
    col = list(col)
    # col1 = list(rgb_to_hsv(col[0][0], col[0][1], col[0][2]))
    # col1[1] *= k
    # col1[2] += (256 - col1[2]) * k
    # col_rgb1 = tuple(map(int, hsv_to_rgb(col1[0], col1[1], col1[2])))
    for i in range(3):
        col[i] += (255-col[i])*(1-k)

    return rgb_to_hex(col)

def br_smooth_draw(start, stop, colorr, count_fl=False):
    x0, y0 = list(map(round, (list(map(float, start)))))
    x1, y1 = list(map(round, list(map(float, stop))))
    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = 0
    I = 1
    dxx = abs(x1 - x0 + 1)
    dyy = abs(y1 - y0 + 1)
    m = min(dxx, dyy)/max(dxx, dyy)  # max?
    if not x1-x0 or not y1-y0:
        m = 1
    w = I - m
    e = 1 / 2
    y = y0
    x = x0
    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), change_brightness(colorr, m / 2), 'line', count_fl)
    if dx >= dy:
        while x < x1:
            if e < w:
                x += 1
                e += m
            else:
                x += 1
                y += diry
                e -= w
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), change_brightness(colorr, e), 'line', count_fl)
    else:
        while y < y1:
            if e < w:
                y += 1
                e += m
            else:
                y += 1
                x += dirx
                e -= w
            draw_dot(round(net_to_canv(x, y)[0]), round(net_to_canv(x, y)[1]), change_brightness(colorr, e), 'line', count_fl)


    # c.create_polygon(list(map(net_to_canv, [[0, 0], [0, 100], [100, 100], [100, 0]])), fill=change_brightness(colorr, k1))
    #
    # c.create_polygon(list(map(net_to_canv, [[102, 0], [102, 100], [202, 100], [202, 0]])), fill=change_brightness(colorr, 1-k1))


def fpart(x):
    return abs(x - int(x))


def vu_draw(start, stop, colorr, count_fl=False):
    x0, y0 = list(map(round, list(map(float, start))))
    x1, y1 = list(map(round, list(map(float, stop))))

    dx = x1 - x0
    dy = y1 - y0

    if dx <= 0 and dy >= 0 and abs(dx) >= abs(dy) or dx <= 0 and dy <= 0 or dx >= 0 and dy <= 0 and abs(dy) > abs(dx):
        x0, y0, x1, y1 = x1, y1, x0, y0

    # if x2 < x1:
    #     x1, x2 = x2, x1
    #     y1, y2 = y2, y1
        # swap(x1, x2)
        # swap(y1, y2)

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    gradient = min(dx, dy)/max(dx, dy)

    diry = y1 - y0
    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    dirx = x1 - x0
    if dirx > 0:
        dirx = 1
    if dirx < 0:
        dirx = -1

    # обработать начальную точку
    xend = round(x0)
    yend = y0 + gradient * (xend - x0)
    xgap = 1 - fpart(x0 + 0.5)
    xpxl1 = xend  # будет использоваться в основном цикле
    ypxl1 = int(yend)
    draw_dot(round(net_to_canv(xpxl1, ypxl1)[0]), round(net_to_canv(xpxl1, ypxl1)[1]),
             change_brightness(colorr, (1 - fpart(yend)) * xgap), 'line', count_fl)
    draw_dot(round(net_to_canv(xpxl1, ypxl1+1)[0]), round(net_to_canv(xpxl1, ypxl1+1)[1]),
             change_brightness(colorr, fpart(yend) * xgap), 'line', count_fl)
    # plot(xpxl1, ypxl1, (1 - fpart(yend)) * xgap)
    # plot(xpxl1, ypxl1 + 1, fpart(yend) × xgap)
    intery = yend + gradient  # первое y - пересечение для цикла
    interx = xend + gradient

    # обработать конечную точку
    xend = round(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = fpart(x1 + 0.5)
    xpxl2 = xend  # будет использоваться в основном цикле
    ypxl2 = int(yend)
    draw_dot(round(net_to_canv(xpxl2, ypxl2)[0]), round(net_to_canv(xpxl2, ypxl2)[1]),
             change_brightness(colorr, (1 - fpart(yend)) * xgap), 'line', count_fl)
    draw_dot(round(net_to_canv(xpxl2, ypxl2 + 1)[0]), round(net_to_canv(xpxl2, ypxl2 + 1)[1]),
             change_brightness(colorr, fpart(yend) * xgap), 'line', count_fl)
    # plot(xpxl2, ypxl2, (1 - fpart(yend)) × xgap)
    # plot(xpxl2, ypxl2 + 1, fpart(yend) × xgap)

    # основной цикл
    if abs(dx) >= abs(dy):
        for x in range(xpxl1, xpxl2):
            if intery >= 0:
                draw_dot(round(net_to_canv(x, int(intery))[0]), round(net_to_canv(x, int(intery))[1]),
                         change_brightness(colorr, 1 - fpart(intery)), 'line', count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(x, int(intery)+1)[0]), round(net_to_canv(x, int(intery)+1)[1]),
                             change_brightness(colorr, fpart(intery)), 'line')
            else:
                draw_dot(round(net_to_canv(x, int(intery))[0]), round(net_to_canv(x, int(intery))[1]),
                         change_brightness(colorr, fpart(intery)), 'line', count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(x, int(intery) - 1)[0]), round(net_to_canv(x, int(intery) + 1)[1]),
                             change_brightness(colorr, 1 - fpart(intery)), 'line')
            intery += gradient*diry
    else:
        for y in range(ypxl1, ypxl2):
            if interx >= 0:
                draw_dot(round(net_to_canv(int(interx), y)[0]), round(net_to_canv(int(interx), y)[1]),
                         change_brightness(colorr, 1 - fpart(interx)), 'line', count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(int(interx)+1, y)[0]), round(net_to_canv(int(interx)+1, y)[1]),
                             change_brightness(colorr, fpart(interx)), 'line')
            else:
                draw_dot(round(net_to_canv(int(interx), y)[0]), round(net_to_canv(int(interx), y)[1]),
                         change_brightness(colorr, fpart(interx)), 'line', count_fl)
                if not count_fl:
                    draw_dot(round(net_to_canv(int(interx) + 1, y)[0]), round(net_to_canv(int(interx) - 1, y)[1]),
                             change_brightness(colorr, 1 - fpart(interx)), 'line')
            interx += gradient*dirx


def line_col_choose():
    global color
    del_with_tag('color')
    color = colorchooser.askcolor()

    if not color:
        return

    c.create_polygon(resized_coords, width=2, fill=color[1], tag='color')


def bg_col_choose():
    global color1
    del_with_tag('color1')
    color1 = colorchooser.askcolor()
    coordinate_field_creation()
    redraw_elems()

    if not color1[0]:
        return

    c.create_polygon(resized_coords1, width=2, fill=color1[1], tag='color1')


def cart_sum(a, b):
    return a[0] + b[0], a[1] + b[1]


def cart_dif(a, b):
    return a[0] - b[0], a[1] - b[1]


def rotate(a, alpha, center):
    a = cart_dif(a, center)
    res = (cos(alpha) * a[0] - sin(alpha) * a[1],
           sin(alpha) * a[0] + cos(alpha) * a[1])
    res = cart_sum(res, center)
    return res


def resize(a, k, center):
    k1 = k[0]
    k2 = k[1]
    a = cart_dif(a, center)
    res = (a[0] * k1, a[1] * k2)
    res = cart_sum(res, center)
    return res


def clean_all():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    # ent7.delete(0, END)
    # ent6.delete(0, END)
    # ent7.delete(0, END)
    ent8.delete(0, END)
    ent9.delete(0, END)
    # ent10.delete(0, END)

    objs = c.find_withtag('rot')
    objs += c.find_withtag('sz')
    objs += c.find_withtag('fox')
    for obj in objs:
        c.delete(obj)


def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

    net = c.find_withtag('net')
    for n in net:
        c.delete(n)


def del_with_tag(tag):
    for obj in c.find_withtag(tag):
        c.delete(obj)

    if tag == 'sz':
        ent2.delete(0, END)
        # ent3.delete(0, END)
        # ent6.delete(0, END)
        ent2.insert(0, 200)
        # ent3.insert(0, 0)
        # ent6.insert(0, 0)

    # if tag == 'rot':
    #     ent4.delete(0, END)
    #     ent5.delete(0, END)
    #     ent7.delete(0, END)
    #     ent4.insert(0, 5)
    #     ent5.insert(0, 0)
    #     ent7.insert(0, 0)


def click(event):
    global res_coords, rot_coords
    # print(method.get())
    if event.x < 65 or event.x > 665 + dx or event.y < 210 or event.y > 810 + dy:
        return

    # if var.get() == 1:
    #     rot_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
    #     if len(rot_coords) > 1:
    #         story.append(f'reprint_dot({rot_coords[-2][:-1]}, {rot_coords[-2][-1]});rot_coords.pop()')
    #     else:
    #         story.append(f'del_with_tag("rot")' + ';rot_coords.pop()' if len(rot_coords) else '')
    # elif var.get() == 0:
    #     res_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
    #     if len(res_coords) > 1:
    #         story.append(f'reprint_dot({res_coords[-2][:-1]}, {res_coords[-2][-1]});res_coords.pop()')
    #     else:
    #         story.append(f'del_with_tag("sz")' + ';res_coords.pop()' if len(res_coords) else '')

    global rotate_point, resize_point
    if var.get() == 1:
        rotate_point = canv_to_net(event.x, event.y)
        reprint_dot(rotate_point)
    elif var.get() == 0:
        resize_point = canv_to_net(event.x, event.y)
        reprint_dot(resize_point)
    elif var.get() == 2:
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent3.insert(0, f'{canv_to_net(event.x, event.y)[0]:g}')
        ent4.insert(0, f'{canv_to_net(event.x, event.y)[1]:g}')


def reprint_dot(coords, fl=0):
    global sz
    try:
        coords[0], coords[1] = float(coords[0]), float(coords[1])
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    buf = net_to_canv(coords[0], coords[1])

    x1, y1 = (buf[0] - 2), (buf[1] - 2)
    x2, y2 = (buf[0] + 2), (buf[1] + 2)

    if (fl == 1 or not var.get()) and fl != 2:
        dotts = c.find_withtag('start')
        for dot in dotts:
            c.delete(dot)
        ent1.delete(0, END)
        ent9.delete(0, END)
        ent1.insert(END, f'{coords[0]:g}')
        ent9.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='start', activeoutline='lightgreen',
                      activefill='lightgreen')
        # c.create_text(x1 - 5, y1 - 9, text='⇖', fill='green', tag='sz', font='Arial 20')
        # c.create_text(x1 + 10, y1 - 9, text='⇗', fill='green', tag='sz', font='Arial 20')
        # c.create_text(x1 - 5, y1 + 7, text='⇙', fill='green', tag='sz', font='Arial 20')
        # c.create_text(x1 + 10, y1 + 7, text='⇘', fill='green', tag='sz', font='Arial 20')
    elif fl == 2 or var.get():
        dotts = c.find_withtag('stop')
        for dot in dotts:
            c.delete(dot)
        ent2.delete(0, END)
        ent8.delete(0, END)
        ent2.insert(END, f'{coords[0]:g}')
        ent8.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='stop', activeoutline='lightgreen',
                      activefill='lightgreen')
        # c.create_text(x1 + 2, y1 - 2, text='↻', fill='green', tag='rot', font='Helvetica 40')


def back():
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

    foxx = c.find_withtag('fox')
    for elem in foxx:
        c.delete(elem)
    fox.analyze_and_redraw()
    fox.draw()

    del story[-1]


def scale(x, y):
    global sz
    prev_sz = sz
    while x < (150 + dx / 4) * sz and y < (150 + dy / 4) * sz:
        sz /= 2

    while x > (300 + dx / 2) * sz or y > (300 + dy / 2) * sz:
        sz *= 2

    if sz != prev_sz:
        redraw()


def redraw():
    global sz

    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

    max_len = 0
    for i in range(65, 665 + dx, 50):
        if len(f'{round((i - 365) * sz, 3):g}') > max_len:
            max_len = len(f'{round((i - 365) * sz, 3):g}')

    for i in range(round(center[0] + 50), 665 + dx, 50):
        c.create_text(i, 530 + dy / 2, fill='grey', text=f'{round((i - center[0]) * sz, 3):g}', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(round(center[0] - 50), 65, -50):
        c.create_text(i, 530 + dy / 2, fill='grey', text=f'{round((i - center[0]) * sz, 3):g}', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(round(center[1] + 50), 810 + dy, 50):
        c.create_text(345 + dx / 2, i + 10, fill='grey', text=f'{round(-(i - center[1]) * sz, 3):g}', tag='coord')

    for i in range(round(center[1] - 50), 210, -50):
        c.create_text(345 + dx / 2, i + 10, fill='grey', text=f'{round(-(i - center[1]) * sz, 3):g}', tag='coord')


# def text_and_labels_creation():
#     label1.place(x=60, y=5)
#     label2.place(x=280, y=5)
#     label3.place(x=535, y=5)
#     label4.place(x=35, y=43)
#     label5.place(x=290, y=43)
#     label6.place(x=295, y=82)
#     label7.place(x=295, y=112)
#     label8.place(x=545, y=82)
#     label9.place(x=545, y=112)
#     label10.place(x=491, y=90)
#     label11.place(x=535, y=43)
#     label12.place(x=241, y=90)
#     label13.place(x=403, y=42)
#     label14.place(x=653, y=42)
#     label15.place(x=150, y=7)
#     label16.place(x=425, y=7)
#     label17.place(x=613, y=7)
#     label18.place(x=20, y=120)
#     label19.place(x=70, y=25)
#     label20.place(x=115, y=25)
#     label21.place(x=320, y=25)
#     label22.place(x=365, y=25)


def buttons_creation():
    # btn_res_l.place(x=330, y=150)
    # btn_res_r.place(x=360, y=150)
    # btn_mv_r.place(x=128, y=100)
    # btn_mv.place(x=165, y=43)
    # btn_mv_l.place(x=85, y=100)
    # btn_mv_u.place(x=106, y=75)
    # btn_mv_d.place(x=106, y=125)
    btn_cl_all.place(x=25, y=170)
    # btn_rot_r.place(x=620, y=150)
    # btn_rot_l.place(x=590, y=150)
    btn_back.place(x=25, y=140)
    btn_exit.place(x=630, y=840)


def coordinate_field_creation():
    global center, color1
    del_with_tag('bg')

    if not color1[1]:
        color1 = ['', 'white']

    c.create_polygon([[65, 210], [65, 810 + dy], [665 + dx, 810 + dy], [665 + dx, 210]], width=2, fill=color1[1],
                     tag='bg')
    center[0] = round(365 + dx / 2)
    center[1] = round(510 + dy / 2)
    clean_coords()
    c.create_line(33, 510 + dy / 2, 695 + dx, 510 + dy / 2, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6", tag='net')
    c.create_line(365 + dx / 2, 835 + dy, 365 + dx / 2, 185, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6", tag='net')
    c.create_line(665 + dx, 210, 665 + dx, 810 + dy, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 810 + dy, 665 + dx, 810 + dy, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 210, 665 + dx, 210, fill='black',
                  width=1, dash=(5, 9), tag='net')
    c.create_line(65, 210, 65, 810 + dy, fill='black',
                  width=1, dash=(5, 9), tag='net')

    c.create_line(225 + dx / 4, 5, 225 + dx / 4, 180, fill='black',
                  width=1, dash=(5, 9), tag='net')

    c.create_line(440 + dx / 2, 5, 440 + dx / 2, 180, fill='black',
                  width=1, dash=(5, 9), tag='net')

    for i in range(round(center[0] + 50), 665 + dx, 50):
        c.create_line(i, 503 + dy / 2, i, 520 + dy / 2, fill='grey', width=2, tag='net')
        c.create_line(i, 210, i, 810 + dy, fill='grey', width=1, dash=(1, 9), tag='net')

    for i in range(round(center[0] - 50), 65, -50):
        c.create_line(i, 503 + dy / 2, i, 520 + dy / 2, fill='grey', width=2, tag='net')
        c.create_line(i, 210, i, 810 + dy, fill='grey', width=1, dash=(1, 9), tag='net')

    for i in range(round(center[1] + 50), 810 + dy, 50):
        c.create_line(358 + dx / 2, i, 372 + dx / 2, i, fill='grey', width=2, tag='net')
        c.create_line(65, i, 665 + dx, i, fill='grey', width=1, dash=(1, 9), tag='net')

    for i in range(round(center[1] - 50), 210, -50):
        c.create_line(358 + dx / 2, i, 372 + dx / 2, i, fill='grey', width=2, tag='net')
        c.create_line(65, i, 665 + dx, i, fill='grey', width=1, dash=(1, 9), tag='net')

    c.create_text(688 + dx, 493 + dy / 2, text='X', font='Verdana 20', fill='green', tag='net')
    c.create_text(380 + dx / 2, 195, text='Y', font='Verdana 20', fill='green', tag='net')
    redraw()


# def radiobutton_creation():
#     var.set(0)
#     set0.place(x=405, y=97)
#     set1.place(x=655, y=97)


# def load_and_transf_coords(file):
#     coords = []
#     with open(file) as f:
#         line = f.readline()
#         while line:
#             loc = list(map(float, line.strip('\n').strip(')').strip('(').split('; ')))
#             loc = net_to_canv(loc[0], loc[1])
#             coords.append(loc)
#             line = f.readline()
#
#     pol1 = [[-157, -116], [-206, -111], [-187, -157]]
#     pol2 = [[177, -65], [182, -50], [188, -38], [205, -35]]
#     for i in range(len(pol1)):
#         pol1[i] = net_to_canv(pol1[i][0], pol1[i][1])
#         coords.append(pol1[i])
#
#     for i in range(len(pol2)):
#         pol2[i] = net_to_canv(pol2[i][0], pol2[i][1])
#         coords.append(pol2[i])
#
#     return coords


def start_state():
    global story, rot_coords, res_coords, lines, bunches
    scale(200, 200)
    story = []
    lines = []
    bunches = []
    clean_all()
    del_with_tag('line')
    ent1.insert(0, 0)
    ent2.insert(0, 200)
    ent3.insert(0, 150)
    ent4.insert(0, -150)
    ent5.insert(0, 100)
    ent6.insert(0, 5)
    # ent7.insert(0, 0)
    ent8.insert(0, 200)
    ent9.insert(0, 0)
    # ent10.insert(0, 15)
    # fox = Fox(load_and_transf_coords('data.txt'))
    # fox.analyze_and_redraw()
    # fox.draw()


old_dx, old_dy = dx, dy


def config(event):
    global dx, dy, old_dx, old_dy, rotate_point, resize_point, resized_coords, resized_coords1
    if event.widget == window:
        kx = window.winfo_width() / win_size[0]
        ky = window.winfo_height() / win_size[1]

        if kx < 0.9 or ky < 0.85:
            return

        max_elems = 30
        ent_places = [0] * max_elems
        lbl_places = [0] * max_elems
        btn_places = [0] * max_elems
        radiobtn_places = [0] * max_elems
        for ent in ents.split('\n'):
            ind = int(ent.split('ent')[1].split('.')[0])
            ent_places[ind] = [int(ent.split('x=')[1].split(',')[0]), int(ent.split('y=')[1].split(')')[0])]

        for lbl in lbls.split('\n'):
            ind = int(lbl.split('label')[1].split('.')[0])
            lbl_places[ind] = [int(lbl.split('x=')[1].split(',')[0]), int(lbl.split('y=')[1].split(')')[0])]

        k = 0
        for btn in btns.split('\n'):
            name = btn.split('.')[0]
            btn_places[k] = [name, int(btn.split('x=')[1].split(',')[0]), int(btn.split('y=')[1].split(')')[0])]
            k += 1

        for rbtn in rbtns.split('\n'):
            ind = int(rbtn.split('set')[1].split('.')[0])
            radiobtn_places[ind] = [int(rbtn.split('x=')[1].split(',')[0]), int(rbtn.split('y=')[1].split(')')[0])]

        for i in range(max_elems):
            if ent_places[i]:
                eval(f'ent{i}.place(x={ent_places[i][0]} * kx, y={ent_places[i][1]} * 1)')
            if lbl_places[i]:
                eval(f'label{i}.place(x={lbl_places[i][0]} * kx, y={lbl_places[i][1]} * 1)')
            if btn_places[i]:
                eval(f'{btn_places[i][0]}.place(x={btn_places[i][1]} * kx, y={btn_places[i][2]} * 1)')
            if radiobtn_places[i]:
                eval(f'set{i}.place(x={radiobtn_places[i][0]} * kx, y={radiobtn_places[i][1]} * 1)')
        btn_exit.place(x=window.winfo_width() - 70, y=window.winfo_height() - 60)
        btn_col_bg.place(x=170, y=window.winfo_height() - 60)

        del_with_tag('color')
        del_with_tag('color1')

        resized_coords = []
        resized_coords1 = []
        # print(color_coords)
        for i in range(len(color_coords)):
            resized_coords.append([color_coords[i][0], color_coords[i][1]])
            resized_coords[i][0] *= kx
            resized_coords1.append([color_coords1[i][0], color_coords1[i][1]])
            resized_coords1[i][1] *= ky
        c.create_polygon(resized_coords, width=2, fill=color[1], tag='color')
        c.create_polygon(resized_coords1, width=2, fill=color1[1], tag='color1')
        label23.place(x=20, y=window.winfo_height() - 60)

        old_dx, old_dy = dx, dy
        dx = window.winfo_width() - win_size[0]
        dy = window.winfo_height() - win_size[1]
        coordinate_field_creation()
        redraw_elems()
        # fox.upd_coords((dx-old_dx)/2, (dy-old_dy)/2)
        # reprint_dot([ent3.get(), ent6.get()], 1)
        # reprint_dot([ent5.get(), ent7.get()], 2)
        # fox.analyze_and_redraw()
        # fox.draw()
        c.place(x=-15, y=0)


# fox = Fox(load_and_transf_coords('data.txt'))

c.bind('<1>', click)
# window.bind("<Command-r>", lambda event: fox.rotate(ent4.get(), [ent5.get(), ent7.get()]))
# window.bind("<Shift-Command-r>", lambda event: fox.rotate('-' + ent4.get(), [ent5.get(), ent7.get()]))
# window.bind("<Command-Up>", lambda event: fox.resize(1, ent2.get(), ent8.get(), [ent3.get(), ent6.get()]))
# window.bind("<Command-Down>", lambda event: fox.resize(-1, ent2.get(), ent8.get(), [ent3.get(), ent6.get()]))
# window.bind("<Up>", lambda event: fox.move(ent10.get(), 'up'))
# window.bind("<Down>", lambda event: fox.move(ent10.get(), 'down'))
# window.bind("<Right>", lambda event: fox.move(ent10.get(), 'right'))
# window.bind("<Left>", lambda event: fox.move(ent10.get(), 'left'))
window.bind("<Command-z>", lambda event: back())
window.bind("<Configure>", config)

# text_and_labels_creation()
buttons_creation()
coordinate_field_creation()
start_state()
# radiobutton_creation()
# default_fox_coords = load_and_transf_coords('data.txt')
# fox.draw()

mmenu = Menu(window)
add_menu = Menu(mmenu)
add_menu.add_command(label='О программе и авторе',
                     command=lambda: messagebox.showinfo('О программе и авторе', TASK + AUTHOR))
add_menu.add_command(label='Выход', command=exit)
mmenu.add_cascade(label='About', menu=add_menu)
window.config(menu=mmenu)

window.geometry('700x900')
c.pack()
window.mainloop()
