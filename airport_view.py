from tkinter import *
import airport_model as m

window = Tk()  
window.title("Airport Finder")  
window.geometry('1800x850')

main_frame = Frame(window)
main_frame.pack()

top_frame = Frame(main_frame)
top_frame.pack(side=TOP)

bottom_frame = Frame(main_frame)
bottom_frame.pack(side=BOTTOM)

btn = Button(top_frame, text="Apply filter",bg="gray68", fg="black", font=("Arial Bold", 10), command=m.clicked1)
btn.grid(column=0, row=4, columnspan=2, pady=10, padx=10, ipady=10, ipadx=10)

btn1 = Button(top_frame, text="Сhip flights",bg="gray68", fg="black", font=("Arial Bold", 10), command=m.clicked2)
btn1.grid(column=2, row=4, columnspan=2, pady=10, padx=10, ipady=10, ipadx=10)


Label(top_frame, text="Min latitude:").grid(row=0, column=0, sticky=W, pady=10, padx=10)
min_lat = Entry(top_frame, width=30)   # текстовое поле  
min_lat.grid(column=0, row=1)
min_lat.delete(0, END)
min_lat.insert(0, '30.0')

Label(top_frame, text="Max latitude:").grid(row=0, column=1, sticky=W, pady=10, padx=10)
max_lat = Entry(top_frame, width=30)   # текстовое поле  
max_lat.grid(column=1, row=1)
max_lat.delete(0, END)
max_lat.insert(0, '70.0')

Label(top_frame, text="Min longitude:").grid(row=2, column=0, sticky=W, pady=10, padx=10)
min_lon = Entry(top_frame, width=30)   # текстовое поле  
min_lon.grid(column=0, row=3)
min_lon.delete(0, END)
min_lon.insert(0, '30.0')

Label(top_frame, text="Max longitude:").grid(row=2, column=1, sticky=W, pady=10, padx=10)
max_lon = Entry(top_frame, width=30)   # текстовое поле  
max_lon.grid(column=1, row=3)
max_lon.delete(0, END)
max_lon.insert(0, '70.0')

Label(top_frame, text="Departure:").grid(row=0, column=2, sticky=W, pady=10, padx=10)
depart = Entry(top_frame, width=30)   # текстовое поле
depart.grid(column=2, row=1)
depart.delete(0, END)
depart.insert(0, '')

Label(top_frame, text="Arrival:").grid(row=2, column=2, sticky=W, pady=10, padx=10)
arr = Entry(top_frame, width=30)   # текстовое поле
arr.grid(column=2, row=3)
arr.delete(0, END)
arr.insert(0, '')


# window.mainloop()


