class Settings:
    """Класс для хранения всех настроек игры Allen Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 2
        self.ship_limit = 3

        # Параметры снаряды
        self.bullet_speed = 1.5
        self.bullet_wigth = 500
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев.
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 обозначает движение влево, -1 вправо.
