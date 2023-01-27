import pygame

# Initialize Pygame
pygame.init()

# Set the screen size and caption
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battletech")

# Run the game until the user closes the window
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic here

    """
    HERE IS WHERE YOU DO EVERYTHING
    examples
    get keyboard input
    show start screen
    show title screen
    start game
    select player
    .....


    """


    # Draw the screen
    screen.fill((0, 0, 0)) # Clear the screen to black
    # Draw your game elements here

    pygame.display.flip()  # Update the screen

# Exit Pygame
pygame.quit()
