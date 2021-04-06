import os             
import pyautogui
import time
from time import sleep
from datetime import datetime
import webbrowser
def join(gcp,link,start_time,leave_time):
    url = link
    webbrowser.register('chrome',
	                        None,
	                        webbrowser.BackgroundBrowser(gcp))
    print("1")
    while 1:
        now = datetime.strftime(datetime.now(),"%H:%M:%S") 
        print("2")
        if now>start_time:
            webbrowser.get('chrome').open(url)
            time.sleep(3)
            join = pyautogui.locateCenterOnScreen("oyta.PNG") 
            pyautogui.moveTo(join)
            pyautogui.click()
            time.sleep(5)
            join = pyautogui.locateCenterOnScreen("omt.PNG") 
            pyautogui.moveTo(join)
            pyautogui.click()
            time.sleep(8)
            audiooff = pyautogui.locateCenterOnScreen("audiooff.PNG") 
            pyautogui.moveTo(audiooff)
            pyautogui.click()
            time.sleep(2)
            join = pyautogui.locateCenterOnScreen("join.PNG") 
            pyautogui.moveTo(join)
            pyautogui.click()
            time.sleep(5)
            break

    while 1:
        now = datetime.strftime(datetime.now(),"%H:%M:%S") 
        if now>leave_time:
            leave = pyautogui.locateCenterOnScreen("leave.PNG") 
            pyautogui.moveTo(leave)
            pyautogui.click()
            break

#join("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",'https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3A89eae9fa2a0847768eff96ceaf3449d9%40thread.tacv2%2F1617653046624%3Fcontext%3D%257b%2522Tid%2522%253a%2522a6de9407-2d24-407d-81e6-941b053c301a%2522%252c%2522Oid%2522%253a%25228352aef6-dbd6-40aa-8112-a592d5682c15%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=9d1427d8-e290-42f3-a272-ca7b96be1235&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true',"16:55:00","17:10:00")