import pygame

# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 181, 218)
LIGHT_BLUE = (204, 229, 255)
GRASS_GREEN = (0, 153, 0)
HOUSE_BASE = (74, 74, 74)
ROOF = (112, 77, 66)
HOUSE = (207, 52, 41)
CLOUD = (237, 237, 237)
SUN_YELLOW = (255, 255, 0)
BOTTOM_HALF_HOUSE = (166, 166, 166)
LIGHT_YELLOW = (255, 255, 204)

pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("noah's first game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
   # --- Main event loop

   # --- All events are detected here
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True

   # --- Game logic should go here

   # --- Screen-clearing code goes here
   #  Here, we clear the screen to white.
   screen.fill(LIGHT_BLUE)


   #grass drawing
   pygame.draw.rect(screen, GRASS_GREEN, [0, 375, 700, 125])
   #house base
   pygame.draw.rect(screen, BOTTOM_HALF_HOUSE, [125, 200, 350, 175])
   pygame.draw.rect(screen, BLACK, [125, 200, 350, 175], 2)
   #roof
   pygame.draw.polygon(screen, HOUSE_BASE, [[125, 200], [475, 200], [300, 100]])
   pygame.draw.polygon(screen, BLACK, [[125, 200], [475, 200], [300, 100]], 2)
   #door
   pygame.draw.rect(screen, ROOF, [175, 250, 75, 125])
   pygame.draw.rect(screen, BLACK, [175, 250, 75, 125], 2)
   pygame.draw.circle(screen, BLACK, [230, 315], 3)
   #window 1
   pygame.draw.rect(screen, LIGHT_YELLOW, [320, 250, 60, 60])
   pygame.draw.rect(screen, BLACK, [320, 250, 60, 60], 2)
   pygame.draw.line(screen, BLACK, [350, 250], [350, 310], 2)
   pygame.draw.line(screen, BLACK, [320, 280], [380, 280], 2)
   #cloud
   pygame.draw.circle(screen, CLOUD, [50, 50], 40)
   pygame.draw.circle(screen, CLOUD, [75, 50], 40)
   pygame.draw.circle(screen, CLOUD, [100, 50], 40)
   pygame.draw.circle(screen, CLOUD, [110, 75], 40)
   pygame.draw.circle(screen, CLOUD, [100, 100], 40)
   #cloud 2
   pygame.draw.circle(screen, CLOUD, [400, 70], 40)
   pygame.draw.circle(screen, CLOUD, [425, 25], 40)
   pygame.draw.circle(screen, CLOUD, [425, 60], 40)
   pygame.draw.circle(screen, CLOUD, [435, 65], 40)
   pygame.draw.circle(screen, CLOUD, [415, 75], 40)
   #sun
   pygame.draw.circle(screen, SUN_YELLOW, [600, 100], 60)

   # --- Go ahead and update the screen with what we've drawn.
   pygame.display.flip()

   # --- Limit to 60 frames per second
   clock.tick(60)

# Close the window and quit.
pygame.quit()



