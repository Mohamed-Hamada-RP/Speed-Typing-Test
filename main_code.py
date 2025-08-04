import curses
from curses import wrapper
import time

wpm=0
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcom to my typing test test")
    stdscr.addstr("\npress any key to start")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)  
    
        
    for i,char in enumerate( current):
        correct_cahr=target[i]
        color =curses.color_pair(1)
        if char !=correct_cahr:
            color=curses.color_pair(2)

        stdscr.addstr(0,i,char, color)
        


def wpm_test(stdscr):
    target_text="Hello world this is some test text for this app"
    current_text=[]
    global wpm 

   

    start_time=time.time()
    stdscr.nodelay(True)
 

    while True:

        tiem_spend=  max(time.time()-start_time,1)
        wpm = round((len(current_text)/5)/(tiem_spend/60 ))

        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False )
            break

        try:
            key =stdscr.getkey()
        except:
            continue

        if key=="\x1b":
            break

        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)



def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    global wpm


    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        
        stdscr.addstr(8,0,f" you completed the text! press any key to continue and your WPM :{wpm}")
        key= stdscr.getkey()
        if key=="":
            break
        



wrapper(main)
