from tkinter import *

win = Tk()

cv = Canvas(win, width=1000, height=1000)
cv.pack()

for i in range(21):
    print(i, i*50)
    y = i * 50
    cv.create_line(0, y, 1000, y, fill='black', width=2)
    x = i * 50
    cv.create_line(x, 0, x, 1000, fill='black', width=2)
    
win.mainloop()    
print(i)