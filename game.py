import pygame
import time
import monkey
import money
import random
import json

def start():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    pygame.init()
    window = pygame.display.set_mode((800, 500))
    fps = pygame.time.Clock()

    moneylist = []
    lengame = 30
    points = 0
    islose = False

    fon = pygame.image.load("gfontex.png")
    fon = pygame.transform.scale(fon, (800, 500))
    losefon = pygame.image.load("pixelartlose.png")
    losefon = pygame.transform.scale(losefon, (800, 500))

    for i in range(lengame):
        moneylist.append(money.Money(random.randint(0, 750), random.randint(-100*lengame, 0), 50, 50 ,5 ,'gmontex.png' ))

    gg = monkey.Monkey(500 , 500 , 50 ,50 ,"gcaptex.png" , 5 , moneylist)

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                data['money'] += gg.getpint()
                with open('data.json', 'w', ) as f:
                    json.dump(data, f, indent=4)
                pygame.quit()

        for mm in moneylist:
            mm.move()
            if mm.hitbox.y > 800 :
                islose = True

        window.blit(fon, [0 , 0])

        gg.move()

        for rm in moneylist:
            rm.render(window)

        gg.render(window)

        if islose:
            window.blit(losefon , [0 ,0])

        pygame.display.flip()
        fps.tick(60)

