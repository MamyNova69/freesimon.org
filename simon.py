import time
import pyautogui
import keyboard
import win32api, win32con


# This script can play https://freesimon.org/, adapt the xy value of each color to your screen

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# x and y value of each color on the game
red = [1727, 432]
green = [2117, 443]
blue = [1689, 776]
yellow = [2149, 761]

# a color is pressed if "red>190" carful not to triger red color with mouse, see offset

# find what key is pressed and save the new variable in a list :
def find_simon_says():
    global nombre_element_dans_liste
    global listen
    global count

    if pyautogui.pixel(red[0],red[1])[0] > 190 :
        while pyautogui.pixel(red[0],red[1])[0] > 190:
            time.sleep(0.01)
        print("red")
        count += 1
        if count > nombre_element_dans_liste:
            color_to_press.append("red")
            listen = False
        nombre_element_dans_liste = len(color_to_press)

    if pyautogui.pixel(green[0],green[1])[0] > 190 :
        while pyautogui.pixel(green[0],green[1])[0] > 190:
            time.sleep(0.01)
        print("green")
        count += 1
        if count > nombre_element_dans_liste:
            color_to_press.append("green")
            listen = False
        nombre_element_dans_liste = len(color_to_press)

    if pyautogui.pixel(blue[0],blue[1])[0] > 190 :
        while pyautogui.pixel(blue[0],blue[1])[0] > 190:
            time.sleep(0.01)
        print("blue")
        count += 1
        if count > nombre_element_dans_liste:
            color_to_press.append("blue")
            listen = False
        nombre_element_dans_liste = len(color_to_press)

    if pyautogui.pixel(yellow[0],yellow[1])[0] > 190 :
        while pyautogui.pixel(yellow[0],yellow[1])[0] > 190:
            time.sleep(0.01)
        print("yellow")
        count += 1
        if count > nombre_element_dans_liste:
            color_to_press.append("yellow")
            listen = False
        nombre_element_dans_liste = len(color_to_press)

    return count, listen

# liste des couleurs à mémoriser
color_to_press =[]

# compteur longeur de la liste
count = 0
nombre_element_dans_liste = len(color_to_press)
listen = True

# cliquer sur les couleurs de la liste avec 1 ou 2 secondes entre chaque clique
offset = 20

# start the game
click(1847, 1069)
time.sleep(0.2)
click(1847, 1069)



# play the game
while 1:
    if listen :
        find_simon_says()
    else :
        print(f"Voici la liste des couleurs à entrer {color_to_press}, le bot va jouer dans 1 sec")
        time.sleep(1)
        for color in color_to_press:
            if color == "red":
                click(red[0] + offset ,red[1] + offset)
                time.sleep(0.3)
            if color == "blue":
                click(blue[0] + offset ,blue[1] + offset)
                time.sleep(0.3)
            if color == "green":
                click(green[0] + offset ,green[1] + offset)
                time.sleep(0.3)
            if color == "yellow":
                click(yellow[0] + offset ,yellow[1] + offset)
                time.sleep(0.3)
        time.sleep(0.01)
        listen = True
        count = 0
