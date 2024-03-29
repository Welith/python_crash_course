import pygame

class Ship():
	"""Creating the ship"""
	def __init__(self, ai_settings, screen):
		self.screen = screen

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings

		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom
		self.center_x = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)

		#Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center_x += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.center_x -= self.ai_settings.ship_speed_factor
		elif self.moving_up and self.rect.top > self.screen_rect.top:
			self.center_y -= self.ai_settings.ship_speed_factor
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.ai_settings.ship_speed_factor


		self.rect.centerx = self.center_x
		self.rect.centery = self.center_y

	def center_ship(self):
		self.center = self.screen_rect.centerx


	def blitme(self):
		#Draw ship
		self.screen.blit(self.image, self.rect)