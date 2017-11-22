import random,pygame,time

pygame.init()

width,height=1366,911
board=pygame.display.set_mode((width,height))



def move_down(l,n):
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
                    l[1][i]=0
        
        for j in range(n,1,-1):
            if l[j][i]==l[j-1][i] and l[j][i]!=0:
                l[j][i]*=2
                l[j-1][i]=0
                
                for k in range(j-1,1,-1):
                    l[k][i]=l[k-1][i]
                l[1][i]=0
                

                
    return l


def move_up(l,n):
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
                    l[n][i]=0
        
        for j in range(1,n):
            if l[j][i]==l[j+1][i] and l[j][i]!=0:
                l[j][i]*=2
                l[j+1][i]=0
                
                for k in range(j+1,n):
                    l[k][i]=l[k+1][i]
                l[n][i]=0
        #print(l)

                
    return l


def move_right(l,n):
    
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
                    l[i][1]=0
        
        for j in range(n,1,-1):
            if l[i][j]==l[i][j-1] and l[i][j]!=0:
                l[i][j]*=2
                l[i][j-1]=0
                
                for k in range(j-1,1,-1):
                    l[i][k]=l[i][k-1]
                l[i][1]=0
                
    return l


def move_left(l,n):
    
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
                    l[i][n]=0
        
        for j in range(1,n):
            if l[i][j]==l[i][j+1] and l[i][j]!=0:
                l[i][j]*=2
                l[i][j+1]=0
                
                for k in range(j+1,n):
                    l[i][k]=l[i][k+1]
                l[i][n]=0
                
    return l
            
            
                
    
    
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
    choose=random.randint(0,len(temp)-1)
    temp=temp[choose]
    
    l[temp[0]][temp[1]]=random.randint(1,2)*2
    
    return l
    
n=4
a=[[0]]
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
            output(white,(int((j-0.5)*width/n),int((i-1)*height/n)),'monaco',100,board,str(l[i][j]))
    

        
        
        
while(True):
    
    white=pygame.Color(255,255,255)
    black=pygame.Color(0,0,0)
    
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                a=move_up(a,4)
            elif event.key==pygame.K_LEFT:
                a=move_left(a,4)
            elif event.key==pygame.K_DOWN:
                a=move_down(a,4)
            elif event.key==pygame.K_RIGHT:
                a=move_right(a,4)
                
            a=get_random(a,n)
            pygame_printing(a,n)
