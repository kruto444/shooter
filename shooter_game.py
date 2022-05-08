#Создай собственный Шутер!
from random import randint
from pygame import *
from time import time as timer
clock = time.Clock()
FPS = 60


h_win = 500 #высота экрана
w_win = 700 #ширина экрана

class GameSprite(sprite.Sprite):
    def __init__(self,name,speed,h,w,y,x,images):
        super().__init__()
        self.name = name
        self.speed = speed
        self.image = transform.scale(image.load(images),(w,h))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        

class Player(GameSprite):
    def update(self):
        global toplivo
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5 and toplivo > 0:
            self.rect.x -= self.speed
            toplivo = toplivo - 1

        if keys[K_d] and self.rect.x < w_win - w_player - 5 and toplivo > 0:
            self.rect.x += self.speed
            toplivo = toplivo - 1
            
    def firee(self):
        global patron
        bullet = Bulet('пуля',5,h_bulet,w_bulet,self.rect.top,self.rect.centerx-w_bulet/2,'bullet.png')
        bullets.add(bullet)
        patron -= 1
class Enemy(GameSprite): 
    def update(self): # Функция перемещения 
        self.rect.y += self.speed
        if self.rect.y > h_win - hight_enemy:
            self.rect.y = 0
            self.rect.x = randint(0,w_win-w_enemy)
            global propushen
            propushen += 1
            global coins
            coins -= 5
class Bulet(GameSprite): 
    def update(self): # Функция перемещения 
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()     
class Boss(GameSprite):
    direction = "left" #направление 
    def update(self):
        if self.rect.x <= 200 : #граница
            self.direction = "right"
        if self.rect.x >= 400:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def firee(self): 
        bullet = bulet_boss('пуля босса',3,h_bullet_boss,w_bullet_boss,self.rect.bottom,self.rect.centerx-w_bullet_boss/2,'bullet.png')
        bullet.image = transform.rotate(bullet.image,180)  
        bullets_boss.add(bullet)
class bulet_boss(GameSprite): 
    def update(self): # Функция перем ещения 
        
        self.rect.y += self.speed
        if self.rect.y > h_win:
            self.kill()
#константы
w_player = 100
h_player = 100

w_enemy = 100
hight_enemy = 100

w_bulet = 20
h_bulet = 20
#босс и его пули
h_bullet_boss = 35
w_bullet_boss = 35

w_boss = 175
h_boss = 175

nope = 1

toplivo_strat = 1000
toplivo = toplivo_strat

patron_start = 20
patron = patron_start

coins_start = 5
coins = coins_start

speed_en_start = 4.5
speed_en = speed_en_start

deadpool_start = 0
deadpool = deadpool_start

lvl_start = 1
lvl = lvl_start

lvl_1 = 1

eybito = 0

hp_player = 3
hp_boos_start = 10
hp_boos = hp_boos_start

propushen_start = 0
propushen = propushen_start

#время
shoot_timer = 0
interval_shoot = 4

font.init()
#создаем фоновую музыку
#шрифты 
font.init()
'''
font1 = font.Font('minecraft.ttf',36)
font2 = font.Font('minecraft.ttf',64)
'''
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',64)
win_text = font2.render('winer',1,(255,0,0))
lose_text = font2.render('loser',1,(255,0,0))
'''
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


win_sound = mixer.Sound('fire.ogg')
'''
#создай окно игры
window = display.set_mode((w_win,h_win))
display.set_caption('Galactic shuter')
#задай фон сцены
b_im = image.load('galaxy.jpg')
bdgr = transform.scale(b_im,(w_win,h_win))
#создай 2 спрайта и размести их на сцене
img_res = 'res.png'

'''
win_text = font.render('mission complete',True,(0,255,0))
fail_text = font.render('mission failed',True,(255,0,0))
'''


player = Player('player',10,h_player,w_player,400,300,'rocket.png')
bosss = Boss('босс',7,h_boss,w_boss,0,w_win/2-w_boss/2,'ufo.png')
'''
monster = Enemy('nps',10,hight_enemy,w_enemy,100,20,'ufo.png')
'''
bullets_boss = sprite.Group(  )
bullets = sprite.Group()
monsters = sprite.Group()


restart = GameSprite('рестарт',0,70,70,50,w_win-120,img_res)

'''
gold = GameSprite('gold',10,100,100,10,330,'treasure.png')
'''
#игровой цыкл
#игровой цыкл
game = True
finish = False
hasBoss = False
while game:
    #обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():#перебор событий
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and patron > 0:
                player.firee()
            if e.key == K_r and coins > 99:
                coins -= 100
                patron += 20
                toplivo += 150
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if restart.rect.collidepoint(e.pos):
                    finish = False
                    propushen = propushen_start
                    coins = coins_start
                    deadpool = deadpool_start
                    speed_en = speed_en_start
                    toplivo = toplivo_strat
                    lvl = lvl_start
                    lvl_1 = 1
                    for a in monsters:
                        a.kill()
                    for i in range(4):
                        rand_x = randint(0,w_win-w_enemy)
                        enemy = Enemy('nps',speed_en,hight_enemy,w_enemy,-hight_enemy,rand_x,'ufo.png')
                        monsters.add(enemy)
                    
    
    if not finish:
        window.blit(bdgr,(0,0))
        player.update()
        monsters.update()
        bullets.update()
        bosss.update()

        list_collides = sprite.groupcollide(monsters,bullets,True,True)
        for colide in list_collides:
            deadpool += 1
            coins += 15
            rand_x = randint(0,w_win-w_enemy)
            rand_y = randint(0,50)
            speed_en += 0.1
            enemy = Enemy('nps',speed_en,hight_enemy,w_enemy,rand_y,rand_x,'ufo.png')
            monsters.add(enemy)
        '''
        if deadpool >= 50:
            finish = True
            window.blit(win_text,(200,300))
            restart.reset()
        '''
        if propushen >= 100:
            finish = True
            window.blit(lose_text,(200,300))
            restart.reset()
        if deadpool >5 and deadpool <16 and nope == 2:
            lvl = 2
            lvl_1 = 2
        if deadpool >15 and deadpool < 31 and nope == 3:
            lvl = 3
            lvl_1 = 3
        if deadpool >30 and deadpool < 51 and nope == 4:
            lvl = 4
            lvl_1 = 4
        if deadpool > 50 and nope == 5:
            lvl = 5
            lvl_1 = 5
        if lvl_1 == 1:
            for i in range(1):
                rand_x = randint(0,w_win-w_enemy)
                enemy = Enemy('nps',speed_en,hight_enemy,w_enemy,-hight_enemy,rand_x,'ufo.png')
                monsters.add(enemy)
            lvl_1 = 0
            nope = 2
        if lvl_1 == 2:
            for a in monsters:
                a.kill()
            for i in range(2):
                rand_x = randint(0,w_win-w_enemy)
                enemy = Enemy('nps',speed_en,hight_enemy,w_enemy,-hight_enemy,rand_x,'ufo.png')
                monsters.add(enemy)
            nope = 3
            lvl_1 = 0
        if lvl_1 == 3:
            for a in monsters:
                a.kill()
            for i in range(3):
                rand_x = randint(0,w_win-w_enemy)
                enemy = Enemy('nps',speed_en,hight_enemy,w_enemy,-hight_enemy,rand_x,'ufo.png')
                monsters.add(enemy)
            nope = 4
            lvl_1 = 0
        if lvl_1 == 4:
            for a in monsters:
                a.kill()
            for i in range(4):
                rand_x = randint(0,w_win-w_enemy)
                enemy = Enemy('nps',speed_en,hight_enemy,w_enemy,-hight_enemy,rand_x,'ufo.png')
                monsters.add(enemy)
            nope = 5
            lvl_1 = 0
        if lvl_1 == 5:
            for a in monsters:
                a.kill()
            bosss.reset()
            now_timer = timer()
            
            if now_timer - shoot_timer >= interval_shoot:
                bosss.firee()
                shoot_timer = timer()
            bullets_boss.update()
            bullets_boss.draw(window)
            nope = 0    
            list_collides_1 = sprite.spritecollide(bosss,bullets,True)
            for colibe in list_collides_1:
                hp_boos -= 1
                if hp_boos == 0:
                    finish = True
                    text_boss =  font2.render('вы выйграли ',1,(255,255,255))
                    window.blit(text_boss,(100,200))
            text_boss =  font2.render('хп боссв: '+str(hp_boos),1,(255,255,255))
            window.blit(text_boss,(10,300))
            
        player.reset()
        monsters.draw(window)
        bullets.draw(window)
        risuem =  font1.render('LVL: '+str(lvl),1,(255,255,255))
        window.blit(risuem,(10,10))
        risuem =  font1.render('Пропущено: '+str(propushen),1,(255,255,255))
        window.blit(risuem,(10,50))
        risuem =  font1.render('Убито: '+str(deadpool),1,(255,255,255))
        window.blit(risuem,(10,90))
        
        risuem =  font1.render('Топливо: '+str(toplivo),1,(255,255,255))
        window.blit(risuem,(10,370))
        risuem =  font1.render('Патроны: '+str(patron),1,(255,255,255))
        window.blit(risuem,(10,410))
        risuem =  font1.render('Cоины: '+str(coins),1,(255,255,255))
        window.blit(risuem,(10,450))
    display.update( )
    clock.tick(FPS)
