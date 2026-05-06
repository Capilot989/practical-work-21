import random
import pygame


class Molecule:
    """
    A class representing a moving molecule with collision detection.

    This class models a circular molecule that moves within a bounded area,
    bounces off walls, and exchanges velocities with other molecules upon collision.

    Attributes:
        x (int): The x-coordinate of the molecule's center.
        y (int): The y-coordinate of the molecule's center.
        radius (int): The radius of the molecule.
        color (tuple): RGB color tuple with values from 0-255.
        vx (float): The velocity in the x-direction (pixels per frame).
        vy (float): The velocity in the y-direction (pixels per frame).
    """
    def __init__(self, x: int, y: int, radius: int) -> None:
        """
        Initialize a Molecule instance.

        Args:
            x (int): The initial x-coordinate of the molecule's center.
            y (int): The initial y-coordinate of the molecule's center.
            radius (int): The radius of the molecule.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

    def move(self, width: int, height: int) -> None:
        """
        Update the molecule's position and handle wall collisions.

        Moves the molecule according to its velocity vector.
        When the molecule hits the boundaries, its velocity is reversed
        to create a bouncing effect.

        Args:
            width (int): The width of the bounding area.
            height (int): The height of the bounding area.
        """
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.vx *= -1

        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.vy *= -1

    def draw(self, screen: 'pygame.Surface') -> None:
        """
        Draw the molecule on the given screen surface.

        Args:
            screen (pygame.Surface): The Pygame surface to draw on.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def collide(self, other: 'Molecule') -> None:
        """
        Handle collision detection and response with another molecule.

        Checks if the distance between the centers of two molecules is less than
        the sum of their radii. If a collision occurs, exchanges their velocities
        to simulate an elastic collision.

        Args:
            other (Molecule): The other molecule to check collision with.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < self.radius + other.radius:
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy
