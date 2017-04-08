from pygame import Surface, Color
import math
class Enemy(object):
	"""docstring for Enemy"""
	def __init__(self, pos, img, typ,life):
		self.pos = pos
		self.life = life
		self.v = const.ENEMY_SPEED
		size = const.ENEMY_SIZE[typ]
		if img == None:
			self.img = Surface((size[0],size[1])).fill(Color(125,125,125))

	def update(self, pl_pos):
		alpha = math.atan((pl_pos[0]-self.pos[0])/(pl_pos[1]-self.pos[1]))
		dx = self.v * math.cos(alpha)
		dy = self.v * math.sin(alpha)
		pos[0] += dx
		pos[1] += dy

	def changeLife(self, dl):
		for x in range(len(self.life)):
			if self.life[0] in dl:
				dl.remove(self.life[0])
			else:
				break
		return self.life

	def draw(self, window):
		window.blit(pos[0],pos[1],self.img)