import lib.screen_arrange as screen_arrange
import lib.bomb_controller as bomb_controller
# import lib.screen_process as screen_process
import sched
import time

s = sched.scheduler(time.time, time.sleep)

re_enter_timer = 180
check_all_rest = 60

re_enter_map_min_count = 0


def main_event_loop():  # this will trigger every 1 mins
    #  global vaiable declare
    global re_enter_map_min_count

    # print('this is main loop')
    all_rest_result = bomb_controller.check_all_rest()
    print(all_rest_result)
    re_enter_map_min_count += 1
    # if re_enter_map_min_count >= 3:
    #     bomb_controller.re_enter_map()
    #     re_enter_map_min_count = 0


def main():
    # before main loop
    # arrange bomb screen
    bombcrypto_wins = screen_arrange.get_bomb_wins_list()
    screen_arrange.arrange_bomb_wins(bombcrypto_wins)

    while True:
        s.enter(10, 1, main_event_loop)
        s.run()


if __name__ == "__main__":
    main()
