import pygame
pygame.init()

win = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Froggame")

walkRight = [pygame.image.load('frogr.png')]
walkLeft = [pygame.image.load('frogl.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('frog.png')

x = 10
y = 600
width = 136
height = 128
vel = 12
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1 >= 3:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update() 


#Mainloop
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1366 - vel - width:  # Making sure the top right corner of our character is less than the screen width - its width 
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False  
        walkCount = 0
    if not(isJump):  
        if keys[pygame.K_DOWN] and y < 768 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
           neg = 1
           if jumpCount < 0:
               neg = -1
           y -= (jumpCount ** 2) * 0.5 * neg
           jumpCount -= 1 
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()


pygame.quit()
