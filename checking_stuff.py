# import keyboard
#
# selected = 1
#
# def show_menu():
#     global selected
#     print("\n" * 30)
#     print("Choose an option:")
#     for i in range(1, 5):
#         print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))
#
# def up():
#     global selected
#     if selected == 1:
#         return
#     selected -= 1
#     show_menu()
#
# def down():
#     global selected
#     if selected == 4:
#         return
#     selected += 1
#     show_menu()
#
# show_menu()
# keyboard.add_hotkey('up', up)
# keyboard.add_hotkey('down', down)
# keyboard.wait()

import curses

classes = ["The sneaky thief", "The smarty wizard", "The proletariat"]


def character(stdscr):
    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0  # last character read
    option = 0  # the current option that is marked
    while c != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr("What is your class?\n", curses.A_UNDERLINE)
        for i in range(len(classes)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}. ".format(i + 1))
            stdscr.addstr(classes[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1

    stdscr.addstr("You chose {0}".format(classes[option]))
    stdscr.getch()

curses.wrapper(character)