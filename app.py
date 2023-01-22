import tkinter
from tkinter import *
from tkinter import messagebox
import os
import threading
import sys



tkWindow = Tk()  
tkWindow.geometry('1000x500')  
tkWindow.title('UAA VPN by Micromoon')
photo = PhotoImage(file = "icon.png")
tkWindow.iconphoto(False, photo)

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def connected():  
    messagebox.showinfo('Success!', 'You connected to our servers at San Francisco, CA! Minimize This Window to keep using the VPN. Your Connection will end after you close this window.')
    os.system('./uaavpn-connect.sh')
def disconnected(): 
    os.system('killall openvpn') 
    messagebox.showinfo('Success!', "You're now using your local network")
    restart_program()


l = Label(tkWindow, text = "UAA VPN by Micromoon")
l.config(font =("Roboto", 20))

z = Label(tkWindow, text = "If You Cannot Reconnect, Please Restart the App.")
z.config(font =("Roboto", 10))


button1 = Button(tkWindow,
	text = 'Connect',
	command = threading.Thread(target=connected).start,
    height=2,
    width=50) 
button2 = Button(tkWindow,
	text = 'Disconnect',
	command = threading.Thread(target=disconnected).start,
    height=2,
    width=50) 
l.pack()
button1.pack(side=tkinter.TOP)  
button2.pack(side=tkinter.TOP) 
z.pack()  



  
tkWindow.mainloop()
tkWindow.update()