import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect() #get.rect()获取矩形框
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  #midbottom:底部中点

    def blitme(self):
        self.screen.blit(self.image, self.rect) #把image绘制到screen的rect上
        #a.blit(b, c)  把b绘制到a的c上