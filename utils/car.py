import random
from math import degrees, radians, sin

from pygame.math import Vector2


class Car:
    def __init__(self, x, y, angle=0.0, max_steering=50):
        self.position = Vector2(x, y)
        self.velocity = Vector2(10, 0.0)
        self.angle = angle
        self.max_steering = max_steering
        self.steering = 0.0

    def update(self, dt):
        if self.steering:
            turning_radius = 5 / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0
        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt
        self.angle = abs(self.angle % 360)

    def stop(self):
        self.velocity = Vector2(0.0, 0.0)
        self.steering = 0.0
