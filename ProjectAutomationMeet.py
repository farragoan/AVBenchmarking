#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pyautogui
import time
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True  # Top left corner will raise exception


# In[84]:


#mic = Point(x=887, y=993)
#end call = Point(x=958, y=989), Point(x=1075, y=597)
#cam = (x=1027, y=986)
#present = Point(x=1787, y=987), Point(x=1745, y=892),Point(x=800, y=249)(subject to change),Point(x=1134, y=519)
def turn_on_mic():
    pyautogui.click(887,993)
def turn_off_mic():
    pyautogui.click(887,993)

def turn_on_cam():
    pyautogui.click(1027,986)
def turn_off_cam():
    pyautogui.click(1027,986)
    
def sharing_screen():
    pyautogui.click(1787,987)
    pyautogui.click(1745,892)
    pyautogui.click(769,219)  #subject to change
    pyautogui.click(1134,519)
    pyautogui.click(352,940)  #play button
    pyautogui.click(117,9)  #return to tab

def start_recording():
    pyautogui.click(1885,996)
    pyautogui.click(1748,505)
    pyautogui.click(1217,678)  #start button
    time.sleep(10)
    
def stop_recording():
    pyautogui.click(1885,996)
    pyautogui.click(1748,505)
    pyautogui.click(1081,660)  #stop button
    
def wireshark_start():
    pyautogui.click(858,1057)  #open apllication
    pyautogui.click(598,753)  #select wifi
    pyautogui.click(369,199)  #start capturing
    
def wireshark_start_continue():
    pyautogui.click(858,1057)  #open apllication
    pyautogui.click(369,199)  #start capturing
    pyautogui.click(1033,551) #continue without saving
    
def wireshark_stop(test_num):
    pyautogui.click(390,199)  #stop capturing
    pyautogui.click(374,177)  #open File
    pyautogui.click(487,422)  #export packet dissections
    pyautogui.click(693,446)  #As csv
    pyautogui.typewrite('Test'+str(test_num))
    pyautogui.click(1061,538) #save
    
def reset_video():
    pyautogui.click(356,11)  #change tab
    pyautogui.click(1217,678)  #pause button
    pyautogui.click(332,914)  #reset to 0
    pyautogui.click(149,10)  #come back to meet tab
    
def start_video():
    pyautogui.click(349,10) #change tab
    pyautogui.click(355,934) #play button
    pyautogui.click(118,12) #change tab to meet
    
    
    
    
def main():
#     print(pyautogui.size())
     print(pyautogui.position())
     a=input()
     print(a)
     time.sleep(10)
#     turn_on_mic()
#     turn_on_cam()
#     sharing_screen()
#     wireshark_start()
#     time.sleep(5)
#     wireshark_stop(5)

# Test 1
#     sharing_screen()
#     start_recording()
#     wireshark_start()
#     time.sleep(5)
#     wireshark_stop(1)
#     stop_recording()
#     reset_video()
    
# #Test2
#     turn_on_mic()
#     start_video()
#     start_recording()
#     wireshark_start()
#     time.sleep(5)
#     wireshark_stop(2)
#     stop_recording()
#     reset_video()
    
# #Test3
#     turn_on_cam()
#     start_video()
#     start_recording()
#     wireshark_start()
#     time.sleep(5)
#     wireshark_stop(3)
#     stop_recording()
#     reset_video()


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




