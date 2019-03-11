import pygame, random

def onRect(rect, x, y):
    if rect[0] < x < rect[0]+rect[2] and rect[1] < y < rect[1]+rect[3]:
        return True
    return False

pygame.init()
width = 1000
height = 660
disp = pygame.display.set_mode((width,height))

#variables
done = False

TICK = 30

dude = pygame.image.load('dude.png')
dude = pygame.transform.scale(dude, (100,150))
xt = 500
yt = 300
parcham = [False, False, False, False] #bala,rast,paein,chap

cour = pygame.font.SysFont('cour.ttf', 35)

joon = 5
ticks = 0
time = 0

NUMBER_OF_BALLSr = 30
xr = NUMBER_OF_BALLSr * [0]
yr = NUMBER_OF_BALLSr * [0]
rr = NUMBER_OF_BALLSr * [0]
dxr = NUMBER_OF_BALLSr * [0]
dyr = NUMBER_OF_BALLSr * [0]
colorr = NUMBER_OF_BALLSr * [0]
for i in range(NUMBER_OF_BALLSr):
    xr[i] = random.randint(50,width - 50)
    yr[i] = random.randint(50,height - 50)
    dxr[i] = random.randint(1,7) * ( 1 if random.randint(1,4) % 2 == 0 else -1)
    dyr[i] = random.randint(1,7) * ( 1 if random.randint(1,4) % 2 == 0 else -1)
    rr[i] = random.randint(10,35)
    colorr[i] = (255,0,0)

NUMBER_OF_BALLSg = 20
xg = NUMBER_OF_BALLSg * [0]
yg = NUMBER_OF_BALLSg * [0]
rg = NUMBER_OF_BALLSg * [0]
dxg = NUMBER_OF_BALLSg * [0]
dyg = NUMBER_OF_BALLSg * [0]
colorg = NUMBER_OF_BALLSg * [0]
for i in range(NUMBER_OF_BALLSg):
    xg[i] = random.randint(50,width - 50)
    yg[i] = random.randint(50,height - 50)
    dxg[i] = random.randint(1,7) * ( 1 if random.randint(1,4) % 2 == 0 else -1)
    dyg[i] = random.randint(1,7) * ( 1 if random.randint(1,4) % 2 == 0 else -1)
    rg[i] = random.randint(10,35)
    colorg[i] = (0,255,0)


#main loop
while not done:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                parcham[3] = True
            if event.key == pygame.K_RIGHT:
                parcham[1] = True
            if event.key == pygame.K_UP:
                parcham[0] = True
            if event.key == pygame.K_DOWN:
                parcham[2] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                parcham[3] = False
            if event.key == pygame.K_RIGHT:
                parcham[1] = False
            if event.key == pygame.K_UP:
                parcham[0] = False
            if event.key == pygame.K_DOWN:
                parcham[2] = False

    #updates
    ticks += 1
    if ticks % TICK == 0:
        time += 1

    text = cour.render('Health = ' + str(joon), True, (0,0,255))
    text2 = cour.render('Time = ' + str(time), True, (0,0,255))

    if parcham[0] and yt >= 0:
        yt = yt - 7
    if parcham[1]and xt <= width - 100:
        xt = xt + 7
    if parcham[2] and yt <= height - 150:
        yt = yt + 7
    if parcham[3] and xt >= 0:
        xt = xt - 7

    for i in range(len(xr)):
        if onRect((xt, yt, 100, 150), xr[i], yr[i]):
            joon -= 1
            xr.pop(i)
            yr.pop(i)
            rr.pop(i)
            dxr.pop(i)
            dyr.pop(i)
            colorr.pop(i)
            break
    for i in range(len(xg)):
        if onRect((xt, yt, 100, 150), xg[i], yg[i]):
            joon += 1
            xg.pop(i)
            yg.pop(i)
            rg.pop(i)
            dxg.pop(i)
            dyg.pop(i)
            colorg.pop(i)
            break

    if joon < 0:
        done = True
        pm = 'You Lose!'
    if len(xg) == 0:
        done = True
        pm = 'You Win!'

    #draws
    disp.fill((0,0,0))
    for i in range(len(xr)):
        pygame.draw.circle(disp, colorr[i], (xr[i]+dxr[i],yr[i]),rr[i],0)
        if xr[i] >= width - rr[i]:
            dxr[i] = -dxr[i]
        if xr[i] <= rr[i]:
            dxr[i] = -dxr[i]
        if yr[i] >= height - rr[i]:
            dyr[i] = -dyr[i]
        if yr[i] <= rr[i]:
            dyr[i] = -dyr[i]
        xr[i] = xr[i] + dxr[i]
        yr[i] = yr[i] + dyr[i]
    for i in range(len(xg)):
        pygame.draw.circle(disp, colorg[i], (xg[i]+dxg[i],yg[i]),rg[i],0)
        if xg[i] >= width - rg[i]:
            dxg[i] = -dxg[i]
        if xg[i] <= rg[i]:
            dxg[i] = -dxg[i]
        if yg[i] >= height - rg[i]:
            dyg[i] = -dyg[i]
        if yg[i] <= rg[i]:
            dyg[i] = -dyg[i]
        xg[i] = xg[i] + dxg[i]
        yg[i] = yg[i] + dyg[i]
    disp.blit(dude,(xt,yt))
    disp.blit(text, (0, 0))
    disp.blit(text2, (width - text.get_width(), 0))
    pygame.display.update()
    pygame.time.Clock().tick(TICK)

disp2 = pygame.display.set_mode((width,height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
    disp2.fill((0,0,0))
    text3 = cour.render(pm, True, (255,255,255))
    disp2.blit(text3, (width / 2 - text3.get_width(), height / 2))
    pygame.display.update()
    pygame.time.Clock().tick(TICK)
pygame.quit()
