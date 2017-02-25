#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
author:no_doudle
date:2017-2-25 14:37
'''
import sys,threading,pvz
from pvz import *
pvz.paoList = [(3,1),(4,1),(3,3),(4,3),(1,5),(6,5),(2,5),(5,5),(3,5),(4,5)]
waveDealPao = 4	
boomList = [(3,8),(3,9),(4,8),(4,9)]

def booming():
	global boomList
	print('boomthread going')
	sleep(6+5)
	for BoomCnt in range(5):
		print('boomcnt:%s' % BoomCnt)
		Card(8) #LilyPad
		Pnt(boomList[BoomCnt % len(boomList)])
		sleep(0.01)
		Card(3) #DoomShroom
		Pnt(boomList[BoomCnt % len(boomList)])
		sleep(0.01)
		Card(4) #CoffeeBean
		Pnt(boomList[BoomCnt % len(boomList)])
		sleep(50)
		
def main():
	if(len(sys.argv)==2): #choosing card
		ChooseCard(2, 7, True) #imIceShroom
		ChooseCard(2, 7) #IceShroom
		ChooseCard(2, 8) #DoomShroom
		ChooseCard(5, 4) #CoffeeBean
		ChooseCard(1, 3) #CherryBomb
		ChooseCard(3, 5) #Jalapeno
		ChooseCard(3, 2) #Squash
		ChooseCard(3, 1) #LilyPad
		ChooseCard(4, 7) #Pumpkin
	    ChooseCard(2, 1) #PuffShroom
        LetsRock()
        return
    print('nowopen %s' % win32gui.GetWindowText(hwnd))
    t = threading.Thread(target=booming, name='boomThread')
    t.start()
    print('mainthread going')
    for wave in range(1, 21):
        print('wave:%s' % wave)
        if(wave == 20):
            preJudge(150, True) #coral, appear in 2s(prejudge 1.73) after warning disappear; 2.5s(prejudge 1.23) start eating
            Pao(4,6)
            sleep(1.5+5.5-3.73)
        else:
            preJudge(2, wave%10==0)
            sleep(5.5-3.75)
        print('mainthread afterpj')
        if(wave % 10 == 0):
            Pao(2,9)
            Pao(5,9)
        else:
            Pao(2,8.15)# for backup dancer
            Pao(5,8.15)
        if(wave % 10 == 9):
            pvz.nowPao += waveDealPao
    t.join()
    
if __name__ == '__main__':
    main()
