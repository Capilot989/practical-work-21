import pygame
from solution import Molecule
import random


def create_moleciles(number_of_molecules: int,
                     width: int, height: int) -> list['Molecule']:
    """
    Create a list of molecules with random positions and sizes.

    Each molecule is placed at a random position within the given dimensions,
    with a safe margin of 50 pixels from the edges to prevent immediate
    boundary collisions.

    Args:
        number_of_molecules (int): The number of molecules to create.
        width (int): The width of the display area.
        height (int): The height of the display area.

    Returns:
        list['Molecule']: A list containing the created Molecule instances.
    """
    molecules = [
        Molecule(
            random.randint(50, width - 50),
            random.randint(50, height - 50),
            random.randint(5, 15)
        )
        for _ in range(number_of_molecules)
    ]
    return molecules

def create_display(
        width: int, height: int
) -> tuple('pygame.Surface', 'pygame.Clock'):
    """
    Initialize and create the Pygame display surface and clock.

    Args:
        width (int): The width of the display window.
        height (int): The height of the display window.

    Returns:
        tuple['pygame.Surface', 'pygame.Clock']: A tuple containing the Pygame
        display surface and clock object.
    """
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    return (screen, clock)

def main() -> None:
    """
    Main function to run the molecule simulation.

    This function:
    1. Gets user input for screen dimensions and number of molecules.
    2. Creates molecules with random properties.
    3. Initializes the Pygame display and clock.
    4. Runs the main simulation loop with:
       - Event handling (including QUIT events).
       - Movement updates for all molecules.
       - Collision detection between molecule pairs.
       - Drawing all molecules on the screen.
       - Display updates at 60 frames per second.

    Returns:
        None
    """
    width = int(input('Введите ширину экрана: '))
    height = int(input('Введите высоту экрана: '))
    number_of_molecules = int(input('Введите количество молекул: '))

    molecules = create_moleciles(number_of_molecules, width, height)
    screen, clock = create_display(width, height)
    print(type(screen), type(clock))

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for m in molecules:
            m.move(width, height)

        for i in range(len(molecules)):
            for j in range(i + 1, len(molecules)):
                molecules[i].collide(molecules[j])

        for m in molecules:
            m.draw(screen)

        pygame.display.flip()
        clock.tick(60)


pygame.quit()

if __name__ == '__main__':
    main()
