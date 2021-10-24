from tkinter import *

win = Tk()
cv = Canvas(win, width=380, height=380)
cv.pack()
for i in range(19):
    y = i * 20
    cv.create_line(0, y, 380, y, fill="black", width = 2)
win.mainloop()
