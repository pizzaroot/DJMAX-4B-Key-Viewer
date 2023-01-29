import keyboard, pygame
import win32gui
import win32con
import json
from datetime import datetime

state = [False, False, False, False]

events = [[], [], [], []]

f = open('keymap.txt')
keymap = json.load(f)
f.close()
velocity = float(open('velocity.txt', 'r').read())

def keydown(i):
    if i.name == keymap[0] and state[0] == False:
        state[0] = True
        events[0].append(i.time)
    if i.name == keymap[1] and state[1] == False:
        state[1] = True
        events[1].append(i.time)
    if i.name == keymap[2] and state[2] == False:
        state[2] = True
        events[2].append(i.time)
    if i.name == keymap[3] and state[3] == False:
        state[3] = True
        events[3].append(i.time)

def keyup(i):
    if i.name == keymap[0]:
        state[0] = False
        events[0].append(i.time)
    if i.name == keymap[1]:
        state[1] = False
        events[1].append(i.time)
    if i.name == keymap[2]:
        state[2] = False
        events[2].append(i.time)
    if i.name == keymap[3]:
        state[3] = False
        events[3].append(i.time)

keyboard.on_press_key(keymap[0], keydown)
keyboard.on_press_key(keymap[1], keydown)
keyboard.on_press_key(keymap[2], keydown)
keyboard.on_press_key(keymap[3], keydown)
keyboard.on_release_key(keymap[0], keyup)
keyboard.on_release_key(keymap[1], keyup)
keyboard.on_release_key(keymap[2], keyup)
keyboard.on_release_key(keymap[3], keyup)

def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Rhythm Game Key Viewer")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500,320))
     
    # define a variable to control the main loop
    running = True
    
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
 
    # main loop
    while running:
        curtime = datetime.now().timestamp()
        screen.fill((0,0,0))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        for i in range(4):
            for j in range(0, len(events[i]), 2):
                pygame.draw.rect(screen, (255,255,255), (i * 125, (curtime - events[i][j]) * 180 * velocity, 125, 15))
        pygame.display.update()

main()
