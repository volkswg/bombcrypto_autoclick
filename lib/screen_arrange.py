import pygetwindow as gw


def get_bomb_wins_list():
    all_wins = gw.getAllTitles()
    bomb_wins_title = [
        e_title for e_title in all_wins if 'Bombcrypto' in e_title]
    bomb_wins_title_count = len(bomb_wins_title)
    if bomb_wins_title_count > 0:
        bomb_wins_obj = gw.getWindowsWithTitle(bomb_wins_title[0])
        return bomb_wins_obj
    return None


def arrange_bomb_wins(bomb_wins_obj, width=850, height=700):
    if bomb_wins_obj is not None:
        print('>> Setup Screen: Start Arrange Windows')
        print('>> Setup Screen: Please Set Zoom to 67%')
        for index, e_bomb_window in enumerate(bomb_wins_obj):
            win_x_pos = (width-15)*index
            win_y_pos = 0
            # print(e_bomb_window, win_x_pos, win_y_pos)
            e_bomb_window.restore()
            e_bomb_window.resizeTo(width, height)
            e_bomb_window.moveTo(win_x_pos, win_y_pos)
            print('>> Setup Screen: Done')
    else:
        print('>> Error: Bombcrypto Window Not Found')
        print('>> Exit... ')
