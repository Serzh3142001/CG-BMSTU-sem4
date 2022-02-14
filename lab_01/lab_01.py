from tkinter import *
import tkinter.messagebox as box

root = Tk()
var = IntVar()

sz = 1

combinations = []
true_combs = []
c = Canvas(root, width=700, height=900, bg='white')
c.create_rectangle(4, 32, 161, 172, outline='black', width=2)
text1 = Text(width=21, height=10)
ent1 = Entry(width=8)
ent2 = Entry(width=8)
ent1.place(x=32, y=177)
ent2.place(x=132, y=177)

def clean_tri():
    triangls = c.find_withtag('triang')
    for tri in triangls:
        c.delete(tri)

def clean_coords():
    coords = c.find_withtag('coord')
    for cor in coords:
        c.delete(cor)

def clean_all():
    dotts = c.find_withtag('dot')
    for dot in dotts:
        c.delete(dot)
    text1.delete(1.0, END)
    clean_tri()

def add_dot():
    d1 = ent1.get()
    d2 = ent2.get()

    try:
        d1 = float(d1)
        d2 = float(d2)
        text1.insert(END, f'({d1:g}; {d2:g})\n')
        dots_update()
    except:
        box.showinfo('Error', 'Некорректные координаты!1')

def select_all():
    text1.tag_add(SEL, "1.0", END)
    text1.mark_set(INSERT, "1.0")
    text1.see(INSERT)

def tri_click(event, tag):
    triangls = list(c.find_withtag('triang'))
    triangls.remove(tag)
    for tri in triangls:
        c.delete(tri)

def is_cursor_touch_triang(tri, event):
    coo = c.coords(tri)[:-2]

    x0, y0 = event.x, event.y
    x1, y1 = int(coo[0]), int(coo[1])
    x2, y2 = int(coo[2]), int(coo[3])
    x3, y3 = int(coo[4]), int(coo[5])

    d1 = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    d2 = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
    d3 = ((x0 - x3) ** 2 + (y0 - y3) ** 2) ** 0.5

    a1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    a2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    a3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

    cos1 = (d1 ** 2 + d2 ** 2 - a1 ** 2) / 2 / d1 / d2
    cos2 = (d2 ** 2 + d3 ** 2 - a2 ** 2) / 2 / d2 / d3
    cos3 = (d1 ** 2 + d3 ** 2 - a3 ** 2) / 2 / d1 / d3

    if abs(cos1 + 1) < 1e-3 or abs(cos2 + 1) < 1e-3 or abs(cos3 + 1) < 1e-3:
        return 1
    else:
        return 0

def click(event):
    # print(text1.index(INSERT))
    # if event.x >= 4 and event.y >= 32 and event.x <= 161 and event.y <= 172:
    #     select_all()
    if event.x < 65 or event.x > 665 or event.y < 210 or event.y > 810:
        return

    print_dot(event)
    # text1.insert(END, f'({event.x}; {event.y}), \n')
    crds = canv_to_net(event.x, event.y)
    text1.insert(END, f'({crds[0]:g}; {crds[1]:g})\n')

    # if var.get():
    #     flag2 += 1
    #     text2.insert(END, f'({event.x - 40}; {event.y - 210}), \n' if flag2 % 3 == 0 \
    #                  else f'({event.x - 40}; {event.y - 210}), ')
    # else:
    #     flag1 += 1
    #     text1.insert(END, f'({event.x - 40}; {event.y - 210}), \n' if flag1 % 3 == 0 \
    #                  else f'({event.x - 40}; {event.y - 210}), ')

def print_dot(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    if var.get():
        c.create_oval(x1, y1, x2, y2, outline='blue', fill='blue', tag='dot')
    else:
        c.create_oval(x1, y1, x2, y2, outline='red', fill='red', tag='dot')

def dots_update():
    sett = text1.get(1.0, END).split('\n')[:-1]

    if not sett[-1]:
        sett = sett[:-1]

    dotts = c.find_withtag('dot')
    clean_tri()

    for dot in dotts:
        c.delete(dot)

    try:
        xs = []
        ys = []
        for dot in sett:
            x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
            xs.append(abs(x))
            ys.append(abs(y))
        max_x, max_y = max(xs), max(ys)
        scale(max_x, max_y)
    except:
        box.showinfo('Error', 'Некорректные координаты!2')
        return


    for dot in sett:
        x, y = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
        x, y = net_to_canv(x, y)
        x2, y2 = x + 2, y + 2
        x -= 2
        y -= 2
        c.create_oval(round(x), round(y), round(x2), round(y2), outline='red', fill='red', tag='dot')

    triang_find_and_draw(0)


def is_dot_in_triang(dot, tri):
    a, b, c = tri
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    x0, y0 = dot
    k1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
    k2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
    k3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
    if k1 > 0 and k2 > 0 and k3 > 0 or k1 < 0 and k2 < 0 and k3 < 0:
        return True

    return False


def is_triangls_intesected(tri1, tri2):
    for i in range(3):
        if is_dot_in_triang(tri1[i], tri2):
            return True

    for i in range(3):
        if is_dot_in_triang(tri2[i], tri1):
            return True

    return False

def draw_triang(tri):
    buf_tr = []
    for i in range(3):
        buf_tr.append(net_to_canv(tri[i][0], tri[i][1]))

    c.create_line(buf_tr[0], buf_tr[1], buf_tr[2], buf_tr[0], fill='green', width=2,
                                  activefill='lightgreen', tag='triang')

def form_all_triang_combinations(dots):
    if not len(dots):
        return

    for i in range(len(dots) - 2):
        for j in range(i + 1, len(dots) - 1):
            for k in range(j + 1, len(dots)):
                a = dots[:]
                del a[i], a[j - 1], a[k - 2]
                buf = (dots[i], dots[j], dots[k])
                combinations.append(buf)
                # del dots[i], dots[j], dots[k]
                form_all_triang_combinations(a)
                # combinations.insert(i, buf[0])
                # combinations.insert(j, buf[1])
                # combinations.insert(k, buf[2])

def form_all_true_combinations(triangs):
    if not len(triangs):
        return

    for i in range(len(triangs)):
        a = triangs[:]
        del a[i]
        for tri in true_combs:
            if not is_triangls_intesected(tri, triangs[i])
        true_combs.append(triangs[i])
        # del dots[i], dots[j], dots[k]
        form_all_true_combinations(a)
        # combinations.insert(i, buf[0])
        # combinations.insert(j, buf[1])
        # combinations.insert(k, buf[2])

def triang_find_and_draw(check=1):
    global combinations
    # dots_update()
    sett = text1.get(1.0, END).split('\n')[:-1]

    if not sett[-1]:
        sett = sett[:-1]

    if check:
        if len(sett) % 3:
            box.showinfo('Error', 'Число точек должно быть кратно 3м!')
            return

        set1_t = []
        for dot in sett:
            x1, y1 = map(float, dot.strip('\n').strip(')').strip('(').split(';'))
            set1_t.append((x1, y1))

        combinations = []
        form_all_triang_combinations(set1_t)
        print(len(combinations), combinations)


    # for i in range(len(combinations) - 1):
    #     for j in range(i + 1, len(combinations)):
    #         if not is_triangls_intesected(combinations[i], combinations[j]):
    #             true_combs.append()

        for tri in combinations:
            draw_triang(tri)

    # for i in range(len(set1_t) - 2):
    #     for j in range(i + 1, len(set1_t) - 1):
    #         for k in range(j + 1, len(set1_t)):
    #             # a = set1_t[:]
    #             # del a[i], a[j - 1], a[k - 2]
    #             if is_dot_in_triang(a, set1_t[i], set1_t[j], set1_t[k]):
    #                 c.create_line(set1_t[i], set1_t[j], set1_t[k], set1_t[i], fill='green', width=2,
    #                               activefill='lightgreen', tag='triang')

def text_and_labels_creation():
    text1.place(x=20, y=33)
    scroll = Scrollbar(command=text1.yview)
    scroll.pack(side=LEFT, fill=Y)
    text1.config(yscrollcommand=scroll.set)

    label1 = Label(text='Множество точек:', font='Arial 15')
    label1.place(x=13, y=5)

def buttons_creation():
    btn_upd = Button(root, text='🔄', fg='green', command=lambda: dots_update())
    btn_add = Button(root, text='добавить', fg='green', command=lambda: add_dot())
    btn_tri = Button(root, text='найти ΔΔ', fg='blue', command=lambda: triang_find_and_draw())
    btn_cl_tri = Button(root, text='🗑ΔΔ', fg='orange', command=lambda: clean_tri())
    btn_cl_all = Button(root, text='🗑всё', fg='orange', command=lambda: clean_all())
    btn_exit = Button(root, text=' выход ', fg='red', command=exit)
    btn_cl_tri.place(x=290, y=140)
    btn_add.place(x=220, y=180)
    btn_cl_all.place(x=365, y=140)
    btn_upd.place(x=290, y=180)
    btn_tri.place(x=327, y=110)
    btn_exit.place(x=650, y=840)

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

def net_to_canv(x, y):
    global sz
    # prev_sz = sz
    center = (365, 510)
    # while x > -150*sz and x < 150*sz and y > -150*sz and y < 150*sz:
    #     sz /= 2
    #
    # while x < -300*sz or x > 300*sz or y < -300*sz or y > 300*sz:
    #     sz *= 2
    #
    # if sz != prev_sz:
    #     redraw()

    return round(x/sz + center[0]), round(center[1] - y/sz)

def canv_to_net(x, y):
    global sz
    center = (365, 510)

    return round((x - center[0])*sz, 3), round((center[1] - y)*sz, 3)

def redraw():
    global sz
    clean_coords()
    max_len = 0
    for i in range(65, 670, 50):
        if len(f'{round((i - 365)*sz, 3):g}') > max_len:
            max_len = len(f'{round((i - 365)*sz, 3):g}')

    for i in range(65, 670, 50):
        c.create_text(i, 530, text=f'{round((i - 365)*sz, 3):g}' if i - 365 else '', tag='coord', font='Verdana 8' if max_len > 6 else 'Verdana 12')

    for i in range(210, 820, 50):
        c.create_text(345, i + 10, text=f'{round(-(i - 510)*sz, 3):g}' if i - 510 else '', tag='coord')

def coordinate_field_creation():
    c.create_line(33, 510, 690, 510, fill='black',
                  width=3, arrow=LAST,
                  activefill='lightgreen',
                  arrowshape="10 20 6")
    c.create_line(365, 820, 365, 185, fill='black',
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

    c.create_text(10, 190, text='X:')
    c.create_text(110, 190, text='Y:')

    for i in range(65, 750, 50):
        c.create_line(i, 503, i, 520, fill='black', width=2)
        c.create_line(i, 210, i, 810, fill='black', width=1, dash=(1, 9))
        c.create_text(i, 530, text=f'{i - 365}' if i - 365 else '', tag='coord')

    for i in range(210, 820, 50):
        c.create_line(358, i, 372, i, fill='black', width=2)
        c.create_line(65, i, 665, i, fill='black', width=1, dash=(1, 9))
        c.create_text(345, i+10, text=f'{-(i - 510)}' if i - 510 else '', tag='coord')

    c.create_text(688, 498, text='X', font='Verdana 20', fill='green')
    c.create_text(380, 195, text='Y', font='Verdana 20', fill='green')


c.bind('<1>', click)

text_and_labels_creation()
buttons_creation()
coordinate_field_creation()

# ent1.insert(0, '0')
# ent2.insert(0, '0')

c.pack()
root.mainloop()
