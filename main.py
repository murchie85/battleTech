import pygame


# ---- ALL THIS RUNS ONLY ONCE 
# Initialize Pygame
pygame.init()

# Set the screen size and caption
screenW, screenH = 1500, 850
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Battletech")

#IMAGE DETAILS 
titleImageLocation  = 'images/titleImage.png'
titleImage          = pygame.image.load(titleImageLocation)

# FONT DETAILS 
fontLocation = 'fonts/Hvymtl1.ttf'
# Initialize font
font      = pygame.font.Font(fontLocation, 100)
smallFont = pygame.font.Font(fontLocation, 70)



# ---EVERYTHING BELOW RUNS 60 TIMES EVERY SECOND

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
    screen.fill((255, 255, 255)) # Clear the screen to black

    screen.blit(titleImage, (0.5*(screenW-titleImage.get_width()), 100))



    # Render text
    topText = font.render("BattleTech", True, (0, 0, 0))
    # Draw text to the screen
    screen.blit(topText, (370, 40))

    # Render text
    text = smallFont.render("InterStellar Operations", True, (0, 0, 0))
    # Draw text to the screen
    screen.blit(text, (200, 700))


    # Draw your game elements here

    pygame.display.flip()  # Update the screen

# Exit Pygame
pygame.quit()
