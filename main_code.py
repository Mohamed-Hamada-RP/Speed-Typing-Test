import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcom to my typing test test")
    stdscr.addstr("\npress any key to start")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, target, curses.color_pair(3)) 
    stdscr.addstr(3, 0, f"WPM: {wpm}", curses.color_pair(3)) 

 
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def wpm_test(stdscr):
    target_text="Hello world this is some test text for this app"
    current_text=[]
    wpm=0 

    stdscr.clear()
    stdscr.addstr(target_text)  
    stdscr.refresh()
    start_time=time.time()
    stdscr.nodelay(True)
 

    while True:

        tiem_spend=  max(time.time()-start_time,1)
        wpm=round((len(current_text)/5)/(tiem_spend/60 ))

        display_text(stdscr, target_text, current_text, wpm)
        stdscr.move(0, len(current_text))  # Keep the cursor at the end
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False )
            break
        try:
            key =stdscr.getkey()
        except:
            continue

        if isinstance(key, str) and len(key) == 1 and ord(key) == 27:
            break


        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)



def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        try:
            key= stdscr.getkey()
            if key=="\x1b":
                break
        except:
            continue



wrapper(main)