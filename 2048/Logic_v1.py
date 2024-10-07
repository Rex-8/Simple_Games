from random import choice

def create_board():return [['' for x in range(4)]for y in range(4)]
    
def add_element(bd):
    try:
        x,y = choice([(x,y) for x in range(4) for y in range(4) if bd[y][x] == '' ])
        bd[y][x] = 2
        return bd
    except:pass
    
def push(row ): 
    [row.remove('') for i in range(row.count(''))]
    row = ['' for i in range(4-len(row))]+row

    if row[3] == row[2]: row  = ['',row[0],row[1],row[2]+row[3]]  
    if row[2] == row[1]: row  = ['',row[0],row[1]+row[2],row[3]]  
    if row[1] == row[0]: row  = ['',row[0]+row[1],row[2],row[3]]  
        
    return list(row) 

def bd_transpose(bd): return [[bd[y][x] for y in range(4)] for x in range(4)]

def move_right(bd ): return add_element([push(row ) for row in bd])

def move_left(bd ): return add_element([push(row[::-1] )[::-1] for row in bd])

def move_down(bd ): return add_element(bd_transpose([push(row ) for row in bd_transpose(bd)]))

def move_up(bd ): return add_element(bd_transpose([push(row[::-1] )[::-1] for row in bd_transpose(bd)]))

def new_game(): return add_element(create_board()) 

def check_win(bd): return 1 in [2048 in row for row in bd]

def check_game_over(bd):
    GO = True
    if (bd[0][0] == bd[0][1]) or (bd[0][0] == bd[1][0]): GO = False
    elif (bd[3][3] == bd[3][2]) or (bd[3][3] == bd[2][3]): GO = False
    elif (bd[0][3] == bd[0][2]) or (bd[0][3] == bd[1][3]): GO = False
    elif (bd[3][0] == bd[2][0]) or (bd[3][0] == bd[3][1]): GO = False
    elif 1 in [bd[y][x] == bd[y][x+1] for x,y in [(1,0),(2,0)]]: GO = False
    elif 1 in [bd[y][x] == bd[y][x-1] for x,y in [(1,3),(2,3)]]: GO = False
    elif 1 in [bd[y][x] == bd[y+1][x] for x,y in [(0,1),(0,2)]]: GO = False
    elif 1 in [bd[y][x] == bd[y-1][x] for x,y in [(3,1),(3,2)]]: GO = False
    elif 1 in [bd[y][x] == bd[yo][xo] for x,y in [(1,1),(1,2),(2,1),(2,2)] for xo,yo in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)] ]:GO=False
    return GO