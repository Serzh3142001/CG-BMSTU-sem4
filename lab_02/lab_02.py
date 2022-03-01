from math import *
from tkinter import *
import tkinter.messagebox as box
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()



# window.resizable(1, 1)
# window.config()
# window.title('Bar simulator')
var = IntVar()
story = []
c = Canvas(window, width=700, height=900, bg='white')
res_coords = []
rot_coords = []
cnt_res_clc = 0
cnt_rot_clc = 0
# frame_bias.pack()
# c.create_rectangle(4, 32, 266, 172, outline='black', width=2)
# c.create_rectangle(429, 32, 691, 172, outline='black', width=2)
# text1 = Text(width=36, height=10)
# text2 = Text(width=36, height=10)
#
# text1.configure(state=DISABLED)
# text2.configure(state=DISABLED)

# image = Image.open('pic.png')
# photo = ImageTk.PhotoImage(image)
# image = c.create_image(120, 250, anchor='nw', image=photo)

ent1 = Entry(width=8)
ent2 = Entry(width=8)
ent3 = Entry(width=8)
ent4 = Entry(width=8)
ent5 = Entry(width=8)
ent6 = Entry(width=8)
ent7 = Entry(width=8)
ent1.place(x=70, y=40)
ent2.place(x=320, y=40)
ent3.place(x=320, y=80)
ent4.place(x=570, y=40)
ent5.place(x=570, y=80)
ent6.place(x=320, y=110)
ent7.place(x=570, y=110)
ent1.insert(0, 15)
ent2.insert(0, 5)
ent3.insert(0, 0)
ent4.insert(0, 5)
ent5.insert(0, 0)
ent6.insert(0, 0)
ent7.insert(0, 0)

TASK = 'Вариант 13:\nНарисовать исходный рисунок, затем его переместить, промасштабировать, повернуть'
AUTHOR = '\n\nНиколаев Сергей ИУ7-44Б'
sz = 1
resize_point = [0, 0]
rotate_point = [0, 0]

def cart_sum(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cart_dif(a, b):
    return (a[0] - b[0], a[1] - b[1])


def rotate(a, alpha, center):
    a = cart_dif(a, center)
    res = (cos(alpha) * a[0] - sin(alpha) * a[1],
           sin(alpha) * a[0] + cos(alpha) * a[1])
    res = cart_sum(res, center)
    return res

def resize(a, k, center):
    a = cart_dif(a, center)
    res = (a[0]*k, a[1]*k)
    res = cart_sum(res, center)
    return res


def clean_tri():
    triangls = c.find_withtag('triang')
    for tri in triangls:
        c.delete(tri)

def rotate_fox(dots, alpha, center, st=1):
    try:
        alpha = radians(float(alpha))
    except:
        box.showinfo('Error', 'Некорректное значение угла поворота!')
        return

    try:
        x, y = float(ent5.get()), float(ent7.get())
    except:
        box.showinfo('Error', 'Некорректные координаты!')
        return

    if st:
        story.append(f'rotate_fox(fox_coords, {-degrees(alpha)}, {center}, 0)')

    global fox_coords, rotate_point

    reprint_dot([x, y], 2)
    rotate_point = [x, y]

    rotated_dots = []
    for dot in dots:
        rotated_dots.append(rotate(dot, alpha, center))

    fox = c.find_withtag('fox')
    for elem in fox:
        c.delete(elem)

    fox_coords = rotated_dots
    analyze_and_redraw()
    draw_fox(fox_coords)

def resize_fox(dots, k, center, st=1):
    try:
        k = float(k)/100 + 1
    except:
        box.showinfo('Error', 'Некорректное значение процента масштабирования!')
        return

    try:
        x, y = float(ent3.get()), float(ent6.get())
    except:
        box.showinfo('Error', 'Некорректные координаты!')
        return

    if st:
        story.append(f'resize_fox(fox_coords, {-(k - 1)*100}, {center}, 0)')

    global fox_coords, resize_point

    reprint_dot([x, y], 1)
    resize_point = [x, y]

    resized_dots = []
    for dot in dots:
        resized_dots.append(resize(dot, k, center))

    fox = c.find_withtag('fox')
    for elem in fox:
        c.delete(elem)

    fox_coords = resized_dots
    analyze_and_redraw()
    draw_fox(fox_coords)


def move_fox(dots, delta, dir, st=1):
    global sz
    try:
        delta = float(delta)/sz
    except:
        box.showinfo('Error', 'Некорректное значение процента масштабирования!')
        return

    if st:
        story.append(f'move_fox(fox_coords, {-delta*sz}, "{dir}", 0)')

    global fox_coords
    moved_dots = []
    for dot in dots:
        if dir == 'up':
            moved_dots.append([dot[0], dot[1] - delta])
        elif dir == 'down':
            moved_dots.append([dot[0], dot[1] + delta])
        elif dir == 'left':
            moved_dots.append([dot[0] - delta, dot[1]])
        elif dir == 'right':
            moved_dots.append([dot[0] + delta, dot[1]])

    fox = c.find_withtag('fox')
    for elem in fox:
        c.delete(elem)

    fox_coords = moved_dots
    analyze_and_redraw()
    draw_fox(fox_coords)


def resize_dots(dots, k, center):
    global fox_coords

    resized_dots = []
    for dot in dots:
        resized_dots.append(resize(dot, k, center))

    fox_coords = resized_dots

def analyze_and_redraw():
    global fox_coords, sz
    max_coord = 0

    for dot in fox_coords:
        dot = canv_to_net(dot[0], dot[1])
        if max(abs(dot[0]), abs(dot[1])) > max_coord:
            max_coord = max(abs(dot[0]), abs(dot[1]))

    try:
        max_coord = max(max_coord, abs(float(ent3.get())), abs(float(ent5.get())),
                        abs(float(ent6.get())), abs(float(ent7.get())))
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    # print(max_coord)
    if 150 * sz <= max_coord <= 300 * sz:
        return

    # fox = c.find_withtag('fox')
    # for elem in fox:
    #     c.delete(elem)

    old = sz
    scale(max_coord, max_coord)
    new = sz
    resize_dots(fox_coords, old/new, net_to_canv(0, 0))
    reprint_dot([float(ent3.get()), float(ent6.get())], 1)
    reprint_dot([float(ent5.get()), float(ent7.get())], 2)


def clean_all():
    # enable()
    # text1.delete(1.0, END)
    # text2.delete(1.0, END)
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)

    objs = c.find_withtag('rot')
    objs += c.find_withtag('sz')
    objs += c.find_withtag('fox')
    for obj in objs:
        c.delete(obj)

    # disable()


def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)


def tri_click(event, tag):
    triangls = list(c.find_withtag('triang'))
    triangls.remove(tag)
    for tri in triangls:
        c.delete(tri)

# def enable():
#     text1.configure(state=NORMAL)
#     text2.configure(state=NORMAL)
#
#
# def disable():
#     text1.configure(state=DISABLED)
#     text2.configure(state=DISABLED)


# def add_dot(num):
#     if num == 1:
#         d1 = ent1.get()
#         d2 = ent2.get()
#     else:
#         d1 = ent3.get()
#         d2 = ent4.get()
#
#     try:
#         d1 = float(d1)
#         d2 = float(d2)
#
#         if num == 1:
#             enable()
#             text1.insert(END, f'({d1:g}; {d2:g})\n')
#             disable()
#             story.append('')
#             sett1 = text1.get(1.0, END).split('\n')[:-1]
#             if not sett1[-1]:
#                 sett1 = sett1[:-1]
#             end = len(sett1)
#             story[-1] += f'text1.delete({end}.0, END)'
#             story[-1] += '; text1.insert(END, "\\n")' if end > 1 else ''
#         else:
#             enable()
#             text2.insert(END, f'({d1:g}; {d2:g})\n')
#             disable()
#             story.append('')
#             sett2 = text2.get(1.0, END).split('\n')[:-1]
#             if not sett2[-1]:
#                 sett2 = sett2[:-1]
#             end = len(sett2)
#             story[-1] += f'text2.delete({end}.0, END)'
#             story[-1] += '; text2.insert(END, "\\n")' if end > 1 else ''
#         dots_update()
#     except:
#         box.showinfo('Error', 'Некорректные координаты!')


# def is_cursor_touch_triang(tri, event):
#     coo = c.coords(tri)[:-2]
#
#     x0, y0 = event.x, event.y
#     x1, y1 = int(coo[0]), int(coo[1])
#     x2, y2 = int(coo[2]), int(coo[3])
#     x3, y3 = int(coo[4]), int(coo[5])
#
#     d1 = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
#     d2 = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
#     d3 = ((x0 - x3) ** 2 + (y0 - y3) ** 2) ** 0.5
#
#     a1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
#     a2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
#     a3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
#
#     cos1 = (d1 ** 2 + d2 ** 2 - a1 ** 2) / 2 / d1 / d2
#     cos2 = (d2 ** 2 + d3 ** 2 - a2 ** 2) / 2 / d2 / d3
#     cos3 = (d1 ** 2 + d3 ** 2 - a3 ** 2) / 2 / d1 / d3
#
#     if abs(cos1 + 1) < 1e-3 or abs(cos2 + 1) < 1e-3 or abs(cos3 + 1) < 1e-3:
#         return 1
#     else:
#         return 0


# def is_cursor_touch_dot(dot, event):
#     coo = c.coords(dot)
#
#     x, y = event.x, event.y
#
#     if coo[0] <= x <= coo[0] + 4 and coo[1] <= y <= coo[1] + 4:
#         return 1
#     else:
#         return 0


def click(event):
    global res_coords, cnt_res_clc, cnt_rot_clc

    # disable()
    # dotts = c.find_withtag('dot')
    # for dot in dotts:
    #     if is_cursor_touch_dot(dot, event):
    #         enable()
    #         tc = c.find_withtag('tc')
    #         for tc1 in tc:
    #             c.delete(tc1)
    #
    #         true_c = canv_to_net(c.coords(dot)[0], c.coords(dot)[1])
    #         c.create_text(298, 842, text=f'{true_c[0] + 2:g}', tag='tc')
    #         c.create_text(388, 842, text=f'{true_c[1] - 2:g}', tag='tc')
    #         text1.configure(state=NORMAL)
    #         text2.configure(state=NORMAL)
    #         coo = c.coords(dot)
    #         crds = canv_to_net(coo[0], coo[1])
    #         text1.insert(END, f'({crds[0]+2:g}; {crds[1]-2:g})\n')
    #         # print(dot, c.coords(dot), event.x, event.y)
    #         # disable()
    #         return
    #
    # triangls = c.find_withtag('triang')
    # for tri in triangls:
    #     if is_cursor_touch_triang(tri, event):
    #         tri_click(event, tri)
    #         return

    if event.x < 65 or event.x > 665 or event.y < 210 or event.y > 810:
        return

    if var.get():
        cnt_rot_clc += 1
        rot_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
        if len(rot_coords) > 1:
            story.append(f'reprint_dot({rot_coords[-2][:-1]}, {rot_coords[-2][-1]});rot_coords.pop()')
    else:
        cnt_res_clc += 1
        res_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
        if len(res_coords) > 1:
            story.append(f'reprint_dot({res_coords[-2][:-1]}, {res_coords[-2][-1]});res_coords.pop()')

    # if not (var.get() and cnt_rot_clc == 1 or not var.get() and cnt_res_clc == 1):
    #     res_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
    # elif cnt_res_clc + cnt_rot_clc == 1:
    #     res_coords.append(canv_to_net(event.x, event.y) + [var.get() + 1])
    #
    # if len(res_coords) > 1 and not (var.get() and cnt_rot_clc == 1 or not var.get() and cnt_res_clc == 1):
    #     story.append(f'reprint_dot({res_coords[-2][:-1]}, {res_coords[-2][-1]});old_clc.pop()')


    # else:
    #     # objs = c.find_withtag('rot')
    #     # objs += c.find_withtag('sz')
    #     # for obj in objs: c.delete(obj)
    #     story.append(f'for obj in c.find_withtag("rot", "sz"): c.delete(obj)')

    global rotate_point, resize_point
    if var.get():
        rotate_point = canv_to_net(event.x, event.y)
        reprint_dot(rotate_point)
    else:
        resize_point = canv_to_net(event.x, event.y)
        reprint_dot(resize_point)

    # reprint_dot(res_coords[-1][:-1])

    # dotts = c.find_withtag('dot')
    # story.append(f'c.delete({dotts[-1]})')
    # # c.delete(dotts[-1])
    #
    # crds = canv_to_net(event.x, event.y)
    # if var.get():
    #     text2.insert(END, f'({crds[0]:g}; {crds[1]:g})\n')
    #
    #
    #     # story[-1] += f'; text2.delete({end}.0, END)'
    #     # story[-1] += '; text2.insert(END, "\\n")' if end > 1 else ''
    # else:
    #     reprint_dot
    #     flag1 += 1
    #     enable()
    #     text1.insert(END, f'({crds[0]:g}; {crds[1]:g})\n')
    #     disable()
    # #
    #     sett1 = text1.get(1.0, END).split('\n')[:-1]
    #     if not sett1[-1]:
    #         sett1 = sett1[:-1]
    #
    #     end = len(sett1)
    #     story[-1] += f'; text1.delete({end}.0, END)'
    #     story[-1] += '; text1.insert(END, "\\n")' if end > 1 else ''


def reprint_dot(coords, fl=0):
    global sz
    buf = net_to_canv(coords[0], coords[1])

    x1, y1 = (buf[0] - 2), (buf[1] - 2)
    x2, y2 = (buf[0] + 2), (buf[1] + 2)

    if (fl == 1 or not var.get()) and fl != 2:
        dotts = c.find_withtag('sz')
        for dot in dotts:
            c.delete(dot)
        ent3.delete(0, END)
        ent6.delete(0, END)
        ent3.insert(END, f'{coords[0]:g}')
        ent6.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='sz', activeoutline='lightgreen', activefill='lightgreen')
        c.create_text(x1-5, y1 - 9, text='⇖', fill='green', tag='sz', font='Arial 20')
        c.create_text(x1 + 10, y1 - 9, text='⇗', fill='green', tag='sz', font='Arial 20')
        c.create_text(x1 - 5, y1 + 7, text='⇙', fill='green', tag='sz', font='Arial 20')
        c.create_text(x1 + 10, y1 + 7, text='⇘', fill='green', tag='sz', font='Arial 20')
    elif fl == 2 or var.get():
        dotts = c.find_withtag('rot')
        for dot in dotts:
            c.delete(dot)
        ent5.delete(0, END)
        ent7.delete(0, END)
        ent5.insert(END, f'{coords[0]:g}')
        ent7.insert(END, f'{coords[1]:g}')
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='rot', activeoutline='lightgreen', activefill='lightgreen')
        c.create_text(x1 + 2, y1 - 2, text='↻', fill='green', tag='rot', font='Helvetica 40')


# def dots_update():
#     sett1 = text1.get(1.0, END).split('\n')[:-1]
#
#     if not sett1[-1]:
#         sett1 = sett1[:-1]
#
#     sett2 = text2.get(1.0, END).split('\n')[:-1]
#
#     if not sett2[-1]:
#         sett2 = sett2[:-1]
#
#     dotts = c.find_withtag('dot')
#
#     for dot in dotts:
#         c.delete(dot)
#
#     clean_tri()
#
#     try:
#         xs = []
#         ys = []
#         for dot in sett1:
#             x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
#             xs.append(abs(x))
#             ys.append(abs(y))
#         for dot in sett2:
#             x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
#             xs.append(abs(x))
#             ys.append(abs(y))
#         max_x, max_y = max(xs), max(ys)
#         if max_y != 0 and max_y != 0:
#             scale(max_x, max_y)
#     except:
#         box.showinfo('Error', 'Некорректные координаты!')
#         return
#
#     for dot in sett1:
#         x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
#         x, y = net_to_canv(x, y)
#         x2, y2 = x + 2, y + 2
#         x -= 2
#         y -= 2
#         c.create_oval(round(x), round(y), round(x2), round(y2), outline='red', fill='red', tag='dot', activeoutline='lightgreen', activefill='lightgreen')
#
#     for dot in sett2:
#         x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
#         x, y = net_to_canv(x, y)
#         x2, y2 = x + 2, y + 2
#         x -= 2
#         y -= 2
#         c.create_oval(round(x), round(y), round(x2), round(y2), outline='blue', fill='blue', tag='dot', activeoutline='lightgreen', activefill='lightgreen')


def net_to_canv(x, y):
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz
    center = (365, 510)

    return [round(x/sz + center[0]), round(center[1] - y/sz)]


def canv_to_net(x, y):
    try:
        x, y = float(x), float(y)
    except:
        box.showinfo('Error', 'Некорректные координаты!')

    global sz
    center = (365, 510)

    return [round((x - center[0])*sz, 3), round((center[1] - y)*sz, 3)]


def back():
    global res_coords, rot_coords
    # enable()
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
        # print(f'[{com}]')
        eval(com)

    del story[-1]
    # dots_update()
    # disable()


def scale(x, y):
    global sz
    prev_sz = sz
    center = (365, 510)
    while x > -150 * sz and x < 150 * sz and y > -150 * sz and y < 150 * sz:
        sz /= 2

    while x < -300 * sz or x > 300 * sz or y < -300 * sz or y > 300 * sz:
        sz *= 2

    if sz != prev_sz:
        redraw()


def redraw():
    global sz
    clean_coords()
    max_len = 0
    for i in range(65, 670, 50):
        if len(f'{round((i - 365)*sz, 3):g}') > max_len:
            max_len = len(f'{round((i - 365)*sz, 3):g}')

    for i in range(65, 670, 50):
        c.create_text(i, 530, fill='grey', text=f'{round((i - 365)*sz, 3):g}' if i - 365 else '', tag='coord',
                      font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(210, 820, 50):
        c.create_text(345, i + 10, fill='grey', text=f'{round(-(i - 510)*sz, 3):g}' if i - 510 else '', tag='coord')


# def is_count_true(set1, set2, a, b, c):
#     count1 = 0
#     count2 = 0
#     x1, y1 = a
#     x2, y2 = b
#     x3, y3 = c
#
#     for dot in set1:
#         x0, y0 = dot
#         k1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
#         k2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
#         k3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
#         if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0:
#             count1 += 1
#
#     for dot in set2:
#         x0, y0 = dot
#         k1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
#         k2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
#         k3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
#         if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0:
#             count2 += 1
#
#     return count1 == count2 and count1


# def triang_find_and_draw():
#     dots_update()
#
#     draw_fl =  0
#     sett1 = text1.get(1.0, END).split('\n')[:-1]
#     if not sett1[-1]:
#         sett1 = sett1[:-1]
#
#     sett2 = text2.get(1.0, END).split('\n')[:-1]
#     if not sett2[-1]:
#         sett2 = sett2[:-1]
#
#     set1_t = []
#     set2_t = []
#
#     for dot in sett1:
#         x1, y1 = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
#         set1_t.append((x1, y1))
#
#     for dot in sett2:
#         x1, y1 = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
#         set2_t.append((x1, y1))
#
#     for i in range(len(set1_t) - 2):
#         for j in range(i + 1, len(set1_t) - 1):
#             for k in range(j + 1, len(set1_t)):
#                 a = set1_t[:]
#                 del a[i], a[j - 1], a[k - 2]
#                 if is_count_true(a, set2_t, set1_t[i], set1_t[j], set1_t[k]):
#                     c.create_line(net_to_canv(set1_t[i][0], set1_t[i][1]),
#                                   net_to_canv(set1_t[j][0], set1_t[j][1]),
#                                   net_to_canv(set1_t[k][0], set1_t[k][1]),
#                                   net_to_canv(set1_t[i][0], set1_t[i][1]), fill='green', width=2,
#                                   activefill='lightgreen', tag='triang')
#                     draw_fl += 1
#
#     if not draw_fl:
#         box.showinfo('Error', 'Треугольники не найдены')
#         return
#
#     tris = c.find_withtag('triang')
#     story.append('')
#     for tri in tris:
#         story[-1] += f'c.delete({tri});'


def text_and_labels_creation():
    pass
    # text1.place(x=20, y=33)
    # scroll = Scrollbar(command=text1.yview)
    # scroll.pack(side=LEFT, fill=Y)
    # text1.config(yscrollcommand=scroll.set)
    #
    # text2.place(x=445, y=33)
    # scroll = Scrollbar(command=text2.yview)
    # scroll.pack(side=RIGHT, fill=Y)
    # text2.config(yscrollcommand=scroll.set)
    # frame_bias = LabelFrame(text='На')
    # frame_bias.place(x=50, y=50)
    # lab1 = Label(frame_bias, width=7, height=4, text='Смещение:')
    # lab1.place(x=50, y=50)

    label1 = Label(text='Смещение:', font='Arial 15')
    label1.place(x=60, y=5)
    label2 = Label(text='Масштабирование:', font='Arial 15')
    label2.place(x=280, y=5)
    label3 = Label(text='Поворот:', font='Arial 15')
    label3.place(x=535, y=5)

    label4 = Label(text='На:', font='Arial 15')
    label4.place(x=35, y=43)
    label5 = Label(text='На:', font='Arial 15')
    label5.place(x=285, y=43)
    label4 = Label(text='X:', font='Arial 15')
    label4.place(x=295, y=82)
    label5 = Label(text='Y:', font='Arial 15')
    label5.place(x=295, y=112)
    label4 = Label(text='X:', font='Arial 15')
    label4.place(x=545, y=82)
    label5 = Label(text='Y:', font='Arial 15')
    label5.place(x=545, y=112)
    label6 = Label(text='Относ.\nточки:', font='Arial 13')
    label6.place(x=491, y=90)
    label7 = Label(text='На:', font='Arial 15')
    label7.place(x=535, y=43)
    label8 = Label(text='Относ.\nточки:', font='Arial 13')
    label8.place(x=241, y=90)
    label8 = Label(text='%', font='Arial 15')
    label8.place(x=403, y=42)
    label8 = Label(text='°', font='Arial 17')
    label8.place(x=653, y=42)
    # label2 = Label(text='Точки второго множества:', font='Arial 15')
    # c.create_text(300, 15, text='                           Смещение:'
    #                             '                           Масштабирование:'
    #                             '                            Поворот:', font='Arial 15')
    # c.create_text(300, 15, text='Масштабирование:', font='Arial 15')
    # c.create_text(550, 15, text='Поворот:', font='Arial 15')


    # label2.place(x=440, y=5)


def buttons_creation():
    btn_rot_r = Button(window, text='↻', fg='green', command=lambda: rotate_fox(fox_coords, ent4.get(),
                                                                                net_to_canv(ent5.get(),
                                                                                            ent7.get())))
    btn_rot_l = Button(window, text='↺', fg='green', command=lambda: rotate_fox(fox_coords, '-'+ent4.get(),
                                                                                net_to_canv(ent5.get(),
                                                                                            ent7.get())))
    btn_res_r = Button(window, text='▲', fg='green', command=lambda: resize_fox(fox_coords, ent2.get(),
                                                                               net_to_canv(ent3.get(),
                                                                                           ent6.get())))
    btn_res_l = Button(window, text='▼', fg='green', command=lambda: resize_fox(fox_coords, '-' + ent2.get(),
                                                                               net_to_canv(ent3.get(),
                                                                                           ent6.get())))
    btn_mv_r = Button(window, text='▶', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'right'))
    btn_mv_l = Button(window, text='◀', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'left'))
    btn_mv_u = Button(window, text='▲', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'up'))
    btn_mv_d = Button(window, text='▼', fg='green', command=lambda: move_fox(fox_coords, ent1.get(), 'down'))

    btn_back = Button(window, text='назад', fg='purple', command=lambda: back())
    btn_cl_all = Button(window, text='🗑заново', fg='orange', command=lambda: start_state())
    btn_exit = Button(window, text=' выход ', fg='red', command=exit)

    btn_res_l.place(x=330, y=150)
    btn_res_r.place(x=360, y=150)

    btn_mv_r.place(x=125, y=110)
    btn_mv_l.place(x=85, y=110)
    btn_mv_u.place(x=105, y=90)
    btn_mv_d.place(x=105, y=130)

    btn_cl_all.place(x=25, y=170)

    btn_rot_r.place(x=620, y=150)
    btn_rot_l.place(x=590, y=150)

    btn_back.place(x=25, y=140)
    btn_exit.place(x=630, y=840)


def coordinate_field_creation():
    c.create_line(33, 510, 690, 510, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6")
    c.create_line(365, 820, 365, 185, fill='grey',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6")
    c.create_line(665, 210, 665, 810, fill='black',
                  width=1, dash=(5, 9))
    c.create_line(65, 810, 665, 810, fill='black',
                  width=1, dash=(5, 9))
    c.create_line(65, 210, 665, 210, fill='black',
                  width=1, dash=(5, 9))
    c.create_line(65, 210, 65, 810, fill='black',
                  width=1, dash=(5, 9))
    c.create_text(355, 520, text='0')

    # c.create_text(10, 190, text='X:')
    # c.create_text(110, 190, text='Y:')
    # c.create_text(438, 190, text='X:')
    # c.create_text(538, 190, text='Y:')
    # c.create_text(272, 842, text='X:', fill='green')
    # c.create_text(358, 842, text='Y:', fill='green')

    for i in range(65, 750, 50):
        c.create_line(i, 503, i, 520, fill='grey', width=2)
        c.create_line(i, 210, i, 810, fill='grey', width=1, dash=(1, 9))
        c.create_text(i, 530, text=f'{i - 365}' if i - 365 else '', fill='grey', tag='coord')

    for i in range(210, 820, 50):
        c.create_line(358, i, 372, i, fill='grey', width=2)
        c.create_line(65, i, 665, i, fill='grey', width=1, dash=(1, 9))
        c.create_text(345, i+10, text=f'{-(i - 510)}' if i - 510 else '', fill='grey', tag='coord')

    c.create_text(688, 498, text='X', font='Verdana 20', fill='green')
    c.create_text(380, 195, text='Y', font='Verdana 20', fill='green')


def radiobutton_creation():
    var.set(0)
    set0 = Radiobutton(text="➚", fg='black', variable=var, value=0)
    set1 = Radiobutton(text="➚", fg='black', variable=var, value=1)
    set0.place(x=405, y=97)
    set1.place(x=655, y=97)


def load_and_transf_coords(file):
    coords = []
    with open(file) as f:
        line = f.readline()
        while line:
            loc = list(map(float, line.strip('\n').strip(')').strip('(').split('; ')))
            loc = net_to_canv(loc[0], loc[1])
            coords.append(loc)
            line = f.readline()

    pol1 = [[-157, -116], [-206, -111], [-187, -157]]
    pol2 = [[177, -65], [182, -50], [188, -38], [205, -35]]
    for i in range(len(pol1)):
        pol1[i] = net_to_canv(pol1[i][0], pol1[i][1])
        coords.append(pol1[i])

    for i in range(len(pol2)):
        pol2[i] = net_to_canv(pol2[i][0], pol2[i][1])
        coords.append(pol2[i])

    return coords

def draw_fox(coords):
    c.create_line(coords[:-7], width=2, activefill='lightgreen', tag='fox')
    c.create_polygon(coords[-4:], width=2, activefill='lightgreen', tag='fox', fill='black')
    c.create_polygon(coords[-7:-4], width=2, activefill='lightgreen', tag='fox', fill='black')

def start_state():
    global story
    scale(200, 200)
    story = []
    clean_all()
    ent1.insert(0, 15)
    ent2.insert(0, 5)
    ent3.insert(0, 0)
    ent4.insert(0, 5)
    ent5.insert(0, 0)
    ent6.insert(0, 0)
    ent7.insert(0, 0)
    draw_fox(default_fox_coords)


c.bind('<1>', click)

text_and_labels_creation()
buttons_creation()
coordinate_field_creation()
radiobutton_creation()
default_fox_coords = load_and_transf_coords('data.txt')
fox_coords = load_and_transf_coords('data.txt')
draw_fox(default_fox_coords)

mmenu = Menu(window)
add_menu = Menu(mmenu)
add_menu.add_command(label='О программе и авторе',
                     command=lambda: messagebox.showinfo('О программе и авторе', TASK + AUTHOR))
add_menu.add_command(label='Выход', command=exit)
mmenu.add_cascade(label='About', menu=add_menu)
window.config(menu=mmenu)

c.pack()
window.mainloop()
