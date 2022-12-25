import tkinter as tk
from roku import Roku

roku = Roku('CHANGE THIS TO YOUR ROKU IP')
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 300, bg='black')
canvas1.pack()

def play ():  
    label1 = tk.Label(root, roku.play(), fg='blue', font=('helvetica', 12, 'bold'))
def left ():  
    label1 = tk.Label(root, roku.left(), fg='blue', font=('helvetica', 12, 'bold'))
def right ():  
    label1 = tk.Label(root, roku.right(), fg='blue', font=('helvetica', 12, 'bold'))
def up ():  
    label1 = tk.Label(root, roku.up(), fg='blue', font=('helvetica', 12, 'bold'))
def down ():  
    label1 = tk.Label(root, roku.down(), fg='blue', font=('helvetica', 12, 'bold'))
def select ():  
    label1 = tk.Label(root, roku.select(), fg='blue', font=('helvetica', 12, 'bold'))
def back ():  
    label1 = tk.Label(root, roku.back(), fg='blue', font=('helvetica', 12, 'bold'))
def home ():  
    label1 = tk.Label(root, roku.home(), fg='blue', font=('helvetica', 12, 'bold'))
def replay ():  
    label1 = tk.Label(root, roku.replay(), fg='blue', font=('helvetica', 12, 'bold'))
def info ():  
    label1 = tk.Label(root, roku.info(), fg='blue', font=('helvetica', 12, 'bold'))
def forward ():  
    label1 = tk.Label(root, roku.forward(), fg='blue', font=('helvetica', 12, 'bold'))
def reverse ():  
    label1 = tk.Label(root, roku.reverse(), fg='blue', font=('helvetica', 12, 'bold'))
  
        
button1 = tk.Button(text='Play/Pause', command=play, bg='grey',fg='white')
canvas1.create_window(100, 220, window=button1)

button2 = tk.Button(text='◄', command=left, bg='grey',fg='white')
canvas1.create_window(70, 140, window=button2)

button3 = tk.Button(text='►', command=right, bg='grey',fg='white')
canvas1.create_window(130, 140, window=button3)

button4 = tk.Button(text='▲', command=up, bg='grey',fg='white')
canvas1.create_window(100, 105, window=button4)

button5 = tk.Button(text='▼', command=down, bg='grey',fg='white')
canvas1.create_window(100, 175, window=button5)

button6 = tk.Button(text='▣', command=select, bg='grey',fg='white')
canvas1.create_window(100, 140, window=button6)

# button7 = tk.Button(text='Play/Pause', command=play, bg='grey',fg='white')
# canvas1.create_window(100, 220, window=button1)

button8 = tk.Button(text='↰', command=back, bg='grey',fg='white')
canvas1.create_window(70, 105, window=button8)

button9 = tk.Button(text='home', command=home, bg='grey',fg='white')
canvas1.create_window(50, 50, window=button9)

button10 = tk.Button(text='↺', command=replay, bg='grey',fg='white')
canvas1.create_window(130, 175, window=button10)

button11 = tk.Button(text='>>', command=forward, bg='grey',fg='white')
canvas1.create_window(130, 250, window=button11)

button12 = tk.Button(text='<<', command=reverse, bg='grey',fg='white')
canvas1.create_window(70, 250, window=button12)

button13 = tk.Button(text='◌*', command=info, bg='grey',fg='white')
canvas1.create_window(130, 105, window=button13)

root.mainloop()
