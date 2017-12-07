import random,pygame,time

pygame.init()

width,height=1000,1000     #editable
n=6                        #editable
board=pygame.display.set_mode((width,height))
pygame.display.set_caption(' '*120+':::2048:::')


a=[[0]]        #NOT to be edited
color2=pygame.Color(214,216,171)
color4=pygame.Color(216,181,124)
color8=pygame.Color(255,156,43)
color16=pygame.Color(255,90,30)
color32=pygame.Color(255,50,16)
color64=pygame.Color(255,0,0)
color128=pygame.Color(216,209,32)
color256=pygame.Color(216,186,48)
color512=pygame.Color(216,156,39)
color1024=pygame.Color(242,175,44)
color2048=pygame.Color(255,184,46)
white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)
    
    
def d_list(l):
    li=[]
    for i in l:
        li.append(list(i))
    return li

def move_down(l,n):
    
    change=False
    for i in range(1,n+1):
        for k in range(n,1,-1):
            conti_nue=False
            
            for j in range(1,k):
                if l[j][i]!=0:
                    conti_nue=True
            
            if conti_nue==True:
                while l[k][i]==0:
                    for j in range(k,1,-1):
                        l[j][i]=l[j-1][i]
                    change=True
                    l[1][i]=0
        
        for j in range(n,1,-1):
            if l[j][i]==l[j-1][i] and l[j][i]!=0:
                l[j][i]*=2
                l[j-1][i]=0
                change=True
                
                for k in range(j-1,1,-1):
                    l[k][i]=l[k-1][i]
                l[1][i]=0
                
    return change,l


def move_up(l,n):
    
    change=False
    for i in range(1,n+1):
        for k in range(1,n+1):
            conti_nue=False
            
            for j in range(k,n+1):
                if l[j][i]!=0:
                    conti_nue=True
            
            if conti_nue==True:
                while l[k][i]==0:
                    for j in range(k,n):
                        l[j][i]=l[j+1][i]
                    change=True
                    l[n][i]=0
        
        for j in range(1,n):
            if l[j][i]==l[j+1][i] and l[j][i]!=0:
                l[j][i]*=2
                l[j+1][i]=0
                change=True
                
                for k in range(j+1,n):
                    l[k][i]=l[k+1][i]
                l[n][i]=0
        #print(l)
    #if change!=False:l=get_random(l,n)
    return change,l


def move_right(l,n):
    
    change=False
    for i in range(1,n+1):
        
        for j in range(n,1,-1):
            
            conti_nue=False
            for k in range(1,j):
                if l[i][k]!=0:
                    conti_nue=True
                
            if conti_nue==True:
                while l[i][j]==0:
                    for k in range(j,1,-1):
                        l[i][k]=l[i][k-1]
                    change=True
                    l[i][1]=0
        
        for j in range(n,1,-1):
            if l[i][j]==l[i][j-1] and l[i][j]!=0:
                l[i][j]*=2
                l[i][j-1]=0
                change=True
                
                for k in range(j-1,1,-1):
                    l[i][k]=l[i][k-1]
                l[i][1]=0
                
    #if change!=False:l=get_random(l,n)
    return change,l


def move_left(l,n):
    
    change=False
    for i in range(1,n+1):
        
        for j in range(1,n+1):
            
            conti_nue=False
            for k in range(j,n+1):
                if l[i][k]!=0:
                    conti_nue=True
                
            if conti_nue==True:
                while l[i][j]==0:
                    for k in range(j,n):
                        l[i][k]=l[i][k+1]
                    change=True
                    l[i][n]=0
        
        for j in range(1,n):
            if l[i][j]==l[i][j+1] and l[i][j]!=0:
                l[i][j]*=2
                l[i][j+1]=0
                change=True
                
                for k in range(j+1,n):
                    l[i][k]=l[i][k+1]
                l[i][n]=0
                
    #if change!=False:l=get_random(l,n)
    return change,l
            
            
                
    
    
def printing(l,n):
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            
            print(l[i][j],'',end='')
        print()
        
    
    
def get_random(l,n):
    temp=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if l[i][j]==0:
                temp.append([i,j])
                
    if len(temp)==0:
        pygame.quit()
        quit()
    choose=random.randint(0,len(temp)-1)
    temp=temp[choose]
    
    l[temp[0]][temp[1]]=random.randint(1,2)*2
    
    return l

for i in range(1,n+1):
    a.append([])
    for j in range(n+1):
        a[i].append(0)

def output(color,coordinates,font,size,surf,text):
    myfont=pygame.font.SysFont(font,size)
    mytext=myfont.render(text,True,color)
    myrect=mytext.get_rect()
    myrect.midtop=coordinates
    surf.blit(mytext,myrect)
    pygame.display.update()

def pygame_printing(l,n):
    board.fill(black)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if l[i][j]!=0:
                pygame.draw.rect(board,eval('color'+str(l[i][j])),(int((j-1)*width/n+2),int((i-1)*height/n+2),int(width/n)-2,int(height/n)-2))
                output(white,(int((j-0.5)*width/n),int((i-1)*height/n)),'monaco',100,board,str(l[i][j]))
                if l[i][j]==2048:
                    output(white,(int(width/2),0),'console',200,board,'YOU WIN!!')
            else:output(white,(int(width/2),0),'console',100,board,' ')
    
def check_lose(l,n):
    if move_right(l,n)[0]==False and move_left(l,n)[0]==False and move_down(l,n)[0]==False and move_up(l,n)[0]==False:
        output(black,(int(width/2),0),'console',100,board,'GAME OVER!!!')
        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    pygame.quit()
                    quit()
                    

                    
output(white,(width/2,50),'console',60,board,'CONTROLS:')
output(white,(width/2,150),'console',40,board,'<-  LEFT')
output(white,(width/2,270),'console',40,board,'-> RIGHT')
output(white,(width/2-60,390),'console',40,board,'^ UP')
output(white,(width/2-96,405),'console',30,board,'|')
output(white,(width/2-90,495),'console',30,board,'|')
output(white,(width/2-30,510),'console',40,board,'V DOWN')
output(white,(width/2,630),'console',40,board,'|__| UNDO')
        
output(white,(width/2,height-50),'monaco',50,board,'...HIT ANY KEY TO CONTINUE...')
        

a=get_random(a,n)
#a=get_random(a,n)
temp=d_list(a)

while(True):

    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:

                temptemp=d_list(temp)
                temp=d_list(a)
                get_rand,a=move_up(a,n)
                if get_rand==True:
                    a=get_random(a,n)
                else:temp=temptemp
                
            elif event.key==pygame.K_LEFT:

                temptemp=d_list(temp)
                temp=d_list(a)
                get_rand,a=move_left(a,n)
                if get_rand==True:
                    a=get_random(a,n)
                    temp=temptemp
                
            elif event.key==pygame.K_DOWN:
                
                temptemp=d_list(temp)
                temp=d_list(a)
                get_rand,a=move_down(a,n)
                if get_rand==True:
                    a=get_random(a,n)
                    temptemp
                
            elif event.key==pygame.K_RIGHT:
                
                temptemp=d_list(temp)
                temp=d_list(a)
                get_rand,a=move_right(a,n)
                if get_rand==True:
                    a=get_random(a,n)
                    temp=temptemp
                    
            elif event.key==pygame.K_SPACE:
                
                a=d_list(temp)

            elif event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            
            pygame_printing(a,n)
            check_lose(d_list(a),n)
