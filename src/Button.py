import pygame as pg

class Button:
    """Класс кнопки с улучшенным визуальным стилем."""
    def __init__(self, text, size, pos, font_path='fonts/UbuntuMono-Regular.ttf', font_size=36):
        self.text = text
        self.width = size[0]
        self.height = size[1]
        self.x = pos[0]
        self.y = pos[1]

        # Стиль кнопки
        self.shadow_offset = (5, 5)  # Смещение тени
        self.shadow_color = (50, 50, 50, 150)  # Цвет тени с прозрачностью
        self.base_color = (100, 149, 237)  # Основной цвет кнопки (синий)
        self.hover_color = (65, 105, 225)  # Цвет при наведении
        self.border_color = (25, 25, 112)  # Цвет границы
        self.text_color = (255, 255, 255)  # Цвет текста
        self.disabled_color = (169, 169, 169)  # Серый цвет для отключённой кнопки
        self.disabled = False  # Состояние кнопки (включена/выключена)
        self.hovered = False  # Наведение на кнопку

        # Шрифт
        self.font = pg.font.Font(font_path, font_size)

    def is_click(self, mouse):
        """Проверка клика на кнопку."""
        if self.disabled:  # Игнорируем клики, если кнопка отключена
            return False

        mouse_pos = mouse[0]  # Позиция мыши
        mouse_click = mouse[1]  # Состояние клика

        m_x, m_y = mouse_pos[0], mouse_pos[1]
        self.hovered = self.x <= m_x <= self.x + self.width and self.y <= m_y <= self.y + self.height

        return self.hovered and mouse_click

    def render(self, surface):
        """Отрисовка кнопки."""
        # Цвет кнопки: отключённая, активная или наведённая
        if self.disabled:
            button_color = self.disabled_color
        elif self.hovered:
            button_color = self.hover_color
        else:
            button_color = self.base_color

        # Отрисовка кнопки с закруглёнными углами
        button_rect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, button_color, button_rect, border_radius=10)
        pg.draw.rect(surface, self.border_color, button_rect, width=2, border_radius=10)

        # Текст на кнопке
        text_surface = self.font.render(self.text, True, self.text_color if not self.disabled else (200, 200, 200))
        text_rect = text_surface.get_rect(center=button_rect.center)
        surface.blit(text_surface, text_rect)
