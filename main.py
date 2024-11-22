import pygame as pg
from src.Menu import Menu
from src.Game import Game
from settings import *

def main():
    pg.init()
    window = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    menu = Menu(window)
    game = Game()  
    game_stage = 'menu'

    while True:
        events = pg.event.get()  # Получаем события один раз за кадр

        for event in events:
            if event.type == pg.QUIT:
                exit()

        if game_stage == 'menu':
            menu.render(window)

            if menu.update(events):  # Передаем события в меню
                game = Game() 
                game_stage = 'game'

        elif game_stage == 'game':
            game.render(window)
            game.update(events)  # Передаем события в игру

            if game.is_escape():
                game_stage = 'menu'

        clock.tick(FPS)
        pg.display.update()

if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
