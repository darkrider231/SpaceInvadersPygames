# Space Invaders Beginner Tutorials
# From: https://www.youtube.com/watch?v=FfWpgLFMI7w&t=339s
# I'm learning Pygames
from os import write
import pygame
from pygame.display import set_icon
import random
import math

#  Intialize the pygame
pygame.init()

# Create the screen size
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load("SpaceInvadersPygames/spaceinvadersbackground1.png")

#  Title and Icon
pygame.display.set_caption("Space Invaders in Pygames")
icon = pygame.image.load("SpaceInvadersPygames/ufo1.png")
pygame.display.set_icon(icon)

# Player 1
player1Img = pygame.image.load('SpaceInvadersPygames/player1.png')
player1X = 370
player1Y = 400
player1X_change = 0

# Player 2
player2Img = pygame.image.load('SpaceInvadersPygames/player2.png')
player2X = 370
player2Y = 480
player2X_change = 0

# Enemy1
enemy1Img = []
enemy1X = []
enemy1Y = []
enemyX1_change = []
enemyY1_change = []
num_of_enemies1 = 6

for i in range(num_of_enemies1):
    enemy1Img.append(pygame.image.load('SpaceInvadersPygames/enemy1.png'))
    enemy1X.append(100)
    enemy1Y.append(80)
    enemyX1_change.append(2)
    enemyY1_change.append(10)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('SpaceInvadersPygames/bullet.png')
bulletX = 0
bullet1Y = 400
bullet2Y = 480
bulletX1_change = 0
bulletY1_change = 10
bulletX2_change = 0
bulletY2_change = 10
bullet_state = "ready"



# Score
score1_value = 0
score2_value = 0
font = pygame.font.Font('SpaceInvadersPygames/PressStart2P-Regular.ttf', 24)
textX = 10
textY = 50
textX2 = 500
textY2 = 50

# Show Title
titleText = font.render('Space Invaders', True, (255, 255, 255))



def show_score1(x,y):
    score1 = font.render("Player 1: " + str(score1_value), True, (255,255,255))
    screen.blit(score1, (x, y))
    screen.blit(titleText, (200,10))

def show_score2(x,y):
    score2 = font.render("Player 2: " + str(score2_value), True, (255,255,255))
    screen.blit(score2, (x,y))

# Player Function
def player1(x, y):
    screen.blit(player1Img, (x, y))

def player2(x, y):
    screen.blit(player2Img, (x,y))

# Enemy Function
def enemy1(x, y, i):
    screen.blit(enemy1Img[i], (x, y))

# Fire Bullet Function
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # Makes the bullet fire between the spaceship
    screen.blit(bulletImg, (x + 16, y + 10))

# Collision Function
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0,80))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        #  if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.QUIT()

            #  Player 1
            if event.key == pygame.K_LEFT:
                player1X_change = -6
                
            if event.key == pygame.K_RIGHT:
                player1X_change = 6

            # Player 2
            if event.key == pygame.K_a:
                player2X_change = -6

            if event.key == pygame.K_d:
                player2X_change = 6

            # Player 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = player1X
                    fire_bullet(player1X, bullet1Y)
            
            # Player 2
            if event.key == pygame.K_LCTRL:
                if bullet_state == "ready":
                    bulletX = player2X
                    fire_bullet(player2X, bullet1Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1X_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player2X_change = 0

    player1X += player1X_change
    player2X += player2X_change

    # Checking for boundaries for spaceship so it doesn't go out of bounds
    # Player 1
    if player1X <= 0:
        player1X = 0
    elif player1X >= 736:
        player1X = 736

    # Player 2
    if player2X <= 0:
        player2X = 0
    elif player2X >= 736:
        player2X = 736

    # Enemy Movement
    for i in range(num_of_enemies1):
        enemy1X[i] += enemyX1_change[i]
        if enemy1X[i] <= 0:
            enemyX1_change[i] = 2
            enemy1Y[i] += enemyY1_change[i]
        elif enemy1X[i] >= 736:
            enemyX1_change[i] = -2
            enemy1Y[i] += enemyY1_change[i]

    # Collision
    collision = isCollision(enemy1X[i], enemy1Y[i], bulletX, bullet1Y)
    if collision:
        bullet1Y = 400
        bullet2Y = 400
        bullet_state = "ready"

        if player1:
            score1_value += 100
            print(score1_value)
        elif player2:
            score2_value += 100
            print(score2_value)
    
    
    enemy1(enemy1X[i], enemy1Y[i], i)


    # Bullet Movement
    if player1: 
        if bullet1Y <= 60:
            bullet1Y = 400
            bullet_state = "ready"
    if player2:
        if bullet2Y <= 30:
            bullet2Y = 480
            bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bullet1Y)
        bullet1Y -= bulletY1_change

    

    player1(player1X, player1Y)
    player2(player2X, player2Y)
    show_score1(textX, textY)
    show_score2(textX2, textY2)

    # Update the Screen
    pygame.display.update()