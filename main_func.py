import pyautogui as pg
from time import sleep


## SETTING ##
class Setting():
    counter = 0


## NEED INFORM ##
flower_list = {"sunflower": 70, "potato": 320, "pumpkin": 1860, "carrot": 3660, "cabbage": 7260}


## SHOP FUNC ##
def shop_buyer(flower_name, win_count): # flower, timer
    if (pg.locateOnScreen("other\shop.png", confidence=0.8)) != None:

        pg.click(pg.locateOnScreen(r"other\shop.png", confidence=0.8), duration=0.2)
        sleep(1)
        pg.click(pg.locateOnScreen(r"other\sell.png", confidence=0.8), duration=0.2)
        sleep(0.5)
        pg.click(pg.locateOnScreen(rf"flowers\sell\{flower_name}.png", confidence=0.8), duration=0.2)
        sleep(0.5)
        pg.click(pg.locateOnScreen(r"other\sell_all.png", confidence=0.8), duration=0.2)
        sleep(0.5)
        pg.click(pg.locateOnScreen(r"other\sell_yes.png", confidence=0.8), duration=0.2)

        sleep(0.5)
        pg.click(pg.locateOnScreen(r"other\buy.png", confidence=0.8), duration=0.2)
        sleep(0.5)
        pg.click(pg.locateOnScreen(rf"flowers\seed\{flower_name}.png", confidence=0.8), duration=0.2)
        sleep(0.5)
        if (pg.locateOnScreen("other\sync.png", confidence=0.8)) == None:
            pg.click(pg.locateOnScreen(r"other\buy_10.png", confidence=0.8), duration=0.2)
            pg.click(pg.locateOnScreen(r"other\buy_10.png", confidence=0.8))
            pg.click(pg.locateOnScreen(r"other\buy_10.png", confidence=0.8))
            pg.click(pg.locateOnScreen(r"other\close_krest.png", confidence=0.8), duration=0.2)
            sleep(1)
        else:
            print(f"--- NEED BUY SEED type {flower_name}")
            pg.click(pg.locateOnScreen(r"other\close_krest.png", confidence=0.8), duration=0.2)

        ##  AVERAGE MOMENT ##
        pg.click(pg.locateOnScreen(r"other\save.png", confidence=0.9), duration=0.3)
        sleep(1)
        if win_count == 1:
            pass
        else:
            while True:
                with pg.hold("alt"):
                    pg.press(["tab"]*win_count)
                if (pg.locateOnScreen(r"other\save.png", confidence=0.9) == None) or (pg.locateOnScreen("other\main_menu.png", confidence=0.7) == None):
                    with pg.hold("alt"):
                        pg.press(["tab"] * win_count)
                else:
                    Setting.counter += 1
                    if Setting.counter == win_count:
                        sleep(flower_list[flower_name])
                    else:
                        sleep(2)

        if (pg.locateOnScreen("other\main_menu.png", confidence=0.8)) != None: loginer()

    else:
        print("---- Where SHOP?!?!?!?")
        with pg.hold("alt"):
            pg.press(["tab"] * win_count)

## LOGIN FUNC ##
def loginer():
    if (pg.locateOnScreen("other\main_menu.png", confidence=0.7)) != None:
        print("Вылет, ждем")
        sleep(5)
        if (pg.locateOnScreen("other\start_but.png", confidence=0.7)) != None:
            pg.click(pg.locateOnScreen("other\start_but.png", confidence=0.7))
            sleep(3)
            if pg.locateOnScreen("other\start_but.png", confidence=0.7) != None:
                with pg.hold("shift"):
                    pg.scroll(-200)
            else:
                with pg.hold("shift"):
                    pg.scroll(-800)
        else:
            sleep(10)
            pg.click(pg.locateOnScreen("other\start_but.png", confidence=0.7))
            sleep(5)
            with pg.hold("shift"):
                pg.scroll(-200)


## MAIN FARMER FUNC ##
def farmer(flower_name, win_count):
    counter = 0

    while True:
        if (pg.locateOnScreen("other\main_menu.png", confidence=0.7)) != None:
            loginer()

        counter += 1
        print(counter)
        if counter >= 28:
            counter = 0
            shop_buyer(flower_name, win_count)

        target = pg.locateOnScreen(rf"flowers\{flower_name}.png", confidence=0.7)
        print(target)
        if target == None:
            pass
        else:
            pg.click(target, duration=0.1)
            pg.click(target)
            pg.click(target)

        if (pg.locateOnScreen(r"other\chest.png", confidence=0.8)) != None:
            pg.click(pg.locateOnScreen(r"other\chest.png", confidence=0.8), duration=0.5)
            pg.click(pg.locateOnScreen(r"other\close.png", confidence=0.8), duration=0.5)
            sleep(1)
        elif (pg.locateOnScreen(r"other\chest_two.png", confidence=0.8)) != None:
            pg.click(pg.locateOnScreen(r"other\chest_two.png", confidence=0.8), duration=0.5)
            pg.click(pg.locateOnScreen(r"other\close.png", confidence=0.8), duration=0.5)
            sleep(1)
        elif (pg.locateOnScreen(r"other\chest_gob.png", confidence=0.8)) != None:
            pg.click(pg.locateOnScreen(r"other\chest_gob.png", confidence=0.8), duration=0.5)
            pg.click(pg.locateOnScreen(r"other\close.png", confidence=0.8), duration=0.5)
            sleep(1)


        target = pg.locateOnScreen(r"flowers\hole.png", confidence=0.8)
        print(target)
        if target == None:
            pass
        else:
            pg.click(target, duration=0.1)
            pg.click(target)