import pygame
from pygame.locals import*

pygame().init()
#定义窗口的标题为hello world
screencaption=pygame.display.set_caption("hello world")
#定义窗口大小为640*480
screen=pygame.set_mode([640,480])
#窗口填充为白色
screen.fill([255,255,2555])