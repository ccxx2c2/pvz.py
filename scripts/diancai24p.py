#!/usr/bin/python  
# -*- coding: utf-8 -*- 
'''
author: no_doudle
date: 2017-2-24 20:00
'''
import sys,threading,pvz
from pvz import *
pvz.paoList = [(x,y) for x in range(1,7) for y in range(7,0,-2)]
waveDealPao = 2	
diancaiList = [(1,9),(2,9),(5,9),(6,9)]
diancaiCnt = 0

def diancai(ww11 = False):
	global diancaiList,diancaiCnt
	for cd in range(4):
		if ww11 and cd < 2:
			continue
		Card(3+cd+diancaiCnt%2*4)
		Pnt(diancaiList[cd])
	diancaiCnt+=1
		
def deldiancai(ww11 = False):
	global diancaiList
	for cd in range(4):
		if ww11 and cd < 2:
			continue
		Card(12)
		Pnt(diancaiList[cd])

def dc(ww11 = False):
	sleep(0.81)
	diancai(ww11)
	sleep(0.03)
	deldiancai(ww11)

def wave10cherry():
	print('cherrythread going')
	sleep(3.73-1)
	sleep(1.08)
	Card(1)
	Pnt((1,9))	

def wave10():
	preJudge(55, True)
	Pao(2,9)
	Pao(5,9)
	sleep(0.84)
	Pao(2,9)
	tch = threading.Thread(target=wave10cherry, name='cherryThread')
	tch.start()
	sleep(1.08-0.84)
	Pao(5,8)

def ChoosingCard():
	ChooseCard(1, 3) #CherryBomb
	ChooseCard(1, 4) #Wall-nut
	ChooseCard(2, 1) #PuffShroom
	ChooseCard(2, 1, True) #imPuffShroom
	ChooseCard(2, 2) #SunShroom
	ChooseCard(2, 6) #ScaredyShroom
	ChooseCard(5, 2) #FlowerPot
	ChooseCard(1, 2) #Sunflower
	ChooseCard(5, 5) #Garlic
	ChooseCard(2, 3) #FumeShroom
	#LetsRock()

def main():
	print('nowopen %s' % win32gui.GetWindowText(hwnd))
	print('mainthread going')
	for wave in range(1, 20):
		while(Countdown()<200):
			pass
			
		print('wave:%s' % wave)
		if wave == 10 :
			wave10()
			continue
			
		preJudge(155)
		print('mainthread afterpj')
		Pao(2,9)
		Pao(5,9)
		if wave == 1:
			sleep(1.08)
			Pao(1,8)
			Pao(5,8)
			continue
		
		tdc = threading.Thread(target=dc, args=(wave == 11,),name='diancaiThread')
		tdc.start()
		sleep(1.08)
		Pao(1,8)
		Pao(5,8)
		tdc.join()
		
		if(wave % 10 == 9):
			sleep(6-1.08)
			Pao(2,9)
			Pao(5,9)
			tdc.start()
			sleep(1.08)
			Pao(1,8.4)
			Pao(5,8.4)
			tdc.join()
			sleep(4)
			Pao(2,9)
			Pao(5,9)
			tdc.start()
			tdc.join()
			
		if(wave == 9):
			pvz.nowPao += waveDealPao
			
	tch.join()
	wave20()
	
if __name__ == '__main__':
	if len(sys.argv) == 2 :
		ChoosingCard()
	else:
		main()
