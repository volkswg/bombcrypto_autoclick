from time import sleep
import pyautogui
import os
import math


def enter_hunting():
    treasure_hunt_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "enterHuntingMap.PNG"))
    if treasure_hunt_btn is not None:
        print('>> Process: Enter Treasure Hunt')
        pyautogui.click(treasure_hunt_btn)


def re_enter_map():
    back_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "backToMenuBtn.PNG"))
    pyautogui.click(back_btn)
    sleep(0.3)
    enter_hunting()


def open_hero_menu():
    print('>> Process: Open Hero Menu')
    open_menu_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "openMenuTab.PNG"), confidence=0.50)
    while open_menu_btn is None:
        open_menu_btn = pyautogui.locateCenterOnScreen(os.path.join(
            "asset_matching", "openMenuTab.PNG"), confidence=0.50)
    pyautogui.click(open_menu_btn)

    sleep(0.8)
    hero_icon_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "heroIcon.PNG"))
    pyautogui.click(hero_icon_btn)
    sleep(2)


def close_hero_menu():
    print('>> Process: Close Hero Menu')
    close_menu_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "closeHeroBtn.PNG"))

    # print('click 1')
    pyautogui.moveTo(close_menu_btn)
    sleep(0.2)
    pyautogui.click()
    sleep(2)
    # print('click 2')
    pyautogui.click(close_menu_btn)


def work_all():
    open_hero_menu()
    print('>> Process: Work All')

    work_all_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "workAllBtn.PNG"))
    print(work_all_btn)
    if work_all_btn is not None:
        pyautogui.moveTo(work_all_btn)
        sleep(0.1)
        pyautogui.click()
        close_hero_menu()


def rest_all():
    open_hero_menu()
    print('>> Process: Rest All')

    work_all_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "restAllBtn.PNG"))
    print(work_all_btn)
    if work_all_btn is not None:
        pyautogui.moveTo(work_all_btn)
        sleep(0.1)
        pyautogui.click()
        close_hero_menu()


def common_work(all_hero_count=15):
    open_hero_menu()
    work_btn = pyautogui.locateAllOnScreen(os.path.join(
        "asset_matching", "workBtnNotActive.PNG"), confidence=0.865)
    first_work_btn_ypos = None
    last_work_btn_ypos = None
    for index, pos in enumerate(work_btn):
        if index == 0:
            first_work_btn_ypos = pos.top + (pos.width / 2)
            work_btn_xpos = pos.left + (pos.width / 2)
        last_work_btn_ypos = pos.top + (pos.width / 2)

    loop_scroll_count = math.ceil(all_hero_count/5)
    for i in range(0, loop_scroll_count):
        common_label_list = list(pyautogui.locateAllOnScreen(os.path.join(
            "asset_matching", "commonLabelComb.PNG"), confidence=0.9))
        # print(common_label_list)
        for index, pos in enumerate(common_label_list):
            x = work_btn_xpos
            y = pos.top
            pyautogui.moveTo(x, y)
            sleep(0.1)
            pyautogui.click()
            sleep(0.2)
        if loop_scroll_count-1 != i:
            pyautogui.moveTo(work_btn_xpos, last_work_btn_ypos)
            pyautogui.dragTo(work_btn_xpos, first_work_btn_ypos,
                             1.2, button='left')
            sleep(3.5)
    close_hero_menu()
