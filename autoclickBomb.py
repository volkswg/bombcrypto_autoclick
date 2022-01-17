import pygetwindow as gw

# get all window title
all_window = gw.getAllTitles()
# filter only bombcrypto title 
filtered_win_title = [e_title for e_title in all_window if 'Bombcrypto' in e_title]
bomb_wins_title_count = len(filtered_win_title)

width = 700
height = 570

if bomb_wins_title_count > 0:
    # get list of bombcrypto window
    bombcrypto_wins = gw.getWindowsWithTitle(filtered_win_title[0])
    print('>> Setup: Start Arrange Windows')
    print('>> Setup: Please Set Zoom to 67%')
    for index, e_bomb_window in enumerate(bombcrypto_wins):
        win_x_pos = (width-15)*index
        win_y_pos = 0
        # print(e_bomb_window, win_x_pos, win_y_pos)
        e_bomb_window.restore()
        e_bomb_window.resizeTo(width, height)
        e_bomb_window.moveTo(win_x_pos, win_y_pos)
        print('>> Setup: Done')
else:
    print('>> Error: Bombcrypto Window Not Found')
    print('>> Exit... ')

# win.resizeTo(100, 100)