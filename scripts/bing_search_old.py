import webbrowser
import time 
import random
import pyautogui
from wonderwords import RandomWord
import keyboard
r=RandomWord()
print("\nStarting!!!")
nsearch=int(input("\nEnter number of search==>"))
i=0
print("\nHang On!!")
while(i<nsearch):
    word1=r.word()
    word3=r.word()
    randomint=random.randint(300,400)
    #"+word1+"+"+word2+"+"+word3+"
    webbrowser.open("https://www.bing.com/search?q="+word1+"+"+word2+"+"+word3+"&qs=n&form=QBRE&sp=-1&lq=0&pq="+word1+"+"+word2+"+"+word3+"&sc=10-14&sk=&cvid=F958C197B98945529D35B01540AC9449&ghsh=0&ghacc=0&ghpl=")
    i=i+1 
    time.sleep(randomint)
    pyautogui.hotkey('command', 'w')
print("\n**ENDED**")