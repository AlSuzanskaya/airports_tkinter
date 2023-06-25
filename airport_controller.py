from tkinter import *
class Table:
	
    def __init__(self,root,data):
        self.data = data
        self.total_rows = len(data)
        self.total_columns = len(data[0])
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                if len(str(self.data[i][j])) >= 25:
                    self.e = Entry(root, width=36, fg='gray25', font=('Calibri Light', 12))
                else:
                    self.e = Entry(root, width=18, fg='gray25',font=('Calibri Light',12))
                self.e.grid(row=i, column=j)
                self.e.insert(END, self.data[i][j])

    
    def destroy(self, root):
        for widget in root.winfo_children():
            widget.destroy()



