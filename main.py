import lib.screen_arrange as screen_arrange
import lib.bomb_controller as bomb_controller
# import lib.screen_process as screen_process
import sched
import time

s = sched.scheduler(time.time, time.sleep)

event_trigger_time = 60


common_started_flag = False
rsr_started_flag = False

wait_for_stamina_flag = False


# min_time_full_stamina = 6000
min_time_full_stamina = 3000
min_wait_stamina_counter = 0


def main_event_loop():  # this will trigger every 1 mins
    #  global vaiable declare
    global common_started_flag
    global rsr_started_flag
    global wait_for_stamina_flag
    global min_wait_stamina_counter

    # check error occur every trigger time
    bomb_error = bomb_controller.check_error_occur()
    if bomb_error:
        # bomb_controller.error_handling()
        print('Error True')
    else:
        print('Continue Process')

    # print('wait_for_stamina_flag', wait_for_stamina_flag)
    if wait_for_stamina_flag:
        min_wait_stamina_counter += 1
        bomb_controller.re_enter_map()
        print(min_wait_stamina_counter)
        if min_wait_stamina_counter >= min_time_full_stamina/event_trigger_time:
            wait_for_stamina_flag = False
            min_wait_stamina_counter = 0

        return

    # print('this is main loop')
    all_rest_result = bomb_controller.check_all_rest()
    print('All Sleep', all_rest_result)
    print('common', common_started_flag)
    print('rsr', rsr_started_flag)

    if all_rest_result:
        # check all empty stamina then wait for stamina
        if common_started_flag is True and rsr_started_flag is True:
            common_started_flag = False
            rsr_started_flag = False
            wait_for_stamina_flag = True

        if wait_for_stamina_flag:
            min_wait_stamina_counter += 1
            bomb_controller.re_enter_map()
            print(min_wait_stamina_counter)
            if min_wait_stamina_counter == min_time_full_stamina/event_trigger_time:
                wait_for_stamina_flag = False
                min_wait_stamina_counter = 0
            return

        if common_started_flag:
            bomb_controller.wake_hero(
                all_hero_count=15, hero_rarity=['rare', 'superrare'])
            # common_started_flag = False
            rsr_started_flag = True
        elif rsr_started_flag:
            bomb_controller.wake_hero(
                all_hero_count=15, hero_rarity=['common'])
            common_started_flag = True
            # rsr_started_flag = False
        else:
            bomb_controller.wake_hero(
                all_hero_count=15, hero_rarity=['common'])
            common_started_flag = True


def main():
    global common_started_flag
    global rsr_started_flag

    # before main loop
    # arrange bomb screen
    bombcrypto_wins = screen_arrange.get_bomb_wins_list()
    screen_arrange.arrange_bomb_wins(bombcrypto_wins)
    bomb_controller.enter_hunting()
    bomb_controller.wake_hero(all_hero_count=15, hero_rarity=['common'])
    common_started_flag = True
    while True:
        s.enter(event_trigger_time, 1, main_event_loop)
        s.run()


if __name__ == "__main__":
    main()
