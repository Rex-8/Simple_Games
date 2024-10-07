from Logic_v1 import *
import pygame

pygame.init()

text_col_dark,text_col_light,border_col,win_col = '#776E65','#837970','#BBADA0','#FAF8EF'
element_bg_col = {'':'#CDC1B4',2 :'#EEE4DA',4 :'#EDE0C8',8 :'#F3B27A',16:'#F69664',32:'#F77C5F',64:'#F75F3B',128:'#EDD073',256:'#EDCC62',512:'#EDC850',1024:'#EDC540',2048:'#EDC22E'}
element_fg_col = {'':'#CDC1B4',2 :'#776E65',4 :'#756C63',8 :'#F9F6F2',16:'#F8F5F1',32:'#F8F5F0',64:'#F9F7F4',128:'#F8F5F1',256:'#F8F5F0',512:'#F9F6F2',1024:'#F9F7F7',2048:'#F9F6F2'}

def draw_base():
    global text2Rect
    win.fill(win_col)
    pygame.draw.rect(win, border_col, pygame.Rect(25, 25+140, 410, 410))
    pygame.draw.line(win, border_col, (25,140),(435,140))
    
    font1 = pygame.font.SysFont('freesansbold.ttf', 100)
    text1 = font1.render('2048', True, text_col_dark, win_col)
    text1Rect = text1.get_rect()
    text1Rect.center = (220, 70)
    win.blit(text1, text1Rect)

def update_board(bd):
    
    for y in range(4):
        for x in range(4):
            pygame.draw.rect(win,element_bg_col[bd[y][x]],pygame.Rect(35 + 100*x , 140 +35 +100*y , 90 , 90))
            font2 = pygame.font.SysFont('freesansbold.ttf', 34)
            texto = str(bd[y][x])
            text2 = font2.render(texto, True, element_fg_col[bd[y][x]],element_bg_col[bd[y][x]])
            text2Rect = text2.get_rect()
            text2Rect.center = (25+10+45 + 100*x, 140 + 25 + 10 + 45 + 100*y)
            win.blit(text2, text2Rect)
            
def game_won(bd):
    font1 = pygame.font.SysFont('freesansbold.ttf', 60)
    
    pygame.draw.rect(win, border_col, pygame.Rect(25, 25+140, 410, 410))
    text1 = font1.render('You Win!', True, win_col, border_col)
    text1Rect = text1.get_rect()
    text1Rect.center = (230, 230 + 140)
    win.blit(text1, text1Rect)
    
def game_over(bd):
    font1 = pygame.font.SysFont('freesansbold.ttf', 60)
    
    pygame.draw.rect(win, border_col, pygame.Rect(25, 25+140, 410, 410))
    text1 = font1.render('Game Over!', True, win_col, border_col)
    text1Rect = text1.get_rect()
    text1Rect.center = (230, 230 + 140)
    win.blit(text1, text1Rect)

win = pygame.display.set_mode((410+50,410+50+200-60))
pygame.display.set_caption('2048')
run = True
draw_base()
bd = new_game( )
game_end = False

while run == True:
    update_board(bd)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif (event.type == pygame.KEYDOWN) and (game_end == False):
            if event.key == pygame.K_LEFT:
                bd = move_left(bd)
            elif event.key == pygame.K_RIGHT:
                bd = move_right(bd)
            elif event.key == pygame.K_DOWN:
                bd = move_down(bd)
            elif event.key == pygame.K_UP:
                bd = move_up(bd)
            elif event.key == pygame.K_1:
                bd[3][3] = 2048
                
    if check_win(bd):
        #game_won(bd)
        pass
    elif check_game_over(bd):
        game_over(bd)
        game_end = True
        
    pygame.display.flip()        
pygame.quit()