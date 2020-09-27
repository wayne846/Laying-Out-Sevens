

import time
import random

import tkinter as tk

a1=[[],[],[],[],[]]  #AI1 的牌
b1=[[],[],[],[],[]]  #AI2 的牌
c1=[[],[],[],[],[]]  #AI3 的牌
d1=[[],[],[],[],[]]  #玩家 的牌
a2=[]                #出牌區
b2=[]
c2=[]
d2=[]

for i in range(4):                  #4種花色
    for j in range(13):             #13種數字
        if i==0:                    #分配梅花
            b=0
            while b!=1: 
                a=random.randint(1,4)   #a為隨機1~4
                if a==1:
                    if len(a1[0])+len(a1[1])+len(a1[2])+len(a1[3])!=13:
                        a1[i].append(j+1)
                        b+=1
                elif a==2:
                    if len(b1[0])+len(b1[1])+len(b1[2])+len(b1[3])!=13:
                        b1[i].append(j+1)
                        b+=1
                elif a==3:
                    if len(c1[0])+len(c1[1])+len(c1[2])+len(c1[3])!=13:
                        c1[i].append(j+1)
                        b+=1
                else:
                    if len(d1[0])+len(d1[1])+len(d1[2])+len(d1[3])!=13:
                        d1[i].append(j+1)
                        b+=1
        elif i==1:                 #分配方塊
            b=0
            while b!=1: 
                a=random.randint(1,4)   
                if a==1:
                    if len(a1[0])+len(a1[1])+len(a1[2])+len(a1[3])!=13:
                        a1[i].append(j+1)
                        b+=1
                elif a==2:
                    if len(b1[0])+len(b1[1])+len(b1[2])+len(b1[3])!=13:
                        b1[i].append(j+1)
                        b+=1
                elif a==3:
                    if len(c1[0])+len(c1[1])+len(c1[2])+len(c1[3])!=13:
                        c1[i].append(j+1)
                        b+=1
                else:
                    if len(d1[0])+len(d1[1])+len(d1[2])+len(d1[3])!=13:
                        d1[i].append(j+1)
                        b+=1
          
        elif i==2:                 #分配愛心
            b=0
            while b!=1: 
                a=random.randint(1,4)   
                if a==1:
                    if len(a1[0])+len(a1[1])+len(a1[2])+len(a1[3])!=13:
                        a1[i].append(j+1)
                        b+=1
                elif a==2:
                    if len(b1[0])+len(b1[1])+len(b1[2])+len(b1[3])!=13:
                        b1[i].append(j+1)
                        b+=1
                elif a==3:
                    if len(c1[0])+len(c1[1])+len(c1[2])+len(c1[3])!=13:
                        c1[i].append(j+1)
                        b+=1
                else:
                    if len(d1[0])+len(d1[1])+len(d1[2])+len(d1[3])!=13:
                        d1[i].append(j+1)
                        b+=1
      
        else:                      #分配黑桃
            b=0
            while b!=1: 
                a=random.randint(1,4)   
                if a==1:
                    if len(a1[0])+len(a1[1])+len(a1[2])+len(a1[3])!=13:
                        a1[i].append(j+1)
                        b+=1
                elif a==2:
                    if len(b1[0])+len(b1[1])+len(b1[2])+len(b1[3])!=13:
                        b1[i].append(j+1)
                        b+=1
                elif a==3:
                    if len(c1[0])+len(c1[1])+len(c1[2])+len(c1[3])!=13:
                        c1[i].append(j+1)
                        b+=1
                else:
                    if len(d1[0])+len(d1[1])+len(d1[2])+len(d1[3])!=13:
                        d1[i].append(j+1)
                        b+=1

win=tk.Tk()
win.geometry('700x500')
win.title('牌七GUI')
win.resizable(False,False)

f=random.randint(0,3)  #從誰開始
if a1[f].count(7)==1:
    s=4
elif b1[f].count(7)==1:
    s=3
elif c1[f].count(7)==1:
    s=2
else:
    s=1 
if s==1:
    s=4
elif s==2:
    s=3
elif s==3:
    s=2
else:
    s=1
def start():
    global s
    global isok
        
     
    cover=False
    

    if s==1:
        for i in range(1):  #輪到1號
            isok=False
            if a1[0].count(7)==1:
                a2.append(7)
                a1[0].remove(7)
                isok=True
                break
            if a1[1].count(7)==1:
                b2.append(7)
                a1[1].remove(7)
                isok=True
                break
            if a1[2].count(7)==1:
                c2.append(7)
                a1[2].remove(7)
                isok=True
                break
            if a1[3].count(7)==1:
                d2.append(7)
                a1[3].remove(7)
                isok=True
                break
            a=[0,1,2,3]
            random.shuffle(a)
            for v in a:
                b=random.randint(0,1)
                if v==0 and a2.count(7)==1:
                    if a1[v].count(min(a2)-1)==1 and a1[v].count(max(a2)+1)==1:
                        if b==0:
                            a2.insert(0,min(a2)-1)
                            a1[v].remove(min(a2))
                            isok=True
                            break
                        if b==1:
                            a2.append(max(a2)+1)
                            a1[v].remove(max(a2))
                            isok=True
                            break
                    if a1[v].count(min(a2)-1)==1:
                        a2.insert(0,min(a2)-1)
                        a1[v].remove(min(a2))
                        isok=True
                        break
                    if a1[v].count(max(a2)+1)==1:
                        a2.append(max(a2)+1)
                        a1[v].remove(max(a2))
                        isok=True
                        break
                if v==1 and b2.count(7)==1:
                    if a1[v].count(min(b2)-1)==1 and a1[v].count(max(b2)+1)==1:
                        if b==0:
                            b2.insert(0,min(b2)-1)
                            a1[v].remove(min(b2))
                            isok=True
                            break
                        if b==1:
                            b2.append(max(b2)+1)
                            a1[v].remove(max(b2))
                            isok=True
                            break
                    if a1[v].count(min(b2)-1)==1:
                        b2.insert(0,min(b2)-1)
                        a1[v].remove(min(b2))
                        isok=True
                        break
                    if a1[v].count(max(b2)+1)==1:
                        b2.append(max(b2)+1)
                        a1[v].remove(max(b2))
                        isok=True
                        break
                if v==2 and c2.count(7)==1:
                    if a1[v].count(min(c2)-1)==1 and a1[v].count(max(c2)+1)==1:
                        if b==0:
                            c2.insert(0,min(c2)-1)
                            a1[v].remove(min(c2))
                            isok=True
                            break
                        if b==1:
                            c2.append(max(c2)+1)
                            a1[v].remove(max(c2))
                            isok=True
                            break
                    if a1[v].count(min(c2)-1)==1:
                        c2.insert(0,min(c2)-1)
                        a1[v].remove(min(c2))
                        isok=True
                        break
                    if a1[v].count(max(c2)+1)==1:
                        c2.append(max(c2)+1)
                        a1[v].remove(max(c2))
                        isok=True
                        break
                if v==3 and d2.count(7)==1:
                    if a1[v].count(min(d2)-1)==1 and a1[v].count(max(d2)+1)==1:
                        if b==0:
                            d2.insert(0,min(d2)-1)
                            a1[v].remove(min(d2))
                            isok=True
                            break
                        if b==1:
                            d2.append(max(d2)+1)
                            a1[v].remove(max(d2))
                            isok=True
                            break
                    if a1[v].count(min(d2)-1)==1:
                        d2.insert(0,min(d2)-1)
                        a1[v].remove(min(d2))
                        isok=True
                        break
                    if a1[v].count(max(d2)+1)==1:
                        d2.append(max(d2)+1)
                        a1[v].remove(max(d2))
                        isok=True
                        break
            if isok==False:
                b=[0,1,2,3]
                random.shuffle(b)
                for v in b:
                    if (v==0)and(len(a1[0])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
                    elif (v==1)and(len(a1[1])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
                    elif (v==2)and(len(a1[2])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
                    elif (v==3)and(len(a1[3])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
        
        msg1_lb.config(text='輪到1號了')
        if cover==True:
            msg2_lb.config(text='1號蓋牌')
            cover=False
        else:
            msg2_lb.config(text='')
        a2_lb.config(text='梅花:'+str(a2))
        b2_lb.config(text='方塊:'+str(b2))
        c2_lb.config(text='愛心:'+str(c2))
        d2_lb.config(text='黑桃:'+str(d2))
        
        
        
    if s==2:  #輪到2號
        for i in range(1):
            isok=False
            if b1[0].count(7)==1: #先出7
                a2.append(7)
                b1[0].remove(7)
                isok=True
                break
            if b1[1].count(7)==1:
                b2.append(7)
                b1[1].remove(7)
                isok=True
                break
            if b1[2].count(7)==1:
                c2.append(7)
                b1[2].remove(7)
                isok=True
                break
            if b1[3].count(7)==1:
                d2.append(7)
                b1[3].remove(7)
                isok=True
                break
            a=[0,1,2,3]
            random.shuffle(a)
            for v in a:      #隨機出牌
                b=random.randint(0,1)
                if v==0 and a2.count(7)==1:
                    if b1[v].count(min(a2)-1)==1 and b1[v].count(max(a2)+1)==1:
                        if b==0:
                            a2.insert(0,min(a2)-1)
                            b1[v].remove(min(a2))
                            isok=True
                            break
                        if b==1:
                            a2.append(max(a2)+1)
                            b1[v].remove(max(a2))
                            isok=True
                            break
                    if b1[v].count(min(a2)-1)==1:
                        a2.insert(0,min(a2)-1)
                        b1[v].remove(min(a2))
                        isok=True
                        break
                    if b1[v].count(max(a2)+1)==1:
                        a2.append(max(a2)+1)
                        b1[v].remove(max(a2))
                        isok=True
                        break
                if v==1 and b2.count(7)==1:
                    if b1[v].count(min(b2)-1)==1 and b1[v].count(max(b2)+1)==1:
                        if b==0:
                            b2.insert(0,min(b2)-1)
                            b1[v].remove(min(b2))
                            isok=True
                            break
                        if b==1:
                            b2.append(max(b2)+1)
                            b1[v].remove(max(b2))
                            isok=True
                            break
                    if b1[v].count(min(b2)-1)==1:
                        b2.insert(0,min(b2)-1)
                        b1[v].remove(min(b2))
                        isok=True
                        break
                    if b1[v].count(max(b2)+1)==1:
                        b2.append(max(b2)+1)
                        b1[v].remove(max(b2))
                        isok=True
                        break
                if v==2 and c2.count(7)==1:
                    if b1[v].count(min(c2)-1)==1 and b1[v].count(max(c2)+1)==1:
                        if b==0:
                            c2.insert(0,min(c2)-1)
                            b1[v].remove(min(c2))
                            isok=True
                            break
                        if b==1:
                            c2.append(max(c2)+1)
                            b1[v].remove(max(c2))
                            isok=True
                            break
                    if b1[v].count(min(c2)-1)==1:
                        c2.insert(0,min(c2)-1)
                        b1[v].remove(min(c2))
                        isok=True
                        break
                    if b1[v].count(max(c2)+1)==1:
                        c2.append(max(c2)+1)
                        b1[v].remove(max(c2))
                        isok=True
                        break
                if v==3 and d2.count(7)==1:
                    if b1[v].count(min(d2)-1)==1 and b1[v].count(max(d2)+1)==1:
                        if b==0:
                            d2.insert(0,min(d2)-1)
                            b1[v].remove(min(d2))
                            isok=True
                            break
                        if b==1:
                            d2.append(max(d2)+1)
                            b1[v].remove(max(d2))
                            isok=True
                            break
                    if b1[v].count(min(d2)-1)==1:
                        d2.insert(0,min(d2)-1)
                        b1[v].remove(min(d2))
                        isok=True
                        break
                    if b1[v].count(max(d2)+1)==1:
                        d2.append(max(d2)+1)
                        b1[v].remove(max(d2))
                        isok=True
                        break
            if isok==False:
                b=[0,1,2,3]
                random.shuffle(b)
                for v in b:   #蓋牌
                    if (v==0)and(len(b1[0])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
                    elif (v==1)and(len(b1[1])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
                    elif (v==2)and(len(b1[2])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
                    elif (v==3)and(len(b1[3])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
        msg1_lb.config(text='輪到2號了')
        if cover==True:
            msg2_lb.config(text='2號蓋牌')
            cover=False
        else:
            msg2_lb.config(text='')
        a2_lb.config(text='梅花:'+str(a2))
        b2_lb.config(text='方塊:'+str(b2))
        c2_lb.config(text='愛心:'+str(c2))
        d2_lb.config(text='黑桃:'+str(d2))
        
        
    
    if s==3:  #輪到3號
        for i in range(1):
            isok=False
            if c1[0].count(7)==1:
                a2.append(7)
                c1[0].remove(7)
                isok=True
                break
            if c1[1].count(7)==1:
                b2.append(7)
                c1[1].remove(7)
                isok=True
                break
            if c1[2].count(7)==1:
                c2.append(7)
                c1[2].remove(7)
                isok=True
                break
            if c1[3].count(7)==1:
                d2.append(7)
                c1[3].remove(7)
                isok=True
                break
            a=[0,1,2,3]
            random.shuffle(a)
            for v in a:
                b=random.randint(0,1)
                if v==0 and a2.count(7)==1:
                    if c1[v].count(min(a2)-1)==1 and c1[v].count(max(a2)+1)==1:
                        if b==0:
                            a2.insert(0,min(a2)-1)
                            c1[v].remove(min(a2))
                            isok=True
                            break
                        if b==1:
                            a2.append(max(a2)+1)
                            c1[v].remove(max(a2))
                            isok=True
                            break
                    if c1[v].count(min(a2)-1)==1:
                        a2.insert(0,min(a2)-1)
                        c1[v].remove(min(a2))
                        isok=True
                        break
                    if c1[v].count(max(a2)+1)==1:
                        a2.append(max(a2)+1)
                        c1[v].remove(max(a2))
                        isok=True
                        break
                if v==1 and b2.count(7)==1:
                    if c1[v].count(min(b2)-1)==1 and c1[v].count(max(b2)+1)==1:
                        if b==0:
                            b2.insert(0,min(b2)-1)
                            c1[v].remove(min(b2))
                            isok=True
                            break
                        if b==1:
                            b2.append(max(b2)+1)
                            c1[v].remove(max(b2))
                            isok=True
                            break
                    if c1[v].count(min(b2)-1)==1:
                        b2.insert(0,min(b2)-1)
                        c1[v].remove(min(b2))
                        isok=True
                        break
                    if c1[v].count(max(b2)+1)==1:
                        b2.append(max(b2)+1)
                        c1[v].remove(max(b2))
                        isok=True
                        break
                if v==2 and c2.count(7)==1:
                    if c1[v].count(min(c2)-1)==1 and c1[v].count(max(c2)+1)==1:
                        if b==0:
                            c2.insert(0,min(c2)-1)
                            c1[v].remove(min(c2))
                            isok=True
                            break
                        if b==1:
                            c2.append(max(c2)+1)
                            c1[v].remove(max(c2))
                            isok=True
                            break
                    if c1[v].count(min(c2)-1)==1:
                        c2.insert(0,min(c2)-1)
                        c1[v].remove(min(c2))
                        isok=True
                        break
                    if c1[v].count(max(c2)+1)==1:
                        c2.append(max(c2)+1)
                        c1[v].remove(max(c2))
                        isok=True
                        break
                if v==3 and d2.count(7)==1:
                    if c1[v].count(min(d2)-1)==1 and c1[v].count(max(d2)+1)==1:
                        if b==0:
                            d2.insert(0,min(d2)-1)
                            c1[v].remove(min(d2))
                            isok=True
                            break
                        if b==1:
                            d2.append(max(d2)+1)
                            c1[v].remove(max(d2))
                            isok=True
                            break
                    if c1[v].count(min(d2)-1)==1:
                        d2.insert(0,min(d2)-1)
                        c1[v].remove(min(d2))
                        isok=True
                        break
                    if c1[v].count(max(d2)+1)==1:
                        d2.append(max(d2)+1)
                        c1[v].remove(max(d2))
                        isok=True
                        break
            if isok==False:
                b=[0,1,2,3]
                random.shuffle(b)
                for v in b:
                    if (v==0)and(len(c1[0])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
                    elif (v==1)and(len(c1[1])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
                    elif (v==2)and(len(c1[2])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
                    elif (v==3)and(len(c1[3])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
        msg1_lb.config(text='輪到3號了')
        if cover==True:
            msg2_lb.config(text='3號蓋牌')
            cover=False
        else:
            msg2_lb.config(text='')
        a2_lb.config(text='梅花:'+str(a2))
        b2_lb.config(text='方塊:'+str(b2))
        c2_lb.config(text='愛心:'+str(c2))
        d2_lb.config(text='黑桃:'+str(d2))
    if s==4:
        msg1_lb.config(text='輪到你了')
        msg2_lb.config(text='')
        start_btn.config(text='別按了')
        isok=False
        

    s+=1
    
    
    
def go():
    cover=False
    global s
    global isok
    if s==1:
        for i in range(1):  #輪到1號
            isok=False
            if a1[0].count(7)==1:
                a2.append(7)
                a1[0].remove(7)
                isok=True
                break
            if a1[1].count(7)==1:
                b2.append(7)
                a1[1].remove(7)
                isok=True
                break
            if a1[2].count(7)==1:
                c2.append(7)
                a1[2].remove(7)
                isok=True
                break
            if a1[3].count(7)==1:
                d2.append(7)
                a1[3].remove(7)
                isok=True
                break
            a=[0,1,2,3]
            random.shuffle(a)
            for v in a:
                b=random.randint(0,1)
                if v==0 and a2.count(7)==1:
                    if a1[v].count(min(a2)-1)==1 and a1[v].count(max(a2)+1)==1:
                        if b==0:
                            a2.insert(0,min(a2)-1)
                            a1[v].remove(min(a2))
                            isok=True
                            break
                        if b==1:
                            a2.append(max(a2)+1)
                            a1[v].remove(max(a2))
                            isok=True
                            break
                    if a1[v].count(min(a2)-1)==1:
                        a2.insert(0,min(a2)-1)
                        a1[v].remove(min(a2))
                        isok=True
                        break
                    if a1[v].count(max(a2)+1)==1:
                        a2.append(max(a2)+1)
                        a1[v].remove(max(a2))
                        isok=True
                        break
                if v==1 and b2.count(7)==1:
                    if a1[v].count(min(b2)-1)==1 and a1[v].count(max(b2)+1)==1:
                        if b==0:
                            b2.insert(0,min(b2)-1)
                            a1[v].remove(min(b2))
                            isok=True
                            break
                        if b==1:
                            b2.append(max(b2)+1)
                            a1[v].remove(max(b2))
                            isok=True
                            break
                    if a1[v].count(min(b2)-1)==1:
                        b2.insert(0,min(b2)-1)
                        a1[v].remove(min(b2))
                        isok=True
                        break
                    if a1[v].count(max(b2)+1)==1:
                        b2.append(max(b2)+1)
                        a1[v].remove(max(b2))
                        isok=True
                        break
                if v==2 and c2.count(7)==1:
                    if a1[v].count(min(c2)-1)==1 and a1[v].count(max(c2)+1)==1:
                        if b==0:
                            c2.insert(0,min(c2)-1)
                            a1[v].remove(min(c2))
                            isok=True
                            break
                        if b==1:
                            c2.append(max(c2)+1)
                            a1[v].remove(max(c2))
                            isok=True
                            break
                    if a1[v].count(min(c2)-1)==1:
                        c2.insert(0,min(c2)-1)
                        a1[v].remove(min(c2))
                        isok=True
                        break
                    if a1[v].count(max(c2)+1)==1:
                        c2.append(max(c2)+1)
                        a1[v].remove(max(c2))
                        isok=True
                        break
                if v==3 and d2.count(7)==1:
                    if a1[v].count(min(d2)-1)==1 and a1[v].count(max(d2)+1)==1:
                        if b==0:
                            d2.insert(0,min(d2)-1)
                            a1[v].remove(min(d2))
                            isok=True
                            break
                        if b==1:
                            d2.append(max(d2)+1)
                            a1[v].remove(max(d2))
                            isok=True
                            break
                    if a1[v].count(min(d2)-1)==1:
                        d2.insert(0,min(d2)-1)
                        a1[v].remove(min(d2))
                        isok=True
                        break
                    if a1[v].count(max(d2)+1)==1:
                        d2.append(max(d2)+1)
                        a1[v].remove(max(d2))
                        isok=True
                        break
            if isok==False:
                b=[0,1,2,3]
                random.shuffle(b)
                for v in b:
                    if (v==0)and(len(a1[0])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
                    elif (v==1)and(len(a1[1])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
                    elif (v==2)and(len(a1[2])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
                    elif (v==3)and(len(a1[3])>0):
                        a1[4].append(min(a1[v]))
                        a1[v].remove(min(a1[v]))
                        cover=True
                        break
        
        msg1_lb.config(text='輪到1號了')
        go_btn.config(text='3')
        if cover==True:
            msg2_lb.config(text='1號蓋牌')
            cover=False
        else:
            msg2_lb.config(text='')
        a2_lb.config(text='梅花:'+str(a2))
        b2_lb.config(text='方塊:'+str(b2))
        c2_lb.config(text='愛心:'+str(c2))
        d2_lb.config(text='黑桃:'+str(d2))
        
        
        
    if s==2:  #輪到2號
        for i in range(1):
            isok=False
            if b1[0].count(7)==1: #先出7
                a2.append(7)
                b1[0].remove(7)
                isok=True
                break
            if b1[1].count(7)==1:
                b2.append(7)
                b1[1].remove(7)
                isok=True
                break
            if b1[2].count(7)==1:
                c2.append(7)
                b1[2].remove(7)
                isok=True
                break
            if b1[3].count(7)==1:
                d2.append(7)
                b1[3].remove(7)
                isok=True
                break
            a=[0,1,2,3]
            random.shuffle(a)
            for v in a:      #隨機出牌
                b=random.randint(0,1)
                if v==0 and a2.count(7)==1:
                    if b1[v].count(min(a2)-1)==1 and b1[v].count(max(a2)+1)==1:
                        if b==0:
                            a2.insert(0,min(a2)-1)
                            b1[v].remove(min(a2))
                            isok=True
                            break
                        if b==1:
                            a2.append(max(a2)+1)
                            b1[v].remove(max(a2))
                            isok=True
                            break
                    if b1[v].count(min(a2)-1)==1:
                        a2.insert(0,min(a2)-1)
                        b1[v].remove(min(a2))
                        isok=True
                        break
                    if b1[v].count(max(a2)+1)==1:
                        a2.append(max(a2)+1)
                        b1[v].remove(max(a2))
                        isok=True
                        break
                if v==1 and b2.count(7)==1:
                    if b1[v].count(min(b2)-1)==1 and b1[v].count(max(b2)+1)==1:
                        if b==0:
                            b2.insert(0,min(b2)-1)
                            b1[v].remove(min(b2))
                            isok=True
                            break
                        if b==1:
                            b2.append(max(b2)+1)
                            b1[v].remove(max(b2))
                            isok=True
                            break
                    if b1[v].count(min(b2)-1)==1:
                        b2.insert(0,min(b2)-1)
                        b1[v].remove(min(b2))
                        isok=True
                        break
                    if b1[v].count(max(b2)+1)==1:
                        b2.append(max(b2)+1)
                        b1[v].remove(max(b2))
                        isok=True
                        break
                if v==2 and c2.count(7)==1:
                    if b1[v].count(min(c2)-1)==1 and b1[v].count(max(c2)+1)==1:
                        if b==0:
                            c2.insert(0,min(c2)-1)
                            b1[v].remove(min(c2))
                            isok=True
                            break
                        if b==1:
                            c2.append(max(c2)+1)
                            b1[v].remove(max(c2))
                            isok=True
                            break
                    if b1[v].count(min(c2)-1)==1:
                        c2.insert(0,min(c2)-1)
                        b1[v].remove(min(c2))
                        isok=True
                        break
                    if b1[v].count(max(c2)+1)==1:
                        c2.append(max(c2)+1)
                        b1[v].remove(max(c2))
                        isok=True
                        break
                if v==3 and d2.count(7)==1:
                    if b1[v].count(min(d2)-1)==1 and b1[v].count(max(d2)+1)==1:
                        if b==0:
                            d2.insert(0,min(d2)-1)
                            b1[v].remove(min(d2))
                            isok=True
                            break
                        if b==1:
                            d2.append(max(d2)+1)
                            b1[v].remove(max(d2))
                            isok=True
                            break
                    if b1[v].count(min(d2)-1)==1:
                        d2.insert(0,min(d2)-1)
                        b1[v].remove(min(d2))
                        isok=True
                        break
                    if b1[v].count(max(d2)+1)==1:
                        d2.append(max(d2)+1)
                        b1[v].remove(max(d2))
                        isok=True
                        break
            if isok==False:
                b=[0,1,2,3]
                random.shuffle(b)
                for v in b:   #蓋牌
                    if (v==0)and(len(b1[0])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
                    elif (v==1)and(len(b1[1])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
                    elif (v==2)and(len(b1[2])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
                    elif (v==3)and(len(b1[3])>0):
                        b1[4].append(min(b1[v]))
                        b1[v].remove(min(b1[v]))
                        cover=True
                        break
        msg1_lb.config(text='輪到2號了')
        go_btn.config(text='2')
        if cover==True:
            msg2_lb.config(text='2號蓋牌')
            cover=False
        else:
            msg2_lb.config(text='')
        a2_lb.config(text='梅花:'+str(a2))
        b2_lb.config(text='方塊:'+str(b2))
        c2_lb.config(text='愛心:'+str(c2))
        d2_lb.config(text='黑桃:'+str(d2))
        
        
    
    if s==3:  #輪到3號
        for i in range(1):
            isok=False
            if c1[0].count(7)==1:
                a2.append(7)
                c1[0].remove(7)
                isok=True
                break
            if c1[1].count(7)==1:
                b2.append(7)
                c1[1].remove(7)
                isok=True
                break
            if c1[2].count(7)==1:
                c2.append(7)
                c1[2].remove(7)
                isok=True
                break
            if c1[3].count(7)==1:
                d2.append(7)
                c1[3].remove(7)
                isok=True
                break
            a=[0,1,2,3]
            random.shuffle(a)
            for v in a:
                b=random.randint(0,1)
                if v==0 and a2.count(7)==1:
                    if c1[v].count(min(a2)-1)==1 and c1[v].count(max(a2)+1)==1:
                        if b==0:
                            a2.insert(0,min(a2)-1)
                            c1[v].remove(min(a2))
                            isok=True
                            break
                        if b==1:
                            a2.append(max(a2)+1)
                            c1[v].remove(max(a2))
                            isok=True
                            break
                    if c1[v].count(min(a2)-1)==1:
                        a2.insert(0,min(a2)-1)
                        c1[v].remove(min(a2))
                        isok=True
                        break
                    if c1[v].count(max(a2)+1)==1:
                        a2.append(max(a2)+1)
                        c1[v].remove(max(a2))
                        isok=True
                        break
                if v==1 and b2.count(7)==1:
                    if c1[v].count(min(b2)-1)==1 and c1[v].count(max(b2)+1)==1:
                        if b==0:
                            b2.insert(0,min(b2)-1)
                            c1[v].remove(min(b2))
                            isok=True
                            break
                        if b==1:
                            b2.append(max(b2)+1)
                            c1[v].remove(max(b2))
                            isok=True
                            break
                    if c1[v].count(min(b2)-1)==1:
                        b2.insert(0,min(b2)-1)
                        c1[v].remove(min(b2))
                        isok=True
                        break
                    if c1[v].count(max(b2)+1)==1:
                        b2.append(max(b2)+1)
                        c1[v].remove(max(b2))
                        isok=True
                        break
                if v==2 and c2.count(7)==1:
                    if c1[v].count(min(c2)-1)==1 and c1[v].count(max(c2)+1)==1:
                        if b==0:
                            c2.insert(0,min(c2)-1)
                            c1[v].remove(min(c2))
                            isok=True
                            break
                        if b==1:
                            c2.append(max(c2)+1)
                            c1[v].remove(max(c2))
                            isok=True
                            break
                    if c1[v].count(min(c2)-1)==1:
                        c2.insert(0,min(c2)-1)
                        c1[v].remove(min(c2))
                        isok=True
                        break
                    if c1[v].count(max(c2)+1)==1:
                        c2.append(max(c2)+1)
                        c1[v].remove(max(c2))
                        isok=True
                        break
                if v==3 and d2.count(7)==1:
                    if c1[v].count(min(d2)-1)==1 and c1[v].count(max(d2)+1)==1:
                        if b==0:
                            d2.insert(0,min(d2)-1)
                            c1[v].remove(min(d2))
                            isok=True
                            break
                        if b==1:
                            d2.append(max(d2)+1)
                            c1[v].remove(max(d2))
                            isok=True
                            break
                    if c1[v].count(min(d2)-1)==1:
                        d2.insert(0,min(d2)-1)
                        c1[v].remove(min(d2))
                        isok=True
                        break
                    if c1[v].count(max(d2)+1)==1:
                        d2.append(max(d2)+1)
                        c1[v].remove(max(d2))
                        isok=True
                        break
            if isok==False:
                b=[0,1,2,3]
                random.shuffle(b)
                for v in b:
                    if (v==0)and(len(c1[0])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
                    elif (v==1)and(len(c1[1])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
                    elif (v==2)and(len(c1[2])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
                    elif (v==3)and(len(c1[3])>0):
                        c1[4].append(min(c1[v]))
                        c1[v].remove(min(c1[v]))
                        cover=True
                        break
        msg1_lb.config(text='輪到3號了')
        go_btn.config(text='1')
        if cover==True:
            msg2_lb.config(text='3號蓋牌')
            cover=False
        else:
            msg2_lb.config(text='')
        a2_lb.config(text='梅花:'+str(a2))
        b2_lb.config(text='方塊:'+str(b2))
        c2_lb.config(text='愛心:'+str(c2))
        d2_lb.config(text='黑桃:'+str(d2))
    if s==4: #輪到玩家
        isok=False
        msg1_lb.config(text='輪到你了')
        msg2_lb.config(text='')
        go_btn.config(text='出牌')
        if ((d1[0].count(7)==1) or (d1[1].count(7)==1) or
            (d1[2].count(7)==1) or (d1[3].count(7)==1) or  
            ((len(a2)>0)and(d1[0].count(min(a2)-1)==1)) or ((len(a2)>0)and(d1[0].count(max(a2)+1)==1)) or
            ((len(b2)>0)and(d1[1].count(min(b2)-1)==1)) or ((len(b2)>0)and(d1[1].count(max(b2)+1)==1)) or
            ((len(c2)>0)and(d1[2].count(min(c2)-1)==1)) or ((len(c2)>0)and(d1[2].count(max(c2)+1)==1)) or
            ((len(d2)>0)and(d1[3].count(min(d2)-1)==1)) or ((len(d2)>0)and(d1[3].count(max(d2)+1)==1))):
            msg4_lb.config(text='選擇花色')
        else:
            msg4_lb.config(text='選擇要蓋牌的花色')
            isok=True
    if s==5: #玩家出牌
        if isok==False: #可以出牌
            p=var.get()
            d=int(num_ety.get())
            if d1[p].count(d)==1:
                try:
                    g=d1[p].index(d)
                    if d==7:
                        if p==0:
                            a2.append(7)
                            d1[p].remove(7)
                        if p==1:
                            b2.append(7)
                            d1[p].remove(7)
                        if p==2:
                            c2.append(7)
                            d1[p].remove(7)
                        if p==3:
                            d2.append(7)
                            d1[p].remove(7)
                    else:           
                        if p==0:
                            if min(a2)-1==d1[p][g]:
                                a2.insert(0,min(a2)-1)
                                d1[p].remove(min(a2))
                            elif max(a2)+1==d1[p][g]:
                                a2.append(max(a2)+1)
                                d1[p].remove(max(a2))
                            else:
                                s=3
                                print('這張牌不能出')
                        elif p==1:
                            if min(b2)-1==d1[p][g]:
                                b2.insert(0,min(b2)-1)
                                d1[p].remove(min(b2))
                            elif max(b2)+1==d1[p][g]:
                                b2.append(max(b2)+1)
                                d1[p].remove(max(b2))
                            else:
                                s=3
                                print('這張牌不能出')
                        elif p==2:
                            if min(c2)-1==d1[p][g]:
                                c2.insert(0,min(c2)-1)
                                d1[p].remove(min(c2))
                            elif max(c2)+1==d1[p][g]:
                                c2.append(max(c2)+1)
                                d1[p].remove(max(c2))
                            else:
                                s=3
                                print('這張牌不能出')
                        elif p==3:
                            if min(d2)-1==d1[p][g]:
                                d2.insert(0,min(d2)-1)
                                d1[p].remove(min(d2))
                            elif max(d2)+1==d1[p][g]:
                               d2.append(max(d2)+1)
                               d1[p].remove(max(d2))
                            else:
                                s=3
                                print('這張牌不能出')
                        else:
                            s=3
                            print('這張牌不能出')                            
                except:
                    s=3
                    print('這張牌不能出')
            else:
                s=3
                print('你沒有這張牌')
        if isok==True: #要蓋牌
            try:   
                p=var.get()
                d=int(num_ety.get())
                g=d1[p].index(d)
                d1[4].append(d1[p][g])
                d1[p].remove(d1[p][g])
            except:
                s=3
                print('你沒有這張牌')
        msg4_lb.config(text='選擇花色')
        go_btn.config(text='4')
        d1_1_lb.config(text='梅花:'+str(d1[0]))
        d1_2_lb.config(text='方塊:'+str(d1[1]))
        d1_3_lb.config(text='愛心:'+str(d1[2]))
        d1_4_lb.config(text='黑桃:'+str(d1[3]))
        a2_lb.config(text='梅花:'+str(a2))
        b2_lb.config(text='方塊:'+str(b2))
        c2_lb.config(text='愛心:'+str(c2))
        d2_lb.config(text='黑桃:'+str(d2))
    s+=1 
    if s==6:
        s=1
    if ((len(a1[0])==0)and(len(a1[1])==0)and #大家牌都沒了
        (len(a1[2])==0)and(len(a1[3])==0)and
        (len(b1[0])==0)and(len(b1[1])==0)and
        (len(b1[2])==0)and(len(b1[3])==0)and
        (len(c1[0])==0)and(len(c1[1])==0)and
        (len(c1[2])==0)and(len(c1[3])==0)and
        (len(d1[0])==0)and(len(d1[1])==0)and
        (len(d1[2])==0)and(len(d1[3])==0)):
        msg1_lb.config(text='遊戲結束')
        s1=s2=s3=s4=0
        for m in a1[4]:
            s1+=m
        for m in b1[4]:
            s2+=m
        for m in c1[4]:
            s3+=m
        for m in d1[4]:
            s4+=m
        a2_lb.config(text='1號蓋牌:'+ str(a1[4])+ ' '+ '總分'+ str(s1) )
        b2_lb.config(text='2號蓋牌:'+ str(b1[4])+ ' '+ '總分'+ str(s2) )
        c2_lb.config(text='3號蓋牌:'+ str(c1[4])+ ' '+ '總分'+ str(s3) )
        d2_lb.config(text='玩家蓋牌:'+ str(d1[4])+ ' '+ '總分'+ str(s4) )
        winer=[s1,s2,s3,s4]
        if s1==min(winer):
            msg2_lb.config(text='贏家是一號')
        if s2==min(winer):
            msg2_lb.config(text='贏家是二號')
        if s3==min(winer):
            msg2_lb.config(text='贏家是三號')
        if s4==min(winer):
            msg2_lb.config(text='贏家是玩家')
    
    


start_btn=tk.Button(win,text='開始遊戲',command=start)  #設置介面
start_btn.pack()
msg1_lb=tk.Label(win,text='歡迎來到牌七')
msg1_lb.place(x=0,y=0)
msg2_lb=tk.Label(win,text='小心這脆弱的程式碼')
msg2_lb.place(x=0,y=20)
a2_lb=tk.Label(win,text='梅花:'+str(a2))
a2_lb.place(x=0,y=50)
b2_lb=tk.Label(win,text='方塊:'+str(b2))
b2_lb.place(x=0,y=80)
c2_lb=tk.Label(win,text='愛心:'+str(c2))
c2_lb.place(x=0,y=110)
d2_lb=tk.Label(win,text='黑桃:'+str(d2))
d2_lb.place(x=0,y=140)
__lb=tk.Label(win,text='------------------------------------------------------------------------------------------------------------')
__lb.place(x=0,y=170)
msg3_lb=tk.Label(win,text='你的牌')
msg3_lb.place(x=0,y=200)
d1_1_lb=tk.Label(win,text='梅花:'+str(d1[0]))
d1_1_lb.place(x=0,y=240)
d1_2_lb=tk.Label(win,text='方塊:'+str(d1[1]))
d1_2_lb.place(x=0,y=270)
d1_3_lb=tk.Label(win,text='愛心:'+str(d1[2]))
d1_3_lb.place(x=0,y=300)
d1_4_lb=tk.Label(win,text='黑桃:'+str(d1[3]))
d1_4_lb.place(x=0,y=330)
msg4_lb=tk.Label(win,text='選擇花色')
msg4_lb.place(x=400,y=240)
var=tk.IntVar()
r1_rbtn=tk.Radiobutton(win,text='梅花',variable=var,value=0)
r1_rbtn.place(x=400,y=270)
r2_rbtn=tk.Radiobutton(win,text='方塊',variable=var,value=1)
r2_rbtn.place(x=400,y=300)
r3_rbtn=tk.Radiobutton(win,text='愛心',variable=var,value=2)
r3_rbtn.place(x=400,y=330)
r4_rbtn=tk.Radiobutton(win,text='黑桃',variable=var,value=3)
r4_rbtn.place(x=400,y=360)
msg5_lb=tk.Label(win,text='選擇數字')
msg5_lb.place(x=400,y=400)
num_ety=tk.Entry(win)
num_ety.place(x=460,y=400)
go_btn=tk.Button(win,text='出牌',command=go)
go_btn.place(x=530,y=300)




win.mainloop()
