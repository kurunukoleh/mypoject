import pygame
pygame.mixer.init()
class Monkey :
    def __init__(self , x , y , w , h , texture , speed , moneylist ):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.moneylist = moneylist
        self.points= 0

    def render(self, window):
        window.blit(self.texture, (self.hitbox.x, self.hitbox.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.hitbox.x < 700:
                self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            if self.hitbox.x > 0:
                self.hitbox.x -= self.speed
        if keys[pygame.K_w]:
            if self.hitbox.y > 0:
                self.hitbox.y -= self.speed
        if keys[pygame.K_s]:
            if self.hitbox.y < 400:
                self.hitbox.y += self.speed
        if keys[pygame.K_RIGHT]:
            if self.hitbox.x < 700:
                self.hitbox.x += self.speed
        if keys[pygame.K_LEFT]:
            if self.hitbox.x > 0:
                self.hitbox.x -= self.speed
        if keys[pygame.K_UP]:
            if self.hitbox.y > 0:
                self.hitbox.y -= self.speed
        if keys[pygame.K_DOWN]:
            if self.hitbox.y < 400:
                self.hitbox.y += self.speed
        for i in self.moneylist:
            if i.hitbox.colliderect(self.hitbox):
                self.moneylist.remove(i)
                self.points += 1

    def getpint(self):
        return self.points
