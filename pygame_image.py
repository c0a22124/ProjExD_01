import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)

    kouka_img = pg.image.load("ex01/fig/3.png") 
    kouka_img = pg.transform.flip(kouka_img,True,False)
    kouka_img2 = pg.transform.rotozoom(kouka_img,10,1.0)
    img_lst = []
    for  i in range(10):
        img_lst.append(pg.transform.rotozoom(kouka_img,i,1.0))
    for j in range(9):
        img_lst.append(pg.transform.rotozoom(kouka_img,9-j,1.0))
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        

        screen.blit(bg_img, [-1*(tmr%2400), 0])
        screen.blit(bg_img2, [-1*(tmr%2400)+1600, 0])
        screen.blit(img_lst[tmr%19],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()