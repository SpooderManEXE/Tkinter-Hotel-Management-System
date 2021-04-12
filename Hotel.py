import tkinter as tk
from tkinter import ttk
import os
import pickle
import sys
from subprocess import call
import sys


font14 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0" 
LARGEFONT =("Verdana", 35)
    
class tkinterApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        stl = ttk.Style()
        stl.configure('C.TLabel',padding=[20,10,20,10])
        stl.map('C.TLabel',
        foreground = [('pressed','red'),('active','blue'),('focus','green')],
        background = [('pressed','!disabled','black'),('active','white')],
        relief=[('pressed', 'sunken'),('!pressed', 'raised')])
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
class HomePage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Sreelux Hotel", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
        button1 = ttk.Button(self, text ="Check In",style='C.TLabel',
        command = lambda : parent.switch_frame(CheckIn))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="Check Out",
        command = lambda : parent.switch_frame(CheckOut))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="Guests List",
        command=lambda: parent.switch_frame(Guests))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
        button4 = ttk.Button(self, text ="Guest Info",
        command = lambda : parent.switch_frame(GuestInfo))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10)
          
class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO  
  
class CheckIn(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Check In", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
        u = list()
        Suite = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
        Basic = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
        Joint = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)
        m = [9]
        G = []
        details_list=[]

        def file_save():
            NAME_PRO = details_list[0]
            ADDRESS_PRO = details_list[1]
            MOBILE_NO_PRO = details_list[2]
            ROOM_NO_PRO = details_list[3]
            PRICE_PRO = details_list[4]
            f = open("hotel.dat", "ab")
            a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
            pickle.dump(a,f,protocol=2)
            f.close()
            listq=[str(NAME_PRO),str(ADDRESS_PRO),str(MOBILE_NO_PRO),str(ROOM_NO_PRO),str(PRICE_PRO)]
            myVars = {'A':NAME_PRO,"B":ADDRESS_PRO,"C":MOBILE_NO_PRO,"D":ROOM_NO_PRO,"E":PRICE_PRO }
            fo=open("recipt.txt","w+")
            for h in range(0,5):
                fo.write(listq[h]+"\r\n")
            fo.close()
            parent.switch_frame(Receipt)
            
        def chk_name():
            self.err1=0
            while True:
                self.k = str(self.name.get())
                a = self.k.isdigit()
                if len(self.k) != 0 and a != True:
                    self.NAME=self.k
                    self.err1=1
                    break
                else:
                    self.Text1.configure(text="please input a valid name""\n")
                    break
                
        def chk_add():
            self.err2=0
            while True:
                self.g = str(self.addr.get())
                ak = self.g.isdigit()
                if len(self.g)!= 0 and ak!=True:
                    self.ADDERESS=self.g
                    self.err2=1
                    break
                else:
                    self.Text1.configure(text="please input a valid address""\n")
                    break

        def chk_mo():
            self.err3=0
            while True:
                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.err3=1
                    break
                else:
                    self.Text1.configure(text="please input a valid mobile number""\n")
                break
            
        def chk_day():
            self.err4=0
            while True:
                self.l = str(self.days.get())
                if self.l.isdigit() == True and len(self.l) != 0:
                    self.DAYS = int(self.l)
                    self.err4=1
                    break
                else:
                    self.Text1.configure(text= "please input number of days""\n")
                    break
                
        def chk_entry():
            chk_day()
            chk_mo()
            chk_add()
            chk_name()
            if(self.err1 and self.err2 and self.err3 and self.err4):
                enter()

        def enter():
            self.pname = self.NAME
            self.address = self.ADDERESS
            self.mobile_no = self.MOBILE
            self.no_of_days = int(self.DAYS)
            self.ch=self.room.get()
            if os.path.exists("recipt.txt"):
              os.remove("recipt.txt")
            if self.ch == 1:
                self.price = 1000 * self.no_of_days
                m[0] = 1
            elif self.ch == 2:
                self.price = 1350 * self.no_of_days
                m[0] = 2
            elif self.ch == 3:
                self.price = 1700 * self.no_of_days
                m[0] = 3
            elif self.ch == 4:
                self.price = 2000 * self.no_of_days
                m[0] = 4
            if m[0] == 1:
                a = Basic
            elif m[0] == 2:
                a = Joint
            elif m[0] == 3:
                a = Delux
            elif m[0] == 4:
                a = Suite
            G = []
            f2 = open("hotel.dat", "rb")
            try:
                while True:
                    s = pickle.load(f2)
                    k = s.room_no
                    G.append(k)
                    continue
            except EOFError:
                pass
            for r in a:
                if r not in G:
                    self.proom = r
                    break
                else:
                    continue
            self.proom = r
            f2.close()
            details_list.append(self.pname)
            details_list.append(self.address)
            details_list.append(self.mobile_no)
            details_list.append(self.proom)
            details_list.append(self.price)
            file_save()
   
        self.Text1 = tk.Label(self)
        self.Text1.grid(row = 8, column = 1, padx = 10, pady = 10)
        label1=ttk.Label(self,text='''Enter name :''',font=font14)
        label1.grid(row = 1, column = 0, padx = 10, pady = 10)
        label2=ttk.Label(self,text='''Enter address :''',font=font14)
        label2.grid(row = 2, column = 0, padx = 10, pady = 10)
        label3=ttk.Label(self,text='''Enter phone no.:''',font=font14)
        label3.grid(row = 3, column = 0, padx = 10, pady = 10)
        label4=ttk.Label(self,text='''Number of days :''',font=font14)
        label4.grid(row = 4, column = 0, padx = 10, pady = 10)
        label5=ttk.Label(self,text='''Choose room :''',font=font14)
        label5.grid(row = 5, column = 0, padx = 10, pady = 10)

        self.name=tk.StringVar()
        self.addr = tk.StringVar()
        self.mobile=tk.StringVar()
        self.days=tk.StringVar()
        entry1=ttk.Entry(self,textvariable=self.name)
        entry1.grid(row = 1, column = 1, padx = 10, pady = 10)
        entry2=ttk.Entry(self,textvariable=self.addr)
        entry2.grid(row = 2, column = 1, padx = 10, pady = 10)
        entry3=ttk.Entry(self,textvariable=self.mobile)
        entry3.grid(row = 3, column = 1, padx = 10, pady = 10)
        entry4=ttk.Entry(self,textvariable=self.days)
        entry4.grid(row = 4, column = 1, padx = 10, pady = 10)

        self.room = tk.IntVar()
        Checkbutton1 = ttk.Radiobutton(self, text="BASIC (1000)", variable=self.room, value=1)
        Checkbutton1.grid(row = 6, column = 1, padx = 10, pady = 10)
        Checkbutton2 = ttk.Radiobutton(self, text="JOINT (1350)", variable=self.room, value=2)
        Checkbutton2.grid(row = 6, column = 2, padx = 10, pady = 10)
        Checkbutton3 = ttk.Radiobutton(self, text="DELUXE (1700)", variable=self.room, value=3)
        Checkbutton3.grid(row = 7, column = 1, padx = 10, pady = 10)
        Checkbutton4 = ttk.Radiobutton(self, text="SUITE (2000)", variable=self.room, value=4)
        Checkbutton4.grid(row = 7, column = 2, padx = 10, pady = 10)
        button0 = ttk.Button(self, text ="Submit",
                            command = chk_entry)
        button0.grid(row = 9, column = 2, padx = 10, pady = 10)
        button1 = ttk.Button(self, text ="HomePage",
                            command = lambda : parent.switch_frame(HomePage))
        button1.grid(row = 9, column = 0, padx = 10, pady = 10)
  
class CheckOut(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Check Out", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
        def check_room():
            self.rom = str(self.data.get())
            if self.rom.isdigit() == True and len(self.rom) != 0:
                self.Text1.configure(text="valid room number ""\n")
                v = int(self.rom)
                f = open("hotel.dat", "rb")
                f1 = open("hote.dat", "ab")
                n = 0
                try:
                    while True:
                        s = pickle.load(f)
                        if s.room_no == v:
                            n = 1
                            name1 = s.name
                            print(" ")
                        else:
                            pickle.dump(s, f1)
                except EOFError:
                    if n == 0:
                        self.Text1.configure(text= "NO GUEST FOUND""\n")
                    elif n == 1:
                        self.Text1.configure(text= "THANK YOU " + name1.upper() + " FOR VISTING US""\n")
                    pass
                f.close()
                f1.close()
                os.remove("hotel.dat")
                os.rename("hote.dat", "hotel.dat")
            else:
                self.Text1.configure(text= "please input a valid ROOM NO.""\n")
        self.data=tk.StringVar()
        self.Text1 = tk.Label(self)
        self.Text1.grid(row = 1, column = 1, padx = 10, pady = 10)
        label1=ttk.Label(self,text='''Enter Room no :''')
        label1.grid(row = 2, column = 0, padx = 10, pady = 10)
        entry1=ttk.Entry(self,textvariable=self.data)
        entry1.grid(row = 2, column = 1, padx = 10, pady = 10)
        button1 = ttk.Button(self, text ="CheckOut",
                            command=check_room)
        button1.grid(row = 2, column = 2, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="HomePage",
                            command = lambda : parent.switch_frame(HomePage))
        button2.grid(row = 3, column = 0, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="Guests List",
                            command = lambda : parent.switch_frame(Guests))
        button3.grid(row = 3, column = 2, padx = 10, pady = 10)

class Guests(tk.Frame):
    def __init__(self, parent):   
        details_list=[]
        l2=[]
        G = []
        tk.Frame.__init__(self, parent)
        t = ttk.Label(self, text ="Guests", font = LARGEFONT)
        t.grid(row = 0, column = 1, padx = 10, pady = 10)
        label = ttk.Label(self)
        label.grid(row = 1, column = 1, padx = 10, pady = 10)
        label2 = ttk.Label(self)
        label2.grid(row = 1, column = 2, padx = 10, pady = 10)
        f2 = open("hotel.dat", "rb")
        try:
           while True:
               s = pickle.load(f2)
               k = s.room_no
               o = s.name.upper()
               l2.append(o)
               G.append(k)
               continue
        except EOFError:
            pass
        f2.close()
        s="Name\n\n"
        h="Room\n\n"
        for i in range(0,len(G)):
            s=s+str(l2[i])+"\n"
            h=h+str(G[i])+"\n"
            label.configure(text= s)
            label2.configure(text= h)
        button1 = ttk.Button(self, text ="HomePage",
                                command =  lambda: parent.switch_frame(HomePage))
        button1.grid(row = 2, column = 0, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="CheckOut",
                                command =  lambda: parent.switch_frame(CheckOut))
        button2.grid(row = 2, column = 3, padx = 10, pady = 10)   
        
class GuestInfo(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Guest Info", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
        def gotinfo():
            self.gettininfo = str(self.gather.get())
            if self.gettininfo.isdigit() == True and len(self.gettininfo) != 0:
                try:
                    n = -1
                    f2 = open("hotel.dat", "rb")
                    while True:
                        s = pickle.load(f2)
                        a = str(s.room_no)
                        if self.gettininfo == a:
                            n = 1
                            sr="Name:\t"+str(s.name)+"\n"
                            sr=sr+"Address:\t"+ str(s.address)+"\n"
                            sr=sr+"Mobile No.:  "+str(s.mobile_no)+"\n"
                            sr=sr+"TOTAL BILL IS Rs."+str(s.price)+"\n"
                            self.Text1.configure(text=sr)
                except EOFError:
                    if n == -1:
                        sr="NO GUEST IN ROOM "+ str(self.gettininfo)
                        self.Text1.configure(text=sr)
                    pass
                    f2.close()
            else:
                self.Text1.configure(text= "please input a valid ROOM NO.""\n")
        self.gather=tk.StringVar()
        label1=ttk.Label(self,text='''Enter Room no :''')
        label1.grid(row = 1, column = 0, padx = 10, pady = 10)
        entry1=ttk.Entry(self,textvariable=self.gather)
        entry1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button1 = ttk.Button(self, text ="Get Info",
                            command=gotinfo)
        button1.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.Text1 = tk.Label(self)
        self.Text1.grid(row = 2, column = 1, padx = 10, pady = 10)
        button1 = ttk.Button(self, text ="HomePage",
                            command = lambda : parent.switch_frame(HomePage))
        button1.grid(row = 3, column = 0, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="Guests List",
                                command =  lambda: parent.switch_frame(Guests))
        button2.grid(row = 2, column = 2, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="CheckOut",
                                command =  lambda: parent.switch_frame(CheckOut))
        button3.grid(row = 3, column = 2, padx = 10, pady = 10)

class Receipt(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        fo1=open("recipt.txt","r")
        list1=fo1.readlines()
        del list1[1]
        del list1[2]
        del list1[3]
        del list1[4]
        del list1[5]
        list1[0]=list1[0][:-1]
        list1[1]=list1[1][:-1]
        list1[2]=list1[2][:-1]
        list1[3]=list1[3][:-1]
        list1[4]=list1[4][:-1]

        p='''
        @@@@@@@@@@  SREELUX HOTEL AND RESORTS  @@@@@@@@@@
        @@@@@@@@@@   SERVING    GUEST   SINCE    @@@@@@@@@@@@
        @@@@@@@@@@@@    ###  2000  ###   @@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        \t\t\tNAME-%s
        \t\t\tADDRESS-%s
        \t\t\tMOBILE NO.-%s
        \t\t\tYOUR TOTAL BILL IS Rs.%s
        \t\t\tYOUR ROOM NUMBER IS %s    
        
        
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

             
             
        '''%(list1[0],list1[1],list1[2],list1[4],list1[3])
        label = ttk.Label(self, text =p)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="HomePage",
                            command = lambda : parent.switch_frame(HomePage))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
app = tkinterApp()
app.mainloop()
