from time import sleep
import pyautogui
import os
import math
import datetime
from lib.process_logging import print_log

# for private use ===========================================================================


def wait_until_found(image_name, confidence=1):
    obj_pos = None
    while obj_pos is None:
        check_error_occur()
        obj_pos = pyautogui.locateCenterOnScreen(os.path.join(
            "asset_matching", image_name), confidence=confidence)
        # print('obj_pos', image_name, obj_pos)
    return obj_pos


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


def scroll_hero_page(xpos_from, xpos_to, ypos_from, ypos_to, duration=1.17):
    pyautogui.moveTo(xpos_from, ypos_from)
    pyautogui.dragTo(xpos_to, ypos_to,
                     duration, button='left')


def get_hero_rarity_pos(rarity='common'):
    rarity_label_file_name = ''
    confidence_rate = 0
    if rarity == 'common':
        rarity_label_file_name = 'commonLabelComb.PNG'
        confidence_rate = 0.9118
    elif rarity == 'rare':
        rarity_label_file_name = 'rareLabel.PNG'
        confidence_rate = 0.97
    elif rarity == 'superrare':
        rarity_label_file_name = 'superRareLabel.PNG'
        confidence_rate = 0.965
    else:
        rarity_label_file_name = 'commonLabelComb.PNG'
        confidence_rate = 0.9
    # print(rarity_label_file_name, confidence_rate)
    ret_pos = (list(pyautogui.locateAllOnScreen(os.path.join(
        "asset_matching", rarity_label_file_name), confidence=confidence_rate)))
    return ret_pos


def remove_dup_top_value(pos_list):
    pos_result = []
    top_list = []
    for pos in pos_list:
        top_val = pos.top
        if top_val not in top_list:
            top_list.append(top_val)
            pos_result.append(pos)
    return pos_result

# for private use ===========================================================================


def enter_hunting():
    treasure_hunt_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "enterHuntingMap.PNG"), confidence=0.9)
    if treasure_hunt_btn is not None:
        print('>> Process: Enter Treasure Hunt')
        pyautogui.moveTo(treasure_hunt_btn)
        sleep(0.2)
        pyautogui.click()


def re_enter_map():
    print_log('Menu', 'Re-Enter Treasure Hunt')
    back_btn = wait_until_found("backToMenuBtn.PNG", 0.9)

    pyautogui.moveTo(back_btn)
    sleep(0.1)
    pyautogui.click()
    sleep(1)
    enter_hunting()


def open_hero_menu():
    print_log('Menu', 'Open Hero Menu')
    open_menu_btn = wait_until_found('openMenuTab.PNG', 0.5)
    pyautogui.moveTo(x=open_menu_btn.x, y=open_menu_btn.y+5)
    check_error_occur()
    pyautogui.click()
    sleep(0.8)

    hero_icon_btn = wait_until_found('heroIcon.PNG', 0.85)
    pyautogui.moveTo(hero_icon_btn)
    check_error_occur()
    pyautogui.click()

    # check open heroes menu success
    print_log('Menu', 'Checking Open Heroes Success')
    wait_until_found("workBtnNotActive.PNG", 0.865)
    sleep(0.8)


def close_hero_menu():
    print_log('Menu', 'Close Hero Menu')
    close_menu_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "closeHeroBtn.PNG"), confidence=0.9)

    # print('click 1')
    pyautogui.moveTo(close_menu_btn)
    sleep(0.2)
    pyautogui.click()
    sleep(2.5)
    # print('click 2')
    pyautogui.click(close_menu_btn)


def work_all():
    open_hero_menu()
    ct = datetime.datetime.now()
    print(ct, '>> Process: Work All')

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
    print_log('Heroes', 'Rest All')

    rest_all_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "restAllBtn.PNG"), confidence=0.9)
    print(rest_all_btn)
    if rest_all_btn is not None:
        pyautogui.moveTo(rest_all_btn)
        sleep(0.1)
        pyautogui.click()
        sleep(0.2)
    close_hero_menu()


def wake_hero(all_hero_count=15, hero_rarity=['all']):
    hero_str_log = ','.join(hero_rarity)
    print_log('Heroes', f'Wake {hero_str_log} Up')
    if 'all' in hero_rarity:
        work_all()
        return
    open_hero_menu()

    # rest all heroes before wake them up =============
    print_log('Heroes', 'Rest All')
    rest_all_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "restAllBtn.PNG"), confidence=0.9)
    if rest_all_btn is not None:
        print_log('System', 'Click Rest All Button')

        pyautogui.moveTo(rest_all_btn)
        sleep(0.1)
        pyautogui.click()
        sleep(0.2)
    else:
        print_log('System', 'Rest All Button Not Found')
    # rest all heroes before wake them up =============

    [work_btn_xpos, first_work_btn_ypos, last_work_btn_ypos] = locate_work_btn()
    loop_scroll_count = math.ceil(all_hero_count/5)

    for i in range(0, loop_scroll_count):
        hero_pos = []
        for e_rarity in hero_rarity:
            hero_pos += get_hero_rarity_pos(e_rarity)

        def sortTop(e):
            return e.top
        hero_pos.sort(key=sortTop)
        hero_pos = remove_dup_top_value(hero_pos)
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
    print_log('Heroes', 'Checking All Heroes Rest')
    open_hero_menu()
    rest_all_btn = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "restAllBtn.PNG"), confidence=0.90)
    print('rest_all_btn', rest_all_btn)
    close_hero_menu()
    if rest_all_btn is not None:
        # print('>> Checking: Not All Rest')
        return False
    else:
        # print('>> Checking: All Rest')
        return True


def check_error_occur():
    # print_log('System', 'Checking Error Occur')
    error_dialog = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "errorDialog.PNG"), confidence=0.9)

    if error_dialog is not None:
        error_handling()
        return True
    else:
        # print('>> Checking: All Rest')
        return False


def error_handling():
    print_log('Error', 'Error Occur')
    print_log('Menu', 'Back to login page')
    error_dialog = pyautogui.locateCenterOnScreen(os.path.join(
        "asset_matching", "errorDialog.PNG"))
    pyautogui.moveTo(error_dialog)
    sleep(0.1)
    pyautogui.click()
    print_log('System', 'Click Ok')
    sleep(1)

    print_log('System', 'Find Connect Wallet')
    connect_wallet_btn = wait_until_found("connectWallet.PNG", 0.8)
    print_log('System', 'Click Connect Wallet')
    pyautogui.moveTo(connect_wallet_btn)
    sleep(0.1)
    pyautogui.click()
    sleep(7)

    print_log('System', 'Find Metamask Sign')
    metamask_login_btn = wait_until_found("metamaskSignin.PNG", 0.9)
    pyautogui.moveTo(metamask_login_btn)
    sleep(0.1)
    pyautogui.click()

    treasure_hunt_btn = wait_until_found("enterHuntingMap.PNG", 0.98)
    pyautogui.moveTo(treasure_hunt_btn)
    sleep(0.1)
    pyautogui.click()
