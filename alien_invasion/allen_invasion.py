import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AllenInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        #  Размер экрана с заданными параметрами файла settings.py
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #  Размер экрана в полноэкранном режиме.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Allen Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()

        pygame.display.flip()

    def run_game(self):
        """Запуска основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()


if __name__ == '__main__':
    #  Создание экземпляра и запуска игры.
    ai = AllenInvasion()
    ai.run_game()