import pygame

from settings import Settings


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, screen):
        """Инициирует корабль и его начальное положение."""
        self.screen = screen
        self.settings = Settings()
        self.screen_rect = screen.get_rect()

        #  Загружает изображение корабля, и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #  Каждый новый корабль появляется у нижнего края.
        self.rect.midbottom = self.screen_rect.midbottom
        #  Сохранения вещественной координаты центра коробля.
        self.x = float(self.rect.x)

        #  Флаг перемещения.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        #  Обновляется атрибут х, не rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #  Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
