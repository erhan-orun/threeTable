from tkinter import *
from tkinter import ttk

root = Tk()
root.title('PythonGuides')
root.geometry('400x300')

table1 = ttk.Treeview(root)
table1['columns'] = ('Rank', 'Name', 'Badge')
table1.column('#0', width=0, stretch=NO)
table1.column('Rank', anchor=CENTER, width=80)
table1.column('Name', anchor=CENTER, width=80)
table1.column('Badge', anchor=CENTER, width=80)

table1.heading('#0', text='', anchor=CENTER)
table1.heading('Rank', text='Id', anchor=CENTER)
table1.heading('Name', text='rank', anchor=CENTER)
table1.heading('Badge', text='Badge', anchor=CENTER)

table1.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
table1.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
table1.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
table1.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
table1.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))
table1.pack()

table2 = ttk.Treeview(root)
table2['columns'] = ('Rank', 'Name', 'Badge')
table2.column('#0', width=0, stretch=NO)
table2.column('Rank', anchor=CENTER, width=80)
table2.column('Name', anchor=CENTER, width=80)
table2.column('Badge', anchor=CENTER, width=80)

table2.heading('#0', text='', anchor=CENTER)
table2.heading('Rank', text='Id', anchor=CENTER)
table2.heading('Name', text='rank', anchor=CENTER)
table2.heading('Badge', text='Badge', anchor=CENTER)

table2.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
table2.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
table2.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
table2.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
table2.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))
table2.pack()

table3 = ttk.Treeview(root)
table3['columns'] = ('Rank', 'Name', 'Badge')
table3.column('#0', width=0, stretch=NO)
table3.column('Rank', anchor=CENTER, width=80)
table3.column('Name', anchor=CENTER, width=80)
table3.column('Badge', anchor=CENTER, width=80)

table3.heading('#0', text='', anchor=CENTER)
table3.heading('Rank', text='Id', anchor=CENTER)
table3.heading('Name', text='rank', anchor=CENTER)
table3.heading('Badge', text='Badge', anchor=CENTER)

table3.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
table3.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
table3.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
table3.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
table3.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))
table3.pack()

root.mainloop()
