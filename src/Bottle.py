import pygame as pg
from src.Button import Button

class Bottle:
    """Класс, представляющий одну бутылку."""
    def __init__(self, id, base_pos, capacity, images, current_water=0):
        self.id = id
        self.base_pos = list(base_pos)  # Позиция бутылки
        self.capacity = capacity  # Вместимость бутылки
        self.current_water = current_water  # Текущий уровень воды
        self.images = images  # Словарь с изображениями (bottle, shadow, water, scale)
        self.selected = False  # Выбрана ли бутылка

        # Кнопки
        button_size = (100, 40)
        self.fill_button = Button("Fill", button_size, (self.base_pos[0], self.base_pos[1] - 160))
        self.empty_button = Button("Empty", button_size, (self.base_pos[0], self.base_pos[1] - 110))

    def rect(self):
        """Возвращает прямоугольник бутылки для обработки кликов."""
        bottle_image, bottle_offset = self.images['bottle']
        return bottle_image.get_rect(
            topleft=(self.base_pos[0] + bottle_offset[0], self.base_pos[1] + bottle_offset[1])
        )

    def toggle_select(self):
        """Переключение состояния выбора бутылки."""
        self.selected = not self.selected
        self.base_pos[1] += -50 if self.selected else 50

    def render(self, surface, font):
        """Отрисовка бутылки, текста количества воды и кнопок."""
        self.render_bottle(surface)
        self.render_water_amount(surface, font)  # Отображение количества воды
        if not self.selected:  # Кнопки отображаются только если бутылка не выбрана
            self.fill_button.render(surface)
            self.empty_button.render(surface)

    def render_bottle(self, surface):
        """Отрисовка элементов бутылки."""
        # Отображение тени
        if not self.selected:
            shadow_image, shadow_offset = self.images['shadow']
            shadow_pos = (self.base_pos[0] + shadow_offset[0], self.base_pos[1] + shadow_offset[1])
            surface.blit(shadow_image, shadow_pos)

        # Отображение бутылки
        bottle_image, bottle_offset = self.images['bottle']
        bottle_pos = (self.base_pos[0] + bottle_offset[0], self.base_pos[1] + bottle_offset[1])
        surface.blit(bottle_image, bottle_pos)

        # Отображение воды
        if self.current_water > 0:
            water_image, water_offsets = self.images['water']
            water_offset = water_offsets[self.current_water]
            water_pos = (self.base_pos[0] + water_offset[0], self.base_pos[1] + water_offset[1])
            surface.blit(water_image, water_pos)

        # Отображение шкалы
        scale_image, scale_offset = self.images['scale']
        scale_pos = (self.base_pos[0] + scale_offset[0], self.base_pos[1] + scale_offset[1])
        surface.blit(scale_image, scale_pos)

    def handle_buttons(self, mouse):
        """Обработка кликов по кнопкам."""
        if self.fill_button.is_click(mouse):
            self.current_water = self.capacity
            return 'fill'
        elif self.empty_button.is_click(mouse):
            self.current_water = 0
            return 'empty'
        return None


    def render_water_amount(self, surface, font):
        """Отображение количества воды с улучшенным оформлением."""
        water_text = f"{self.current_water}"  # Текущий объем воды
        text_surface = font.render(water_text, True, (90, 90, 90))  # Белый текст
        text_rect = text_surface.get_rect(
            center=(self.base_pos[0] + 25, self.base_pos[1] - 30)  # Центр текста
        )
        
        # Рисуем фон с закругленными углами
        rect_color = (255, 255, 255)  # Цвет фона (стальной синий)
        border_color = (30, 70, 120)  # Цвет границы (темный синий)
        border_radius = 8
        inflated_rect = text_rect.inflate(20, 20)  # Увеличиваем размер прямоугольника для фона
        
        # Отрисовка прямоугольника с границей
        pg.draw.rect(surface, border_color, inflated_rect, border_radius=border_radius)
        pg.draw.rect(surface, rect_color, inflated_rect.inflate(-4, -4), border_radius=border_radius)
        
        # Отрисовка текста
        surface.blit(text_surface, text_rect)


def render_buttons(self, surface):
    """Отрисовка кнопок с использованием класса Button."""
    # Проверка состояния бутылки для кнопок
    self.fill_button.disabled = self.current_water == self.capacity  # Отключаем Fill, если бутылка полная
    self.empty_button.disabled = self.current_water == 0  # Отключаем Empty, если бутылка пустая

    # Отрисовка кнопок
    self.fill_button.render(surface)
    self.empty_button.render(surface)