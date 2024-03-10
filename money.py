import pygame

class Money:
    def __init__(self , x , y , w , h , speed ,  texture ,):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))

    def move(self):
        self.hitbox.y += self.speed