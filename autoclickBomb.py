import lib.screen_arrange as screen_arrange
import lib.bomb_controller as bomb_controller
import lib.screen_process as screen_process
import sched
import time

s = sched.scheduler(time.time, time.sleep)


# arrange bomb screen
bombcrypto_wins = screen_arrange.get_bomb_wins_list()
screen_arrange.arrange_bomb_wins(bombcrypto_wins)


re_enter_timer = 300
check_all_rest = 5

# print('>> Process: Start Game Loop')
while True:
    # s.enter(re_enter_timer, 1, bomb_controller.re_enter_map)
    s.enter(check_all_rest, 1, screen_process.capture_screen)
    # s.enter(re_enter_timer, 1, bomb_controller.re_enter_map)
    s.run()
    # bomb_controller.enter_hunting()
    # bomb_controller.wake_hero(15, ['rare', 'superrare'])
