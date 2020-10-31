import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from player import play_sound


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Timer')
        self.geometry('550x550')
        self.iconbitmap('images/icontimer.ico')
        self.configure(background='#00060D')
        self.resizable(False, False)

        self.data = '00:00:00'
        self.stop_countdown = False

        self.image_ellipse = tk.PhotoImage(file='images/ellipse.png')
        self.image_start = tk.PhotoImage(file='images/button1.png')
        self.image_pause = tk.PhotoImage(file='images/button2.png')
        self.image_stop = tk.PhotoImage(file='images/button3.png')
        self.image_config = tk.PhotoImage(file='images/button4.png')
        self.image_cont = tk.PhotoImage(file='images/button5.png')

        self.timer_label = tk.Label(self, bg='#00060D', image=self.image_ellipse, compound='center',
                                    text='00:00:00', font=('DS-Digital', 40, 'bold'), fg='#05F2DB')
        self.timer_label.image = self.image_ellipse
        self.timer_label.pack(pady=20)

        self.button_start = tk.Button(self, image=self.image_start, bg='#00060D', bd=0, relief='flat',
                                      activebackground='#00060D', command=self.start_timer)
        self.button_start.image = self.image_start
        self.button_start.pack(side='left', padx=50)

        self.button_config = tk.Button(self, image=self.image_config, bg='#00060D', bd=0, relief='flat',
                                       activebackground='#00060D', command=lambda: ConfigureWindow(self))
        self.button_config.image = self.image_config
        self.button_config.pack(side='right', padx=50)

        self.button_pause = tk.Button(self, image=self.image_pause, bg='#00060D', bd=0, relief='flat',
                                      activebackground='#00060D', command=self.pause_timer)
        self.button_pause.image = self.image_pause

        self.button_cont = tk.Button(self, image=self.image_cont, bg='#00060D', bd=0, relief='flat',
                                     activebackground='#00060D', command=self.continue_timer)
        self.button_cont.image = self.image_cont

        self.button_stop = tk.Button(self, image=self.image_stop, bg='#00060D', bd=0, relief='flat',
                                     activebackground='#00060D', command=self.stop_timer)
        self.button_stop.image = self.image_stop
        
    def start_timer(self):
        if self.timer_label['text'] == '00:00:00':
            messagebox.showinfo('Alert', 'Informe os valores da contagem')
        else:
            self.button_start.forget()
            self.button_config.forget()

            self.button_pause.pack(side='left', padx=50)
            self.button_stop.pack(side='right', padx=50)

            play_sound()
            self.stop_countdown = False
            self.countdown()

    def pause_timer(self):
        play_sound()
        self.stop_countdown = True

        self.button_pause.forget()
        self.button_cont.pack(side='left', padx=50)

    def continue_timer(self):
        self.button_cont.forget()
        self.button_pause.pack(side='left', padx=50)

        play_sound()
        self.stop_countdown = False
        self.countdown()

    def stop_timer(self):
        self.button_pause.forget()
        self.button_cont.forget()
        self.button_stop.forget()

        self.button_start.pack(side='left', padx=50)
        self.button_config.pack(side='right', padx=50)

        play_sound()
        self.stop_countdown = True
        self.timer_label['text'] = '00:00:00'

    def countdown(self):
        if self.stop_countdown:
            return
        time = self.timer_label['text']
        time = time.split(':')
        hours, minutes, seconds = time
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        if not hours == minutes == seconds == 0:
            if minutes == seconds == 0:
                hours -= 1
                minutes = 59
                seconds = 59
            elif seconds == 0:
                minutes -= 1
                seconds = 59
            else:
                seconds -= 1

            t = f'{hours}:{minutes}:{seconds}'
            time_convert = datetime.strptime(t, '%H:%M:%S')

            self.timer_label['text'] = time_convert.strftime('%H:%M:%S')
            self.after(1000, self.countdown)

    def set_values(self):
        try:
            time_convert = datetime.strptime(self.data, '%H:%M:%S')
            self.timer_label['text'] = time_convert.strftime('%H:%M:%S')
        except ValueError:
            messagebox.showerror('ValueError', 'Os valores de horas, minutos e segundos não podem ser maiores que 59')


class ConfigureWindow(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.transient(master)
        self.title('Configure')
        self.geometry('250x230')
        self.iconbitmap('images/icontimer.ico')
        self.resizable(False, False)
        self.configure(background='#00060D')

        line1 = tk.Frame(self, bg='#00060D')
        line2 = tk.Frame(self, bg='#00060D')
        line3 = tk.Frame(self, bg='#00060D')
        line1.pack(pady=20)
        line2.pack()
        line3.pack(pady=20)

        label_h = tk.Label(line1, text='Hours:', bg='#00060D', fg='white', font=('Roboto', 12))
        self.entry_h = tk.Entry(line1, bg='white', fg='black', width=5, font=('DS-Digital', 14, 'bold'),
                                justify='center')
        label_h.pack(side='left', padx=10)
        self.entry_h.pack(side='left')

        label_m = tk.Label(line2, text='Minutes:', bg='#00060D', fg='white', font=('Roboto', 12))
        self.entry_m = tk.Entry(line2, bg='white', fg='black', width=5, font=('DS-Digital', 14, 'bold'),
                                justify='center')
        label_m.pack(side='left', padx=10)
        self.entry_m.pack(side='left')

        label_s = tk.Label(line3, text='Seconds:', bg='#00060D', fg='white', font=('Roboto', 12))
        self.entry_s = tk.Entry(line3, bg='white', fg='black', width=5, font=('DS-Digital', 14, 'bold'),
                                justify='center')
        label_s.pack(side='left', padx=10)
        self.entry_s.pack(side='left')

        button = tk.Button(self, text='CONFIRM', bg='#05F2DB', fg='#364F52', font=('Roboto', 12, 'bold'),
                           activebackground='#05F2DB', relief='solid', bd=1, command=self.confirm)
        button.pack(pady=10)

    def confirm(self):
        def check_get(value):
            if value == '':
                return '0'
            else:
                return value

        hours = check_get(self.entry_h.get())
        minutes = check_get(self.entry_m.get())
        seconds = check_get(self.entry_s.get())

        if int(hours) == int(minutes) == int(seconds) == 0:
            messagebox.showinfo('ValueError', 'Informe os valores!')
        else:
            time = f'{hours}:{minutes}:{seconds}'

            self.master.data = time
            self.master.set_values()
            self.destroy()


def main():
    MainWindow().mainloop()


if __name__ == '__main__':
    main()
