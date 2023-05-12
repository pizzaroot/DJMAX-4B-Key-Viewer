import keyboard, pygame
import win32gui
import win32con
import json
from datetime import datetime

state8 = [False, False, False, False, False, False, False, False]
state6 = [False, False, False, False, False, False]
state5 = [False, False, False, False, False, False]
state4 = [False, False, False, False]

events8 = [[], [], [], [], [], [], [], []]
events6 = [[], [], [], [], [], []]
events5 = [[], [], [], [], [], []]
events4 = [[], [], [], []]

mode = 4

f = open('keymap8.txt')
keymap8 = json.load(f)
f.close()
f = open('keymap4.txt')
keymap4 = json.load(f)
f.close()
f = open('keymap5.txt')
keymap5 = json.load(f)
f.close()
f = open('keymap6.txt')
keymap6 = json.load(f)
f.close()

last = 0
diff = 0
velocity = float(open('velocity.txt', 'r').read())
def keydown(i):
    global last, diff
    if mode == 8:
        for j in range(8):
            if i.name.lower() == keymap8[j] and state8[j] == False:
                state8[j] = True
                if i.time - last > 2:
                    diff = 0
                    last = i.time
                elif i.time - last > 0.02:
                    diff = i.time - last
                    last = i.time
                events8[j].append(i.time)
    if mode == 4:
        for j in range(4):
            if i.name.lower() == keymap4[j] and state4[j] == False:
                state4[j] = True
                if i.time - last > 2:
                    diff = 0
                    last = i.time
                elif i.time - last > 0.02:
                    diff = i.time - last
                    last = i.time
                events4[j].append(i.time)
    if mode == 6:
        for j in range(6):
            if i.name.lower() == keymap6[j] and state6[j] == False:
                state6[j] = True
                if i.time - last > 2:
                    diff = 0
                    last = i.time
                elif i.time - last > 0.02:
                    diff = i.time - last
                    last = i.time
                events6[j].append(i.time)
    if mode == 5:
        for j in range(6):
            if i.name.lower() == keymap5[j] and state5[j] == False:
                state5[j] = True
                if i.time - last > 2:
                    diff = 0
                    last = i.time
                elif i.time - last > 0.02:
                    diff = i.time - last
                    last = i.time
                events5[j].append(i.time)

def keyup(i):
    if mode == 8:
        for j in range(8):
            if i.name.lower() == keymap8[j]:
                state8[j] = False
                events8[j].append(i.time)
    if mode == 4:
        for j in range(4):
            if i.name.lower() == keymap4[j]:
                state4[j] = False
                events4[j].append(i.time)
    if mode == 5:
        for j in range(6):
            if i.name.lower() == keymap5[j]:
                state5[j] = False
                events5[j].append(i.time)
    if mode == 6:
        for j in range(6):
            if i.name.lower() == keymap6[j]:
                state6[j] = False
                events6[j].append(i.time)

dic = {}

for i in range(6):
    dic[keymap5[i]] = True
    dic[keymap6[i]] = True
for i in range(4):
    dic[keymap4[i]] = True
for i in range(8):
    dic[keymap8[i]] = True

for key in dic:
    keyboard.on_press_key(key, keydown)
    keyboard.on_release_key(key, keyup)

def reset(m):
    global state8, state4, state6, state5, events8, events4, events6, events5, mode
    state8 = [False, False, False, False, False, False, False, False]
    state6 = [False, False, False, False, False, False]
    state5 = [False, False, False, False, False, False]
    state4 = [False, False, False, False]

    events8 = [[], [], [], [], [], [], [], []]
    events6 = [[], [], [], [], [], []]
    events5 = [[], [], [], [], [], []]
    events4 = [[], [], [], []]

    mode = m

keyboard.add_hotkey('alt+1', reset, args=[4])
keyboard.add_hotkey('alt+2', reset, args=[5])
keyboard.add_hotkey('alt+3', reset, args=[6])
keyboard.add_hotkey('alt+4', reset, args=[8])

def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Rhythm Game Key Viewer")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((504,330))
    font = pygame.font.SysFont("Arial", 30)
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
        if mode == 8:
            for i in range(2):
                for j in range(0, len(events8[i + 6]), 2):
                    pygame.draw.rect(screen, (255,0,0), (i * 252, (curtime - events8[i + 6][j]) * 282 * velocity, 252, 15))
            for i in range(6):
                for j in range(0, len(events8[i]), 2):
                    if i % 3 == 1:
                        pygame.draw.rect(screen, (0,0,255), (i * 84, (curtime - events8[i][j]) * 282 * velocity, 84, 15))
                    else:
                        pygame.draw.rect(screen, (255,255,255), (i * 84, (curtime - events8[i][j]) * 282 * velocity, 84, 15))
        elif mode == 6:
            for i in range(6):
                for j in range(0, len(events6[i]), 2):
                    if i % 3 == 1:
                        pygame.draw.rect(screen, (0,0,255), (i * 84, (curtime - events6[i][j]) * 282 * velocity, 84, 15))
                    else:
                        pygame.draw.rect(screen, (255,255,255), (i * 84, (curtime - events6[i][j]) * 282 * velocity, 84, 15))
        elif mode == 4:
            for i in range(4):
                for j in range(0, len(events4[i]), 2):
                    if i == 1 or i == 2:
                        pygame.draw.rect(screen, (0,0,255), (i * 126, (curtime - events4[i][j]) * 282 * velocity, 126, 15))
                    else:
                        pygame.draw.rect(screen, (255,255,255), (i * 126, (curtime - events4[i][j]) * 282 * velocity, 126, 15))
        elif mode == 5:
            for i in range(2):
                for j in range(0, len(events5[i]), 2):
                    if i == 1:
                        pygame.draw.rect(screen, (0,0,255), (i * 101, (curtime - events5[i][j]) * 282 * velocity, 101, 15))
                    else:
                        pygame.draw.rect(screen, (255,255,255), (i * 101, (curtime - events5[i][j]) * 282 * velocity, 101, 15))
            for i in range(2):
                for j in range(0, len(events5[i + 2]), 2):
                    pygame.draw.rect(screen, (255,255,255), (i * 50 + 202, (curtime - events5[i + 2][j]) * 282 * velocity, 50, 15))
            for i in range(2):
                for j in range(0, len(events5[i + 4]), 2):
                    if i == 0:
                        pygame.draw.rect(screen, (0,0,255), (i * 101 + 302, (curtime - events5[i + 4][j]) * 282 * velocity, 101, 15))
                    else:
                        pygame.draw.rect(screen, (255,255,255), (i * 101 + 302, (curtime - events5[i + 4][j]) * 282 * velocity, 101, 15))

        text = font.render(str(int(diff * 1000)) + " ms", True, (255, 255, 255))
        screen.blit(text, [10, 10])
        pygame.display.update()

main()
