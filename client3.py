import  socket 
import sys
from thread import *
from Tkinter import*
import random

host ='localhost'
port = 5100
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect((host, port))

def callback(event):

    print "clicked at", event.x,event.y

def text_place_handler(event):

    print "clicked at", event.x,event.y

def text_enter_handler(event):
	content=msg_tosend.get()
	message=content
	msgtextdisplay.delete(150.5,END)	
	msgtextdisplay.insert(150.5,message)

def create_client_module(parent):
	def recv():
		i=0
    		while True:
			data = s.recv(1024)
			if not data: sys.exit(0)
			print data
			ct=[random.randrange(256) for x in range(3)]
			brightness=int(round(0.299*ct[0]+0.587*ct[1]+0.114*ct[2]))
			ct_hex="%02x%02x%02x" % tuple(ct)
			bg_colour='#'+"".join(ct_hex)
			button=Button(parent, text=str(data),width=7 , height=1, fg="red", bg=bg_colour)
			
			button.bind("<Button-1>",callback)
			button.place(x=20,y=30+i*30,width=120,height=25)

                        send_btn=Button(root,text="SEND")
                        send_btn.place(x=420, y=455, width=70, height=35)
			
			i=i+1
	start_new_thread(recv ,())

class DrawBottomFrame:

    def __init__(self,root):

        fm=Frame(root,bg="white smoke")
        fm.place(x=150,y=350,width=350,height=150)
        
        self.msgtextdisplay=Text(root,wrap=WORD)
	self.msgtextdisplay.place(x=150, y=5, width=350, height=340)

        self.msg_tosend=Entry(root)
	self.msg_tosend.place(x=155, y=355, width=340, height=140)
	#self.msg_tosend.bind("<Enter>", text_enter_handler)
	
		
	self.send_btn=Button(root,text="SEND", command=self.sendmsg)
	self.send_btn.place(x=420, y=455, width=70, height=35)

    def sendmsg(self):
	content=self.msg_tosend.get()
	message=content
	self.msgtextdisplay.delete(150.5,END)	
	self.msgtextdisplay.insert(150.5,message)

class Syst():
    def __init__(self, root):
	self.create_widget()

    def create_widget(self):
	send_btn=Button(root,text="SEND", command=self.sendmsg)
	send_btn.place(x=420, y=455, width=70, height=35)
	self.msg_send =Entry(root)
	self.msg_send.place(x=155, y=355, width=340, height=140)
	self.msgtext=Text(root,wrap=WORD)
	self.msgtext.place(x=150, y=5, width=350, height=350)

   
    def sendmsg(self):
	content=msg_send.get()
	message=content
	root.text.insert(150.5,message)

	
root=Tk()
left_frame=Frame(root,bg="bisque3")
left_frame.place(x=0,y=0,width=150,height=500)
create_client_module(left_frame)

center_frame=Frame(root,bg="gainsboro")
center_frame.place(x=150,y=0,width=350,height=350)

bottom=DrawBottomFrame(root)
root.geometry('500x500')
root.resizable(width=False,height=False)
root.mainloop()




