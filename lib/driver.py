import random,pygame,json

pygame.init()

with open('lib/config.json',) as json_file:
    configs = json.load(json_file)

width=configs['board']['width']
height=configs['board']['height']
n=configs['board']['blocks']
spacing=configs['visuals']['spacing']
design_spacing=configs['visuals']['design_spacing']
board=pygame.display.set_mode((width,height))
pygame.display.set_caption(' '*120+':::2048:::')


a=[[0]]        #NOT to be edited
color0=pygame.Color(configs['colors']['block0'])
color2=pygame.Color(configs['colors']['block2'])
color4=pygame.Color(configs['colors']['block4'])
color8=pygame.Color(configs['colors']['block8'])
color16=pygame.Color(configs['colors']['block16'])
color32=pygame.Color(configs['colors']['block32'])
color64=pygame.Color(configs['colors']['block64'])
color128=pygame.Color(configs['colors']['block128'])
color256=pygame.Color(configs['colors']['block256'])
color512=pygame.Color(configs['colors']['block512'])
color1024=pygame.Color(configs['colors']['block1024'])
color2048=pygame.Color(configs['colors']['block2048'])
white=pygame.Color(configs['colors']['white'])
brown=pygame.Color(configs['colors']['brown'])
black=(configs['colors']['black'])
    
    
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
    pygame.draw.rect(board,brown,(int(width/n*spacing+design_spacing),int(height/n*spacing+design_spacing),int(width*(1-2/n*spacing)-2*design_spacing),int(height*(1-2/n*spacing)-2*design_spacing)))
    for i in range(1,n+1):
        for j in range(1,n+1):
            
            pygame.draw.rect(board,eval('color'+str(l[i][j])),(int((j-1+spacing)*width/n),int((i-1+spacing)*height/n),int(width/n*(1-2*spacing)),int(height/n*(1-2*spacing))))
            if l[i][j]!=0:
                
                output(white,(int((j-0.5)*width/n),int((i-0.5)*height/n)),'monaco',int(500/n),board,str(l[i][j]))
                if l[i][j]==2048:
                    output(white,(int(width/2),50),'console',100,board,'YOU WIN!!')
                    while True:
                        for event in pygame.event.get():
                            if event.type==pygame.KEYDOWN:
                                pygame.quit()
                                quit()
                    
            else:output(white,(int(width/2),0),'console',100,board,' ')
    
def check_lose(l,n):
    if move_right(l,n)[0]==False and move_left(l,n)[0]==False and move_down(l,n)[0]==False and move_up(l,n)[0]==False:
        output(brown,(int(width/2),0),'console',100,board,'GAME OVER!!!')
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
        
output(white,(width/2,750),'monaco',50,board,'...HIT ANY KEY TO CONTINUE...')
        

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
                else:
                    temp=temptemp
                
            elif event.key==pygame.K_LEFT:

                temptemp=d_list(temp)
                temp=d_list(a)
                get_rand,a=move_left(a,n)
                if get_rand==True:
                    a=get_random(a,n)
                else:
                    temp=temptemp
                
            elif event.key==pygame.K_DOWN:
                
                temptemp=d_list(temp)
                temp=d_list(a)
                get_rand,a=move_down(a,n)
                if get_rand==True:
                    a=get_random(a,n)
                else:
                    temp=temptemp
                
            elif event.key==pygame.K_RIGHT:
                
                temptemp=d_list(temp)
                temp=d_list(a)
                get_rand,a=move_right(a,n)
                if get_rand==True:
                    a=get_random(a,n)
                else:
                    temp=temptemp
                    
            elif event.key==pygame.K_SPACE:
                
                a=d_list(temp)

            elif event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            
            pygame_printing(a,n)
            check_lose(d_list(a),n)
