#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
author:no_doudle
date:2017-2-25 14:37
'''
import sys,threading,pvz
from pvz import *
pvz.paoList = [(x,y) for x in range(1,7) for y in range(7,0,-2) if(not(y==7 and (x==3 or x==4)))]
waveDealPao = 6	
diancaiList = [(5,9),(6,9)]
diancaiCnt = 0
iceList = [(3,9),(4,9)]
iceCnt = 0

def FillIce(set):
	global iceList
	sleep(3-1)
	for fillIceCnt in range(5) :
		print('fill ice %s when cnt==%s' % (set,fillIceCnt))
		Card(set+1)
		Pnt(iceList[set])
		sleep(51)
		if(set == 1 and fillIceCnt == 1):
			sleep(6)
		
		
def diancai():
	global diancaiList,diancaiCnt
	for cd in range(2):
		Card(7+cd+diancaiCnt%2*2)
		Pnt(diancaiList[cd])
	diancaiCnt+=1
	
	sleep(2)
	
	for cd in range(2):
		Card(12)
		Pnt(diancaiList[cd])
	
def ice():
	global iceCnt,iceList
	Card(3)
	Pnt(iceList[iceCnt%2])
	iceCnt+=1
	
def ChoosingCard():
	ChooseCard(2, 7, True) #imIceShroom
	ChooseCard(2, 7) #IceShroom
	ChooseCard(5, 4) #CoffeeBean
	ChooseCard(1, 3) #CherryBomb
	ChooseCard(3, 5) #Jalapeno
	ChooseCard(4, 7) #Pumpkin
	ChooseCard(2, 1) #PuffShroom
	ChooseCard(2, 2) #SunShroom
	ChooseCard(2, 6) #ScaredyShroom
	ChooseCard(5, 2) #FlowerPot
	#LetsRock()
	
def main():
	print('nowopen %s' % win32gui.GetWindowText(hwnd))
	print('mainthread going')
	fillIceA = threading.Thread(target=FillIce, args=(0,), name='FillIceAThread')
	fillIceB = threading.Thread(target=FillIce, args=(1,), name='FillIceBThread')
	for wave in [1,3,5,7,9,10,12,14,16,18,19]:
		print('wave:%s' % wave) #PSDPD
		
		if wave == 1:
			preJudge(130) #-3.73-2+2.12+2.12
		elif wave == 10 :
			preJudge(55, True)
		else:
			Pao(2,9) #10-3.75
			Pao(5,9)
			sleep(2.17)
			Pao(1,8.4)
			Pao(5,8.4)
			sleep(2.17)
			
		Pao(1,9)
		Pao(2,9)
		Pao(5,9)
		if wave == 19:
			break
		sleep(1.1)
		Pao(1,9)
		Pao(5,8)
		sleep(0.2-4.3-1.1+2+3.75)
			
		if wave != 10:
			sleep(6-2.98)
		else:
			sleep(6-2.98-(1.30-0.55))
		ice()#i+pp,i operate at +0.2
		sleep(1)
		tdc = threading.Thread(target=diancai, name='diancaiThread')
		tdc.start()
		if(wave+1 == 2):
			fillIceA.start()
		if(wave+1 == 4):
			fillIceB.start()
		
		sleep(2.98) #pp at 1.2(+3.75)
		if wave == 9:
			Pao(6,8.5)
			Pao(6,8.4)
            pvz.nowPao += 15
            sleep(3.73-1)
            Card(12)
            Pnt((6,9))
            Card(4)
            Pnt((6,9))
            continue
        Pao(2,7.3)
        Pao(5,7.3)
        
        sleep(9.6-1.2-3.75) #pp down at 10
    
    pvz.nowPao += 8
    wave20()

if __name__ == '__main__':
    if len(sys.argv) == 2 :
        ChoosingCard()
    else:
        main()
