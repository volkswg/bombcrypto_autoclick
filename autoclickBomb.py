import lib.bomb_controller as bomb_controller
import lib.screen_arrange as screen_arrange

# arrange bomb screen
bombcrypto_wins = screen_arrange.get_bomb_wins_list()
screen_arrange.arrange_bomb_wins(bombcrypto_wins)

bomb_controller.enter_hunting()
bomb_controller.common_work()
