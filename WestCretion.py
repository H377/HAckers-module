import os
from time import sleep
from win32api import SetSystemTime
import datetime
import easygui
#WC module
#Better if you use admin rules
def killBackGround():
	#Can be used without admin
	os.system("taskkill /F /IM explorer.exe")
def executeBackGround():
	os.system("start C:/Windows/explorer.exe")
def blockTaskMgr():
	os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /f /v "DisableTaskMgr" /t REG_DWORD /d 1')
def unblockTaskMgr():
	os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /f /v "DisableTaskMgr" /t REG_DWORD /d 0')
def blockRegEdit():
	#WARNING CANT BE UNLOCKED
	os.system('REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /t Reg_dword /v DisableRegistryTools /f /d 1')
def shutDownWindows():
	os.system("shutdown /s /t 15")
def sleepWindows():
	os.system("sleep /s /t 15")
def executeShell(shell):
	#Sometimes need admin rules
	command = "start " + shell
	os.system(command)
def stopCode(time):
	sleep(time)
def timeSet(year,month,dayweek,day,hour,minute,second):
	millseconds = 0
	SetSystemTime(year,month,dayweek,day,hour,minute,second,millseconds)
def timeNow():
	nowtime = datetime.datetime.now()
	print(nowtime.strftime("%d-%m-%Y %H:%M"))
def openBrowserPage(page):
	url = ("start " + page)
	os.system(url)
def createFile(name):
	f = open(name,"w")
def editFile(name):
	f = open(name,"a")
def deleteFile(path):
	os.remove(path)
def createMsgBox(msg,title):
	easygui.msgbox(msg = msg, title = title)
def createBttBox(msg,title,choices):
	easygui.msgbox(msg = msg, title = title, choices = choices)
#module v2.0







