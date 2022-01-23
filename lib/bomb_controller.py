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
    sleep(0.2)
    enter_hunting()


def open_hero_menu():
    print('>> Process: Open Hero Menu')
    open_menu_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "openMenuTab.PNG"), confidence=0.50)
    while open_menu_btn is None:
        open_menu_btn = pyautogui.locateCenterOnScreen(os.path.join(
            "asset_matching", "openMenuTab.PNG"), confidence=0.50)
    pyautogui.moveTo(x=open_menu_btn.x, y=open_menu_btn.y+2)
    pyautogui.click()

    sleep(1.7)
    hero_icon_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "heroIcon.PNG"), confidence=0.85)
    pyautogui.moveTo(hero_icon_btn)
    pyautogui.click()
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

    rest_all_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "restAllBtn.PNG"))
    # print(rest_all_btn)
    if rest_all_btn is not None:
        pyautogui.moveTo(rest_all_btn)
        sleep(0.1)
        pyautogui.click()
        sleep(0.2)
    close_hero_menu()


def locate_work_btn():
    work_btn = pyautogui.locateAllOnScreen(os.path.join(
        "asset_matching", "workBtnNotActive.PNG"), confidence=0.865)
    first_work_btn_ypos = None
    last_work_btn_ypos = None
    for index, pos in enumerate(work_btn):
        if index == 0:
            first_work_btn_ypos = pos.top + (pos.width / 2)
            work_btn_xpos = pos.left + (pos.width / 2)
        last_work_btn_ypos = pos.top + (pos.width / 2)
    return [work_btn_xpos, first_work_btn_ypos, last_work_btn_ypos]


def scroll_hero_page(xpos_from, xpos_to, ypos_from, ypos_to, speed=1.15):
    pyautogui.moveTo(xpos_from, ypos_from)
    pyautogui.dragTo(xpos_to, ypos_to,
                     speed, button='left')


def get_hero_rarity_pos(rarity='common'):
    rarity_label_file_name = ''
    confidence_rate = 0
    if rarity == 'common':
        rarity_label_file_name = 'commonLabelComb.PNG'
        confidence_rate = 0.91
    elif rarity == 'rare':
        rarity_label_file_name = 'rareLabel.PNG'
        confidence_rate = 0.975
    elif rarity == 'superrare':
        rarity_label_file_name = 'superRareLabel.PNG'
        confidence_rate = 0.97
    else:
        rarity_label_file_name = 'commonLabelComb.PNG'
        confidence_rate = 0.9
    # print(rarity_label_file_name, confidence_rate)
    ret_pos = (list(pyautogui.locateAllOnScreen(os.path.join(
        "asset_matching", rarity_label_file_name), confidence=confidence_rate)))
    return ret_pos


def wake_hero(all_hero_count=15, hero_rarity=['all']):
    if 'all' in hero_rarity:
        work_all()
        return
    open_hero_menu()
    print('>> Process: Wake hero_rarity Up')
    [work_btn_xpos, first_work_btn_ypos, last_work_btn_ypos] = locate_work_btn()
    loop_scroll_count = math.ceil(all_hero_count/5)

    for i in range(0, loop_scroll_count):
        hero_pos = []
        for e_rarity in hero_rarity:
            hero_pos += get_hero_rarity_pos(e_rarity)

        def sortTop(e):
            return e.top
        hero_pos.sort(key=sortTop)

        for index, pos in enumerate(hero_pos):
            x = work_btn_xpos
            y = pos.top
            pyautogui.moveTo(x, y)
            sleep(0.05)
            pyautogui.click()
            sleep(0.5)
        if loop_scroll_count-1 != i:
            scroll_hero_page(work_btn_xpos, work_btn_xpos,
                             last_work_btn_ypos, first_work_btn_ypos)
            sleep(3.5)
    close_hero_menu()
    sleep(2)


def check_all_rest():
    print('>> Checking: All Hero Rest')
    open_hero_menu()
    rest_all_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "restAllBtn.PNG"))
    close_hero_menu()
    if rest_all_btn is not None:
        # print('>> Checking: Not All Rest')
        return False
    else:
        # print('>> Checking: All Rest')
        return True
