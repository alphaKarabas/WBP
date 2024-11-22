import pygame as pg
from src.Button import Button
from src.tools import *
from settings import *

class Menu:
	def __init__(self, surface):
		self.width = surface.get_size()[0]
		self.height = surface.get_size()[1]
		play_btn_pos = in_center((180, 50), (self.width, self.height), (0, 100))
		exit_btn_pos = in_center((180, 50), (self.width, self.height), (0, 170))
		self.play_btn = Button(text='Start', size=(180, 50), pos=play_btn_pos)
		self.exit_btn = Button(text='Exit', size=(180, 50), pos=exit_btn_pos)

	def render(self, surface):
		surface.fill(BG_COLOR)
		big_font = pg.font.Font('fonts/UbuntuMono-Regular.ttf', 64)
		title = big_font.render(MENU_TITLE, True, TEXT_COLOR)
		title_width = title.get_rect().width 
		title_height = title.get_rect().height
		title_pos = in_center((title_width, title_height), (self.width, self.height), (0, 0))
		surface.blit(title, title_pos)
		self.play_btn.render(surface)
		self.exit_btn.render(surface)

	def update(self, events):
		pg.display.set_caption(MENU_TITLE)
		mouse_pos = pg.mouse.get_pos()
		mouse_click = False

		for event in events:
			if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
				mouse_click = True

		mouse = (mouse_pos, mouse_click)
		
		if self.play_btn.is_click(mouse=mouse):
			return True
		elif self.exit_btn.is_click(mouse=mouse):
			exit()

