from pygame import Surface, Color, key
import pygame.KEYDOWN
import const


class Player(object):
	"""docstring for Player"""
	def __init__(self, img):
		if img == None:
			self.img = Surface((24,24)).fill(Color(255,255,255))

	def update(self,events):
		res = list()
		for e in events:
			if e.type == KEYDOWN:
				res.append(ord(e.key))
		return res

	def draw(self, window):
		window.blit(const.PLAYER_POS[0],const.PLAYER_POS[1],self.img)
		