# -*- coding: utf-8 -*-
'''
description: a python module contains some method of game "Plants Vs Zombies"
author: no_doudle
date: 2017-2-24 20:00
'''
import win32api, win32con, win32gui, win32process, ctypes 
from time import sleep

x, y = win32api.GetCursorPos()
hwnd = win32gui.WindowFromPoint((x, y))
# hwnd = win32gui.GetForegroundWindow()
# equal to
nowPao = 0
memoryAddress = -1
Screenx = 800
Screeny = 600
scene = 'PE'

PROCESS_ALL_ACCESS  =  ( 0x000F0000 | 0x00100000 | 0xFFF )
tid,pid = win32process.GetWindowThreadProcessId(hwnd)
PROCESS = win32api.OpenProcess(PROCESS_ALL_ACCESS, 0, pid)
rPM = ctypes.WinDLL('kernel32', use_last_error=True).ReadProcessMemory
buffer = ctypes.create_string_buffer(4)
bytes_read = ctypes.c_size_t()

def ReadMemory(address):
    global PROCESS, buffer
    rPM(PROCESS.handle, address, buffer, 4, ctypes.byref(bytes_read))
    ret=0x0
    cnt = len(buffer.value) -1
    while cnt >= 0:
        ret *= 256
        ret += buffer.value[cnt]
        cnt -= 1
    return ret
    
def MUP(x, y, right = False):
    global Screenx,Screeny
    x *= (Screenx/800)
    y *= (Screeny/600)
    if(right):
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, win32con.NULL, y*65536+x)
    else:
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.NULL, y*65536+x)
    
def MDOWN(x, y, right = False):
    global Screenx,Screeny
    x *= (Screenx/800)
    y *= (Screeny/600)
    if(right):
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.NULL, y*65536+x)
    else:
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.NULL, y*65536+x)

def Click(x, y, right = False):
    MDOWN(x, y)
    MUP(x, y)

def safeClick():
    Click(60, 50, True)
    
def Countdown():
    global memoryAddress
    if memoryAddress < 0 :
        memoryAddress = ReadMemory(0x6a9ec0) + 0x768
        memoryAddress = ReadMemory(memoryAddress) + 0x559c
        
    countdown = ReadMemory(memoryAddress) 
    while countdown == 0 :
        countdown = ReadMemory(memoryAddress)
    return countdown
    
def ChooseCard(row, column, imitater = False):
    if(imitater):
        Click(500, 550) #center of imitater
        sleep(0.2) #second, wait for menu of seeds
        x, y = 190, 125 #top left corner of imitater peashooter
    else:
        x, y = 22, 123 #top left corner of peashooter
    x += 50/2
    y += 70/2
    #a card is 50px in width(+3px space) and 70px in height 
    x += (column - 1)* 53
    y += (row - 1)* 70
    Click(x, y)
        
def LetsRock():
    sleep(0.01) #wait for button available
    MDOWN(225, 565) #LET'S ROCK button
    sleep(0.01) 
    MUP(225, 565) 

def Card(num):
    Click(50 + 50 * num, 70)
    
def Pnt(pnt):
    global scene
    row = pnt[0]
    column = pnt[1]
    
    if (scene == 'PE'):
        Click(80 * column, 30 + 85 * row)
    elif (scene == 'DE'):
        Click(80 * column, 30 + 100 * row)
    else :
        if (column > 5):
            Click(80 * column, 85 * row)
        else:
            Click(80 * column, 85 * row + (120 - 20 * column))

def preJudge(t, hugewave = False): #unit of t:centisec
    if(hugewave == False):
        while(Countdown() > t):
            pass 
    
    else:
        while(Countdown() > 4):#warning appears, new wave after 7.24s
            pass
        sleep((724-t)/100)

def Pao(row, column):
    global nowPao,paoList
    nowPao %= len(paoList)
    for i in range(10):
        Pnt(paoList[nowPao])
    Pnt((row, column))
    safeClick()
    nowPao += 1
    
def wave20():
    preJudge(150, True) #coral, appear in 2s(prejudge 1.73) after warning disappear; 2.5s(prejudge 1.23) start eating
    Pao(4,7)
    sleep(0.9)
    Pao(2,9)
    Pao(2,9)
    Pao(5,9)
    Pao(5,9)
    sleep(1.08)
    Pao(1,9)
    Pao(2,9)
    Pao(5,9)
    Pao(5,9)
