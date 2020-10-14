import tkinter as tk


class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title('Timer')
        self.master.geometry('550x550')
        self.master.iconbitmap('images/icontimer.ico')
        self.master.configure(background='#00060D')
        self.master.resizable(False, False)

        self.image_ellipse = tk.PhotoImage(file='images/ellipse.png')
        self.image_start = tk.PhotoImage(file='images/button1.png')
        self.image_pause = tk.PhotoImage(file='images/button2.png')
        self.image_stop = tk.PhotoImage(file='images/button3.png')
        self.image_config = tk.PhotoImage(file='images/button4.png')

        timer_label = tk.Label(self.master, bg='#00060D', image=self.image_ellipse, compound='center', text='00:00:00',
                               font=('DS-Digital', 40, 'bold'), fg='#05F2DB')
        timer_label.image = self.image_ellipse
        timer_label.pack(pady=20)

        self.button_start = tk.Button(self.master, image=self.image_start, bg='#00060D', bd=0, relief='flat',
                                      activebackground='#00060D', command=self.start)
        self.button_start.image = self.image_start
        self.button_start.pack(side='left', padx=50)

        self.button_config = tk.Button(self.master, image=self.image_config, bg='#00060D', bd=0, relief='flat',
                                       activebackground='#00060D')
        self.button_config.image = self.image_config
        self.button_config.pack(side='right', padx=50)

        self.button_pause = tk.Button(self.master, image=self.image_pause, bg='#00060D', bd=0, relief='flat',
                                      activebackground='#00060D')
        self.button_pause.image = self.image_pause

        self.button_stop = tk.Button(self.master, image=self.image_stop, bg='#00060D', bd=0, relief='flat',
                                     activebackground='#00060D', command=self.stop)
        self.button_stop.image = self.image_stop
        
    def start(self):
        self.button_start.forget()
        self.button_config.forget()

        self.button_pause.pack(side='left', padx=50)
        self.button_stop.pack(side='right', padx=50)

        # timer(10)

    def stop(self):
        self.button_pause.forget()
        self.button_stop.forget()

        self.button_start.pack(side='left', padx=50)
        self.button_config.pack(side='right', padx=50)


app = tk.Tk()
Interface(app)
app.mainloop()
