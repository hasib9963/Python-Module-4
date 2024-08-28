import pyautogui
def draw_pyramid(n):
    for i in range(n):
        print("#" * (i + 1))
        pyautogui.typewrite("#" * (i + 1))
n = int(input())
draw_pyramid(n)
