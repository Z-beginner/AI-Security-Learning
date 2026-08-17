import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #self.bg_color = (230, 230, 230) #R G B
        #上述已被self.settings.bg_color替代
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) #创建游戏窗口
        pygame.display.set_caption("Alien Invasion") #设置窗口标题
        self.ship = Ship(self)
    def run_game(self):
        while True:
            for event in pygame.event.get(): #获取玩家产生的所有事件
                if event.type == pygame.QUIT: #玩家退出
                    sys.exit()
            self.screen.fill(self.settings.bg_color)  #填充屏幕
            self.ship.blitme()
            pygame.display.flip() #更新屏幕
            self.clock.tick(60) #tick:跳动一次，限制不超过60帧，给循环限速
if __name__ == "__main__": #打开python直接运行游戏
    ai = AlienInvasion()
    ai.run_game()