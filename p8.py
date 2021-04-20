import random
import wx
import pyttsx3
import re
import os
engine = pyttsx3.init()
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 160)
class MyFrame(wx.Frame) :
    def __init__(self) :  
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition, size=wx.Size(500,500),style=wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX| wx.CLOSE_BOX | wx.CLIP_CHILDREN,title="Guess Game")
        panel= wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl1=wx.StaticText(panel,label="Enter The Number :",size = wx.Size(400,30))
        self.txt1 = wx.TextCtrl(panel,style= wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt1.SetFocus()
        self.txt1.SetHint("Take a Guess")
        self.btn = wx.ToggleButton(panel,-1,"Submit") 
        self.btn.Bind(wx.EVT_TOGGLEBUTTON,self.OnEnter)
        my_sizer.Add(lbl1, 0,wx.ALL,5)
        my_sizer.Add(self.txt1,0,wx.ALL,5)
        my_sizer.Add(self.btn,0,wx.ALIGN_CENTER,5)
        panel.SetSizer(my_sizer)
        self.Show()
    def OnEnter(self, event) :
        input1= self.txt1.GetValue()
        if input1=="" :
            print("Enter the value")
            engine.say("Please Enter the value")
            engine.runAndWait()
        elif int(input1) <= 20 and int(input1) >= 1  :
            secretno = random.randint(1, 20)
            guess = int(input1)
            if guess < secretno :
                    print('guess is too low')
                    engine.say("guess is too low")
                    engine.runAndWait()
            elif guess > secretno :
                    print('guess is too high')
                    engine.say("guess is too high")
                    engine.runAndWait()
            if guess == secretno :
                print('WOW !!!! Your guess is right !!!')
                engine.say("WOW !!!! Your guess is right !!!"+ input1)
                engine.runAndWait()
            else :
                print('Nope, the number i was thinking was' + str(secretno))
                engine.say('Nope, the number i was thinking was ' + str(secretno))
                engine.runAndWait()
        else :
            print("Enter the value between 1 and 20 and enter the integer")
            engine.say("Enter the value between 1 and 20 and enter the integer")
            engine.runAndWait()
if  __name__ == "__main__" :
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
    