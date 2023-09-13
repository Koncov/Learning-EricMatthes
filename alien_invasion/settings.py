class Settings:
    """Класс для хранения всех настроек игры Allen Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры снаряды
        self.bullet_wigth = 500
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев.
        self.fleet_drop_speed = 10

        # Темп ускорения игры.
        self.speedup_scale = 0.1
        # Темп роста стоимости пришельцев.
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 2
        self.bullet_speed = 1.5
        self.alien_speed = 0.2

        self.fleet_direction = 1  # 1 обозначает движение влево, -1 вправо.

        # Подсчет очков.
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.alien_speed += self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
