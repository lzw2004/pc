import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
	"""显示得分的类"""

	def __init__(self, ai_game):
		"""初始化现实得分涉及到的属性"""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# 显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# 准备初始包晗最高得分和当前得分得图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()


	def prep_score(self):
		"""将得分信息转换为一幅渲染的图像"""
		rounded_score = round(self.stats.score, -1)
		score_scr = "{:,}".format(rounded_score)
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True,
				self.text_color, self.settings.bg_color)

		# 在屏幕右上角显示得分
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""在屏幕上显示得分、等级、剩余飞船数"""
		#     得分
		self.screen.blit(self.score_image, self.score_rect)
		#     最高得分
		self.screen.blit(self.high_score_image, self.high_score_rect)
		#     等级
		self.screen.blit(self.lever_image, self.level_rect)
		#     剩余飞船
		self.ships.draw(self.screen)

	def prep_high_score(self):
		"""将最高得分转换为渲染图像"""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
				self.text_color, self.settings.bg_color)

		# 将最高得分放在屏幕顶部中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def check_high_score(self):
		"""检查是否诞生了最高的分"""
		if self.stats.score >= self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()	

	def prep_level(self):
		"""将等级转换为渲染图像"""
		level_str = str(self.stats.level)
		self.lever_image = self.font.render(level_str, True,
				self.text_color, self.settings.bg_color)

		# 将显示等级在得分下方
		self.level_rect = self.lever_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10	

	def prep_ships(self):
		"""显示还余下多少艘飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)			
					