import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
	#Initialize game screen
	pygame.init() #Set-ups the library
	ai_settings = Settings() #Inheriting all of the function from Settings
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	#alien = Alien(ai_settings, screen)
	aliens = Group()
	play_button = Button(ai_settings, screen, "Play")

	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Main loop
	while True:

		#Keyboard and mouse events
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship,
			 aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

		#Screen changes
		gf.update_screen(ai_settings, screen, stats, sb, ship,
		 aliens, bullets, play_button)

run_game()