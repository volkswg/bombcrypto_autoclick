import lib.screen_arrange as screen_arrange
import lib.bomb_controller as bomb_controller
# import lib.screen_process as screen_process
import sched
import time

s = sched.scheduler(time.time, time.sleep)

event_trigger_time = 60

# waking state
# 0 = common
# 1 = rare
# 2 = super rare
waking_hero_state = 0


wait_for_stamina_flag = False


# min_time_full_stamina = 6000
min_time_full_stamina = 3000
min_wait_stamina_counter = 0


def main_event_loop():  # this will trigger every 1 mins
    #  global vaiable declare
    global wait_for_stamina_flag
    global min_wait_stamina_counter

    global waking_hero_state

    hero_status = bomb_controller.full_process_auto(
        wait_for_stamina_flag, waking_hero_state)

    print(hero_status)
    waking_hero_state = hero_status['next_state']

    if wait_for_stamina_flag:
        min_wait_stamina_counter += 1
        print(
            f'Wait({min_wait_stamina_counter}/{int(min_time_full_stamina/event_trigger_time)})')
        if min_wait_stamina_counter >= min_time_full_stamina/event_trigger_time:
            wait_for_stamina_flag = False
            min_wait_stamina_counter = 0

    if waking_hero_state == 3 and hero_status['is_all_rest']:
        wait_for_stamina_flag = True


def main():
    global waking_hero_state

    # before main loop
    # arrange bomb screen
    bombcrypto_wins = screen_arrange.get_bomb_wins_list()
    screen_arrange.arrange_bomb_wins(bombcrypto_wins)
    bomb_controller.enter_hunting()
    bomb_controller.wake_hero(
        all_hero_count=15, hero_rarity=['common'])
    waking_hero_state += 1
    while True:
        s.enter(event_trigger_time, 1, main_event_loop)
        s.run()


if __name__ == "__main__":
    main()
