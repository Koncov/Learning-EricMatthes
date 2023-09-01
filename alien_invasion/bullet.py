import pygame
from pygame.sprite import Sprite

from settings import Settings


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенные кораблем."""

    def __init__(self, screen):
        """Создает объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = screen
        self.settings = Settings()
        self.color = self.settings.bullet_color

        #  Создание снарядов в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_wigth, self.settings.bullet_height)
        self.rect.midtop = screen.ship.rect.midtop

        #  Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        #  Обновление позиции снаряда в вещественном формате.
        self.y -= self.settings.bullet_speed
        #  Обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
