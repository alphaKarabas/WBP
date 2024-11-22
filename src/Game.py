import os
import pygame as pg
from settings import *
from bottle_loader import load_bottles
from src.Button import Button

class Game:
    def __init__(self):
        self.running = True
        self.steps = 0
        self.selected_bottle = None
        self.bottles = self.load_bottles()
        self.escape = False
        self.won = False
        self.font = pg.font.Font('fonts/UbuntuMono-Regular.ttf', 36)
        self.win_font = pg.font.Font('fonts/UbuntuMono-Regular.ttf', 72)

        # Кнопка "Try again"
        button_size = (200, 50)
        button_pos = (400, 300)  # Центр экрана
        self.try_again_button = Button("Try again", button_size, button_pos)

        # Загрузка фона
        self.background = pg.transform.scale(self.load_image('background.jpg'), (WIDTH, HEIGHT))

    def load_image(self, filename):
        path = os.path.join('images', filename)
        return pg.image.load(path).convert_alpha()

    def load_bottles(self):
        return load_bottles(self.load_image, {'8': 8, '5': 0, '3': 0})

    def render(self, surface):
        """Отрисовка бутылок, счётчика шагов и текста победы."""
        # Отображение фона
        surface.blit(self.background, (0, 0))

        # Отрисовка бутылок
        for bottle in self.bottles.values():
            bottle.render(surface, self.font)

        # Отрисовка счётчика шагов, если нет победы
        if not self.won:
            self.render_step_counter(surface)

        # Затемнение экрана и текст победы
        if self.won:
            self.render_win_overlay(surface)

    def render_step_counter(self, surface):
        """Отображение счётчика ходов на верхней части экрана."""
        steps_text = f"Steps: {self.steps}"
        text_surface = self.font.render(steps_text, True, TEXT_COLOR)  # Чёрный текст
        surface.blit(text_surface, (20, 20))  # Позиция в верхнем левом углу

    def render_win_overlay(self, surface):
        """Отображение затемнения экрана, текста победы и кнопки."""
        # Полупрозрачное затемнение
        overlay = pg.Surface(surface.get_size(), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        surface.blit(overlay, (0, 0))

        # Большая надпись "WIN!"
        win_text = "WIN!"
        win_surface = self.win_font.render(win_text, True, (0, 255, 0))
        win_rect = win_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 100))
        surface.blit(win_surface, win_rect)

        # Счётчик шагов
        steps_text = f"Steps: {self.steps}"
        steps_surface = self.font.render(steps_text, True, (255, 255, 255))
        steps_rect = steps_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 40))
        surface.blit(steps_surface, steps_rect)

        # Размещаем кнопку "Try again" по центру
        self.try_again_button.x = (surface.get_width() - self.try_again_button.width) // 2
        self.try_again_button.y = (surface.get_height() // 2) + 20

        # Рендер кнопки "Try again"
        self.try_again_button.render(surface)



    def reset_game(self):
        """Сбрасывает состояние игры."""
        self.running = True
        self.steps = 0
        self.selected_bottle = None
        self.bottles = self.load_bottles()
        self.won = False
        
    def render_win_text(self, surface):
        """Отображение текста победы."""
        # Большая надпись "WIN!"
        win_text = "WIN!"
        win_surface = self.win_font.render(win_text, True, (0, 255, 0))  # Зелёный текст
        win_rect = win_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 40))
        surface.blit(win_surface, win_rect)

        # Отображение счётчика ходов под текстом победы
        steps_text = f"Steps: {self.steps}"
        steps_surface = self.font.render(steps_text, True, TEXT_COLOR)  # Чёрный текст
        steps_rect = steps_surface.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 + 20))
        surface.blit(steps_surface, steps_rect)

    def handle_click(self, pos):
        """Обработка кликов."""
        if self.won:  # Если игра завершена победой
            if self.try_again_button.is_click((pos, pg.mouse.get_pressed()[0])):
                self.reset_game()
            return  # Игнорируем остальные клики, если экран победы активен

        for bottle in self.bottles.values():
            # Передаём позицию мыши и статус клика
            action = bottle.handle_buttons((pos, pg.mouse.get_pressed()[0]))
            if action:
                self.steps += 1
                return

            if bottle.rect().collidepoint(pos):
                if self.selected_bottle is None:
                    self.selected_bottle = bottle
                    bottle.toggle_select()
                elif self.selected_bottle == bottle:
                    bottle.toggle_select()
                    self.selected_bottle = None
                else:
                    self.pour_water(self.selected_bottle, bottle)
                    self.selected_bottle.toggle_select()
                    self.selected_bottle = None
                break

    def pour_water(self, src, dst):
        """Переливание воды между бутылками."""
        available_space = dst.capacity - dst.current_water
        pour_amount = min(src.current_water, available_space)
        src.current_water -= pour_amount
        dst.current_water += pour_amount
        self.steps += 1

        # Проверка на победу
        if any(bottle.current_water == 4 for bottle in self.bottles.values()):
            self.won = True

    def update(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.escape = True
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.handle_click(event.pos)

    def is_running(self):
        return self.running

    def is_escape(self):
        return self.escape