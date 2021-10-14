# Basic Pygame Structure

import pygame  # Imports pygame and other libraries
import random
# Define Classes (sprites) here

pygame.init()                           # Pygame is initialised (starts running)


class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.timecreated = pygame.time.get_ticks()
        self.image = pygame.Surface([30, 30])
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 670)
        self.rect.y = 0

    def setImage(self, graphicSelected):
        fallingObjectsImage = pygame.image.load(graphicSelected)
        self.image.blit(fallingObjectsImage, (0, 0))

    def moveFallingObjects(self, distance):
        if self.rect.y <= 470:
            self.rect.y = self.rect.y + distance
    def deleteFallingObjects(self):
        if self.rect.y > 470:
            self.kill()

class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.Surface([50,60])
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = 420

        self.image.blit(pygame.image.load("Superhero.png"),(0,0))
    def moveCharacter(self,movement):
        if self.rect.x >= 5 and self.rect.x <= 645:
            self.rect.x = self.rect.x + movement
        if self.rect.x<5:
            self.rect.x = 5
        if self.rect.x>645:
            self.rect.x=645


screen = pygame.display.set_mode([700, 500])  # Set the width and height of the screen [width,height]
pygame.display.set_caption("My Game")
background_image = pygame.image.load("OrchardBackground.jpg").convert()
done = False                                # Loop until the user clicks the close button.
clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
black = (0,   0,   0)                 # Define some colors using rgb values.  These can be
white = (255, 255, 255)                 # used throughout the game instead of using rgb values.

# Define additional Functions and Procedures here
allFallingObjects = pygame.sprite.Group()
nextApple = pygame.time.get_ticks() + 2500

charactersGroup = pygame.sprite.Group()
character = Character()
charactersGroup.add(character)
movement = 0

# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get():        # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:       # If user clicked close window
            done = True                     # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement= -5
            if event.key == pygame.K_RIGHT:
                movement = 5
        if event.type == pygame.KEYUP:
            movement= 0
    # Update sprites here
    if pygame.time.get_ticks() > nextApple:
        nextObject = FallingObject()
        nextObject.setImage("Apple.png")
        allFallingObjects.add(nextObject)
        nextApple = pygame.time.get_ticks() + 450

    for eachObject in (allFallingObjects.sprites()):
        eachObject.moveFallingObjects(5)

        eachObject.deleteFallingObjects()

    character.moveCharacter(movement)
    screen.blit(background_image, [0, 0])
    allFallingObjects.draw(screen)
    charactersGroup.draw(screen)
    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.
    clock.tick(20)                          # Limit to 20 frames per second

pygame.quit()                               # Close the window and quit.
