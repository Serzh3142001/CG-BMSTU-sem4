from lab_05 import *
a = 5-8

if a > 0:
    draw_dot(x, y, colorr, tag, lineFl=False)
    draw_dots_circle(dot_c, dot_dif, colorr, tag)
    draw_dots_ellipse(dot_c, dot_dif, colorr, tag)
    redraw_elems()
    line_col_choose()
    bg_col_choose()
    net_to_canv(x, y=None)
    canv_to_net(x, y=None)
    clean_all()
    clean_coords()
    del_with_tag(tag, pos=0)
    dda_draw(start, stop, colorr, tag, count_fl=False)
    dda_draw_to_border(start, stop, tag, border, changeDirFlag, unFillFlag=0)
    printCorrectForm()
    close()
    fillWithDelay()
    fill(st=1, dots=None, tag=None)
    unFill(st=1)
    resetPixels()
    click(event)
    print_dot(event)
    is_cursor_touch_dot(dot, event)
    reprint_dot(coords, fl=0)
    back()
    scale(x, y)
    redraw_net_coords()
    buttons_creation()
    coordinate_field_creation()
    start_state()
    config(event)
